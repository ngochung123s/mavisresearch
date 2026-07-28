"""Verify tat ca MD files trong 09_Source - Markdown co day du khong.

Logic:
- Phan loai tu: 'vn_diac' (co dau) | 'vn_no_diac' (tieng Viet khong dau) | 'other' (English, so, ky tu dac biet)
- Ratio = vn_diac / (vn_diac + vn_no_diac) - chi tinh tren tu tieng Viet
- Threshold:
  - < 0.50: [FAIL] - can review hoac convert
  - 0.50-0.80: [WARN] - chap nhan (co the co tu ambiguous)
  - >= 0.80: [OK] - tot

Note: bai y khoa co nhieu thuat ngu y khoa tieng Anh (aspirin, hCG, GnRH, ACOG, FIGO, ISSHP...)
-> 'other' duoc bo qua khi tinh ratio, chi tinh tren tu tieng Viet.
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown")

# Vietnamese diacritics (co dau)
VIETNAMESE_DIACRITICS = set(
    "àáảãạằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ"
    "ÀÁẢÃẠẰẮẲẴẶÂẦẤẨẪẬĐÈÉẺẼẸÊỀẾỂỄỆÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘỜỚỞỠỢÙÚỦŨỤỪỨỬỮỰỲÝỶỸỴ"
)

# Vietnamese letters (khong dau nhung van la tieng Viet dac trung)
VN_SPECIAL_LETTERS = set("ăâđêôơưĂÂĐÊÔƠƯ")


def classify_word(word):
    """Phan loai tu: 'vn_diac' | 'vn_no_diac' | 'other'."""
    # Strip punctuation (chi giu letters, digits, chu dac biet tieng Viet)
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
    # All ASCII letters, no Vietnamese marker - probably English
    if all(c.isascii() for c in clean):
        return 'other'
    return 'other'


def count_words_classified(text):
    """Dem so tu theo loai. Tra ve (vn_diac, vn_no_diac, other)."""
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)
    # Remove markdown table syntax (|---)
    text = re.sub(r"\|[\s\-:|]+\|", " ", text)
    # Remove markdown syntax
    text = re.sub(r"[#*_`|>\[\]()-]+", " ", text)
    # Split by whitespace
    words = text.split()
    vn_diac = 0
    vn_no_diac = 0
    other = 0
    for w in words:
        if len(w) < 2:
            continue
        # Skip words that are pure punctuation or numbers
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


def main():
    md_files = list(ROOT.rglob("*.md"))
    if not md_files:
        print("Khong tim thay MD files.")
        return
    print(f"Verifying {len(md_files)} MD files...\n")
    print(f"{'File':<60} {'Ratio':>7} {'VN':>5} {'Status':<10}")
    print("-" * 90)
    failed = []
    warning = []
    passed = []
    for path in sorted(md_files):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            vn_diac, vn_no_diac, other = count_words_classified(text)
            vn_total = vn_diac + vn_no_diac
            ratio = vn_diac / vn_total if vn_total > 0 else 1.0
            rel = str(path.relative_to(ROOT))
            if ratio < 0.50:
                status = "[FAIL]"
                failed.append((rel, ratio, vn_diac, vn_no_diac, other))
            elif ratio < 0.80:
                status = "[WARN]"
                warning.append((rel, ratio, vn_diac, vn_no_diac, other))
            else:
                status = "[OK]"
                passed.append((rel, ratio, vn_diac, vn_no_diac, other))
            print(f"{rel[:58]:<60} {ratio:>6.1%} {vn_total:>5}  {status:<10}")
        except Exception as e:
            print(f"{str(path.relative_to(ROOT)):<60}  [ERR]  {e}")
    print("-" * 90)
    print(f"\nTong ket:")
    print(f"  [OK]   : {len(passed)}/{len(md_files)} (ratio >= 0.80)")
    print(f"  [WARN] : {len(warning)}/{len(md_files)} (ratio 0.50-0.80)")
    print(f"  [FAIL] : {len(failed)}/{len(md_files)} (ratio < 0.50 - can review)")
    if failed:
        print(f"\n[FAIL] files can review (chua convert hoac viet sai):")
        for rel, ratio, w_d, w_nd, o in failed:
            print(f"  - {rel} ({w_d}/{w_d+w_nd} tieng Viet co dau, {o} English/so)")
    if warning:
        print(f"\n[WARN] files chap nhan (co the co tu ambiguous):")
        for rel, ratio, w_d, w_nd, o in warning:
            print(f"  - {rel} ({ratio:.1%})")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
