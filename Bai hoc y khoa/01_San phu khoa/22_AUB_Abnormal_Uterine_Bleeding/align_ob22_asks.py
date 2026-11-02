# -*- coding: utf-8 -*-
"""align_ob22_asks.py — Đồng bộ hoàn hảo giữa Front, Back và asks theo chuẩn card_lint."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
import card_lint as lint
import lesson_manifest

def clean_label(lbl):
    # Loại bỏ các ký tự đặc biệt như <, >, quotes
    return re.sub(r"[^\w\s\(\)/–\-]+", " ", lbl).strip()

def align():
    manifest_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\22_AUB_Abnormal_Uterine_Bleeding")
    json_path = manifest_dir / "AUB_Abnormal_Uterine_Bleeding_2026-06-29.cards.v2.json"
    cards = json.loads(json_path.read_text(encoding="utf-8"))
    
    spec = lesson_manifest.load(manifest_dir).lint_spec()

    for c in cards:
        if c.get("id") == "OB22-B6-01":
            c["back"] = c["back"].replace("Phụ nữ dưới 45 tuổi có yếu tố nguy cơ phơi nhiễm Estrogen không đối kháng:", "Phụ nữ dưới 45 tuổi có nguy cơ:")
        if c.get("type") != "basic":
            continue

        back = c["back"]
        items = lint.core_items(back)
        if not items:
            c.pop("asks", None)
            continue

        raw_labels = [lbl for lbl, _ in items if lbl]
        # Kiểm tra xem có label nào kích hoạt is_facet_label không
        has_facet = any(lint.is_facet_label(lbl) for lbl in raw_labels)

        if not has_facet:
            # Không có facet label -> không dùng asks
            c.pop("asks", None)
        else:
            # Có facet label -> tất cả các items cấp 1 đều phải có label trong asks
            # Đảm bảo mỗi item đều có label rõ ràng
            # Chỉnh sửa back nếu có item thiếu label
            # Tạo asks danh sách chuẩn
            asks = raw_labels
            c["asks"] = asks
            
            # Đảm bảo mỗi ask có trong Front
            front = c["front"]
            missing = [a for a in asks if lint.fold(a) not in lint.fold(front)]
            if missing:
                # Bổ sung các khía cạnh còn thiếu vào Front
                q_clean = front.rstrip(" ?.")
                # Nếu đã có ngoặc gồm các khía cạnh thì thay thế
                q_clean = re.sub(r"\s*\(gồm.*?\)$", "", q_clean, flags=re.I)
                c["front"] = f"{q_clean} (gồm: {', '.join(asks)})?"

    # Chạy linter kiểm tra
    issues = lint.lint_cards(cards, spec)
    print(f"Total issues after alignment: {len(issues)}")
    by_code = {}
    for iss in issues:
        by_code.setdefault(iss.code, []).append(iss)
    for code, errs in by_code.items():
        print(f"  {code}: {len(errs)}")
        for e in errs[:3]:
            print(f"    [{e.card_id}] {e.message}")

    # Ghi lại
    json_path.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(cards)} cards successfully")

if __name__ == "__main__":
    align()
