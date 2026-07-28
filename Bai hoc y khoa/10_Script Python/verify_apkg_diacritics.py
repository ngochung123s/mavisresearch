"""verify_apkg_diacritics.py — Đọc file .apkg, kiểm tra dấu tiếng Việt trong tất cả fields.

Logic:
- Mở .apkg (ZIP chứa SQLite collection.anki2)
- Đọc tất cả notes → lấy fields
- Strip HTML tags → phân loại từ: vn_diac / vn_no_diac / other
- Ratio = vn_diac / (vn_diac + vn_no_diac)
- Threshold: < 0.80 → FAIL, < 0.50 → BLOCK

Usage:
    python verify_apkg_diacritics.py <file.apkg>
    python verify_apkg_diacritics.py --all  # scan tất cả .apkg trong project

Exit code: 0 = OK, 1 = WARN (<80%), 2 = BLOCK (<50%)
"""
import sys
import re
import zipfile
import sqlite3
import tempfile
import shutil
from pathlib import Path

# Force UTF-8 stdout for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Vietnamese diacritics (có dấu)
VIETNAMESE_DIACRITICS = set(
    "àáảãạằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ"
    "ÀÁẢÃẠẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘỜỚỞỠỢÙÚỦŨỤỪỨỬỮỰỲÝỶỸỴ"
)
VN_SPECIAL_LETTERS = set("ăâđêôơưĂÂĐÊÔƠƯ")


def classify_word(word):
    """Phân loại từ: 'vn_diac' | 'vn_no_diac' | 'other'."""
    clean = re.sub(r'[^\wăâđêôơưĂÂĐÊÔƠƯ]', '', word, flags=re.UNICODE)
    if not clean:
        return 'other'
    if clean.isdigit():
        return 'other'
    has_diac = any(c in VIETNAMESE_DIACRITICS for c in clean)
    if has_diac:
        return 'vn_diac'
    has_vn_special = any(c in VN_SPECIAL_LETTERS for c in clean)
    if has_vn_special:
        return 'vn_no_diac'
    if all(c.isascii() for c in clean):
        return 'other'
    return 'other'


def count_words_classified(text):
    """Đếm từ theo loại sau khi strip HTML."""
    # Strip HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Remove HTML entities
    text = re.sub(r'&[a-z]+;', ' ', text)
    # Remove cloze markers
    text = re.sub(r'\{\{c\d+::', '', text)
    text = text.replace('}}', '')
    words = text.split()
    vn_diac = 0
    vn_no_diac = 0
    other = 0
    for w in words:
        if len(w) < 2:
            continue
        if not any(c.isalpha() for c in w):
            continue
        cls = classify_word(w)
        if cls == 'vn_diac':
            vn_diac += 1
        elif cls == 'vn_no_diac':
            vn_no_diac += 1
        else:
            other += 1
    return vn_diac, vn_no_diac, other


def verify_apkg(apkg_path):
    """Verify 1 file .apkg. Returns (ratio, vn_diac, vn_total, notes_count, cards_count)."""
    apkg_path = Path(apkg_path)
    tmp_dir = tempfile.mkdtemp(prefix='apkg_check_')
    try:
        with zipfile.ZipFile(apkg_path) as z:
            z.extractall(tmp_dir)

        db_path = Path(tmp_dir) / 'collection.anki2'
        if not db_path.exists():
            return None, 0, 0, 0, 0

        db = sqlite3.connect(str(db_path))
        cur = db.cursor()

        notes_count = cur.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
        cards_count = cur.execute("SELECT COUNT(*) FROM cards").fetchone()[0]

        all_text = ""
        for row in cur.execute("SELECT flds FROM notes"):
            fields = row[0].split("\x1f")
            for f in fields:
                all_text += ' ' + f

        db.close()

        vn_diac, vn_no_diac, other = count_words_classified(all_text)
        vn_total = vn_diac + vn_no_diac
        ratio = vn_diac / vn_total if vn_total > 0 else 1.0
        return ratio, vn_diac, vn_total, notes_count, cards_count
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def scan_all_apkgs(root_dir):
    """Scan tất cả file .apkg trong thư mục project."""
    apkgs = list(Path(root_dir).rglob("*.apkg"))
    return sorted(apkgs)


def main():
    if '--all' in sys.argv:
        root = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
        apkgs = scan_all_apkgs(root)
        if not apkgs:
            print("Không tìm thấy file .apkg nào.")
            return 0
    else:
        apkgs = []
        for arg in sys.argv[1:]:
            if arg == '--all':
                continue
            p = Path(arg)
            if p.exists():
                apkgs.append(p)
        if not apkgs:
            print("Usage: python verify_apkg_diacritics.py <file.apkg> [file2.apkg ...] [--all]")
            return 0

    print(f"Verifying {len(apkgs)} APKG file(s)...\n")
    print(f"{'File':<60} {'Ratio':>8} {'VN':>6} {'Notes':>6} {'Status':<10}")
    print("-" * 100)

    failed = []
    warning = []
    passed = []

    for apkg_path in apkgs:
        try:
            result = verify_apkg(apkg_path)
            if result[0] is None:
                print(f"{apkg_path.name:<60}  {'N/A':>8} {'0':>6} {'0':>6}  [ERR: no DB]")
                continue

            ratio, vn_diac, vn_total, notes, cards = result
            name = apkg_path.name if len(apkg_path.name) < 58 else apkg_path.name[:55] + '...'

            if vn_total < 10:
                status = "[OK] (few VN words)"
                passed.append((name, ratio, vn_diac, vn_total, notes, cards))
            elif ratio < 0.50:
                status = "[BLOCK]"
                failed.append((name, ratio, vn_diac, vn_total, notes, cards))
            elif ratio < 0.80:
                status = "[WARN]"
                warning.append((name, ratio, vn_diac, vn_total, notes, cards))
            else:
                status = "[OK]"
                passed.append((name, ratio, vn_diac, vn_total, notes, cards))

            print(f"{name:<60} {ratio:>7.1%} {vn_total:>6} {notes:>6}  {status:<10}")
        except Exception as e:
            print(f"{apkg_path.name:<60}  {'ERR':>8} {'-':>6} {'-':>6}  [ERR: {e}]")

    print("-" * 100)
    total = len(passed) + len(warning) + len(failed)
    print(f"\nTổng kết ({total} files):")
    print(f"  [OK]    : {len(passed)} — ratio >= 80%")
    print(f"  [WARN]  : {len(warning)} — ratio 50-80%")
    print(f"  [BLOCK] : {len(failed)} — ratio < 50%")

    if failed:
        print(f"\n[BLOCK] files — can kiem tra encoding JSON nguon:")
        for name, ratio, vn_diac, vn_total, notes, cards in failed:
            print(f"  - {name} ({ratio:.1%}, {vn_diac}/{vn_total} tu VN co dau, {notes} notes)")

    if warning:
        print(f"\n[WARN] files:")
        for name, ratio, vn_diac, vn_total, notes, cards in warning:
            print(f"  - {name} ({ratio:.1%}, {vn_diac}/{vn_total} từ VN có dấu, {notes} notes)")

    if failed:
        return 2
    elif warning:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
