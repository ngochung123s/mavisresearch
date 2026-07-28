import zipfile, sqlite3, os, re, shutil

for apkg in [
    r"F:\DL\mavisresearch\Bai hoc y khoa\08_Anki Deck - apkg\Anki - Phan loai thuoc YHCT v2 ngan - 2026-06-17.apkg",
    r"F:\DL\mavisresearch\Bai hoc y khoa\08_Anki Deck - apkg\Anki - Tra cuu vi thuoc YHCT - 2026-06-17.apkg",
]:
    print('='*60)
    print('FILE:', os.path.basename(apkg))
    print('SIZE:', os.path.getsize(apkg), 'bytes')
    tmp = r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\_check_v2"
    if os.path.exists(tmp): shutil.rmtree(tmp)
    os.makedirs(tmp)
    with zipfile.ZipFile(apkg) as z: z.extractall(tmp)
    db = sqlite3.connect(os.path.join(tmp, "collection.anki2"))
    n = db.execute("SELECT COUNT(*) FROM notes").fetchone()[0]
    c = db.execute("SELECT COUNT(*) FROM cards").fetchone()[0]
    print(f"  notes={n}, cards={c}")
    for i, row in enumerate(db.execute("SELECT flds FROM notes LIMIT 2")):
        parts = row[0].split("\x1f")
        for j, p in enumerate(parts):
            t = re.sub(r"<[^>]+>", " ", p)
            t = re.sub(r"\s+", " ", t).strip()
            cut = t[:150] + ("..." if len(t) > 150 else "")
            print(f"  field{j+1}: {cut}")
        print("---")
    shutil.rmtree(tmp)
