import re
from pathlib import Path

p = Path("../12_Nhi khoa/06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_2026-09-19_RELEASE_v1.md")
text = p.read_text(encoding="utf-8")
lines = text.splitlines()
new_lines = []
for line in lines:
    line_str = line.strip()
    if not line_str:
        new_lines.append("")
        continue
    if (line_str.startswith("#") or line_str.startswith("|") or line_str.startswith("```") or 
        line_str.startswith("---") or line_str.startswith(">") or line_str.startswith("$$") or
        "{claim:" in line_str or line_str.startswith("[") or line_str.startswith("+") or line_str.startswith("- ") or
        re.match(r"^\d+\.", line_str)):
        new_lines.append(line_str)
        continue
    sentences = re.split(r"(?<=[.?!:])\s+(?=[A-Z\u00C0-\u1EF90-9])", line_str)
    for s in sentences:
        if s.strip():
            new_lines.append(s.strip())

formatted = "\n".join(new_lines)
nonblank = len([l for l in formatted.splitlines() if l.strip()])
print("Words:", len(formatted.split()), "Nonblank lines:", nonblank)
p.write_text(formatted + "\n", encoding="utf-8")
