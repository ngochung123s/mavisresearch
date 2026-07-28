import sqlite3, json

db_path = r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\_apkg_inspect\collection.anki2"
db = sqlite3.connect(db_path)
cur = db.cursor()

print("=== COL schema ===")
for row in cur.execute("PRAGMA table_info(col)"):
    print(" ", row)

print()
print("=== COL row count ===")
print(" ", cur.execute("SELECT COUNT(*) FROM col").fetchone()[0])

print()
print("=== COL data (first 4000 chars) ===")
for row in cur.execute("SELECT * FROM col"):
    for i, val in enumerate(row):
        if isinstance(val, str) and len(val) > 4000:
            print(f"[col-{i}] (truncated):", val[:4000], "...[truncated]")
        else:
            print(f"[col-{i}]:", val)

print()
print("=== NOTES schema ===")
for row in cur.execute("PRAGMA table_info(notes)"):
    print(" ", row)

print()
print("=== NOTES count ===")
print(" ", cur.execute("SELECT COUNT(*) FROM notes").fetchone()[0])

print()
print("=== FIRST 8 NOTES (front/back) ===")
for row in cur.execute("SELECT id, flds FROM notes LIMIT 8"):
    parts = row[1].split("\x1f")
    print(f"--- Note id={row[0]} ({len(parts)} fields) ---")
    for j, p in enumerate(parts):
        print(f"  field{j+1}: {p[:500]}")
    print()
