"""Scan folder Bai hoc y khoa, extract metadata, generate dashboard HTML.

Features:
- Auto-detect folder structure (01_San phu khoa, 02_ART, 03_Sieu am thai, ...)
- For each lesson folder: detect .md, .docx, .apkg, .html files
- Extract title (from MD H1 hoặc filename), date (from filename pattern YYYY-MM-DD)
- Build cards grid + sidebar filter + search
- Dark mode toggle
- Tailwind CDN + minimal vanilla JS
"""
import re
import json
from pathlib import Path
from datetime import datetime


# ============================
# CONFIG
# ============================
ROOT = Path(r'F:\DL\mavisresearch\Bai hoc y khoa')

SPECIALTY_MAP = {
    '01_San phu khoa': {'name': 'Sản phụ khoa', 'short': 'OB/GYN', 'icon': '🤰', 'color': 'pink'},
    '02_Ho tro sinh san ART': {'name': 'Hỗ trợ sinh sản (ART)', 'short': 'ART', 'icon': '🧬', 'color': 'purple'},
    '03_Sieu am thai': {'name': 'Siêu âm thai', 'short': 'Fetal US', 'icon': '🔊', 'color': 'cyan'},
    '04_Sieu am tong quat': {'name': 'Siêu âm tổng quát', 'short': 'General US', 'icon': '🫀', 'color': 'teal'},
    '05_Noi tiet - Hormone': {'name': 'Nội tiết - Hormone', 'short': 'Endo', 'icon': '⚗️', 'color': 'amber'},
    '06_Vi sinh - Mien dich': {'name': 'Vi sinh - Miễn dịch', 'short': 'Micro', 'icon': '🦠', 'color': 'green'},
    '07_Ung thu phu khoa': {'name': 'Ung thư phụ khoa', 'short': 'Gyn Onc', 'icon': '🎗️', 'color': 'red'},
}

# Folder thư viện HTML output
LIBRARY_DIR = ROOT / '00_Tong hop' / 'Library'
LIBRARY_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_HTML = LIBRARY_DIR / 'index.html'


# ============================
# SCAN
# ============================
def count_apkg_cards(apkg_path: Path) -> int:
    """Count cards in an .apkg file (SQLite inside zip)."""
    import zipfile
    import sqlite3
    import tempfile
    import os
    try:
        with zipfile.ZipFile(apkg_path, 'r') as z:
            # Find collection.anki2 or collection.anki21
            db_member = None
            for name in z.namelist():
                if 'collection.anki2' in name:
                    db_member = name
                    break
            if not db_member:
                return 0
            # Extract to temp file
            with tempfile.NamedTemporaryFile(suffix='.anki2', delete=False) as tmp:
                tmp.write(z.read(db_member))
                tmp_path = tmp.name
            try:
                conn = sqlite3.connect(tmp_path)
                cur = conn.cursor()
                # Count cards (type=0 for cards, 1 for notes)
                result = cur.execute("SELECT COUNT(*) FROM cards").fetchone()
                return result[0] if result else 0
            finally:
                conn.close()
                try:
                    os.unlink(tmp_path)
                except Exception:
                    pass
    except Exception as e:
        return 0


def extract_title_from_md(md_path: Path) -> str:
    """Extract first H1 title from MD file."""
    try:
        content = md_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:
            content = md_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return md_path.stem

    # Match first # heading
    m = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        # Strip emoji at start
        return title
    return md_path.stem


def extract_description_from_md(md_path: Path, max_chars: int = 200) -> str:
    """Extract short description (paragraph after first H1)."""
    try:
        content = md_path.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:
            content = md_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return ''

    lines = content.split('\n')
    in_first_section = False
    desc_lines = []
    for line in lines:
        # Skip until first H1
        if line.startswith('# '):
            in_first_section = True
            continue
        # Skip until first H2 (next section)
        if in_first_section and line.startswith('## '):
            break
        # Skip blockquotes, empty lines
        if in_first_section and line.strip() and not line.startswith('>') and not line.startswith('*') and not line.startswith('#'):
            desc_lines.append(line.strip())
            if len(' '.join(desc_lines)) > max_chars:
                break
    return ' '.join(desc_lines)[:max_chars].strip()


def extract_date_from_name(name: str) -> str:
    """Extract YYYY-MM-DD from filename."""
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', name)
    if m:
        return f'{m.group(1)}-{m.group(2)}-{m.group(3)}'
    return ''


def normalized_tokens(text: str) -> set:
    """ASCII-ish tokens for fuzzy matching filenames/folders."""
    import unicodedata
    text = unicodedata.normalize('NFD', text.lower())
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn').replace('đ', 'd')
    stop = {'2026', 'bai', 'hoc', 'lesson', 'visual', 'summary', 'anki', 'cards', 'card'}
    return {t for t in re.sub(r'[^a-z0-9]+', ' ', text).split() if len(t) >= 3 and t not in stop}


def fuzzy_score(a: str, b: str) -> float:
    a_tokens = normalized_tokens(a)
    b_tokens = normalized_tokens(b)
    if not a_tokens or not b_tokens:
        return 0.0
    return len(a_tokens & b_tokens) / max(1, min(len(a_tokens), len(b_tokens)))


def find_source_file(lesson_name: str, suffix: str) -> Path:
    """Find source MD/cards by fuzzy name match in 09_Source - Markdown."""
    source_root = ROOT / '09_Source - Markdown'
    if not source_root.exists():
        return None
    best_score, best_path = 0.0, None
    for path in source_root.rglob(f'*{suffix}'):
        if path.name.startswith('citation_audit'):
            continue
        if suffix == '.json' and 'card' not in path.name.lower():
            continue
        score = fuzzy_score(lesson_name, f'{path.stem} {path.parent.name}')
        if score > best_score:
            best_score, best_path = score, path
    return best_path if best_score >= 0.45 else None


def detect_tags(folder_name: str, title: str, md_content: str = '') -> list:
    """Auto-detect tags from title and content."""
    text = (folder_name + ' ' + title + ' ' + md_content).lower()
    tags = []

    # Topic tags
    tag_keywords = {
        'IVF': ['ivf', 'thụ tinh ống nghiệm'],
        'ICSI': ['icsi'],
        'FET': ['fet', 'frozen embryo'],
        'ART': ['art'],
        'Endometriosis': ['endometriosis', 'lạc nội mạc'],
        'Adenomyosis': ['adenomyosis'],
        'Preeclampsia': ['preeclampsia', 'tiền sản giật', 'tién sản'],
        'OHSS': ['ohss'],
        'GnRH': ['gnrh'],
        'Progesterone': ['progesterone', 'luteal', 'pha hoàng thể'],
        'Doppler': ['doppler'],
        'Fetal Echo': ['tim thai', 'fetal echo', 'echocardiography'],
        'Cervical Length': ['cervical length', 'chiều dài cổ tử cung'],
        'First Trimester': ['first trimester', 'tam cá nguyệt 1', 'sàng lọc quý 1'],
        'FGR': ['fgr', 'fetal growth restriction'],
        'Labor': ['chuyển dạ', 'labor', 'parturition'],
        'Operative Vaginal Delivery': ['đẻ chỉ huy', 'ovd', 'vacuum', 'forceps'],
        'Twin Pregnancy': ['song thai', 'mcma', 'twin'],
        'IUI': ['iui'],
        'Asherman': ['asherman'],
        'DuoStim': ['duostim', 'nang ton du'],
        'Testosterone': ['testosterone', 'androgel'],
        'Uterus': ['tử cung', 'tu cung', 'hypoplastic', 'nhi hoa'],
        'Pregnancy': ['thai', 'pregnancy'],
        'GDM': ['gdm', 'đái tháo đường thai kỳ', 'gestational diabetes'],
        'AUB': ['aub', 'abnormal uterine bleeding', 'xuất huyết tử cung'],
        'PGT-A': ['pgt-a', 'preimplantation genetic testing', 'aneuploidy'],
        'Poor responder': ['poor ovarian response', 'poseidon', 'bologna', 'đáp ứng kém'],
        'HyCoSy': ['hycosy', 'hyfosy', 'tubal patency', 'vòi trứng'],
        'Amniotic fluid': ['nước ối', 'amniotic fluid', 'thiểu ối', 'đa ối'],
        'Biometry': ['sinh trắc', 'biometry', 'efw', 'hadlock'],
        'Anatomy scan': ['hình thái', 'anatomy scan', 'mid trimester'],
        'Neurosonography': ['neurosonography', 'thần kinh thai'],
        'Thyroid US': ['tuyến giáp', 'ti-rads', 'thyroid'],
        'Breast US': ['tuyến vú', 'bi-rads', 'breast'],
        'Abdominal US': ['ổ bụng', 'gan', 'túi mật', 'tụy', 'lách', 'thận'],
    }

    for tag, keywords in tag_keywords.items():
        if any(kw in text for kw in keywords):
            tags.append(tag)

    return sorted(set(tags))


def scan_lesson_folder(lesson_dir: Path) -> dict:
    """Scan a lesson folder for files."""
    files = {
        'md': None,
        'docx': None,
        'apkg': None,
        'html': None,
    }

    md_candidates = [m for m in lesson_dir.rglob('*.md') if not m.name.startswith('citation_audit')]
    if md_candidates:
        files['md'] = sorted(md_candidates, key=lambda p: p.stat().st_mtime, reverse=True)[0]
    else:
        files['md'] = find_source_file(lesson_dir.name, '.md')

    for kind, suffix in [('docx', '.docx'), ('apkg', '.apkg'), ('html', '.html')]:
        candidates = sorted(lesson_dir.rglob(f'*{suffix}'), key=lambda p: p.stat().st_mtime, reverse=True)
        if candidates:
            files[kind] = candidates[0]

    return files


def find_apkg(lesson_name: str, title: str) -> Path:
    """Search for APKG matching lesson."""
    apkg_dir = ROOT / '08_Anki Deck - apkg'
    best_score, best_path = 0.0, None
    for apkg in apkg_dir.glob('*.apkg'):
        score = max(fuzzy_score(lesson_name, apkg.stem), fuzzy_score(title, apkg.stem))
        if score > best_score:
            best_score, best_path = score, apkg
    return best_path if best_score >= 0.45 else None


def find_html(lesson_name: str, title: str) -> Path:
    """Search for HTML visual matching lesson."""
    html_dir = ROOT / '07_Visual Summary - HTML'
    best_score, best_path = 0.0, None
    for html in html_dir.glob('*.html'):
        score = max(fuzzy_score(lesson_name, html.stem), fuzzy_score(title, html.stem))
        if score > best_score:
            best_score, best_path = score, html
    return best_path if best_score >= 0.45 else None


def scan_all_lessons() -> list:
    """Scan all lesson folders and return list of lesson dicts."""
    lessons = []

    for specialty_dir in sorted(ROOT.iterdir()):
        if not specialty_dir.is_dir():
            continue
        if not any(specialty_dir.name.startswith(p) for p in SPECIALTY_MAP.keys()):
            continue

        specialty_key = specialty_dir.name
        if specialty_key not in SPECIALTY_MAP:
            continue

        specialty_info = SPECIALTY_MAP[specialty_key]

        # Find sub-folders
        subfolders = [d for d in specialty_dir.iterdir() if d.is_dir()]
        # Also look for .docx files directly in specialty folder (older style)
        docx_in_root = list(specialty_dir.glob('*.docx'))

        for sub in subfolders:
            # Skip empty folders
            has_files = any(sub.iterdir())
            if not has_files:
                continue
            lesson = build_lesson_dict(sub, specialty_key, specialty_info, sub.name)
            if lesson:
                # Skip if no actual content files
                if not any(lesson['files'].values()):
                    continue
                lessons.append(lesson)

        # Process orphan .docx files in specialty root
        for docx in docx_in_root:
            # Already counted via subfolder? Skip
            pass

    return lessons


def build_lesson_dict(lesson_dir: Path, specialty_key: str, specialty_info: dict, folder_name: str) -> dict:
    """Build lesson dict from a folder."""
    files = scan_lesson_folder(lesson_dir)

    # Title
    title = folder_name
    description = ''
    md_content = ''
    if files['md']:
        title = extract_title_from_md(files['md'])
        description = extract_description_from_md(files['md'])
        try:
            md_content = files['md'].read_text(encoding='utf-8', errors='ignore')[:5000]
        except Exception:
            pass
    else:
        # Try DOCX only
        if files['docx']:
            title = files['docx'].stem.replace('_', ' ').replace('-', ' ')

    # Date
    date = extract_date_from_name(folder_name)
    if not date and files['md']:
        date = extract_date_from_name(files['md'].name)
    if not date and files['docx']:
        date = extract_date_from_name(files['docx'].name)

    # Tags
    tags = detect_tags(folder_name, title, md_content)
    tags.append(specialty_info['short'])

    # Find APKG and HTML (in folder first, then global)
    apkg = files['apkg'] if files['apkg'] else find_apkg(folder_name, title)
    html = files['html'] if files['html'] else find_html(folder_name, title)

    # Count Anki cards
    apkg_cards = count_apkg_cards(apkg) if apkg else 0

    return {
        'title': title,
        'description': description or 'Bài học y khoa tổng hợp theo guideline hiện hành.',
        'specialty': specialty_info['name'],
        'specialty_key': specialty_key,
        'specialty_short': specialty_info['short'],
        'specialty_color': specialty_info['color'],
        'specialty_icon': specialty_info['icon'],
        'tags': tags,
        'date': date,
        'folder': str(lesson_dir.relative_to(ROOT)).replace('\\', '/'),
        'apkg_cards': apkg_cards,
        'files': {
            'md': str(files['md'].relative_to(ROOT)).replace('\\', '/') if files['md'] else None,
            'docx': str(files['docx'].relative_to(ROOT)).replace('\\', '/') if files['docx'] else None,
            'apkg': str(apkg.relative_to(ROOT)).replace('\\', '/') if apkg else None,
            'html': str(html.relative_to(ROOT)).replace('\\', '/') if html else None,
        },
    }


# ============================
# HTML GENERATION
# ============================

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thư viện Bài học Y khoa — Mavis</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            primary: {{
              50: '#fdf2f8', 100: '#fce7f3', 200: '#fbcfe8', 300: '#f9a8d4',
              400: '#f472b6', 500: '#ec4899', 600: '#db2777', 700: '#be185d',
              800: '#9d174d', 900: '#831843'
            }}
          }}
        }}
      }}
    }}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', system-ui, sans-serif; }}
    .card-hover {{ transition: all 0.2s ease; }}
    .card-hover:hover {{ transform: translateY(-4px); }}
    .tag-pill {{ transition: all 0.15s ease; }}
    .tag-pill.active {{
      background: linear-gradient(135deg, #ec4899, #be185d);
      color: white;
      box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3);
    }}
    .specialty-btn.active {{
      background: linear-gradient(135deg, #6366f1, #4338ca);
      color: white;
      transform: scale(1.05);
    }}
    .dark .specialty-btn.active {{
      background: linear-gradient(135deg, #818cf8, #6366f1);
    }}
    /* Scrollbar styling */
    ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: #d1d5db; border-radius: 5px; }}
    .dark ::-webkit-scrollbar-thumb {{ background: #4b5563; }}
    /* Smooth transitions */
    * {{ transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease; }}
    /* Hide cards filtered out */
    .lesson-card.hidden {{ display: none; }}
  </style>
</head>
<body class="bg-stone-50 dark:bg-stone-950 text-stone-800 dark:text-stone-100 min-h-screen">

  <!-- ========== HEADER ========== -->
  <header class="sticky top-0 z-40 bg-white/80 dark:bg-stone-900/80 backdrop-blur-lg border-b border-stone-200 dark:border-stone-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-4">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-2xl sm:text-3xl font-bold bg-gradient-to-r from-pink-600 to-purple-600 bg-clip-text text-transparent">
            📚 Thư viện Bài học Y khoa
          </h1>
          <p class="text-sm text-stone-500 dark:text-stone-400 mt-1">
            <span id="readCounter">{total_lessons} bài · {total_specialties} chuyên khoa · cập nhật {today}</span>
          </p>
        </div>
        <div class="flex items-center gap-3">
          <!-- Search box -->
          <div class="relative">
            <input id="searchInput" type="text" placeholder="🔍 Tìm bài..."
                   class="w-48 sm:w-64 pl-4 pr-4 py-2 rounded-xl bg-stone-100 dark:bg-stone-800 border border-stone-200 dark:border-stone-700 focus:outline-none focus:ring-2 focus:ring-pink-500 text-sm">
          </div>
          <!-- Dark mode toggle -->
          <button id="themeToggle" class="p-2 rounded-xl bg-stone-100 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 transition" aria-label="Toggle theme">
            <span class="dark:hidden">🌙</span>
            <span class="hidden dark:inline">☀️</span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 py-6 flex gap-6">

    <!-- ========== SIDEBAR FILTERS ========== -->
    <aside class="w-56 shrink-0 hidden md:block">
      <div class="sticky top-24 space-y-6">

        <!-- Specialty filter -->
        <div>
          <h3 class="text-xs font-bold uppercase text-stone-500 dark:text-stone-400 mb-3 tracking-wider">Chuyên khoa</h3>
          <div class="space-y-2" id="specialtyFilters">
            <button data-specialty="all" class="specialty-btn active w-full text-left px-3 py-2 rounded-lg text-sm font-medium bg-stone-200 dark:bg-stone-800 hover:bg-stone-300 dark:hover:bg-stone-700 transition">
              🌐 Tất cả ({total_lessons})
            </button>
            {specialty_buttons}
          </div>
        </div>

        <!-- Tag filter -->
        <div>
          <h3 class="text-xs font-bold uppercase text-stone-500 dark:text-stone-400 mb-3 tracking-wider">Tags phổ biến</h3>
          <div class="flex flex-wrap gap-1.5" id="tagFilters">
            {tag_buttons}
          </div>
        </div>

        <!-- Sort -->
        <div>
          <h3 class="text-xs font-bold uppercase text-stone-500 dark:text-stone-400 mb-3 tracking-wider">Sắp xếp</h3>
          <select id="sortSelect" class="w-full px-3 py-2 rounded-lg bg-stone-100 dark:bg-stone-800 border border-stone-200 dark:border-stone-700 text-sm focus:outline-none focus:ring-2 focus:ring-pink-500">
            <option value="date-desc">Mới nhất</option>
            <option value="date-asc">Cũ nhất</option>
            <option value="title-asc">A → Z</option>
            <option value="title-desc">Z → A</option>
          </select>
        </div>

        <!-- Stats -->
        <div class="p-4 rounded-xl bg-gradient-to-br from-pink-50 to-purple-50 dark:from-pink-950 dark:to-purple-950 border border-pink-200 dark:border-pink-900">
          <h3 class="text-xs font-bold uppercase text-pink-700 dark:text-pink-300 mb-2 tracking-wider">📊 Thống kê</h3>
          <div class="space-y-1 text-xs mb-3">
            <div class="flex justify-between"><span>Tổng bài:</span><strong>{total_lessons}</strong></div>
            <div class="flex justify-between"><span>Có DOCX:</span><strong>{count_docx}</strong></div>
            <div class="flex justify-between"><span>Có Anki:</span><strong>{count_apkg}</strong></div>
            <div class="flex justify-between"><span>Có Visual:</span><strong>{count_html}</strong></div>
          </div>
          <!-- Read progress -->
          <div class="border-t border-pink-200 dark:border-pink-800 pt-2 mt-2">
            <div class="flex justify-between text-xs mb-1">
              <span class="font-medium">📖 Đã đọc:</span>
              <strong id="readStat">0 / {total_lessons}</strong>
            </div>
            <div class="w-full bg-pink-200 dark:bg-pink-900 rounded-full h-2 overflow-hidden">
              <div id="readBar" class="bg-gradient-to-r from-pink-500 to-purple-500 h-2 rounded-full transition-all" style="width: 0%"></div>
            </div>
          </div>
        </div>

        <!-- Filter unread -->
        <div>
          <h3 class="text-xs font-bold uppercase text-stone-500 dark:text-stone-400 mb-3 tracking-wider">Lọc theo trạng thái</h3>
          <div class="space-y-1">
            <label class="flex items-center gap-2 text-sm cursor-pointer">
              <input type="checkbox" id="filterUnread" class="rounded">
              <span>Chỉ hiện chưa đọc</span>
            </label>
          </div>
        </div>

        <!-- Keyboard shortcuts -->
        <div>
          <h3 class="text-xs font-bold uppercase text-stone-500 dark:text-stone-400 mb-3 tracking-wider">⌨️ Phím tắt</h3>
          <div class="space-y-1 text-xs text-stone-600 dark:text-stone-400">
            <div class="flex justify-between"><kbd class="px-1.5 py-0.5 bg-stone-100 dark:bg-stone-800 rounded">/</kbd> <span>Search</span></div>
            <div class="flex justify-between"><kbd class="px-1.5 py-0.5 bg-stone-100 dark:bg-stone-800 rounded">Esc</kbd> <span>Reset</span></div>
            <div class="flex justify-between"><kbd class="px-1.5 py-0.5 bg-stone-100 dark:bg-stone-800 rounded">1/2/3</kbd> <span>Filter CK</span></div>
            <div class="flex justify-between"><kbd class="px-1.5 py-0.5 bg-stone-100 dark:bg-stone-800 rounded">u</kbd> <span>Toggle unread</span></div>
            <div class="flex justify-between"><kbd class="px-1.5 py-0.5 bg-stone-100 dark:bg-stone-800 rounded">d</kbd> <span>Toggle dark</span></div>
          </div>
        </div>
      </div>
    </aside>

    <!-- ========== MAIN GRID ========== -->
    <main class="flex-1">
      <!-- Filter info bar -->
      <div class="mb-4 flex items-center justify-between">
        <p id="filterInfo" class="text-sm text-stone-500 dark:text-stone-400">
          Hiển thị <span id="visibleCount">{total_lessons}</span> / {total_lessons} bài
        </p>
        <button id="resetFilters" class="text-xs text-pink-600 dark:text-pink-400 hover:underline hidden">
          ✕ Reset filter
        </button>
      </div>

      <!-- Cards grid -->
      <div id="cardsGrid" class="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-5">
        {cards}
      </div>

      <!-- Empty state -->
      <div id="emptyState" class="hidden text-center py-20 text-stone-400 dark:text-stone-600">
        <div class="text-6xl mb-4">🔍</div>
        <p class="text-lg">Không tìm thấy bài nào khớp filter.</p>
        <button onclick="resetFilters()" class="mt-4 px-4 py-2 rounded-lg bg-pink-600 text-white text-sm hover:bg-pink-700">
          Reset filter
        </button>
      </div>
    </main>
  </div>

  <!-- ========== FOOTER ========== -->
  <footer class="border-t border-stone-200 dark:border-stone-800 mt-12 py-6 text-center text-xs text-stone-500 dark:text-stone-400">
    <p>Thư viện Bài học Y khoa · Auto-generated by <strong>Mavis</strong></p>
    <p class="mt-1">Mở bằng trình duyệt (Chrome/Edge/Firefox) · {today}</p>
  </footer>

  <!-- ========== JAVASCRIPT ========== -->
  <script>
    const lessons = {lessons_json};

    // Theme toggle
    const themeToggle = document.getElementById('themeToggle');
    const html = document.documentElement;
    if (localStorage.getItem('library-theme') === 'dark' || (!localStorage.getItem('library-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
      html.classList.add('dark');
    }}
    themeToggle.addEventListener('click', () => {{
      html.classList.toggle('dark');
      localStorage.setItem('library-theme', html.classList.contains('dark') ? 'dark' : 'light');
    }});

    // ========== READ TRACKING ==========
    function getReadMap() {{
      try {{ return JSON.parse(localStorage.getItem('library-read') || '{{}}'); }}
      catch (e) {{ return {{}}; }}
    }}
    function setReadMap(map) {{
      localStorage.setItem('library-read', JSON.stringify(map));
    }}
    function isRead(id) {{
      return !!getReadMap()[id];
    }}
    function setRead(id, val) {{
      const map = getReadMap();
      if (val) map[id] = Date.now();
      else delete map[id];
      setReadMap(map);
    }}

    // Apply read state to all cards on load
    function applyReadBadges() {{
      const readMap = getReadMap();
      const cards = document.querySelectorAll('.lesson-card');
      cards.forEach(card => {{
        const id = card.dataset.lessonId;
        const badge = card.querySelector('.read-badge');
        const btn = card.querySelector('.toggle-read-btn');
        if (readMap[id]) {{
          badge?.classList.remove('hidden');
          card.classList.add('opacity-70');
          card.classList.add('ring-2');
          card.classList.add('ring-emerald-200');
          card.classList.add('dark:ring-emerald-800');
          if (btn) btn.innerHTML = '☑ Đã đọc';
        }} else {{
          badge?.classList.add('hidden');
          card.classList.remove('opacity-70');
          card.classList.remove('ring-2');
          card.classList.remove('ring-emerald-200');
          card.classList.remove('dark:ring-emerald-800');
          if (btn) btn.innerHTML = '☐ Đánh dấu đã đọc';
        }}
      }});
      updateReadStats();
    }}

    function updateReadStats() {{
      const readMap = getReadMap();
      const total = document.querySelectorAll('.lesson-card').length;
      const read = Object.keys(readMap).length;
      document.getElementById('readStat').textContent = `${{read}} / ${{total}}`;
      const pct = total > 0 ? Math.round(read / total * 100) : 0;
      document.getElementById('readBar').style.width = pct + '%';
    }}

    window.toggleRead = function(btn) {{
      const card = btn.closest('.lesson-card');
      const id = card.dataset.lessonId;
      setRead(id, !isRead(id));
      applyReadBadges();
      render();
    }};

    // ========== OPEN ALL FILES ==========
    window.openAll = function(btn) {{
      const filesStr = btn.dataset.files;
      if (!filesStr) return;
      const files = filesStr.split('|').filter(f => f);
      files.forEach((f, i) => {{
        // Open all in separate tabs (browser may block >2-3 popups without user gesture; we're already in click handler so OK)
        setTimeout(() => window.open(f, '_blank'), i * 100);
      }});
    }};

    // ========== STATE ==========
    let currentSpecialty = 'all';
    let currentTags = new Set();
    let currentSearch = '';
    let unreadOnly = false;

    function render() {{
      const grid = document.getElementById('cardsGrid');
      const cards = grid.querySelectorAll('.lesson-card');
      let visible = 0;

      cards.forEach(card => {{
        const specialty = card.dataset.specialty;
        const tags = card.dataset.tags.split(',');
        const title = card.dataset.title.toLowerCase();
        const desc = card.dataset.desc.toLowerCase();
        const id = card.dataset.lessonId;

        const matchSpecialty = currentSpecialty === 'all' || specialty === currentSpecialty;
        const matchTags = currentTags.size === 0 || [...currentTags].every(t => tags.includes(t));
        const matchSearch = !currentSearch || title.includes(currentSearch) || desc.includes(currentSearch) || tags.some(t => t.toLowerCase().includes(currentSearch));
        const matchUnread = !unreadOnly || !isRead(id);

        if (matchSpecialty && matchTags && matchSearch && matchUnread) {{
          card.classList.remove('hidden');
          visible++;
        }} else {{
          card.classList.add('hidden');
        }}
      }});

      document.getElementById('visibleCount').textContent = visible;
      document.getElementById('emptyState').classList.toggle('hidden', visible > 0);
      document.getElementById('resetFilters').classList.toggle('hidden', currentSpecialty === 'all' && currentTags.size === 0 && !currentSearch && !unreadOnly);

      // Sort
      const sortVal = document.getElementById('sortSelect').value;
      const sortedCards = [...cards].sort((a, b) => {{
        if (sortVal === 'title-asc') return a.dataset.title.localeCompare(b.dataset.title);
        if (sortVal === 'title-desc') return b.dataset.title.localeCompare(a.dataset.title);
        if (sortVal === 'date-asc') return (a.dataset.date || '').localeCompare(b.dataset.date || '');
        return (b.dataset.date || '').localeCompare(a.dataset.date || '');
      }});
      sortedCards.forEach(c => grid.appendChild(c));
    }}

    // ========== FILTERS ==========
    document.querySelectorAll('.specialty-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.specialty-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentSpecialty = btn.dataset.specialty;
        render();
      }});
    }});

    document.querySelectorAll('.tag-pill').forEach(pill => {{
      pill.addEventListener('click', () => {{
        const tag = pill.dataset.tag;
        if (currentTags.has(tag)) {{
          currentTags.delete(tag);
          pill.classList.remove('active');
        }} else {{
          currentTags.add(tag);
          pill.classList.add('active');
        }}
        render();
      }});
    }});

    document.getElementById('searchInput').addEventListener('input', e => {{
      currentSearch = e.target.value.toLowerCase().trim();
      render();
    }});

    document.getElementById('sortSelect').addEventListener('change', render);
    document.getElementById('filterUnread').addEventListener('change', e => {{
      unreadOnly = e.target.checked;
      render();
    }});

    // ========== RELATED LINKS (smooth scroll) ==========
    document.addEventListener('click', e => {{
      const link = e.target.closest('.related-link');
      if (link) {{
        e.preventDefault();
        const targetId = link.dataset.relatedId;
        const target = document.getElementById('lesson-' + targetId);
        if (target) {{
          target.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          target.classList.add('ring-4', 'ring-pink-400');
          setTimeout(() => target.classList.remove('ring-4', 'ring-pink-400'), 2000);
        }}
      }}
    }});

    // ========== KEYBOARD SHORTCUTS ==========
    document.addEventListener('keydown', e => {{
      // Ignore if typing in input
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {{
        if (e.key === 'Escape') {{
          e.target.blur();
          resetFilters();
          e.preventDefault();
        }}
        return;
      }}

      if (e.key === '/') {{
        e.preventDefault();
        document.getElementById('searchInput').focus();
      }} else if (e.key === 'Escape') {{
        resetFilters();
      }} else if (e.key === '1') {{
        // First specialty button
        const btns = document.querySelectorAll('.specialty-btn');
        if (btns[1]) btns[1].click();
      }} else if (e.key === '2') {{
        const btns = document.querySelectorAll('.specialty-btn');
        if (btns[2]) btns[2].click();
      }} else if (e.key === '3') {{
        const btns = document.querySelectorAll('.specialty-btn');
        if (btns[3]) btns[3].click();
      }} else if (e.key === '0' || e.key.toLowerCase() === 'a') {{
        const btns = document.querySelectorAll('.specialty-btn');
        if (btns[0]) btns[0].click();
      }} else if (e.key.toLowerCase() === 'u') {{
        const cb = document.getElementById('filterUnread');
        cb.checked = !cb.checked;
        cb.dispatchEvent(new Event('change'));
      }} else if (e.key.toLowerCase() === 'd') {{
        themeToggle.click();
      }}
    }});

    // ========== RESET ==========
    function resetFilters() {{
      currentSpecialty = 'all';
      currentTags.clear();
      currentSearch = '';
      unreadOnly = false;
      document.getElementById('searchInput').value = '';
      document.getElementById('filterUnread').checked = false;
      document.querySelectorAll('.specialty-btn').forEach(b => b.classList.toggle('active', b.dataset.specialty === 'all'));
      document.querySelectorAll('.tag-pill').forEach(p => p.classList.remove('active'));
      render();
    }}
    document.getElementById('resetFilters').addEventListener('click', resetFilters);
    window.resetFilters = resetFilters;

    // Initial apply
    applyReadBadges();
    render();
  </script>
</body>
</html>
'''


# Card template
CARD_TEMPLATE = '''<article id="lesson-{lesson_id}" class="lesson-card card-hover bg-white dark:bg-stone-900 rounded-2xl border border-stone-200 dark:border-stone-800 p-5 flex flex-col relative scroll-mt-24"
             data-specialty="{specialty_short}"
             data-tags="{tags_csv}"
             data-title="{title_search}"
             data-desc="{description_search}"
             data-date="{date}"
             data-lesson-id="{lesson_id}">
  <!-- Read status badge -->
  <div class="read-badge hidden absolute top-3 right-3 px-2 py-0.5 rounded-full text-xs font-semibold bg-emerald-100 dark:bg-emerald-900 text-emerald-700 dark:text-emerald-300">
    ✓ Đã đọc
  </div>

  <div class="flex items-start justify-between mb-3 pr-16">
    <span class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold bg-{color}-100 dark:bg-{color}-900 text-{color}-700 dark:text-{color}-300">
      {icon} {specialty_short}
    </span>
    <span class="text-xs text-stone-400">{date_display}</span>
  </div>

  <h3 class="text-lg font-bold leading-tight mb-2 line-clamp-2">
    {title}
  </h3>

  <p class="text-sm text-stone-600 dark:text-stone-400 mb-4 line-clamp-3 flex-1">
    {description}
  </p>

  <!-- Tags -->
  <div class="flex flex-wrap gap-1 mb-3">
    {tag_pills}
  </div>

  <!-- APKG card count -->
  {apkg_badge}

  <!-- Related lessons -->
  {related_section}

  <!-- File links -->
  <div class="flex flex-wrap gap-1.5 pt-3 border-t border-stone-100 dark:border-stone-800">
    {file_links}
  </div>

  <!-- Action buttons -->
  <div class="flex flex-wrap gap-1.5 mt-2">
    <button onclick="openAll(this)" data-files="{files_csv}" class="open-all-btn text-xs px-2.5 py-1 rounded-lg bg-pink-100 dark:bg-pink-900 text-pink-700 dark:text-pink-300 hover:bg-pink-200 dark:hover:bg-pink-800 transition font-medium" title="Mở tất cả file của bài này">
      📂 Open all ({file_count})
    </button>
    <button onclick="toggleRead(this)" data-id="{lesson_id}" class="toggle-read-btn text-xs px-2.5 py-1 rounded-lg bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 hover:bg-stone-200 dark:hover:bg-stone-700 transition font-medium" title="Đánh dấu đã đọc / chưa đọc">
      ☐ Đánh dấu đã đọc
    </button>
    {show_folder_btn}
  </div>
</article>'''


def lesson_id_from_title(title: str) -> str:
    """Generate URL-safe ID from title."""
    import re as _re
    slug = _re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')
    return slug[:50]


def find_related_lessons(lesson: dict, all_lessons: list, max_n: int = 3) -> list:
    """Find related lessons: same specialty + share at least 1 tag."""
    related = []
    lesson_tags = set(lesson['tags'])
    for other in all_lessons:
        if other['title'] == lesson['title']:
            continue
        if other['specialty_short'] != lesson['specialty_short']:
            continue
        other_tags = set(other['tags'])
        shared = lesson_tags & other_tags
        if shared:
            related.append({
                'id': lesson_id_from_title(other['title']),
                'title': other['title'],
                'shared_tags': list(shared),
                'shared_count': len(shared),
            })
    # Sort by shared tag count desc, then by date desc
    related.sort(key=lambda x: (-x['shared_count'], x['title']))
    return related[:max_n]


def render_card(lesson: dict, all_lessons: list = None, path_mode: str = 'relative') -> str:
    """Render a single lesson card with all features.

    path_mode:
    - 'relative' (default): paths relative to library/ folder (../../F:/.../file)
    - 'absolute': file:// URLs (works when HTML is moved anywhere)
    """
    # HTML escape
    def esc(s):
        return str(s).replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

    title_display = esc(lesson['title'])
    desc_display = esc(lesson['description'][:200])
    if len(lesson['description']) > 200:
        desc_display += '...'

    title_search = lesson['title'].lower()
    desc_search = lesson['description'].lower()

    # Color
    color_map = {
        'pink': 'pink', 'purple': 'purple', 'cyan': 'cyan',
        'teal': 'teal', 'amber': 'amber', 'green': 'green', 'red': 'red',
    }
    color = color_map.get(lesson['specialty_color'], 'pink')

    # Date display
    date_display = lesson['date'] if lesson['date'] else '—'

    # Tags
    tags_csv = ','.join(lesson['tags'])

    # Tag pills (limit 6 to avoid clutter)
    tag_pills = ''
    for tag in lesson['tags'][:6]:
        tag_pills += f'<span class="text-xs px-2 py-0.5 rounded-full bg-stone-100 dark:bg-stone-800 text-stone-600 dark:text-stone-300">{esc(tag)}</span>\n    '

    # APKG card count badge
    apkg_badge = ''
    if lesson.get('apkg_cards', 0) > 0:
        apkg_badge = f'<div class="mb-2"><span class="inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full bg-orange-100 dark:bg-orange-900 text-orange-700 dark:text-orange-300 font-medium">🎴 {lesson["apkg_cards"]} Anki cards</span></div>'

    # Related lessons section
    related_section = ''
    if all_lessons:
        related = find_related_lessons(lesson, all_lessons, max_n=3)
        if related:
            related_html = '<div class="mb-3 p-2 rounded-lg bg-stone-50 dark:bg-stone-800/50 border border-stone-100 dark:border-stone-800"><div class="text-xs font-semibold text-stone-500 dark:text-stone-400 mb-1.5">🔗 Bài liên quan:</div>'
            for r in related:
                related_html += f'<a href="#lesson-{esc(r["id"])}" data-related-id="{esc(r["id"])}" class="related-link block text-xs text-pink-600 dark:text-pink-400 hover:underline truncate" title="{esc(r["title"])}">→ {esc(r["title"][:55])}</a>\n      '
            related_html += '</div>'
            related_section = related_html

    # File links (relative paths from library/ OR absolute file:// URLs)
    file_links = ''
    files_for_csv = []
    file_count = 0
    icon_map = {
        'md': ('📝', 'MD', 'gray'),
        'docx': ('📄', 'DOCX', 'blue'),
        'apkg': ('🎴', 'Anki', 'orange'),
        'html': ('📊', 'Visual', 'emerald'),
    }

    for file_type, (icon, label, color_name) in icon_map.items():
        if lesson['files'].get(file_type):
            path = lesson['files'][file_type]
            # Build URL based on path_mode
            if path_mode == 'absolute':
                abs_path = str(ROOT / path).replace('\\', '/')
                href = 'file:///' + abs_path.replace(' ', '%20').replace('#', '%23')
            else:
                href = f'../../{path}'
            files_for_csv.append(href)
            file_count += 1
            file_links += f'<a href="{href}" target="_blank" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg text-xs font-medium bg-{color_name}-100 dark:bg-{color_name}-900 text-{color_name}-700 dark:text-{color_name}-300 hover:bg-{color_name}-200 dark:hover:bg-{color_name}-800 transition" title="{path}">{icon} {label}</a>\n    '

    files_csv = '|'.join(files_for_csv)

    # Show folder button (open file:// to folder containing first file)
    show_folder_btn = ''
    if file_count > 0:
        # Find first non-empty file path
        first_file_path = None
        for ft in ['docx', 'md', 'apkg', 'html']:
            if lesson['files'].get(ft):
                first_file_path = lesson['files'][ft]
                break
        if first_file_path:
            folder_path = '/'.join(first_file_path.split('/')[:-1])
            if path_mode == 'absolute':
                abs_folder = str(ROOT / folder_path).replace('\\', '/')
                folder_url = 'file:///' + abs_folder.replace(' ', '%20')
            else:
                folder_url = f'../../{folder_path}'
            show_folder_btn = f'<button onclick="window.open(\'{folder_url}/\', \'_blank\')" class="text-xs px-2.5 py-1 rounded-lg bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 hover:bg-stone-200 dark:hover:bg-stone-700 transition font-medium" title="Mở folder chứa bài trong trình duyệt">📁 Folder</button>'

    # Lesson ID
    lesson_id = lesson_id_from_title(lesson['title'])

    return CARD_TEMPLATE.format(
        specialty_short=lesson['specialty_short'],
        color=color,
        icon=lesson['specialty_icon'],
        date_display=date_display,
        title=title_display,
        title_search=title_search,
        description=desc_display,
        description_search=desc_search,
        tags_csv=tags_csv,
        tag_pills=tag_pills,
        apkg_badge=apkg_badge,
        related_section=related_section,
        file_links=file_links,
        files_csv=files_csv,
        file_count=file_count,
        show_folder_btn=show_folder_btn,
        date=lesson['date'],
        lesson_id=lesson_id,
    )


def main():
    import sys
    # CLI: python build_library_dashboard.py [--mode relative|absolute] [--out path]
    path_mode = 'relative'
    output_path = None
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--mode' and i + 1 < len(args):
            path_mode = args[i + 1]
            i += 2
        elif args[i] == '--out' and i + 1 < len(args):
            output_path = Path(args[i + 1])
            i += 2
        else:
            i += 1

    print(f'Mode: {path_mode}')
    if output_path:
        print(f'Output: {output_path}')

    print('Scanning lesson folders...')
    lessons = scan_all_lessons()
    print(f'Found {len(lessons)} lessons')

    # Sort by date desc
    lessons.sort(key=lambda x: (x['date'] or '', x['title']), reverse=True)

    # Stats
    count_docx = sum(1 for l in lessons if l['files'].get('docx'))
    count_apkg = sum(1 for l in lessons if l['files'].get('apkg'))
    count_html = sum(1 for l in lessons if l['files'].get('html'))

    # Specialty buttons
    specialty_counts = {}
    for l in lessons:
        specialty_counts[l['specialty_short']] = specialty_counts.get(l['specialty_short'], 0) + 1

    specialty_buttons = ''
    # Build buttons per unique specialty (NOT per lesson)
    unique_specialties = {}
    for l in lessons:
        if l['specialty_short'] not in unique_specialties:
            unique_specialties[l['specialty_short']] = {
                'full': l['specialty'],
                'icon': l['specialty_icon'],
                'color': l['specialty_color'],
            }

    # Sort specialties by count desc
    sorted_specialties = sorted(unique_specialties.items(), key=lambda x: -specialty_counts.get(x[0], 0))

    for sp_short, sp_info in sorted_specialties:
        sp_full = sp_info['full']
        icon = sp_info['icon']
        count = specialty_counts.get(sp_short, 0)
        specialty_buttons += f'<button data-specialty="{sp_short}" class="specialty-btn w-full text-left px-3 py-2 rounded-lg text-sm font-medium bg-stone-100 dark:bg-stone-800 hover:bg-stone-200 dark:hover:bg-stone-700 transition">{icon} {sp_full} ({count})</button>\n            '

    # Tag buttons (top 15 most common)
    tag_counts = {}
    for l in lessons:
        for tag in l['tags']:
            if tag == l['specialty_short']:
                continue
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    top_tags = sorted(tag_counts.items(), key=lambda x: -x[1])[:18]
    tag_buttons = ''
    for tag, count in top_tags:
        tag_buttons += f'<button data-tag="{tag}" class="tag-pill text-xs px-2.5 py-1 rounded-full bg-stone-100 dark:bg-stone-800 text-stone-700 dark:text-stone-300 hover:bg-stone-200 dark:hover:bg-stone-700">{tag} ({count})</button>\n            '

    # Cards
    cards = '\n'.join(render_card(l, all_lessons=lessons, path_mode=path_mode) for l in lessons)

    # Today
    today = datetime.now().strftime('%Y-%m-%d')

    # Final HTML
    html = HTML_TEMPLATE.format(
        total_lessons=len(lessons),
        total_specialties=len(specialty_counts),
        today=today,
        specialty_buttons=specialty_buttons,
        tag_buttons=tag_buttons,
        cards=cards,
        count_docx=count_docx,
        count_apkg=count_apkg,
        count_html=count_html,
        lessons_json=json.dumps([{'title': l['title'], 'specialty': l['specialty_short']} for l in lessons], ensure_ascii=False),
    )

    final_path = output_path if output_path else OUTPUT_HTML
    final_path.parent.mkdir(parents=True, exist_ok=True)
    final_path.write_text(html, encoding='utf-8')
    print(f'Saved: {final_path}')
    print(f'  - {len(lessons)} lessons')
    print(f'  - {count_docx} DOCX, {count_apkg} APKG, {count_html} HTML')


if __name__ == '__main__':
    main()
