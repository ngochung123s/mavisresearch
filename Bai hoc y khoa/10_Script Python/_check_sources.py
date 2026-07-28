import zipfile, re
import os

candidates = [
    r"F:\DL\mavisresearch\Bai hoc y khoa\11_Cham cuu YHCT\4_Thuốc (verbatim) - 2026-06-16.docx",
    r"F:\DL\mavisresearch\Bai hoc y khoa\11_Cham cuu YHCT\5_Thuốc (verbatim) - 2026-06-16.docx",
    r"F:\DL\mavisresearch\Bai hoc y khoa\11_Cham cuu YHCT\4_Thuoc (v2 dien giai) - 2026-06-17.docx",
    r"F:\DL\mavisresearch\Bai hoc y khoa\11_Cham cuu YHCT\5_Thuoc (v2 dien giai) - 2026-06-17.docx",
    r"F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\Anki_DeThi_YHCT_Review 1.docx",
    r"F:\DL\mavisresearch\Bai hoc y khoa\09_Source - Markdown\Anki_DeThi_YHCT_Review_Full.docx",
]

# Anchors from the apkg content
anchors = [
    "GIẢI BIỂU",
    "Tân ôn giải biểu",
    "Ma hoàng",
    "Quế chi",
    "Tế tân",
    "Bạch chỉ",
    "Sinh khương",
    "Tía tô",
    "Hương nhu",
    "Khương hoạt",
    "Phòng phong",
    "Tân giao",
    "Bạc hà",
    "Cúc hoa",
    "Tang diệp",
    "Mạn kinh tử",
    "Ngưu bàng tử",
    "Cát cánh",
    "Sài hồ",
    "Thăng ma",
    "Phù bình",
]

def extract_docx_text(path):
    out = []
    with zipfile.ZipFile(path) as z:
        with z.open("word/document.xml") as f:
            xml = f.read().decode("utf-8", errors="replace")
    # strip tags
    text = re.sub(r"<[^>]+>", " ", xml)
    text = re.sub(r"\s+", " ", text).strip()
    return text

for path in candidates:
    if not os.path.exists(path):
        print(f"MISSING: {path}")
        continue
    text = extract_docx_text(path)
    found = [a for a in anchors if a in text]
    print(f"\n{'='*80}\nFILE: {os.path.basename(path)}")
    print(f"  size = {len(text)} chars, {len(text.split())} words")
    print(f"  anchors hit: {len(found)}/{len(anchors)}")
    if found:
        print(f"  matched: {found[:5]}{'...' if len(found)>5 else ''}")
