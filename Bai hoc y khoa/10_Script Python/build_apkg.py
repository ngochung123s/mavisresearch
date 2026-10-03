"""build_apkg.py — script thống nhất build APKG cho mọi bài học.

Usage:
    python build_apkg.py <cards.v2.json>
    python build_apkg.py <cards.v2.json> --output "path/to/output.apkg"
    python build_apkg.py <cards.v2.json> --verify

Auto-detect:
    - Format: V2 ([{type, front, back, text}]) hoặc V1 ({"deck_name", "cards": [{front, back}]})
    - Specialty folder từ path (01_San phu khoa, 02_Ho tro sinh san ART, 03_Sieu am thai)
    - Model ID / Deck ID ổn định từ hash(tên + ngày)

Output: file .apkg trong folder chuyên khoa tương ứng.
Exit code: 0 = OK, 1 = diacritics WARN, 2 = FAIL.
"""
import sys
import re
import hashlib
import json
import html as html_lib
import warnings
from pathlib import Path

# Force UTF-8 stdout for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Suppress genanki HTML warnings for cloze cards (comparisons like "HbA1c <{{c1::6.0%}}" trigger harmless warnings)
warnings.filterwarnings('ignore', category=UserWarning, module='genanki')

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from lesson_builder import (
    build_pastel_model_and_deck,
    build_pastel_cloze_model,
    add_cards_from_json,
    add_cards_from_json_v2,
    add_card_to_deck,
    write_apkg,
    _check_json_diacritics,
)
import genanki


def stable_id(seed_str):
    """Tạo model_id / deck_id ổn định (13-digit) từ hash của seed string."""
    h = hashlib.md5(seed_str.encode()).hexdigest()[:12]
    return int(h, 16) % 9000000000000 + 1000000000000


def detect_specialty(cards_path):
    """Auto-detect specialty folder từ path của cards JSON."""
    path_str = str(cards_path).lower()
    if 'san_phu_khoa' in path_str or '01_san' in path_str:
        return PROJECT_ROOT / '01_San phu khoa'
    elif 'ho_tro_sinh_san' in path_str or '02_ho' in path_str or 'art' in path_str:
        return PROJECT_ROOT / '02_Ho tro sinh san ART'
    elif 'sieu_am_thai' in path_str or '03_sie' in path_str:
        return PROJECT_ROOT / '03_Sieu am thai'
    elif '11_noi' in path_str or 'noi khoa' in path_str:
        return PROJECT_ROOT / '11_Noi khoa'
    else:
        return PROJECT_ROOT / '08_Anki Deck - apkg'


def detect_main_deck(cards_path):
    """Auto-detect Anki main deck name từ path.
    
    Quy tắc đặt tên deck (AGENTS.md):
    - ART                  ← 02_Ho tro sinh san ART
    - Fetal ultrasound     ← 03_Sieu am thai
    - OB/GYN               ← 01_San phu khoa
    """
    path_str = str(cards_path).lower()
    if 'san_phu_khoa' in path_str or '01_san' in path_str:
        return 'OB/GYN'
    elif 'ho_tro_sinh_san' in path_str or '02_ho' in path_str or 'art' in path_str:
        return 'ART'
    elif 'sieu_am_thai' in path_str or '03_sie' in path_str:
        return 'Fetal ultrasound'
    elif '11_noi' in path_str or 'noi khoa' in path_str:
        return 'Internal medicine'
    elif '12_nhi' in path_str or 'nhi khoa' in path_str:
        return 'Nhi khoa Y6'
    else:
        return 'Medical'


def detect_date_from_path(cards_path):
    """Extract YYYY-MM-DD from path or filename."""
    m = re.search(r'(\d{4}-\d{2}-\d{2})', str(cards_path))
    return m.group(1) if m else None


def build_apkg(cards_json_path, output_path=None, deck_name=None):
    """Build APKG từ cards JSON. Tự động detect format V1/V2."""
    cards_json_path = Path(cards_json_path).resolve()
    if not cards_json_path.exists():
        print(f"  [APKG ERROR] File không tồn tại: {cards_json_path}")
        return 2

    # Detect format
    with open(cards_json_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    date = detect_date_from_path(cards_json_path)
    stem = cards_json_path.stem.replace('.cards', '').replace('.v2', '')
    topic = stem.replace('_', ' ')

    # Determine output path
    if output_path:
        output_path = Path(output_path)
    else:
        specialty_dir = detect_specialty(cards_json_path)
        parent_dir = cards_json_path.parent
        # If cards are in a subfolder like "01_San phu khoa/08_GDM/GDM_Comprehensive/", use that folder
        if specialty_dir in parent_dir.parents or parent_dir == specialty_dir:
            out_dir = parent_dir
        else:
            out_dir = specialty_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        output_path = out_dir / f"Anki - {stem} - {date or 'undated'}.apkg"

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Generate stable IDs
    seed = stem + (date or '')
    basic_model_id = stable_id(seed + '_basic')
    cloze_model_id = stable_id(seed + '_cloze')
    deck_id = stable_id(seed + '_deck')
    main_deck = detect_main_deck(cards_json_path)
    topic_short = stem
    # Remove date suffix from topic for cleaner display
    if date:
        topic_short = stem.replace('_' + date, '').replace(date, '')
    if deck_name:
        deck_full = deck_name
    elif isinstance(raw_data, dict) and raw_data.get('topic'):
        deck_full = raw_data['topic']
    else:
        deck_full = f'{main_deck}::{topic_short}::{date or ""}'.rstrip(':')

    print(f"\n{'='*60}")
    print(f"  BUILD APKG")
    print(f"  Source: {cards_json_path.name}")
    print(f"  Output: {output_path}")
    print(f"  Deck: {deck_full}")
    print(f"{'='*60}")

    # Normalize cards list and detect V1 vs V2
    if isinstance(raw_data, list):
        cards_list = raw_data
        is_v2 = True
    elif isinstance(raw_data, dict) and 'cards' in raw_data:
        cards_list = raw_data['cards']
        is_v2 = any(isinstance(c, dict) and 'type' in c for c in cards_list)
    else:
        cards_list = []
        is_v2 = False

    # DIACRITICS CHECK — run before build
    vn_diac, vn_total, ratio = _check_json_diacritics(cards_list)
    status = 'OK' if ratio >= 0.80 else 'WARN' if ratio >= 0.50 else 'FAIL'
    print(f"  {status}: Diacritics {ratio:.1%} ({vn_diac}/{vn_total} tu VN co dau)")

    if status == 'FAIL':
        print(f"  [APKG BLOCK] Diacritics ratio < 50% — KHÔNG build. Kiểm tra file JSON encoding!")
        return 2

    # Build
    if is_v2:
        # V2 format
        basic_model = build_pastel_model_and_deck(
            model_id=basic_model_id,
            model_name=f'{stem}_Basic_Pastel',
            deck_id=deck_id,
            deck_name=deck_full,
            deck_description=f'{topic} - {date or ""}',
        )[0]

        cloze_model = build_pastel_cloze_model(
            model_id=cloze_model_id,
            model_name=f'{stem}_Cloze_Pastel'
        )

        deck = genanki.Deck(deck_id, deck_full)
        deck.description = f'{topic} - {date or ""}'

        basic_count = 0
        cloze_count = 0
        for card in cards_list:
            card_type = card.get('type', 'basic')
            raw_tags = card.get('tags', [])
            if isinstance(raw_tags, list):
                tag_list = [str(t).replace(' ', '_') for t in raw_tags if t]
                tag_str = ' '.join(f'<span class="tag">{html_lib.escape(str(t))}</span>' for t in raw_tags if t)
            elif isinstance(raw_tags, str) and raw_tags:
                tag_list = [raw_tags.replace(' ', '_')]
                tag_str = f'<span class="tag">{html_lib.escape(raw_tags)}</span>'
            else:
                tag_list = []
                tag_str = ''

            if card_type == 'basic':
                front = html_lib.escape(card.get('front', ''))
                back = card.get('back', '')
                extra = card.get('extra', '')
                if extra:
                    back = back + ('<br><br>' + html_lib.escape(extra) if back else html_lib.escape(extra))
                note = genanki.Note(model=basic_model, fields=[front, back, tag_str], tags=tag_list)
                deck.add_note(note)
                basic_count += 1
            elif card_type == 'cloze':
                text = card.get('text', '')
                extra = html_lib.escape(card.get('extra', ''))
                note = genanki.Note(model=cloze_model, fields=[text, extra], tags=tag_list)
                deck.add_note(note)
                cloze_count += 1
        write_apkg(deck, str(output_path))
        total = basic_count + cloze_count
        print(f"  [APKG] Built {total} cards ({basic_count} basic + {cloze_count} cloze)")
        print(f"  [APKG] IDs: basic={basic_model_id}, cloze={cloze_model_id}, deck={deck_id}")
        print(f"  [APKG] Saved: {output_path}")

    else:
        # V1 format (legacy)
        deck_name = raw_data.get('deck_name', topic) if isinstance(raw_data, dict) else topic
        model, deck = build_pastel_model_and_deck(
            model_id=basic_model_id,
            model_name=f'{stem}_Pastel',
            deck_id=deck_id,
            deck_name=deck_name,
            deck_description=f'{topic} - {date or ""}',
        )
        n_cards = add_cards_from_json(deck, model, str(cards_json_path), topic)
        write_apkg(deck, str(output_path))
        total = n_cards
        print(f"  [APKG] Built {total} cards (V1 legacy format)")
        print(f"  [APKG] Saved: {output_path}")

    if status == 'WARN':
        return 1
    return 0


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='Build APKG from cards JSON (V1 or V2)')
    ap.add_argument('cards_json', help='Path to cards.json hoặc cards.v2.json')
    ap.add_argument('--output', '-o', help='Output .apkg path (auto-detect nếu không chỉ định)')
    ap.add_argument('--deck', '-d', help='Tên deck đầy đủ (ghi đè auto-detect)')
    ap.add_argument('--verify', '-v', action='store_true', help='Chạy verify_apkg_diacritics sau build')
    args = ap.parse_args()

    rc = build_apkg(args.cards_json, args.output, deck_name=args.deck)
    if args.verify and rc != 2:
        out_path = args.output or Path(args.cards_json).parent / f"Anki - {Path(args.cards_json).stem.replace('.cards','').replace('.v2','')} - {detect_date_from_path(args.cards_json) or 'undated'}.apkg"
        if Path(out_path).exists():
            print()
            import subprocess
            vr = subprocess.run(
                [sys.executable, str(SCRIPT_DIR / 'verify_apkg_diacritics.py'), str(out_path)],
                capture_output=True, text=True
            )
            print(vr.stdout)
            if vr.returncode != 0:
                print(vr.stderr)
                rc = max(rc, vr.returncode)

    sys.exit(rc)
