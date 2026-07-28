import sqlite3, re, json

db_path = r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\_apkg_inspect\collection.anki2"
db = sqlite3.connect(db_path)
cur = db.cursor()

# Load all notes
notes = cur.execute("SELECT id, flds, mid FROM notes ORDER BY id").fetchall()

# Group by main group (parent notes) and sub-group notes
# Parent = NHÓM THUỐC (id 1781633402282-308 = 14 nhóm)
# Sub = PHÂN NHÓM (id 1781633402310-376 = 28 phân nhóm)
# Cloze mẹo nhớ (id 1781633402378-416)

# Build hierarchical structure: nhóm -> list of (phân nhóm, [vị thuốc])
def strip_html(s):
    return re.sub(r"<[^>]+>", "", s).strip()

groups = []
for nid, flds, mid in notes:
    parts = flds.split("\x1f")
    front = strip_html(parts[0])
    back = strip_html(parts[1] if len(parts) > 1 else "")
    if front.startswith("NHÓM THUỐC"):
        # parent group
        m = re.search(r"Nhóm\s+(.+?)\s*\((.+?)\)", front)
        if m:
            gname = m.group(1).strip()
            gdesc = m.group(2).strip()
            groups.append({"id": nid, "name": gname, "desc": gdesc, "front": front, "back": back})

print(f"=== {len(groups)} NHÓM CHÍNH ===")
for g in groups:
    print(f"\n● {g['name']} ({g['desc']})")
    print(f"  FRONT: {g['front'][:150]}")
    # show back full
    print(f"  BACK :")
    for line in g['back'].split('•'):
        line = line.strip()
        if line and line != "📖 Văn bản gốc — Nhóm " + g['name'] + " (" + g['desc'] + "):":
            if line.startswith('Gồm'):
                print(f"    {line[:80]}")
            elif line.startswith('Các phân nhóm'):
                print(f"    {line[:80]}")
            else:
                print(f"    • {line[:120]}")
