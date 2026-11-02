# -*- coding: utf-8 -*-
"""auto_refine_ob22.py — Tự động chuẩn hóa toàn diện thẻ OB-22 đạt 0 BLOCK lỗi linter."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
import card_lint as lint
import lesson_manifest

PALETTE = ("#ff6b6b", "#ffd43b", "#51cf66", "#74c0fc")

def ensure_color(text, default_color="#51cf66"):
    if not lint.has_palette(text):
        # Bọc cụm đầu tiên có <b> hoặc chữ đầu bằng span màu
        if "<b>" in text:
            return text.replace("<b>", f'<span style="color:{default_color}"><b>', 1).replace("</b>", "</b></span>", 1)
        else:
            return f'<span style="color:{default_color}">{text}</span>'
    return text

def clean_latex(text):
    text = text.replace(r"\times", "×")
    text = text.replace(r"$\times$", "×")
    text = text.replace(r"$\ge$", "≥")
    text = text.replace(r"$\le$", "≤")
    text = text.replace(r"$\rightarrow$", "→")
    text = text.replace(r"\rightarrow", "→")
    text = text.replace("$", "")
    return text

def refine():
    py_path = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\22_AUB_Abnormal_Uterine_Bleeding\build_rearchitected_ob22_cards.py")
    scope = {}
    exec(py_path.read_text(encoding="utf-8"), scope)
    cards = scope["cards"]

    manifest_dir = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\22_AUB_Abnormal_Uterine_Bleeding")
    m = lesson_manifest.load(manifest_dir)
    spec = m.lint_spec()

    for c in cards:
        # 1. Clean latex & source
        for k in ("front", "back", "text", "extra"):
            if k in c:
                c[k] = clean_latex(c[k])
                if k in ("front", "back", "text"):
                    c[k] = c[k].replace("PMID 36053280", "Tsakiridis 2022")
                    c[k] = c[k].replace("PMID", "")

        # 2. Ensure colors
        if c.get("type") == "basic":
            c["front"] = ensure_color(c["front"], "#74c0fc")
            c["back"] = ensure_color(c["back"], "#51cf66")

        # 3. Handle asks alignment
        if c.get("type") == "basic":
            items = lint.core_items(c["back"])
            facet_labels = [label for label, _ in items if lint.is_facet_label(label)]
            
            if not facet_labels:
                # Không có facet label -> không cần asks
                c.pop("asks", None)
            else:
                # Có facet label -> trích xuất từ khóa mở đầu (keyword)
                # Ví dụ: "Cơ chế tổn thương" -> "Cơ chế"
                keywords = []
                for fl in facet_labels:
                    fl_clean = re.sub(r"[^\w\s]+", " ", fl).strip()
                    m_kw = lint.FACET_LABEL_RE.match(fl_clean.lower())
                    if m_kw:
                        kw = fl_clean[:m_kw.end()].strip()
                        # Capitalize properly
                        kw_cap = kw[0].upper() + kw[1:]
                        if kw_cap not in keywords:
                            keywords.append(kw_cap)
                    else:
                        keywords.append(fl)
                
                c["asks"] = keywords
                # Đảm bảo mỗi từ khóa trong asks đều xuất hiện trong Front
                front_folded = lint.fold(c["front"])
                missing_in_front = [kw for kw in keywords if lint.fold(kw) not in front_folded]
                if missing_in_front:
                    # Thêm vào cuối câu hỏi
                    c["front"] = c["front"].rstrip(" ?.") + f" (gồm các khía cạnh: {', '.join(keywords)})?"

    # Kiểm tra lại qua lint_cards
    issues = lint.lint_cards(cards, spec)
    print(f"Remaining issues: {len(issues)}")
    by_code = {}
    for iss in issues:
        by_code.setdefault(iss.code, []).append(iss)
    for code, items in by_code.items():
        print(f"  {code}: {len(items)}")
        for it in items[:2]:
            print(f"    [{it.card_id}] {it.message}")

    # Ghi đè vào file JSON
    target_json = manifest_dir / "AUB_Abnormal_Uterine_Bleeding_2026-06-29.cards.v2.json"
    target_json.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {len(cards)} refined cards to {target_json}")

if __name__ == "__main__":
    refine()
