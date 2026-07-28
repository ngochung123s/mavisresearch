import sqlite3, json, re

db_path = r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\_apkg_inspect\collection.anki2"
db = sqlite3.connect(db_path)
cur = db.cursor()

# Get all notes
notes = cur.execute("SELECT id, flds, mid FROM notes ORDER BY id").fetchall()
print(f"Total notes: {len(notes)}\n")

# Notetypes
print("=== NOTETYPE IDs ===")
mid_to_name = {1700000002: "YHCT Basic", 1700000003: "YHCT Cloze"}
for mid in set(n[2] for n in notes):
    print(f"  mid={mid} -> {mid_to_name.get(mid, '?')}")

print()
print("=== ALL NOTES (front only + 200 chars of back) ===")
for nid, flds, mid in notes:
    parts = flds.split("\x1f")
    ntype = mid_to_name.get(mid, "?")
    print(f"\n--- id={nid} [{ntype}] ({len(parts)} fields) ---")
    # show field1 (front) and truncated field2 (back)
    f1 = re.sub(r"<[^>]+>", "", parts[0]).strip()
    f2 = re.sub(r"<[^>]+>", "", parts[1] if len(parts) > 1 else "").strip()
    print(f"FRONT: {f1[:200]}")
    print(f"BACK : {f2[:200]}{'...' if len(f2) > 200 else ''}")
