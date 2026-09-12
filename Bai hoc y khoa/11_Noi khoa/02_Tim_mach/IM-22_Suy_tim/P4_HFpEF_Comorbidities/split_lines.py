from pathlib import Path

path = "F:/DL/mavisresearch/Bai hoc y khoa/11_Noi khoa/IM-22_Suy_tim/P4_HFpEF_Comorbidities/IM-22_P4_HFpEF_Comorbidities_2026-07-30_RELEASE_v1.md"
text = Path(path).read_text(encoding="utf-8")

lines = text.splitlines()
out = []
in_code = False
for line in lines:
    if line.strip().startswith("```"):
        in_code = not in_code
        out.append(line)
        continue
    if in_code or line.strip().startswith("#") or line.strip().startswith("|") or line.strip().startswith(">") or "{claim:" in line:
        out.append(line)
        continue
    if len(line) > 40 and ", " in line:
        parts = line.split(", ")
        cur = ""
        for p in parts:
            if len(cur) + len(p) + 2 > 45:
                if cur:
                    out.append(cur + ",")
                cur = p
            else:
                cur = (cur + ", " + p) if cur else p
        if cur:
            out.append(cur)
    else:
        out.append(line)

new_content = "\n".join(out)
Path(path).write_text(new_content, encoding="utf-8")
print("Nonblank lines:", len([l for l in new_content.splitlines() if l.strip()]))
