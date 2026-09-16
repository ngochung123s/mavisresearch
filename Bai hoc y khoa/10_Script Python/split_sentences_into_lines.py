import re
from pathlib import Path

target_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.md")
text = target_path.read_text(encoding="utf-8")

lines = text.splitlines()
out_lines = []

in_code = False
for line in lines:
    stripped = line.strip()
    if not stripped:
        out_lines.append("")
        continue
    if stripped.startswith("```"):
        in_code = not in_code
        out_lines.append(stripped)
        continue
    if in_code:
        out_lines.append(line)
        continue
    if stripped.startswith("#") or stripped.startswith("|") or stripped.startswith(">") or stripped.startswith("- **Chuỗi") or "→" in stripped or "{claim:" in stripped:
        out_lines.append(stripped)
        continue
    if stripped.startswith("1.") or stripped.startswith("2.") or stripped.startswith("3.") or stripped.startswith("4.") or stripped.startswith("5.") or stripped.startswith("6.") or stripped.startswith("7.") or stripped.startswith("8.") or stripped.startswith("9.") or stripped.startswith("10."):
        # Check if reference or numbered list
        if "PMID:" in stripped:
            out_lines.append(stripped)
            continue
    # Split sentences on period followed by space and capital letter or digit
    # Avoid splitting inside abbreviations like "e.g.", "i.e.", "CA1", "vs.", "al."
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÀ-Ỹ0-9])', stripped)
    for s in sentences:
        sub = s.strip()
        if sub:
            out_lines.append(sub)

new_text = "\n".join(out_lines).strip() + "\n"
target_path.write_text(new_text, encoding="utf-8")

words = len(new_text.split())
nonblank = len([l for l in new_text.splitlines() if l.strip()])
print(f"Formatted {target_path}: {words} words, {nonblank} nonblank lines")
