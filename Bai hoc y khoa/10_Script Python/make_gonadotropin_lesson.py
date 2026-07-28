"""Build Anki deck (.apkg) cho bai Gonadotropin Dosing trong IVF.
20 cards, Pastel theme.
"""
import json
from pathlib import Path
from lesson_builder import (
    build_pastel_model_and_deck, add_cards_from_json, write_apkg
)

ROOT = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
SOURCE = ROOT / "09_Source - Markdown" / "02_Ho tro sinh san ART" / "17_Gonadotropin_Dosing"
APKG_OUT = ROOT / "02_Ho tro sinh san ART" / "17_Gonadotropin_Dosing" / f"Anki - Gonadotropin Dosing IVF 20 cards - 2026-06-27.apkg"

CARDS = [
    # === Tong quan ===
    {
        "front": "3 tru cot quyet dinh lieu gonadotropin khoi dau trong IVF?",
        "back": "1) Du tru buong trung (AMH + AFC + tuoi). 2) Phac do kich thich (antagonist vs long agonist). 3) Muc tieu noan (so phoi can cho 1 lan sinh - 'one healthy baby at a time')."
    },
    {
        "front": "Lieu FSH khoi dau cho hyper-responder (AMH > 36 pmol/L, AFC > 18, tuoi < 35) theo ESHRE 2025?",
        "back": "100 - < 150 IU/ngay. Protocol: GnRH antagonist. Trigger: GnRH agonist + freeze-all. Muc tieu: 8-15 noan, an toan."
    },
    {
        "front": "Lieu FSH khoi dau cho normal responder (AMH 12-32 pmol/L, AFC 8-18, tuoi 30-38)?",
        "back": "150 - 225 IU/ngay. Protocol: antagonist hoac long agonist. Trigger: hCG 5000-10000 IU. Muc tieu: 8-15 noan."
    },
    {
        "front": "Lieu FSH khoi dau cho suboptimal/poor responder (POSEIDON 1-4) theo ESHRE 2025?",
        "back": "225 - 300 IU/ngay. Protocol: antagonist + dual trigger. Co the can nhac DuoStim, corifollitropin. Muc tieu: 3-8 noan. ESHRE 2025: Strong NOT recommended > 300 IU cho low responder."
    },

    # === Cac loai gonadotropin ===
    {
        "front": "Phan biet rFSH va HP-hMG?",
        "back": "rFSH (Gonal-F, Puregon): tai to hop, tinh khiet, khong co LH activity. HP-hMG (Menopur): tu nuoc tieu phu nu man kinh, co FSH + LH + hCG activity (LH tu hCG)."
    },
    {
        "front": "So sanh rFSH va HP-hMG theo Bordewijk 2019 meta-analysis (PMID 31206036)?",
        "back": "Luong gonadotropin tong can de dat 1 live birth TUONG DUONG. Profile an toan gan nhu nhau. Chon rFSH cho normal responder; HP-hMG cho poor responder can LH activity."
    },
    {
        "front": "Corifollitropin alpha (Elonva) la gi va khi nao dung?",
        "back": "rFSH gan CTP (hCG beta tail) - long-acting. 1 mui duy nhat thay 7 ngay rFSH. Phu hop normal responder. KHONG phu hop poor responder (can linh hoat dose adjustment hang ngay)."
    },

    # === Du tru buong trung ===
    {
        "front": "Nguong AMH va AFC cho hyperresponse theo HERA consensus 2024 (PMID 39603489)?",
        "back": "AMH > 36.2 pmol/L (~5 ng/mL) HOAC AFC > 18-24 nang. Nguong poor response: AMH < 7.7 pmol/L (< 1.1 ng/mL) HOAC AFC < 5-7 nang."
    },
    {
        "front": "Thuat toan AMH-based dosing theo Sopa 2019 (PMID 31009858)?",
        "back": "AMH < 12 pmol/L: toi da (corifollitropin). AMH 12-32 pmol/L: tieu chuan 150 IU/ngay rFSH. AMH > 32 pmol/L: toi thieu 112 IU/ngay HP-hMG. Duy tri ti le thai, giam OHSS."
    },
    {
        "front": "POSEIDON criteria phan nhom the nao?",
        "back": "4 nhom dua tren: tuoi (< 35 vs >= 35), du tru buong trung (binh thuong vs giam), va dap ung truoc do. Group 1: tuoi < 35 + du tru binh thuong + poor prev. Group 2: tuoi >= 35 + du tru binh thuong + poor prev. Group 3: tuoi < 35 + du tru giam. Group 4: tuoi >= 35 + du tru giam."
    },

    # === Bang chung tu RCT ===
    {
        "front": "OPTIMIST trial (van Tilborg 2017, PMID 29121350) ket luan gi?",
        "back": "RTC da trung tam Ha Lan (n=1515) so sanh individualized dosing (dua tren AFC+AMH) vs standard 150 IU. Ket qua: individualized KHONG tang ongoing pregnancy, NHUNG giam chi phi o nhom du tru cao. Cung cap bang chung AMH/AFC co the ca nhan hoa lieu."
    },
    {
        "front": "Liu 2023 RCT (PMID 37105131) so sanh 300 IU vs 150 IU o poor responder?",
        "back": "RCT Trung Quoc (n=686) o poor responder. Nhom 300 IU: nhieu noan hon (+2-3), nhieu phoi hon, NHUNG KHONG tang live birth rate. Khong tang OHSS. Phu hop ESHRE 2025 Strong NOT recommended > 300 IU."
    },
    {
        "front": "Ai that su benefit tu tang lieu 300 IU o poor responders (Liu 2023 secondary, PMID 37844507)?",
        "back": "Benh nhan AMH >= 1 ng/mL + tuoi < 38: CO THE benefit tu 300 IU. Benh nhan AMH < 1 ng/mL hoac tuoi >= 38: KHONG benefit ro rang, nen chuyen sang chien luoc khac (mini-IVF, DuoStim, donor)."
    },
    {
        "front": "Chen 2026 personalized FSH cho PCOS (PMID 42072310) de xuat gi?",
        "back": "369 benh nhan PCOS GnRH antagonist. Phat trien cong cu ca nhan hoa lieu rFSH dua tren dap ung ca nhan (oocyte target 10-20, >= 40% nang >= 16 mm). Goi y: BAT DAU THAP + tang dan dua tren monitoring som tot hon bat dau cao roi coasting."
    },

    # === Dieu chinh lieu trong cycle ===
    {
        "front": "Theo doi som ngay 5-7 trong cycle IVF: can xet gi va quyet dinh dieu chinh the nao?",
        "back": "E2 huyet thanh + sieu am so nang >= 10 mm + noi mac tu cung. E2 < 200 pg/mL -> step-up; E2 > 500-800 pg/mL -> step-down. < 4 nang ngay 7 -> tang lieu; > 14 nang -> giam lieu/coasting."
    },
    {
        "front": "Coasting la gi va khi nao ap dung?",
        "back": "Ngung gonadotropin 1-3 ngay khi E2 > 4000-5000 pg/mL, cho E2 giam, roi trigger. Hieu qua trung binh trong phong ngua OHSS."
    },
    {
        "front": "Dual trigger (GnRH agonist + hCG lieu thap) la gi va khi nao dung?",
        "back": "Ket hop GnRH agonist + hCG lieu thap o trigger cuoi cung. Cho suboptimal responder: cai thien ti le noan truong thanh va ti le thai. Phu hop POSEIDON 3, 4."
    },

    # === Chien luoc dac biet ===
    {
        "front": "Cac lua chon cho poor/suboptimal responder NGOAI tang lieu?",
        "back": "DuoStim (ESHRE 2025 Strong); Mini-IVF + clomiphene; Androgen priming (testosterone/DHEA); Corifollitropin + LH supplementation; Donor oocyte (khi AMH cuc thap + tuoi cao)."
    },
    {
        "front": "Hyper-responder / PCOS can chien luoc gi?",
        "back": "Lieu thap 100-125 IU; GnRH antagonist; GnRH agonist trigger; Freeze-all neu nguy co OHSS cao; Cabergoline du phong; Coasting neu E2 > 4000-5000 pg/mL."
    },
    {
        "front": "Tac kich thich (repeated COS) co anh huong xau khong (Wang 2025, PMID 40319269)?",
        "back": "Lap lai COS 2-3 chu ky KHONG anh huong xau den ovarian reserve markers (AMH, AFC) hoac pregnancy outcomes. Yen tam cho benh nhan can nhieu chu ky."
    },
]
# Note: 20 cards above (counted).

# Save JSON
SOURCE.mkdir(parents=True, exist_ok=True)
json_path = SOURCE / "gonadotropin_dosing_cards.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump({"deck_name": "Gonadotropin Dosing IVF 2026-06-27", "cards": CARDS}, f, ensure_ascii=False, indent=2)
print(f"JSON saved: {json_path} ({len(CARDS)} cards)")

# Build deck
model, deck = build_pastel_model_and_deck(
    model_id=1607392320,
    model_name="Gonadotropin Dosing IVF (Pastel)",
    deck_id=2059390112,
    deck_name="ART::Gonadotropin Dosing trong IVF (2026-06-27)",
    deck_description="20 cards ve lieu gonadotropin trong IVF: phan nhom dap ung, AMH/AFC, OPTIMIST trial, ESHRE 2025. Pastel theme."
)

n = add_cards_from_json(deck, model, json_path, "Gonadotropin_Dosing")
print(f"Added {n} cards to deck")

write_apkg(deck, APKG_OUT)
print(f"APKG saved: {APKG_OUT}")
