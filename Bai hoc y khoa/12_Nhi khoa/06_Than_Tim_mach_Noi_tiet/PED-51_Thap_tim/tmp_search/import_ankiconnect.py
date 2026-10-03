# -*- coding: utf-8 -*-
"""Import 10 MASTER decks into Anki Desktop via AnkiConnect (bulk addNotes)."""
import json
import re
import urllib.request

ANKI = "http://localhost:8765"
BASE = "F:/DL/mavisresearch/Bai hoc y khoa/12_Nhi khoa"

CSS = """
.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #090e17;
  padding: 18px;
  max-width: 680px;
  margin: 0 auto;
}
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.badge-barem {
  background-color: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}
.badge-ebm {
  background-color: rgba(6, 182, 212, 0.15);
  color: #22d3ee;
  border: 1px solid rgba(6, 182, 212, 0.4);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 10px;
}
.answer-box {
  background-color: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  padding: 14px 16px;
  border-left: 3px solid #38bdf8;
  margin-top: 10px;
  font-size: 14.5px;
}
.cloze {
  font-weight: 700;
  color: #38bdf8;
  border-bottom: 2px solid #0284c7;
  padding: 0 2px;
}
.extra-box {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.04);
  border-left: 3px solid #38bdf8;
  font-size: 14px;
  color: #cbd5e1;
}
.extra-title {
  font-weight: 700;
  color: #38bdf8;
  margin-bottom: 4px;
}
"""

BASIC_Q = '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>'
BASIC_A = ('<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{Front}}</div>'
           '<hr id="answer"><div class="answer-box">{{Back}}</div>'
           '{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn & lưu ý:</div>{{Extra}}</div>{{/Extra}}')
CLOZE_Q = '<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div>'
CLOZE_A = ('<div class="badge {{BadgeClass}}">{{Badge}} • {{Category}}</div><div class="question">{{cloze:Text}}</div>'
           '<hr id="answer">{{#Extra}}<div class="extra-box"><div class="extra-title">Nguồn & lưu ý:</div>{{Extra}}</div>{{/Extra}}')

DECKS = [
    ("06_Than_Tim_mach_Noi_tiet/PED-51_Thap_tim/PED-51_Thap_tim_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-51: Thấp tim ở trẻ em"),
    ("01_Hoi_suc_Cap_cuu_Ngo_doc/PED-52_Danh_gia_va_xu_tri_benh_nhan_nang/PED-52_Danh_gia_va_xu_tri_benh_nhan_nang_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-52: Đánh giá & Xử trí bệnh nhân nặng"),
    ("05_Truyen_nhiem/PED-53_Hach_to/PED-53_Hach_to_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-53: Hạch to ở trẻ em"),
    ("05_Truyen_nhiem/PED-54_Tiep_can_tre_dau_khop/PED-54_Tiep_can_tre_dau_khop_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-54: Tiếp cận trẻ đau khớp"),
    ("01_Hoi_suc_Cap_cuu_Ngo_doc/PED-11_Roi_loan_toan_kiem_va_Doc_khi_mau_dong_mach_nhi/PED-11_Roi_loan_toan_kiem_va_Doc_khi_mau_dong_mach_nhi_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-11: Rối loạn toan kiềm & Đọc khí máu động mạch nhi"),
    ("01_Hoi_suc_Cap_cuu_Ngo_doc/PED-50_Roi_loan_nuoc_va_dien_giai_o_tre_em/PED-50_Roi_loan_nuoc_va_dien_giai_o_tre_em_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-50: Tiếp cận & Xử trí Rối loạn điện giải ở trẻ em"),
    ("04_Tieu_hoa_va_Dinh_duong/PED-46_Tiep_can_gan_to/PED-46_Tiep_can_gan_to_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-46: Tiếp cận gan to ở trẻ em"),
    ("06_Than_Tim_mach_Noi_tiet/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot/PED-43_Benh_tim_bam_sinh_thuong_gap_va_Con_tim_Fallot_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-43: Bệnh tim bẩm sinh thường gặp & Cơn tim Fallot"),
    ("06_Than_Tim_mach_Noi_tiet/PED-47_Tiep_can_dai_mau/PED-47_Tiep_can_dai_mau_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-47: Tiếp cận đái máu ở trẻ em"),
    ("06_Than_Tim_mach_Noi_tiet/PED-48_Suy_tim_o_tre_em/PED-48_Suy_tim_o_tre_em_MASTER_v1.cards.v2.json",
     "Nhi khoa Y6::PED-48: Suy tim ở trẻ em"),
]


def invoke(action, **params):
    req = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    with urllib.request.urlopen(urllib.request.Request(ANKI, req), timeout=120) as r:
        res = json.loads(r.read())
    if res.get("error"):
        raise RuntimeError(f"{action}: {res['error']}")
    return res.get("result")


def esc(t):
    return re.sub(r"<(?!(?:b|/b|i|/i|br|div|/div|span|/span|hr)\b)", "&lt;", t or "")


def ensure_model(name, fields, templates, is_cloze=False):
    try:
        invoke("createModel", modelName=name, inOrderFields=fields, css=CSS,
               isCloze=is_cloze, cardTemplates=templates)
        print(f"  model created: {name}")
    except RuntimeError as e:
        if "exists" in str(e).lower() or "duplicate" in str(e).lower():
            print(f"  model exists, reuse: {name}")
        else:
            raise


def main():
    ensure_model("NhiKhoa_Master_Basic",
                 ["Front", "Back", "Extra", "Category", "Badge", "BadgeClass"],
                 [{"Name": "Master Basic", "Front": BASIC_Q, "Back": BASIC_A}])
    ensure_model("NhiKhoa_Master_Cloze",
                 ["Text", "Extra", "Category", "Badge", "BadgeClass"],
                 [{"Name": "Master Cloze", "Front": CLOZE_Q, "Back": CLOZE_A}],
                 is_cloze=True)
    total = 0
    for rel, deck in DECKS:
        d = json.load(open(f"{BASE}/{rel}", encoding="utf-8"))
        cards = d.get("cards") if isinstance(d, dict) else d
        invoke("createDeck", deck=deck)
        notes = []
        for c in cards:
            barem = c.get("track") == "barem_goc"
            badge = "🏛️ BAREM GỐC Y THÁI BÌNH" if barem else "🔬 EBM HIỆN ĐẠI & LÂM SÀNG"
            bclass = "badge-barem" if barem else "badge-ebm"
            if c["type"] == "basic":
                notes.append({"deckName": deck, "modelName": "NhiKhoa_Master_Basic",
                              "fields": {"Front": esc(c["front"]), "Back": esc(c["back"]),
                                         "Extra": esc(c.get("extra", "")), "Category": c.get("category", ""),
                                         "Badge": badge, "BadgeClass": bclass},
                              "tags": c.get("tags", []),
                              "options": {"allowDuplicate": False, "duplicateScope": "deck"}})
            else:
                notes.append({"deckName": deck, "modelName": "NhiKhoa_Master_Cloze",
                              "fields": {"Text": esc(c["text"]), "Extra": esc(c.get("extra", "")),
                                         "Category": c.get("category", ""), "Badge": badge, "BadgeClass": bclass},
                              "tags": c.get("tags", []),
                              "options": {"allowDuplicate": False, "duplicateScope": "deck"}})
        res = invoke("addNotes", notes=notes)
        added = sum(1 for x in res if x)
        dupes = len(res) - added
        got = invoke("findCards", query=f'deck:"{deck}"')
        print(f"{deck}: input={len(cards)} added={added} dupes_skipped={dupes} in_anki={len(got)}")
        assert len(got) == len(cards), f"COUNT MISMATCH {deck}"
        total += len(got)
    print(f"ALL OK — total {total} cards in 10 decks.")


if __name__ == "__main__":
    main()
