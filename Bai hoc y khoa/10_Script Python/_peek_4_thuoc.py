import zipfile, re, os, sys

def get_text(path):
    with zipfile.ZipFile(path) as z:
        with z.open("word/document.xml") as f:
            xml = f.read().decode("utf-8", errors="replace")
    text = re.sub(r"<[^>]+>", "\n", xml)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text

# Both 4_Thuoc and 5_Thuoc (v2)
p4 = r"F:\DL\mavisresearch\Bai hoc y khoa\11_Cham cuu YHCT\4_Thuoc (v2 dien giai) - 2026-06-17.docx"
p5 = r"F:\DL\mavisresearch\Bai hoc y khoa\11_Cham cuu YHCT\5_Thuoc (v2 dien giai) - 2026-06-17.docx"

for p in [p4, p5]:
    t = get_text(p)
    print(f"\n{'='*80}\n{os.path.basename(p)}")
    print(f"  length: {len(t)} chars")
    # show first 1500 chars
    print("--- first 1500 chars ---")
    print(t[:1500])
    print("--- search for keyword 'GIẢI BIỂU' or 'GIAI BIEU' ---")
    for kw in ["GIẢI BIỂU", "GIAI BIEU", "giải biểu", "Ma hoàng", "Tân ôn"]:
        idx = t.find(kw)
        if idx >= 0:
            print(f"  found '{kw}' at {idx}: ...{t[max(0,idx-50):idx+200]}...")
