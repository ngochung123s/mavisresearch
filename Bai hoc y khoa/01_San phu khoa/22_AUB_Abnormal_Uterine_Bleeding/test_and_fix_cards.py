# -*- coding: utf-8 -*-
"""test_and_fix_cards.py — Chạy linter trực tiếp trong memory và tinh chỉnh từng thẻ."""
import json
import re
import sys
from pathlib import Path

# Thêm đường dẫn tới Script Python
sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
import card_lint as lint
import lesson_manifest

PALETTE = ("#ff6b6b", "#ffd43b", "#51cf66", "#74c0fc")

def main():
    # Chạy build script trước
    py_path = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\22_AUB_Abnormal_Uterine_Bleeding\build_rearchitected_ob22_cards.py")
    
    # Đọc script và xử lý
    code = py_path.read_text(encoding="utf-8")
    
    # Thực thi mã để lấy biến `cards`
    scope = {}
    exec(code, scope)
    cards = scope["cards"]
    print(f"Loaded {len(cards)} cards in memory")

    # Kiểm tra lint
    manifest_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\22_AUB_Abnormal_Uterine_Bleeding")
    m = lesson_manifest.load(manifest_dir)
    spec = m.lint_spec()

    # Phân tích từng lỗi
    issues = lint.lint_cards(cards, spec)
    print(f"Total issues initially: {len(issues)}")

    # Ghi nhận các loại lỗi
    by_code = {}
    for iss in issues:
        by_code.setdefault(iss.code, []).append(iss)
    
    for c, items in by_code.items():
        print(f"  {c}: {len(items)} issues")
        for it in items[:3]:
            print(f"    [{it.card_id}] {it.message}")

if __name__ == "__main__":
    main()
