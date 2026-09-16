# -*- coding: utf-8 -*-
"""Update all PED-07 artifacts and build the verified release markdown."""
import json
import re
import subprocess
import sys
from pathlib import Path

target_dir = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh")
script_dir = Path("F:/DL/mavisresearch/Bai hoc y khoa/10_Script Python")
bundle_path = target_dir / "evidence_bundle.json"

# 1. Update abstract_match.jsonl with C-013
jsonl_file = target_dir / "abstract_match.jsonl"
lines = [json.loads(line) for line in jsonl_file.read_text(encoding="utf-8").splitlines() if line.strip()]
if not any(row.get("claim_id") == "C-013" for row in lines):
    lines.append({
        "pmid": "40770931",
        "claim_id": "C-013",
        "claim_text": "Nghiên cứu FEBSTAT theo dõi đoàn hệ trẻ có trạng thái động kinh do sốt (Febrile status epilepticus and epileptogenesis: The FEBSTAT study) ghi nhận hình ảnh MRI cấp tính cho thấy tăng tín hiệu T2 hồi hải mã một bên (unilateral hyperintense hippocampus T2 hyperintensity)",
        "abstract_snippet": "Initial magnetic resonance images (MRIs), done within days after FSE, showed a unilateral hyperintense hippocampus ... predicting hippocampal sclerosis and epileptogenesis.",
        "claim_type": "factual",
        "match": True,
        "reason": "Acute unilateral hyperintense hippocampus finding verified from FEBSTAT abstract."
    })
with jsonl_file.open("w", encoding="utf-8") as f:
    for row in lines:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
print(f"Updated abstract_match.jsonl: {len(lines)} rows")

# 2. Update full_verify_table.md with C-013
table_file = target_dir / "full_verify_table.md"
table_text = table_file.read_text(encoding="utf-8").strip()
if "C-013" not in table_text:
    table_text += "\n| **C-013** | Nghiên cứu FEBSTAT ghi nhận tăng tín hiệu T2 hồi hải mã một bên trên MRI cấp tính sau FSE | T2 hyperintensity, FSE | FEBSTAT Study (PMID: 40770931) | unilateral hyperintense hippocampus | KHỚP | Chỉ dấu sinh học sớm của tổn thương tế bào và quá trình sinh động kinh |\n"
    table_file.write_text(table_text, encoding="utf-8")
    print("Updated full_verify_table.md")

# 3. Update PED-07_RESEARCH_BRIEF.md with C-013
brief_file = target_dir / "PED-07_RESEARCH_BRIEF.md"
brief_text = brief_file.read_text(encoding="utf-8")
if "C-013" not in brief_text:
    old_row = "| **C-012** | Nghiên cứu FEBSTAT theo dõi 10 năm ghi nhận 10 trong số 14 trẻ có tăng tín hiệu T2 hải mã cấp tính tiến triển thành xơ teo hải mã (definite hippocampal sclerosis) và 44 trẻ phát triển thành động kinh sau trạng thái động kinh do sốt | Trẻ trạng thái động kinh do sốt theo dõi 10 năm | PMID: 38606600 | [DATA VERIFIED] |"
    new_rows = old_row + "\n| **C-013** | Nghiên cứu FEBSTAT theo dõi đoàn hệ trẻ có trạng thái động kinh do sốt (Febrile status epilepticus and epileptogenesis: The FEBSTAT study) ghi nhận hình ảnh MRI cấp tính cho thấy tăng tín hiệu T2 hồi hải mã một bên (unilateral hyperintense hippocampus T2 hyperintensity) | Trẻ trạng thái động kinh do sốt | PMID: 40770931 | [DATA VERIFIED] |"
    brief_text = brief_text.replace(old_row, new_rows)
    brief_file.write_text(brief_text, encoding="utf-8")
    print("Updated PED-07_RESEARCH_BRIEF.md with C-013")

print("Artifacts synchronized successfully!")
