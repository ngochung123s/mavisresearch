# -*- coding: utf-8 -*-
"""barem_audit.py — Kiểm định sự sát barem 5 cổng cho 11 bài Ngoại khoa (Desktop barem <-> Repo BAREM <-> Thẻ Anki <-> AnkiConnect <-> HungMed).

Chạy:
  python barem_audit.py
  python barem_audit.py --skip-anki   # khi Anki không mở
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sqlite3
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
NGOAI_DIR = REPO_ROOT / "16_Ngoai khoa"
DESKTOP_BAREM_DIR = Path(r"C:\Users\THANHANH\Desktop\barem")
CATALOG_PATH = REPO_ROOT / "hungmed" / "CATALOG_PED_VIEWER.json"
REPORT_PATH = Path(__file__).resolve().parent / "audit_reports" / "barem_fidelity_report.md"
ANKI_URL = "http://127.0.0.1:8765"

PAIRS = [
    ("01_Ung_thu_thuc_quan_barem.md", "SURG-20B_Ung_thu_thuc_quan"),
    ("02_Ung_thu_da_day_barem.md", "SURG-21_Ung_thu_da_day"),
    ("03_Ung_thu_gan_barem.md", "SURG-31_Ung_thu_gan"),
    ("04_Ung_thu_dai_trang_barem.md", "SURG-22_Ung_thu_dai_trang"),
    ("05_Ung_thu_truc_trang_barem.md", "SURG-23_Ung_thu_truc_trang"),
    ("06_Ung_thu_than_barem.md", "SURG-56_Ung_thu_than"),
    ("07_Ung_thu_tuyen_tien_liet_barem.md", "SURG-58_Ung_thu_tuyen_tien_liet"),
    ("08_Soc_nhiem_khuan_barem.md", "SURG-R1_Soc_nhiem_khuan"),
    ("09_Hoi_suc_suy_tuan_hoan_barem.md", "SURG-R3_Hoi_suc_suy_tuan_hoan"),
    ("10_Suy_ho_hap_cap_barem.md", "SURG-R4_Suy_ho_hap_cap"),
    ("11_Soc_chan_thuong_barem.md", "SURG-R2_Soc_chan_thuong"),
]

TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")
CLOZE_WRAP_RE = re.compile(r"\{\{c\d+::(.*?)\}\}", re.S)

# Số liệu + đơn vị lâm sàng để kiểm chứng độ phủ nguyên tử
NUM_UNIT_RE = re.compile(
    r"(?<![A-Za-zÀ-Ỹ0-9])(\d+(?:[.,]\d+)?(?:\s*(?:%|cm|mm|mg|ml|ng|g/l|g/dl)?\s*[–\-~]\s*\d+(?:[.,]\d+)?)?\s*"
    r"(?:%|mg/dL|mg/l|ng/ml|ng/dL|µg/kg/ph(?:út)?|mcg/kg/ph|mmol/L|mmol/l|g/dL|g/L|g/l|"
    r"cmH₂O|cmH2O|mmHg|ml/kg/giờ|ml/kg/h|ml/kg|ml/giờ|ml/h|lít/phút|L/phút|L/ph|"
    r"lần/phút|nhịp/phút|mm³|cm³|Gy|Fr|đv/phút|J|°C|mm|cm|mg|g|ml|kg|tuổi|năm|tháng|tuần|ngày|giờ|phút|giây|chu kỳ|lần))(?![A-Za-zÀ-Ỹ])",
    re.I,
)


def ac(action: str, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    with urllib.request.urlopen(urllib.request.Request(ANKI_URL, payload), timeout=20) as resp:
        res = json.loads(resp.read())
    if res.get("error"):
        raise RuntimeError(res["error"])
    return res["result"]


def norm_text(s: str) -> str:
    s = html.unescape(TAG_RE.sub(" ", s or ""))
    s = CLOZE_WRAP_RE.sub(r"\1", s)
    # Chuẩn hóa LaTeX & Unicode trong barem gốc sang dạng văn bản thống nhất
    replacements = [
        (r"\ge", "≥"), (r"\geq", "≥"), (r"\le", "≤"), (r"\leq", "≤"),
        (r"\rightarrow", "→"), (r"\to", "→"), (r"\downarrow", "↓"), (r"\uparrow", "↑"),
        (r"\approx", "≈"), (r"\times", "×"), (r"\pm", "±"), (r"^\circ C", "°C"),
        (r"^\circC", "°C"), (r"O_2", "O₂"), (r"CO_2", "CO₂"), (r"PaO_2", "PaO₂"),
        (r"PaCO_2", "PaCO₂"), (r"FiO_2", "FiO₂"), (r"SpO_2", "SpO₂"),
        (r"ScvO_2", "ScvO₂"), (r"SvO_2", "SvO₂"), (r"HCO_3^-", "HCO₃⁻"),
        (r"Ca^{2+}", "Ca²⁺"), (r"K^+", "K⁺"), (r"\text{", ""), (r"$", ""), (r"}", ""),
    ]
    for old, new in replacements:
        s = s.replace(old, new)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def strip_barem_meta(md_text: str) -> str:
    """Bỏ phần header metadata đầu file và phần TÀI LIỆU THAM KHẢO cuối file để tránh check năm xuất bản."""
    lines = md_text.splitlines()
    kept = []
    skip_refs = False
    for i, line in enumerate(lines):
        if i < 6 and any(line.startswith(p) for p in ("**Nguồn", "**Phương pháp", "**Tác giả", "**Đối tượng")):
            continue
        if re.match(r"^##\s*TÀI LIỆU THAM KHẢO", line.strip(), re.I):
            skip_refs = True
            continue
        if not skip_refs:
            kept.append(line)
    return "\n".join(kept)


def norm_token(tok: str) -> str:
    t = tok.lower().strip()
    t = t.replace("–", "-").replace(" ", "")
    t = re.sub(r"(?<=\d)\.(?=\d{3}(?!\d))", "", t)
    t = re.sub(r"(%|cm|mm|mg|ml|ng|g/l|g/dl|mmol/l|mmhg|cmh₂o|cmh2o|giờ|phút|lít|tuổi|năm|tháng|giây)-(?=\d)", "-", t)
    t = t.replace("giờ", "h").replace("phút", "ph").replace("lít", "l")
    t = t.replace("cmh2o", "cmh₂o").replace("nhịp/ph", "lần/ph")
    t = t.replace("³", "3").replace(",", ".")
    return t


def extract_num_tokens(text: str) -> list[str]:
    clean = norm_text(text)
    tokens = []
    for m in NUM_UNIT_RE.finditer(clean):
        tok = m.group(1).strip()
        # Bỏ các mốc năm tài liệu như 1974, 2018... nếu muốn vẫn giữ lại bằng đơn vị 'năm' hoặc kiểm riêng
        tokens.append(tok)
    return tokens


def extract_core_side(card: dict) -> str:
    if (card.get("type") or "").lower() == "cloze" or ("text" in card and "front" not in card):
        return card.get("text", "")
    back = card.get("back", "")
    # Tách chỉ lấy phần 🎯 Trả lời cốt lõi (không tính 💡 Giải thích của AI)
    core = back.split("💡 Giải thích của AI:")[0]
    return f"{card.get('front', '')} {core}"


def count_table_rows(md_text: str) -> int:
    rows = 0
    for line in md_text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|") and not re.match(r"^\|[\s:\-|]+\|$", s):
            rows += 1
    return rows


def apkg_note_count(apkg_path: Path) -> int:
    if not apkg_path.exists():
        return -1
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(apkg_path) as zf:
            db = next(n for n in ("collection.anki21", "collection.anki2") if n in zf.namelist())
            zf.extract(db, tmp)
        con = sqlite3.connect(Path(tmp) / db)
        try:
            return con.execute("select count(*) from notes").fetchone()[0]
        finally:
            con.close()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-anki", action="store_true")
    args = ap.parse_args(argv)

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    cat_by_id = {x["id"]: x for x in catalog.get("ngoai", [])}
    anki_decks = None if args.skip_anki else set(ac("deckNames"))

    lines = [
        "# BÁO CÁO KIỂM ĐỊNH SỰ SÁT BAREM — 11 BÀI NGOẠI KHOA",
        "",
        "| Mã bài | Thư mục | Manifest OK | Cards (.py/json/apkg/Anki/Web) | Mã `[Bx.yy]` | Bảng (Gốc/Repo) | Số liệu gốc thiếu trong Core thẻ | Số lạ trong Core (cần rà) | Trạng thái |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
    ]

    details = []
    total_fail = 0

    for desktop_name, folder_name in PAIRS:
        d_path = DESKTOP_BAREM_DIR / desktop_name
        l_dir = NGOAI_DIR / folder_name
        lj = json.loads((l_dir / "lesson.json").read_text(encoding="utf-8"))
        lid = lj["id"]
        deck_spec = lj["deck"]

        # Gate 1: Manifest & Sync
        expected_barem_md = f"{folder_name}_BAREM.md"
        manifest_errs = []
        if lj.get("lesson") != expected_barem_md:
            manifest_errs.append(f"lesson={lj.get('lesson')} != {expected_barem_md}")
        if lj.get("barem") != expected_barem_md:
            manifest_errs.append(f"barem={lj.get('barem')} != {expected_barem_md}")
        if not deck_spec.get("required_sections"):
            manifest_errs.append("thiếu required_sections trong deck")

        # Load cards from .py
        import importlib.util
        src_path = l_dir / deck_spec["cards_source"]
        spec = importlib.util.spec_from_file_location(src_path.stem, src_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        cards = mod.cards_data

        json_path = l_dir / f"{deck_spec['basename']}.cards.v2.json"
        apkg_path = l_dir / f"{deck_spec['basename']}.apkg"
        n_py = len(cards)
        n_json = len(json.loads(json_path.read_text(encoding="utf-8"))["cards"]) if json_path.exists() else -1
        n_apkg = apkg_note_count(apkg_path)

        if args.skip_anki:
            n_anki = "-"
            legacy_alive = []
        else:
            dname = deck_spec["deck_name"]
            nids = ac("findNotes", query=f'deck:"{dname}"') if dname in anki_decks else []
            n_anki = len(nids)
            legacy_alive = [ld for ld in deck_spec.get("legacy_anki_decks", []) if ld in anki_decks]
            if legacy_alive:
                manifest_errs.append(f"còn legacy deck: {legacy_alive}")
            if nids and json_path.exists():
                lock_path = l_dir / "anki_lock.json"
                if lock_path.exists():
                    lock_data = json.loads(lock_path.read_text(encoding="utf-8"))
                    json_cards = {c["id"]: c for c in json.loads(json_path.read_text(encoding="utf-8"))["cards"]}
                    live_infos = {i["noteId"]: i for i in ac("notesInfo", notes=nids)}
                    mismatch_fields = 0
                    for cid, cdata in json_cards.items():
                        nid = lock_data.get(cid, {}).get("note_id")
                        info = live_infos.get(nid)
                        if not info:
                            mismatch_fields += 1
                            continue
                        fields = info["fields"]
                        if "Text" in fields:
                            if html.unescape(fields["Text"]["value"]).strip() != html.unescape(cdata.get("text", "")).strip():
                                mismatch_fields += 1
                        else:
                            if (html.unescape(fields["Front"]["value"]).strip() != html.unescape(cdata.get("front", "")).strip()
                                    or html.unescape(fields["Back"]["value"]).strip() != html.unescape(cdata.get("back", "")).strip()):
                                mismatch_fields += 1
                    if mismatch_fields:
                        manifest_errs.append(f"lệch nội dung live Anki: {mismatch_fields} thẻ")

        cat_entry = cat_by_id.get(lid, {})
        n_web = cat_entry.get("cards_count", -1)
        if cat_entry.get("word_count", 0) > 6000:
            manifest_errs.append(f"HungMed đang dùng bài dài cũ ({cat_entry.get('word_count')} từ)")

        counts_ok = (n_py == n_json == n_apkg == n_web) and (args.skip_anki or n_anki == n_py)
        if not counts_ok:
            manifest_errs.append(f"lệch số thẻ py={n_py}/json={n_json}/apkg={n_apkg}/anki={n_anki}/web={n_web}")

        # Gate 2 & 3: Độ phủ mã [Bx.yy], bảng và số liệu + đơn vị
        desktop_raw = strip_barem_meta(d_path.read_text(encoding="utf-8"))
        repo_barem_path = l_dir / expected_barem_md
        repo_raw = strip_barem_meta(repo_barem_path.read_text(encoding="utf-8")) if repo_barem_path.exists() else ""

        barem_codes = set(re.findall(r"\[(B\d+\.\d+)\]", repo_raw))
        covered_codes = set()
        for c in cards:
            covered_codes.update(re.findall(r"\b(B\d+\.\d+)\b", c.get("extra", "")))
        missing_codes = sorted(barem_codes - covered_codes)

        t_orig = count_table_rows(desktop_raw)
        t_repo = count_table_rows(repo_raw)

        # So khớp số + đơn vị giữa desktop barem vs Core của thẻ
        orig_tokens = extract_num_tokens(desktop_raw)
        core_all = " || ".join(norm_text(extract_core_side(c)) for c in cards)
        full_all = " || ".join(norm_text(f"{c.get('front','')} {c.get('back','')} {c.get('text','')}") for c in cards)
        core_norm_compact = norm_token(core_all)
        full_norm_compact = norm_token(full_all)
        orig_norm_compact = norm_token(norm_text(desktop_raw))

        missing_in_core = []
        missing_everywhere = []
        seen = set()
        for tok in orig_tokens:
            nt = norm_token(tok)
            if nt in seen:
                continue
            seen.add(nt)
            if nt not in core_norm_compact:
                # Khớp theo 2 đầu mút của khoảng (vd a-b unit -> có mặt trong core) hoặc số đơn nằm trong khoảng a-b unit
                m_rng = re.match(r"^(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)([a-z%µ°/²³₀-₉]+)$", nt)
                if m_rng and f"{m_rng.group(1)}{m_rng.group(3)}" in core_norm_compact and f"{m_rng.group(2)}{m_rng.group(3)}" in core_norm_compact:
                    continue
                m_one = re.match(r"^(\d+(?:\.\d+)?)([a-z%µ°/²³₀-₉]+)$", nt)
                if m_one and re.search(rf"(?<!\d){re.escape(m_one.group(1))}-\d+(?:\.\d+)?{re.escape(m_one.group(2))}", core_norm_compact):
                    continue
                in_full = nt in full_norm_compact
                if in_full:
                    missing_in_core.append(tok)
                else:
                    missing_everywhere.append(tok)

        # Gate 4: Số có đơn vị xuất hiện trong Core thẻ nhưng KHÔNG có trong desktop barem
        card_tokens = extract_num_tokens(core_all)
        extra_in_core = []
        seen_c = set()
        for tok in card_tokens:
            nt = norm_token(tok)
            if nt in seen_c:
                continue
            seen_c.add(nt)
            if nt not in orig_norm_compact:
                extra_in_core.append(tok)

        is_pass = (not manifest_errs) and (not missing_codes) and (not missing_everywhere)
        if not is_pass:
            total_fail += 1
        status = "PASS" if is_pass else "REVIEW"

        lines.append(
            f"| **{lid}** | `{folder_name}` | {'OK' if not manifest_errs else 'LỖI (' + str(len(manifest_errs)) + ')'} | "
            f"`{n_py}/{n_json}/{n_apkg}/{n_anki}/{n_web}` | `{len(covered_codes)}/{len(barem_codes)}` | "
            f"`{t_orig}/{t_repo}` | `{len(missing_everywhere)}` hẳn / `{len(missing_in_core)}` ở 💡 | "
            f"`{len(extra_in_core)}` | **{status}** |"
        )

        details.append(f"## {lid} — `{folder_name}` ({status})")
        if manifest_errs:
            details.append("- **Lỗi Manifest / Sync:** " + "; ".join(manifest_errs))
        if missing_codes:
            details.append(f"- **Thiếu mã barem `[Bx.yy]`:** {missing_codes}")
        if missing_everywhere:
            details.append(f"- **Số liệu có ở Desktop barem nhưng chưa thấy khớp chính xác trong thẻ (`{len(missing_everywhere)}`):** `{', '.join(missing_everywhere)}`")
        if missing_in_core:
            details.append(f"- **Số liệu nằm ở phần `💡 Giải thích` (chưa thấy ở mặt hỏi/`🎯` cốt lõi) (`{len(missing_in_core)}`):** `{', '.join(missing_in_core)}`")
        if extra_in_core:
            details.append(f"- **Số có đơn vị ở Core thẻ chưa khớp nguyên cụm trong Desktop barem (`{len(extra_in_core)}`):** `{', '.join(extra_in_core)}`")
        if not (manifest_errs or missing_codes or missing_everywhere or missing_in_core or extra_in_core):
            details.append("- Khớp sạch hoàn toàn mọi tiêu chí tự động.")
        details.append("")

    report_text = "\n".join(lines + ["", "---", ""] + details)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report_text, encoding="utf-8")
    print(report_text)
    print(f"\n[REPORT] Đã lưu báo cáo tại: {REPORT_PATH} (total_review={total_fail})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
