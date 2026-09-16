# -*- coding: utf-8 -*-
"""Update CATALOG_PED_VIEWER.json with PED-07 lesson entry."""
import json
from pathlib import Path

catalog_path = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/CATALOG_PED_VIEWER.json")
lesson_dir = Path("F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa/01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh")

lesson_md = lesson_dir / "PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.md"
cards_json = lesson_dir / "PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.cards.v2.json"
apkg_file = "PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh_2026-09-16_RELEASE_v1.apkg"

ped_content = lesson_md.read_text(encoding="utf-8")
cards_data = json.loads(cards_json.read_text(encoding="utf-8"))

catalog = json.loads(catalog_path.read_text(encoding="utf-8"))

# Check if PED-07 already in lessons
existing_ids = [l["id"] for l in catalog["lessons"]]
if "PED-07" in existing_ids:
    catalog["lessons"] = [l for l in catalog["lessons"] if l["id"] != "PED-07"]

new_entry = {
    "id": "PED-07",
    "priority": "P0",
    "title": "Co giật do sốt & Cắt cơn co giật / Trạng thái động kinh",
    "block": "Block 1 — Hồi sức, Cấp cứu & Ngộ độc Nhi khoa",
    "scope": "Sốt co giật đơn thuần vs phức hợp; phác đồ cắt cơn từng phút (Midazolam buccal/tiêm bắp, Diazepam bơm hậu môn/tĩnh mạch); chỉ định chọc dịch não tủy.",
    "dependency": "PED-01, 03",
    "curriculum_status": "✅ GATES ĐẠT (MD + APKG 36 thẻ)",
    "has_ped": True,
    "has_pedytb": False,
    "has_cards": True,
    "ped_file": lesson_md.name,
    "ped_content": ped_content,
    "pedytb_file": None,
    "pedytb_content": "",
    "cards_count": len(cards_data),
    "cards_data": cards_data,
    "apkg_file": apkg_file,
    "html_file": None,
    "folder_rel": "01_Hoi_suc_Cap_cuu_Ngo_doc/PED-07_Co_giat_do_sot_va_Trang_thai_dong_kinh"
}

# Insert in sorted order by ID
catalog["lessons"].append(new_entry)
catalog["lessons"].sort(key=lambda x: int(x["id"].split("-")[1]) if "-" in x["id"] and x["id"].split("-")[1].isdigit() else 999)

# Update metadata
catalog["metadata"]["total_ped"] = sum(1 for l in catalog["lessons"] if l.get("has_ped"))
catalog["metadata"]["total_cards"] = sum(l.get("cards_count", 0) for l in catalog["lessons"])

block_1 = "Block 1 — Hồi sức, Cấp cứu & Ngộ độc Nhi khoa"
if block_1 not in catalog["metadata"]["blocks"]:
    catalog["metadata"]["blocks"].insert(1, block_1)

catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated {catalog_path} successfully. Total lessons: {len(catalog['lessons'])}, total cards: {catalog['metadata']['total_cards']}")
