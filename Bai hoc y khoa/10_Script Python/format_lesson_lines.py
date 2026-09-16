import re
from pathlib import Path

p = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.md")
text = p.read_text(encoding="utf-8")

lines = text.splitlines()
new_lines = []
for line in lines:
    line_str = line.strip()
    if not line_str:
        new_lines.append("")
        continue
    if line_str.startswith("#") or line_str.startswith("|") or line_str.startswith("```") or line_str.startswith("---") or line_str.startswith(">"):
        new_lines.append(line_str)
        continue
    if "{claim:" in line_str:
        new_lines.append(line_str)
        continue
    sentences = re.split(r"(?<=[.?!:])\s+(?=[A-ZÀ-Ỹ0-9])", line_str)
    for s in sentences:
        if s.strip():
            new_lines.append(s.strip())

formatted = "\n".join(new_lines)
nonblank = len([l for l in formatted.splitlines() if l.strip()])
print(f"Words: {len(formatted.split())}, Nonblank lines: {nonblank}")
p.write_text(formatted + "\n", encoding="utf-8")
