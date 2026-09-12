import json
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "Sieu_am_theo_doi_kich_thich_buong_trung_slider3636.deck.json"
SRC = "Nguồn: bài soạn đã verify — PMID 32395637; 41732035; 33280722; 21558332; 26597569"


def s(kind, **kw):
    d = {"type": kind}
    d.update(kw)
    return d


def content(title, points, variant="bullets"):
    return s("content", title=title, variant=variant, points=points, footnote=SRC)


def twocol(title, lt, lp, rt, rp, variant="compared"):
    return s("two_column", title=title, variant="vs_compare" if variant == "compared" else "cards",
             left_title=lt, left_points=lp, right_title=rt, right_points=rp, note=SRC)


def three(title, cols):
    return s("three_column", title=title, variant="pillars", columns=cols)


def sec(n, t, sub=""):
    return s("section", variant="number_block", part_number=n, part_title=t, part_subtitle=sub)


def keymsg(msg, variant="dark_hero", kicker=""):
    return s("key_message", variant=variant, message=msg, kicker=kicker)


def table(title, headers, rows):
    return s("table", variant="comparison_highlight", title=title, headers=headers, rows=rows)


def checklist(title, items):
    return s("criteria", variant="score_points", title=title, items=[{"text": i, "points": "\u2713"} for i in items])


def yesno(title, question, yes, no):
    return s("algorithm", variant="branching_yesno", title=title, question=question, yes_branch=yes, no_branch=no)


def flow(title, steps):
    nodes = []
    for i, t in enumerate(steps):
        nodes.append({"text": t, "type": "start" if i == 0 else "end" if i == len(steps) - 1 else "process"})
    return s("algorithm", variant="linear_flow", title=title, nodes=nodes)


def mechanism(title, steps):
    return s("mechanism", variant="horizontal_steps", title=title, steps=[{"title": t[0], "desc": t[1]} for t in steps])


def timeline(title, events):
    return s("timeline", variant="horizontal_milestones", title=title, events=[{"date": e[0], "title": e[1], "desc": e[2]} for e in events])


def defin(term, definition):
    return s("definition", variant="term_box", term=term, definition=definition)


def big(title, stats):
    return s("big_number", variant="single_hero", title=title, stats=stats)


def summary(title, points):
    return s("summary", variant="takeaways", title=title, points=points)


def refs(title, refs_list):
    return s("references", variant="numbered", title=title, refs=refs_list)


slides = [
    # ═══ COVER ═══
    s("title", variant="split_dark",
      title="Si\u00eau \u00e2m theo d\u00f5i qu\u00e1 tr\u00ecnh k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng",
      subtitle="Ch\u01b0\u01a1ng 5 \u2014 Deck h\u1ecdc c\u00e1 nh\u00e2n",
      author="B\u00e1c s\u0129 Ng\u1ecdc H\u01b0ng",
      specialty="ART / IVF-ICSI",
      date="2026-07-03"),

    s("outline", variant="numbered", title="N\u1ed9i dung b\u00e0i h\u1ecdc", chapters=[
        "I. \u0110\u1ea1i c\u01b0\u01a1ng",
        "II. C\u00e1c ph\u00e1c \u0111\u1ed3 KTBT \u2014 1. D\u1ef1 tr\u1eef & \u0111\u00e1p \u1ee9ng",
        "II. 2. C\u01a1 s\u1edf l\u00fd thuy\u1ebft c\u1ee7a ph\u00e1c \u0111\u1ed3",
        "II. 3. C\u00e1c ph\u00e1c \u0111\u1ed3 ch\u00ednh",
        "II. 4. Th\u1eddi \u0111i\u1ec3m k\u00edch th\u00edch",
        "II. 5. Li\u1ec1u FSH & theo d\u00f5i",
        "II. 6. Tr\u01b0\u1edfng th\u00e0nh no\u00e3n (trigger)",
        "II. 7. \u0110\u00f4ng ph\u00f4i to\u00e0n b\u1ed9",
        "III. K\u1ebft lu\u1eadn & TLTK",
    ]),

    # ═══ I. ĐẠI CƯƠNG ═══
    sec("I", "\u0110\u1ea0I C\u01af\u01a0NG",
        "Si\u00eau \u00e2m theo d\u00f5i qu\u00e1 tr\u00ecnh k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng"),

    content("\u0110\u1ea1i c\u01b0\u01a1ng \u2014 t\u1ea7m quan tr\u1ecdng",
            ["K\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng l\u00e0 m\u1ed9t b\u01b0\u1edbc r\u1ea5t quan tr\u1ecdng trong h\u1ed7 tr\u1ee3 sinh s\u1ea3n.",
             "\u0110\u00e1nh gi\u00e1 d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng tr\u01b0\u1edbc KTBT gi\u00fap TI\u00caN L\u01af\u1ee2NG v\u00e0 \u0110\u1ecaNH LI\u1ec0U FSH kh\u1edfi \u0111\u1ea7u.",
             "Li\u1ec1u qu\u00e1 th\u1ea5p \u2192 nang tho\u00e1i h\u00f3a.",
             "Li\u1ec1u qu\u00e1 cao \u2192 nguy c\u01a1 qu\u00e1 k\u00edch bu\u1ed3ng tr\u1ee9ng + t\u0103ng chi ph\u00ed."]),

    content("Vai tr\u00f2 theo d\u00f5i trong KTBT",
            ["Theo d\u00f5i s\u1ef1 ph\u00e1t tri\u1ec3n nang no\u00e3n \u0111\u1ec3 k\u1ecbp th\u1eddi \u0111i\u1ec1u ch\u1ec9nh li\u1ec1u.",
             "B\u1ed5 sung antagonist \u0111\u00fang th\u1eddi \u0111i\u1ec3m.",
             "Quy\u1ebft \u0111\u1ecbnh th\u1eddi gian tr\u01b0\u1edfng th\u00e0nh no\u00e3n (trigger).",
             "Ph\u00e1t hi\u1ec7n s\u1edbm nguy c\u01a1 qu\u00e1 k\u00edch bu\u1ed3ng tr\u1ee9ng \u0111\u1ec3 \u0111i\u1ec1u ch\u1ec9nh k\u1ecbp th\u1eddi."]),

    content("C\u1eadp nh\u1eadt: ASRM v\u1ec1 ovarian reserve",
         ["ASRM \u0111\u1ecbnh ngh\u0129a ovarian reserve l\u00e0 S\u1ed0 L\u01af\u1ee2NG NO\u00c3N C\u00d2N L\u1ea0I.",
          "AMH v\u00e0 AFC h\u1eefu \u00edch \u0111\u1ec3 d\u1ef1 \u0111o\u00e1n oocyte yield sau controlled ovarian stimulation.",
          "Nh\u01b0ng l\u00e0 POOR PREDICTORS c\u1ee7a reproductive potential n\u1ebfu t\u00e1ch kh\u1ecfi y\u1ebfu t\u1ed1 TU\u1ed4I.",
          "PMID: 33280722"]),

    content("C\u1eadp nh\u1eadt: ESHRE 2020 \u2192 2025/2026",
         ["ESHRE 2020: 84 khuy\u1ebfn c\u00e1o cho ch\u1ecdn ph\u00e1c \u0111\u1ed3, li\u1ec1u, theo d\u00f5i, trigger, ph\u00f2ng OHSS.",
          "ESHRE update 2025/2026: m\u1edf r\u1ed9ng th\u00e0nh 121 khuy\u1ebfn c\u00e1o.",
          "Nh\u1ea5n m\u1ea1nh C\u00c1 TH\u1ec2 H\u00d3A theo \u0111\u00e1p \u1ee9ng d\u1ef1 ki\u1ebfn, hi\u1ec7u qu\u1ea3 v\u00e0 an to\u00e0n.",
          "PMID: 32395637; 41732035"]),

    # ═══ II.1. DỰ TRỮ BUỒNG TRỨNG ═══
    sec("II.1", "D\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng & \u0111\u00e1p \u1ee9ng",
        "Ovarian reserve \u2260 Ovarian response"),

    content("Kh\u00e1i ni\u1ec7m d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng",
            ["Tr\u01b0\u1edbc KTBT, ph\u1ea3i \u0111\u00e1nh gi\u00e1 d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng (ovarian reserve).",
             "M\u1ee5c ti\u00eau: ti\u00ean l\u01b0\u1ee3ng kh\u1ea3 n\u0103ng thu \u0111\u01b0\u1ee3c no\u00e3n sau KTBT v\u00e0 \u0111\u1ecbnh li\u1ec1u FSH kh\u1edfi \u0111\u1ea7u.",
             "C\u00e1c marker: tu\u1ed5i, FSH \u0111\u1ea7u chu k\u1ef3, AFC, AMH, tr\u1ecdng l\u01b0\u1ee3ng, ti\u1ec1n s\u1eed."]),

    content("4 marker d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng ch\u00ednh",
            ["1) Tu\u1ed5i: c\u00e0ng t\u0103ng th\u00ec d\u1ef1 tr\u1eef c\u00e0ng gi\u1ea3m.",
             "2) FSH \u0111\u1ea7u chu k\u1ef3: n\u1ebfu tr\u00ean 10 IU/L th\u00ec d\u1ef1 tr\u1eef gi\u1ea3m.",
             "3) AFC: \u0111\u1ebfm s\u1ed1 nang th\u1ee9 c\u1ea5p tr\u00ean si\u00eau \u00e2m.",
             "4) AMH: Anti-Mullerian Hormone.",
             "Hi\u1ec7n nay AFC v\u00e0 AMH l\u00e0 hai ch\u1ec9 s\u1ed1 \u0111\u01b0\u1ee3c s\u1eed d\u1ee5ng nhi\u1ec1u nh\u1ea5t."]),

    content("Ovarian response \u2014 \u0111\u00e1p \u1ee9ng bu\u1ed3ng tr\u1ee9ng",
            ["Kh\u00f4ng ph\u1ea3i b\u1ec7nh nh\u00e2n n\u00e0o c\u00f3 d\u1ef1 tr\u1eef t\u1ed1t c\u0169ng \u0111\u00e1p \u1ee9ng t\u1ed1t.",
             "Ovarian response l\u00e0 KH\u1ea2 N\u0102NG PH\u00c1T TRI\u1ec2N nang no\u00e3n khi KTBT.",
             "FOI (follicle-oocyte-index): s\u1ed1 no\u00e3n ch\u1ecdc h\u00fat / s\u1ed1 nang th\u1ee9 c\u1ea5p.",
             "FORT (Follicular Output Rate): s\u1ed1 nang tr\u01b0\u1edfng th\u00e0nh / s\u1ed1 nang th\u1ee9 c\u1ea5p."]),

    twocol("D\u1ef1 tr\u1eef vs \u0110\u00e1p \u1ee9ng",
           "Ovarian reserve", ["S\u1ed1 l\u01b0\u1ee3ng no\u00e3n ti\u1ec1m n\u0103ng", "AMH/AFC d\u1ef1 \u0111o\u00e1n oocyte yield", "Kh\u00f4ng ph\u1ea3n \u00e1nh ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n"],
           "Ovarian response", ["S\u1ed1 nang/no\u00e3n TH\u1ef0C T\u1ebe sau KTBT", "Ph\u1ee5 thu\u1ed9c li\u1ec1u, protocol, ti\u1ec1n s\u1eed", "C\u00f3 th\u1ec3 kh\u00e1c d\u1ef1 \u0111o\u00e1n ban \u0111\u1ea7u"]),

    content("C\u1eadp nh\u1eadt: Reserve \u2260 Response",
         ["Reserve l\u00e0 s\u1ed1 l\u01b0\u1ee3ng ti\u1ec1m n\u0103ng; response l\u00e0 s\u1ed1 nang/no\u00e3n TH\u1ef0C S\u1ef0 thu \u0111\u01b0\u1ee3c.",
          "AMH/AFC th\u1ea5p th\u01b0\u1eddng nguy c\u01a1 \u0111\u00e1p \u1ee9ng k\u00e9m.",
          "TU\u1ed4I v\u1eabn l\u00e0 y\u1ebfu t\u1ed1 l\u1edbn nh\u1ea5t chi ph\u1ed1i ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n v\u00e0 ti\u00ean l\u01b0\u1ee3ng sinh s\u1ed1ng."]),

    table("B\u1ea3ng c\u1eadp nh\u1eadt \u2014 Marker d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng",
          ["Marker", "D\u1ef1 \u0111o\u00e1n t\u1ed1t", "H\u1ea1n ch\u1ebf", "Ghi nh\u1edb"],
          [["AMH", "Oocyte yield", "Kh\u00f4ng thay tu\u1ed5i \u0111\u1ec3 d\u1ef1 \u0111o\u00e1n ch\u1ea5t l\u01b0\u1ee3ng", "\u1ed4n \u0111\u1ecbnh \u2192 l\u1ea5y b\u1ea5t k\u1ef3 ng\u00e0y"],
           ["AFC", "S\u1ed1 nang huy \u0111\u1ed9ng", "Ph\u1ee5 thu\u1ed9c ng\u01b0\u1eddi si\u00eau \u00e2m", "C\u1ea7n si\u00eau \u00e2m t\u1ed1t"],
           ["FSH", "Reserve gi\u1ea3m khi t\u0103ng r\u00f5", "Dao \u0111\u1ed9ng gi\u1eefa c\u00e1c chu k\u1ef3", "H\u1eefu \u00edch khi AMH/AFC th\u1ea5p"],
           ["Tu\u1ed5i", "Ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n & l\u1ec7ch b\u1ed9i", "Kh\u00f4ng \u0111o s\u1ed1 nang tr\u1ef1c ti\u1ebfp", "Bi\u1ebfn ti\u00ean l\u01b0\u1ee3ng l\u1edbn nh\u1ea5t"]]),

    # --- 1.1 AFC ---
    sec("II.1.1", "\u0110\u1ebfm s\u1ed1 nang th\u1ee9 c\u1ea5p (AFC)", ""),

    content("AFC \u2014 \u0110\u1ecbnh ngh\u0129a",
            ["Nang th\u1ee9 c\u1ea5p: c\u00e1c nang c\u00f3 k\u00edch th\u01b0\u1edbc t\u1eeb 2 \u0111\u1ebfn 9 mm.",
             "\u0110o v\u00e0 \u0111\u1ebfm v\u00e0o ng\u00e0y \u0111\u1ea7u chu k\u1ef3 kinh.",
             "\u0110\u00e2y l\u00e0 \u0111o\u00e0n h\u1ec7 nang \u0111\u00e3 \u0111\u01b0\u1ee3c tuy\u1ec3n ch\u1ecdn t\u1eeb tr\u01b0\u1edbc, s\u1ebd ph\u00e1t tri\u1ec3n trong chu k\u1ef3 n\u00e0y v\u00e0 ph\u1ee5 thu\u1ed9c FSH.",
             "AFC \u0111\u01b0\u1ee3c d\u00f9ng \u0111\u1ec3 ti\u00ean l\u01b0\u1ee3ng d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng v\u00e0 \u0111\u1ecbnh li\u1ec1u FSH kh\u1edfi \u0111\u1ea7u."]),

    content("AFC \u2014 \u0110\u00e1nh gi\u00e1 \u0111\u1ed9 \u0111\u1ed3ng \u0111\u1ec1u",
            ["Trong si\u00eau \u00e2m, c\u1ea7n \u0111\u00e1nh gi\u00e1 s\u1ef1 \u0110\u1ed2NG \u0110\u1ec0U c\u1ee7a c\u00e1c nang.",
             "Nang kh\u00f4ng \u0111\u1ed3ng \u0111\u1ec1u \u2192 ph\u00e1t tri\u1ec3n kh\u00f4ng \u0111\u1ec1u \u2192 c\u00f3 nang tr\u01b0\u1edfng th\u00e0nh xen l\u1eabn no\u00e3n tho\u00e1i h\u00f3a v\u00e0 no\u00e3n non.",
             "M\u1ed9t s\u1ed1 t\u00e1c gi\u1ea3 ch\u1ee7 tr\u01b0\u01a1ng \u0110\u1ed2NG B\u1ed8 H\u00d3A b\u1eb1ng estrogen trong pha ho\u00e0ng th\u1ec3 tr\u01b0\u1edbc KTBT.",
             "M\u1ee5c ti\u00eau: t\u0103ng s\u1ed1 no\u00e3n, t\u0103ng s\u1ed1 ph\u00f4i."]),

    content("AFC \u2014 Ti\u1ebfp c\u1eadn \u0111\u1ea7u d\u00f2",
            ["\u0110\u00e1nh gi\u00e1 ti\u1ebfp c\u1eadn c\u1ee7a \u0111\u1ea7u d\u00f2 \u0111\u1ebfn bu\u1ed3ng tr\u1ee9ng.",
             "Bu\u1ed3ng tr\u1ee9ng xa \u0111\u1ea7u d\u00f2 \u2192 KH\u00d3 KH\u0102N khi ch\u1ecdc h\u00fat no\u00e3n.",
             "Nguy\u00ean nh\u00e2n c\u00f3 th\u1ec3 do VI\u00caM D\u00cdNH, bu\u1ed3ng tr\u1ee9ng b\u1ecb k\u00e9o cao.",
             "\u1ea2nh h\u01b0\u1edfng t\u1edbi t\u01b0\u1edbi m\u00e1u bu\u1ed3ng tr\u1ee9ng \u2192 gi\u00e1n ti\u1ebfp \u1ea3nh h\u01b0\u1edfng \u0111\u00e1p \u1ee9ng."]),

    # --- 1.2 AMH ---
    sec("II.1.2", "N\u1ed3ng \u0111\u1ed9 AMH", ""),

    content("AMH \u2014 B\u1ea3n ch\u1ea5t v\u00e0 ngu\u1ed3n g\u1ed1c",
            ["AMH l\u00e0 hormon kh\u00e1ng \u1ed1ng Muller.",
             "\u0110\u01b0\u1ee3c b\u00e0i ti\u1ebft b\u1edfi c\u00e1c T\u1ebe B\u00c0O H\u1ea0T c\u1ee7a nang no\u00e3n nh\u1ecf v\u00e0 nang c\u00f3 h\u1ed1c.",
             "T\u00e1c d\u1ee5ng: \u01afC CH\u1ebe tuy\u1ec3n ch\u1ecdn nang no\u00e3n.",
             "AMH gi\u1ea3m d\u1ea7n theo \u0111\u1ed9 tu\u1ed5i c\u1ee7a ng\u01b0\u1eddi ph\u1ee5 n\u1eef."]),

    content("AMH \u2014 Di\u1ec5n gi\u1ea3i l\u00e2m s\u00e0ng",
            ["PCOS: AMH CAO \u2192 nang kh\u00f4ng ph\u00e1t tri\u1ec3n v\u00e0 tr\u01b0\u1edfng th\u00e0nh \u0111\u01b0\u1ee3c.",
             "Gi\u1ea3m d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng: AMH r\u1ea5t th\u1ea5p (s\u1ed1 nang d\u1ef1 tr\u1eef c\u00f2n l\u1ea1i \u00edt).",
             "\u01afu \u0111i\u1ec3m: n\u1ed3ng \u0111\u1ed9 KH\u00d4NG thay \u0111\u1ed5i trong chu k\u1ef3 \u2192 l\u1ea5y b\u1ea5t k\u1ef3 ng\u00e0y n\u00e0o.",
             "Ch\u00ednh x\u00e1c v\u00e0 thu\u1eadn ti\u1ec7n h\u01a1n so v\u1edbi FSH."]),

    # --- 1.3 Các chỉ số khác ---
    sec("II.1.3", "C\u00e1c ch\u1ec9 s\u1ed1 kh\u00e1c", "Tu\u1ed5i, FSH, m\u1ee5c ti\u00eau s\u1ed1 no\u00e3n"),

    content("Tu\u1ed5i \u2014 Y\u1ebfu t\u1ed1 quan tr\u1ecdng nh\u1ea5t",
            ["Tu\u1ed5i ph\u1ea3n \u00e1nh m\u1ed9t ph\u1ea7n d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng nh\u01b0ng kh\u00f4ng ph\u1ea3i ho\u00e0n to\u00e0n.",
             "C\u00e0ng l\u1edbn tu\u1ed5i th\u00ec d\u1ef1 tr\u1eef c\u00e0ng gi\u1ea3m.",
             "T\u1eeb 35 tu\u1ed5i tr\u1edf l\u00ean: d\u1ef1 tr\u1eef gi\u1ea3m + t\u1ef7 l\u1ec7 B\u1ea4T TH\u01af\u1edcNG NHI\u1ec4M S\u1eaeC TH\u1ec2 T\u0102NG.",
             "H\u1ec7 qu\u1ea3: t\u1ef7 l\u1ec7 c\u00f3 thai TH\u1ea4P."]),

    content("FSH \u0111\u1ea7u chu k\u1ef3",
            ["FSH l\u00e0 hormon h\u01b0\u1edbng sinh d\u1ee5c do tuy\u1ebfn y\u00ean b\u00e0i ti\u1ebft.",
             "Khi d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng gi\u1ea3m \u2192 FSH c\u00e0ng t\u0103ng cao.",
             "FSH > 10 IU/L \u2192 d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng gi\u1ea3m r\u1ea5t nhi\u1ec1u, KTBT th\u01b0\u1eddng \u0111\u00e1p \u1ee9ng k\u00e9m.",
             "Hi\u1ec7n FSH ch\u1ee7 y\u1ebfu \u0111\u01b0\u1ee3c xem x\u00e9t khi AFC v\u00e0 AMH th\u1ea5p.",
             "FSH cao \u1edf b\u1ec7nh nh\u00e2n \u0111\u00e3 gi\u1ea3m d\u1ef1 tr\u1eef \u2192 ti\u00ean l\u01b0\u1ee3ng K\u00c9M h\u01a1n FSH b\u00ecnh th\u01b0\u1eddng."]),

    content("M\u1ee5c ti\u00eau s\u1ed1 no\u00e3n \u2014 nghi\u00ean c\u1ee9u c\u1ee7a Sunkara",
            ["M\u1ee5c \u0111\u00edch KTBT trong IVF: \u0111\u1ee7 nang, ch\u1ea5t l\u01b0\u1ee3ng t\u1ed1t, an to\u00e0n.",
             "Nghi\u00ean c\u1ee9u Sunkara (HFEA): ph\u00e2n t\u00edch 400.135 chu k\u1ef3 IVF.",
             "Live birth rate T\u0102NG theo s\u1ed1 no\u00e3n thu \u0111\u01b0\u1ee3c \u0111\u1ebfn kho\u1ea3ng 15 no\u00e3n.",
             "Sau 15-20 no\u00e3n: PLATEAU, kh\u00f4ng t\u0103ng th\u00eam.",
             "S\u1ed1 no\u00e3n r\u1ea5t cao \u2192 LIVE BIRTH RATE GI\u1ea2M + t\u0103ng t\u1ef7 l\u1ec7 OHSS."]),

    big("S\u1ed1 no\u00e3n t\u1ed1i \u01b0u \u2192 ~15 no\u00e3n",
        [{"value": "~15", "label": "no\u00e3n l\u00e0 v\u00f9ng t\u1ed1i \u01b0u trong nghi\u00ean c\u1ee9u HFEA 400.135 chu k\u1ef3; sau \u0111\u00f3 plateau v\u00e0 nguy c\u01a1 t\u0103ng (PMID 21558332)"}]),

    content("C\u1eadp nh\u1eadt: M\u1ee5c ti\u00eau kh\u00f4ng ph\u1ea3i c\u00e0ng nhi\u1ec1u c\u00e0ng t\u1ed1t",
         ["M\u1ee5c ti\u00eau th\u1ef1c h\u00e0nh l\u00e0 T\u1ed0I \u01afU s\u1ed1 no\u00e3n \u0111i k\u00e8m AN TO\u00c0N.",
          "Kh\u00f4ng ph\u1ea3i k\u00edch c\u00e0ng nhi\u1ec1u c\u00e0ng t\u1ed1t.",
          "S\u1ed1 no\u00e3n r\u1ea5t cao \u2192 nguy c\u01a1 OHSS, kh\u00f4ng c\u1ea3i thi\u1ec7n live birth th\u00eam.",
          "PMID: 21558332"]),

    # ═══ II.2. CƠ SỞ LÝ THUYẾT ═══
    sec("II.2", "C\u01a1 s\u1edf l\u00fd thuy\u1ebft c\u1ee7a ph\u00e1c \u0111\u1ed3", "FSH threshold \u2013 FSH window \u2013 LH control"),

    content("Ba kh\u00e1i ni\u1ec7m c\u1ea7n ph\u00e2n bi\u1ec7t",
            ["Ovarian stimulation: d\u00f9ng thu\u1ed1c k\u00edch th\u00edch nang ph\u00e1t tri\u1ec3n (th\u01b0\u1eddng cho IUI).",
             "COH (Controlled Ovarian Hyperstimulation): d\u00f9ng thu\u1ed1c + KI\u1ec2M SO\u00c1T LH \u2192 tr\u00e1nh ho\u00e0ng th\u1ec3 s\u1edbm (th\u01b0\u1eddng cho IVF).",
             "Ovulation induction (trigger): k\u00edch th\u00edch nang v\u1ee1, gi\u1ea3i ph\u00f3ng no\u00e3n, gi\u00fap no\u00e3n MI \u2192 MII \u0111\u1ec3 th\u1ee5 tinh."]),

    mechanism("Gi\u1ea3 thuy\u1ebft hai hormon, hai t\u1ebf b\u00e0o",
              [("LH", "K\u00edch th\u00edch t\u1ebf b\u00e0o v\u1ecf \u2192 b\u00e0i ti\u1ebft androgen"),
               ("Androgen", "T\u00e1c \u0111\u1ed9ng v\u00e0o t\u1ebf b\u00e0o h\u1ea1t"),
               ("FSH", "Th\u01a1m h\u00f3a androgen \u2192 estrogen"),
               ("K\u1ebft qu\u1ea3", "N\u1ebfu thi\u1ebfu LH \u2192 gi\u1ea3m th\u01a1m h\u00f3a \u2192 gi\u1ea3m estrogen")]),

    defin("FSH threshold",
          "Gi\u00e1 tr\u1ecb n\u1ed3ng \u0111\u1ed9 FSH m\u00e0 tr\u00ean gi\u00e1 tr\u1ecb n\u00e0y nang no\u00e3n s\u1ebd ph\u00e1t tri\u1ec3n. M\u1ed6I NANG C\u00d3 M\u1ed8T NG\u01af\u1ee0NG KH\u00c1C NHAU."),

    defin("FSH window",
          "Kho\u1ea3ng th\u1eddi gian n\u1ed3ng \u0111\u1ed9 FSH n\u1eb1m tr\u00ean ng\u01b0\u1ee1ng. Ph\u1ea3i \u0111\u1ee7 l\u00e2u \u0111\u1ec3 nhi\u1ec1u nang c\u00f9ng ph\u00e1t tri\u1ec3n."),

    content("Ng\u01b0\u1ee1ng LH v\u00e0 c\u1eeda s\u1ed5 LH",
            ["Theo Howles: c\u00f3 m\u1ed9t \u2018c\u1eeda s\u1ed5\u2019 n\u1ed3ng \u0111\u1ed9 LH.",
             "LH n\u1eb1m trong c\u1eeda s\u1ed5 \u2192 nang ph\u00e1t tri\u1ec3n b\u00ecnh th\u01b0\u1eddng.",
             "LH v\u01b0\u1ee3t qu\u00e1 ng\u01b0\u1ee1ng \u2192 nang tho\u00e1i h\u00f3a ho\u1eb7c ho\u00e0ng th\u1ec3 h\u00f3a s\u1edbm.",
             "LH d\u01b0\u1edbi ng\u01b0\u1ee1ng \u2192 nang kh\u00f4ng ph\u00e1t tri\u1ec3n \u0111\u01b0\u1ee3c."]),

    content("C\u01a1 s\u1edf l\u00fd thuy\u1ebft c\u1ee7a ph\u00e1c \u0111\u1ed3 KTBT",
            ["N\u00e2ng FSH l\u00ean tr\u00ean ng\u01b0\u1ee1ng + k\u00e9o d\u00e0i FSH window \u2192 nhi\u1ec1u nang c\u00f9ng ph\u00e1t tri\u1ec3n.",
             "Tr\u00e1nh ho\u00e0ng th\u1ec3 h\u00f3a s\u1edbm \u2192 KI\u1ec2M SO\u00c1T \u0110\u1ec8NH LH.",
             "T\u0103ng FSH: d\u00f9ng FSH NGO\u1ea0I SINH; li\u1ec1u t\u00f9y b\u1ec7nh nh\u00e2n.",
             "Ki\u1ec3m so\u00e1t LH: GnRH agonist (ph\u00e1c \u0111\u1ed3 d\u00e0i), GnRH antagonist (ng\u00e0y 5-6), ho\u1eb7c progestin (PPOS)."]),

    content("C\u1eadp nh\u1eadt: Antagonist \u0111\u01b0\u1ee3c \u01b0u ti\u00ean h\u01a1n",
         ["Hi\u1ec7n nay ph\u00e1c \u0111\u1ed3 antagonist th\u01b0\u1eddng \u0111\u01b0\u1ee3c \u01b0u ti\u00ean \u1edf nhi\u1ec1u nh\u00f3m b\u1ec7nh nh\u00e2n.",
          "L\u00fd do: th\u1eddi gian NG\u1eaeN h\u01a1n, THU\u1eacN TI\u1ec6N h\u01a1n, cho ph\u00e9p GnRH agonist trigger khi nguy c\u01a1 OHSS cao.",
          "Ph\u00e1c \u0111\u1ed3 d\u00e0i v\u1eabn c\u00f3 vai tr\u00f2 ch\u1ecdn l\u1ecdc nh\u01b0ng KH\u00d4NG c\u00f2n l\u00e0 l\u1ef1a ch\u1ecdn M\u1eb6C \u0110\u1ecaNH cho m\u1ecdi b\u1ec7nh nh\u00e2n IVF."]),

    content("K\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng KH\u00d4NG l\u00e0m gi\u1ea3m d\u1ef1 tr\u1eef",
            ["KTBT ch\u1ec9 l\u00e0m TR\u00c1NH THO\u00c1I H\u00d3A c\u00e1c nang l\u1ebd ra s\u1ebd b\u1ecb tho\u00e1i h\u00f3a.",
             "KTBT KH\u00d4NG l\u00e0m gi\u1ea3m d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng.",
             "\u0110i\u1ec3m c\u1ea7n t\u01b0 v\u1ea5n cho b\u1ec7nh nh\u00e2n: KTBT huy \u0111\u1ed9ng nang c\u1ee7a chu k\u1ef3 \u0111\u00f3, kh\u00f4ng l\u1ea5y nang c\u1ee7a t\u01b0\u01a1ng lai."]),

    content("Follicular waves \u2014 nhi\u1ec1u \u0111\u1ee3t tuy\u1ec3n ch\u1ecdn",
            ["\u0110\u1ea7u chu k\u1ef3: 1 \u0111o\u00e0n h\u1ec7 nang \u0111\u01b0\u1ee3c tuy\u1ec3n ch\u1ecdn \u2192 1-2 nang v\u01b0\u1ee3t tr\u1ed9i (thuy\u1ebft tuy\u1ec3n ch\u1ecdn \u0111\u01a1n).",
             "Hi\u1ec7n \u0111\u00e3 c\u00f3 b\u1eb1ng ch\u1ee9ng: trong 1 chu k\u1ef3 c\u00f3 NHI\u1ec0U L\u00c0N S\u00d3NG tuy\u1ec3n ch\u1ecdn nang.",
             "\u0110a s\u1ed1 ph\u1ee5 n\u1eef c\u00f3 HAI \u0111\u1ee3t: \u0111\u1ee3t 1 \u0111\u1ea7u pha nang, \u0111\u1ee3t 2 \u0111\u1ea7u pha ho\u00e0ng th\u1ec3.",
             "\u0110\u00e2y l\u00e0 c\u01a1 s\u1edf cho: DuoStim (KTBT k\u00e9p) v\u00e0 Random start."]),

    content("DuoStim v\u00e0 Random start \u2014 ch\u1ec9 \u0111\u1ecbnh ch\u1ecdn l\u1ecdc",
            ["DuoStim: khuy\u1ebfn c\u00e1o cho gi\u1ea3m d\u1ef1 tr\u1eef bu\u1ed3ng tr\u1ee9ng n\u1eb7ng.",
             "Random start: \u00e1p d\u1ee5ng khi c\u1ea7n b\u1ea3o t\u1ed3n sinh s\u1ea3n (h\u00f3a ch\u1ea5t/tia x\u1ea1) \u2192 ch\u1ea1y \u0111ua th\u1eddi gian.",
             "HI\u1ec6N T\u1ea0I: d\u1eef li\u1ec7u v\u1ec1 DuoStim v\u00e0 random start CH\u1ec8 khuy\u1ebfn c\u00e1o cho c\u00e1c t\u00ecnh hu\u1ed1ng ch\u1ecdn l\u1ecdc.",
             "KH\u00d4NG ph\u1ea3i ph\u00e1c \u0111\u1ed3 routine cho m\u1ecdi b\u1ec7nh nh\u00e2n."]),

    # ═══ II.3. CÁC PHÁC ĐỒ KTBT ═══
    sec("II.3", "C\u00e1c ph\u00e1c \u0111\u1ed3 k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng",
        "Agonist (d\u00e0i / flare-up) \u2014 Antagonist \u2014 C\u00e1c ph\u00e1c \u0111\u1ed3 kh\u00e1c"),

    content("Hai lo\u1ea1i ph\u00e1c \u0111\u1ed3 ch\u00ednh",
            ["1) Ph\u00e1c \u0111\u1ed3 AGONIST: t\u1eebng ph\u1ed5 bi\u1ebfn, g\u1ed3m ph\u00e1c \u0111\u1ed3 ng\u1eafn (flare up) v\u00e0 ph\u00e1c \u0111\u1ed3 d\u00e0i (long protocol).",
             "Flare up: l\u1ee3i d\u1ee5ng t\u00e1c d\u1ee5ng flare up c\u1ee7a agonist \u2192 t\u0103ng FSH n\u1ed9i sinh + FSH ngo\u1ea1i sinh \u2192 KTBT.",
             "Long protocol: \u1ee9c ch\u1ebf tuy\u1ebfn y\u00ean b\u1eb1ng agonist t\u1eeb gi\u1eefa pha ho\u00e0ng th\u1ec3 \u2192 d\u00f9ng FSH ngo\u1ea1i sinh.",
             "2) Ph\u00e1c \u0111\u1ed3 ANTAGONIST: ki\u1ec3m so\u00e1t \u0111\u1ec9nh LH b\u1eb1ng antagonist, th\u00e2n thi\u1ec7n h\u01a1n, an to\u00e0n h\u01a1n \u2192 \u0111a ph\u1ea7n trung t\u00e2m d\u00f9ng."]),

    # --- 3.1 Long protocol ---
    sec("II.3.1", "Ph\u00e1c \u0111\u1ed3 d\u00e0i (long protocol)", ""),

    content("Long protocol \u2014 T\u1ed5ng quan",
            ["T\u1eebng \u0111\u01b0\u1ee3c s\u1eed d\u1ee5ng nhi\u1ec1u nh\u1ea5t, xem l\u00e0 ph\u00e1c \u0111\u1ed3 CHU\u1ea8N.",
             "\u01afu \u0111i\u1ec3m: nang \u0111\u1ed3ng \u0111\u1ec1u, ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n t\u1ed1t (tuy\u1ebfn y\u00ean b\u1ecb \u1ee9c ch\u1ebf ho\u00e0n to\u00e0n tr\u01b0\u1edbc KTBT).",
             "Nh\u01b0\u1ee3c \u0111i\u1ec3m: k\u00edch th\u00edch d\u00e0i ng\u00e0y, d\u00f9ng nhi\u1ec1u gonadotropin, nguy c\u01a1 OHSS CAO h\u01a1n."]),

    content("Long protocol \u2014 Hai pha",
            ["Pha 1 (\u1ee8C CH\u1ebe TUY\u1ebeN Y\u00caN): GnRH agonist t\u1eeb gi\u1eefa pha ho\u00e0ng th\u1ec3 \u2192 khi \u1ee9c ch\u1ebf ho\u00e0n to\u00e0n.",
             "Ti\u00eau ch\u00ed \u1ee9c ch\u1ebf: LH < 5 IU/L v\u00e0 E2 < 50 pg/mL.",
             "Th\u1eddi gian d\u00f9ng agonist: th\u01b0\u1eddng 12-14 ng\u00e0y.",
             "Pha 2 (KTBT): d\u00f9ng FSH ngo\u1ea1i sinh, ti\u1ebfp t\u1ee5c agonist li\u1ec1u gi\u1ea3m 1/2 so v\u1edbi ban \u0111\u1ea7u, \u0111\u1ebfn ng\u00e0y tr\u01b0\u1edfng th\u00e0nh no\u00e3n."]),

    twocol("Long protocol: \u01afu v\u00e0 Nh\u01b0\u1ee3c",
           "\u01afu \u0111i\u1ec3m", ["Nang \u0111\u1ed3ng \u0111\u1ec1u", "Ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n t\u1ed1t", "\u1ee8c ch\u1ebf LH m\u1ea1nh"],
           "Nh\u01b0\u1ee3c \u0111i\u1ec3m", ["Th\u1eddi gian d\u00e0i", "Nhi\u1ec1u FSH \u2192 t\u0103ng chi ph\u00ed", "OHSS cao h\u01a1n, nh\u1ea5t v\u1edbi PCOS", "HI\u1ec6N R\u1ea4T \u00cdT D\u00d9NG"]),

    # --- 3.2 Flare-up ---
    sec("II.3.2", "Ph\u00e1c \u0111\u1ed3 ng\u1eafn (flare up)", ""),

    content("Flare up protocol \u2014 C\u01a1 ch\u1ebf & gi\u1edbi h\u1ea1n",
            ["D\u1ef1a tr\u00ean t\u00e1c d\u1ee5ng FLARE UP c\u1ee7a agonist \u2192 t\u0103ng FSH n\u1ed9i sinh + FSH ngo\u1ea1i sinh \u2192 KTBT.",
             "NH\u01af\u1ee2C \u0111i\u1ec3m l\u1edbn: t\u0103ng FSH n\u1ed9i sinh \u0111i k\u00e8m T\u0102NG LH \u2192 KH\u00d4NG ki\u1ec3m so\u00e1t t\u1ed1t \u0111\u1ec9nh LH.",
             "H\u1ec7 qu\u1ea3: ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n KH\u00d4NG t\u1ed1t, nang ph\u00e1t tri\u1ec3n kh\u00f4ng \u0111\u1ed3ng \u0111\u1ec1u.",
             "Th\u01b0\u1eddng \u00e1p d\u1ee5ng cho b\u1ec7nh nh\u00e2n L\u1edaN TU\u1ed4I, GI\u1ea2M D\u1ef0 TR\u1eee.",
             "HI\u1ec6N NAY: g\u1ea7n nh\u01b0 r\u1ea5t \u00edt \u0111\u01b0\u1ee3c \u00e1p d\u1ee5ng."]),

    content("Flare up \u2014 C\u00e1ch th\u1ef1c hi\u1ec7n",
            ["B\u1eaft \u0111\u1ea7u GnRH agonist t\u1eeb ng\u00e0y th\u1ee9 2 c\u1ee7a chu k\u1ef3 kinh.",
             "D\u00f9ng \u0110\u1ed2NG TH\u1edcI v\u1edbi FSH.",
             "Theo d\u00f5i KTBT b\u1eb1ng si\u00eau \u00e2m nang no\u00e3n, ni\u00eam m\u1ea1c t\u1eed cung v\u00e0 \u0111\u1ecbnh l\u01b0\u1ee3ng hormon.",
             "Khi \u0111\u1ee7 ti\u00eau chu\u1ea9n \u2192 trigger b\u1eb1ng hCG."]),

    # --- 3.3 Antagonist ---
    sec("II.3.3", "Ph\u00e1c \u0111\u1ed3 \u0111\u1ed1i v\u1eadn (antagonist)", ""),

    content("Antagonist protocol \u2014 \u01afu \u0111i\u1ec3m n\u1ed5i b\u1eadt",
            ["\u00c1p d\u1ee5ng H\u1ea6U H\u1ebeT cho c\u00e1c b\u1ec7nh nh\u00e2n KTBT.",
             "L\u1ea5y B\u1ec6NH NH\u00c2N L\u00c0M TRUNG T\u00c2M.",
             "Th\u1eddi gian KTBT ng\u1eafn, \u1ee9c ch\u1ebf \u0111\u1ec9nh LH T\u1ed0T, ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n t\u01b0\u01a1ng t\u1ef1 ph\u00e1c \u0111\u1ed3 d\u00e0i.",
             "Th\u1eddi gian k\u00edch th\u00edch NG\u1eaeN h\u01a1n, \u00edt OHSS h\u01a1n.",
             "C\u00f3 th\u1ec3 tr\u01b0\u1edfng th\u00e0nh no\u00e3n b\u1eb1ng AGONIST khi nguy c\u01a1 OHSS."]),

    content("Antagonist \u2014 C\u00e1ch th\u1ef1c hi\u1ec7n",
            ["Gonadotropin (FSH) b\u1eaft \u0111\u1ea7u t\u1eeb ng\u00e0y th\u1ee9 2-3 c\u1ee7a chu k\u1ef3 kinh.",
             "Antagonist \u0111\u01b0\u1ee3c d\u00f9ng theo 2 c\u00e1ch:",
             "FIXED: antagonist c\u1ed1 \u0111\u1ecbnh v\u00e0o ng\u00e0y 5 ho\u1eb7c 6 KTBT.",
             "FLEXIBLE: antagonist khi nang l\u1edbn nh\u1ea5t \u0111\u1ea1t 14 mm, kh\u00f4ng mu\u1ed9n h\u01a1n ng\u00e0y 7 KTBT.",
             "Antagonist d\u00f9ng song song FSH \u0111\u1ebfn ng\u00e0y tr\u01b0\u1edfng th\u00e0nh no\u00e3n."]),

    twocol("Fixed vs Flexible Antagonist",
           "Fixed", ["B\u1eaft \u0111\u1ea7u ng\u00e0y 5-6 KTBT", "D\u1ec5 v\u1eadn h\u00e0nh, gi\u1ea3m nguy c\u01a1 qu\u00ean/mu\u1ed9n", "Thu\u1eadn ti\u1ec7n khi logistics \u0111\u00f4ng"],
           "Flexible", ["B\u1eaft khi nang l\u1edbn nh\u1ea5t \u2248 14 mm", "C\u00e1 th\u1ec3 h\u00f3a h\u01a1n", "Gi\u1ea3m s\u1ed1 ng\u00e0y d\u00f9ng antagonist", "Nh\u01b0ng C\u1ea6N SI\u00caU \u00c2M \u0111\u00fang th\u1eddi \u0111i\u1ec3m"]),

    content("C\u1eadp nh\u1eadt: Fixed vs Flexible",
         ["Fixed: gi\u1ea3m nguy c\u01a1 qu\u00ean/mu\u1ed9n antagonist, thu\u1eadn ti\u1ec7n v\u1eadn h\u00e0nh.",
          "Flexible: gi\u1ea3m s\u1ed1 ng\u00e0y d\u00f9ng antagonist nh\u01b0ng \u0111\u00f2i h\u1ecfi SI\u00caU \u00c2M \u0111\u00fang th\u1eddi \u0111i\u1ec3m.",
          "L\u1ef1a ch\u1ecdn d\u1ef1a tr\u00ean: nguy c\u01a1 LH surge, logistics trung t\u00e2m, kinh nghi\u1ec7m theo d\u00f5i."]),

    # --- 3.4 Các phác đồ khác ---
    sec("II.3.4", "C\u00e1c ph\u00e1c \u0111\u1ed3 kh\u00e1c", "Mild \u2014 DuoStim \u2014 PPOS"),

    content("Mild stimulation",
            ["\u0110\u1ecbnh ngh\u0129a: k\u1ebft h\u1ee3p thu\u1ed1c u\u1ed1ng (clomiphene citrate ho\u1eb7c aromatase inhibitor) + FSH li\u1ec1u th\u1ea5p.",
             "FSH th\u01b0\u1eddng kh\u00f4ng qu\u00e1 150 \u0111\u01a1n v\u1ecb.",
             "C\u00f3 th\u1ec3 ph\u00f9 h\u1ee3p \u1edf m\u1ed9t s\u1ed1 b\u1ec7nh nh\u00e2n GI\u1ea2M D\u1ef0 TR\u1eee.",
             "Nh\u01b0ng c\u1ea7n \u0111\u00e1nh gi\u00e1 theo m\u1ee5c ti\u00eau c\u00e1 th\u1ec3 h\u00f3a: chi ph\u00ed, s\u1ed1 no\u00e3n k\u1ef3 v\u1ecdng, \u0111\u1eb7c \u0111i\u1ec3m b\u1ec7nh nh\u00e2n."]),

    content("Duo stimulation \u2014 KTBT k\u00e9p",
            ["T\u00e1c gi\u1ea3 Kuang Yanping b\u00e1o c\u00e1o \u0111\u1ea7u ti\u00ean.",
             "Ch\u1ec9 \u0111\u1ecbnh: GI\u1ea2M D\u1ef0 TR\u1eee N\u1eb6NG.",
             "K\u1ebft qu\u1ea3: s\u1ed1 no\u00e3n thu trong pha ho\u00e0ng th\u1ec3 NHI\u1ec0U h\u01a1n pha nang no\u00e3n.",
             "Ch\u1ec9 \u0111\u1ecbnh ch\u1ee7 y\u1ebfu: gi\u1ea3m d\u1ef1 tr\u1eef + b\u1ea3o t\u1ed3n sinh s\u1ea3n tr\u01b0\u1edbc h\u00f3a/x\u1ea1 tr\u1ecb.",
             "M\u1ed9t s\u1ed1 nghi\u00ean c\u1ee9u: t\u1ef7 l\u1ec7 thu no\u00e3n v\u00e0 ph\u00f4i pha ho\u00e0ng th\u1ec3 > pha nang."]),

    content("PPOS \u2014 Progestin-Primed Ovarian Stimulation",
            ["Nguy\u00ean l\u00fd: progestin \u1ee9c ch\u1ebf \u0111\u1ec9nh LH t\u01b0\u01a1ng t\u1ef1 antagonist.",
             "Kh\u00e1c bi\u1ec7t: t\u00e1c d\u1ee5ng \u1ee9c ch\u1ebf KH\u00d4NG T\u1ee8C TH\u1edcI nh\u01b0 antagonist \u2192 c\u1ea7n d\u00f9ng S\u1edaM h\u01a1n.",
             "N\u1ebfu d\u00f9ng dydrogesterone: b\u1eaft \u0111\u1ea7u NGAY t\u1eeb khi KTBT, li\u1ec1u 30 mg/ng\u00e0y.",
             "B\u1eaft bu\u1ed9c: \u0110\u00d4NG PH\u00d4I TO\u00c0N B\u1ed8 (n\u1ed9i m\u1ea1c kh\u00f4ng \u0111\u1ed3ng b\u1ed9 v\u1edbi ph\u00f4i)."]),

    content("C\u1eadp nh\u1eadt: PPOS v\u00e0 freeze-all",
         ["PPOS l\u00e0 l\u1ef1a ch\u1ecdn h\u1eefu \u00edch khi d\u1ef1 ki\u1ebfn freeze-all.",
          "T\u00ecnh hu\u1ed1ng: b\u1ea3o t\u1ed3n sinh s\u1ea3n, nguy c\u01a1 OHSS, chi\u1ebfn l\u01b0\u1ee3c \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9.",
          "KH\u00d4NG ph\u00f9 h\u1ee3p n\u1ebfu m\u1ee5c ti\u00eau l\u00e0 chuy\u1ec3n ph\u00f4i T\u01af\u01a0I c\u00f9ng chu k\u1ef3."]),

    # ═══ II.4. THỜI ĐIỂM KTBT ═══
    sec("II.4", "Th\u1eddi \u0111i\u1ec3m k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng", ""),

    content("Th\u1eddi \u0111i\u1ec3m theo ph\u00e1c \u0111\u1ed3",
            ["Long protocol: b\u1eaft \u0111\u1ea7u agonist t\u1eeb GI\u1eee_A PHA HO\u00c0NG TH\u1ec2, th\u00f4ng th\u01b0\u1eddng ng\u00e0y 21 c\u1ee7a chu k\u1ef3, trong kho\u1ea3ng 2 tu\u1ea7n.",
             "Sau khi tuy\u1ebfn y\u00ean b\u1ecb \u1ee9c ch\u1ebf ho\u00e0n to\u00e0n \u2192 chuy\u1ec3n sang FSH.",
             "Flare up / Antagonist: b\u1eaft \u0111\u1ea7u \u0110\u1ea6U CHU K\u1ef2 KINH, th\u01b0\u1eddng t\u1eeb ng\u00e0y 2 \u0111\u1ebfn ng\u00e0y 4.",
             "C\u01a1 s\u1edf: nang th\u1ee9 c\u1ea5p \u0111\u01b0\u1ee3c tuy\u1ec3n m\u1ed9 v\u00e0o \u0111\u1ea7u chu k\u1ef3, ph\u00e1t tri\u1ec3n d\u01b0\u1edbi t\u00e1c d\u1ee5ng c\u1ee7a FSH."]),

    content("Random start \u2014 C\u01a1 s\u1edf v\u00e0 ch\u1ec9 \u0111\u1ecbnh",
            ["Xu\u1ea5t ph\u00e1t t\u1eeb nghi\u00ean c\u1ee9u b\u1ea3o t\u1ed3n sinh s\u1ea3n cho b\u1ec7nh nh\u00e2n \u00e1c t\u00ednh.",
             "\u1ede m\u1ed7i ph\u1ee5 n\u1eef c\u00f3 th\u1ec3 c\u00f3 NHI\u1ec0U \u0111\u1ee3t s\u00f3ng chi\u00eau m\u1ed9 nang (th\u01b0\u1eddng 2, c\u00e1 bi\u1ec7t 3).",
             "\u2192 C\u00f3 th\u1ec3 KTBT v\u00e0o B\u1ea4T K\u1ef2 th\u1eddi \u0111i\u1ec3m n\u00e0o n\u1ebfu d\u1ef1 \u0111\u1ecbnh \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9."]),

    content("Nghi\u00ean c\u1ee9u v\u1ec1 th\u1eddi \u0111i\u1ec3m KTBT",
            ["Liu v\u00e0 cs: b\u1ec7nh nh\u00e2n l\u1edbn tu\u1ed5i/gi\u1ea3m d\u1ef1 tr\u1eef \u2192 s\u1ed1 no\u00e3n PHA HO\u00c0NG TH\u1ec2 > PHA NANG.",
             "Baris Ata ph\u00e2n t\u00edch: KTBT pha nang / pha ho\u00e0ng th\u1ec3 / k\u00e9p \u1edf nh\u00f3m b\u1ea3o t\u1ed3n, gi\u1ea3m d\u1ef1 tr\u1eef, v\u00f4 sinh.",
             "K\u1ebft qu\u1ea3: s\u1ed1 no\u00e3n, s\u1ed1 ph\u00f4i, t\u1ef7 l\u1ec7 c\u00f3 thai T\u01af\u01a0NG \u0110\u01af\u01a0NG khi KTBT b\u1ea5t k\u1ef3 th\u1eddi \u0111i\u1ec3m n\u00e0o.",
             "Pha ho\u00e0ng th\u1ec3: k\u1ebft qu\u1ea3 c\u00f3 ph\u1ea7n NH\u1ec8NH h\u01a1n nh\u01b0ng l\u01b0\u1ee3ng FSH ngo\u1ea1i sinh NHI\u1ec0U h\u01a1n."]),

    content("C\u1eadp nh\u1eadt: Random start & DuoStim",
         ["Random start v\u00e0 DuoStim l\u00e0 chi\u1ebfn l\u01b0\u1ee3c CH\u1eccN L\u1eccC.",
          "Random start ph\u00f9 h\u1ee3p nh\u1ea5t khi c\u1ea7n r\u00fat ng\u1eafn th\u1eddi gian tr\u01b0\u1edbc \u0111i\u1ec1u tr\u1ecb gonadotoxic.",
          "DuoStim: c\u00e2n nh\u1eafc \u1edf b\u1ec7nh nh\u00e2n ti\u00ean l\u01b0\u1ee3ng k\u00e9m/gi\u1ea3m d\u1ef1 tr\u1eef c\u1ea7n gom no\u00e3n nhanh.",
          "KH\u00d4NG ph\u1ea3i ph\u00e1c \u0111\u1ed3 ROUTINE cho m\u1ecdi b\u1ec7nh nh\u00e2n."]),

    # ═══ II.5. LIỀU FSH & THEO DÕI ═══
    sec("II.5", "Li\u1ec1u FSH kh\u1edfi \u0111\u1ea7u & theo d\u00f5i",
        "\u0110\u00e1nh gi\u00e1 tr\u01b0\u1edbc KTBT \u2014 Theo d\u00f5i \u0111\u00e1p \u1ee9ng"),

    content("Li\u1ec1u FSH kh\u1edfi \u0111\u1ea7u \u2014 C\u00e1c y\u1ebfu t\u1ed1",
            ["D\u1ef1a v\u00e0o: c\u00e2n n\u1eb7ng, AMH, AFC, FSH \u0111\u1ea7u chu k\u1ef3 v\u00e0 TI\u1ec0N S\u1eec \u0111\u00e1p \u1ee9ng (n\u1ebfu c\u00f3).",
             "La Marca: \u0111\u1ec1 xu\u1ea5t c\u00e1ch x\u00e1c \u0111\u1ecbnh li\u1ec1u kh\u1edfi \u0111\u1ea7u theo c\u00e1c ch\u1ec9 s\u1ed1 d\u1ef1 tr\u1eef.",
             "C\u0169ng c\u00f3 th\u1ec3 d\u1ef1a v\u00e0o AMH v\u00e0 c\u00e2n n\u1eb7ng \u0111\u1ec3 \u0111\u1ecbnh li\u1ec1u (v\u00ed d\u1ee5: follitropin delta)."]),

    content("Li\u1ec1u FSH t\u1ed1i \u0111a",
            ["C\u00e1c t\u00e1c gi\u1ea3 TH\u1ed0NG NH\u1ea4T: li\u1ec1u FSH t\u1ed1i \u0111a KH\u00d4NG QU\u00c1 300 \u0111\u01a1n v\u1ecb/ng\u00e0y.",
             "\u0110\u00e2y l\u00e0 li\u1ec1u \u0111\u1ee7 \u0111\u1ec3 KTBT.",
             "\u0110\u00e3 \u0111\u01b0\u1ee3c ESHRE KHUY\u1ebeN C\u00c1O."]),

    content("\u0110\u00e1p \u1ee9ng k\u00e9m \u2014 T\u0103ng li\u1ec1u c\u00f3 hi\u1ec7u qu\u1ea3 kh\u00f4ng?",
            ["\u0110\u1ed1i v\u1edbi b\u1ec7nh nh\u00e2n \u0111\u00e3 d\u00f9ng li\u1ec1u cao nh\u01b0ng kh\u00f4ng \u0111\u00e1p \u1ee9ng:",
             "Theo Khalaf Y v\u00e0 cs: VI\u1ec6C T\u0102NG LI\u1ec0U KH\u00d4NG C\u1ea2I THI\u1ec6N \u0111\u01b0\u1ee3c k\u1ebft qu\u1ea3.",
             "\u2192 T\u0103ng li\u1ec1u v\u00f4 h\u1ea1n \u1edf poor responder l\u00e0 KH\u00d4NG C\u00d3 C\u01a0 S\u1ede."]),

    content("C\u1eadp nh\u1eadt: C\u00e1 th\u1ec3 h\u00f3a li\u1ec1u (ESHRE)",
         ["ESHRE khuy\u1ebfn c\u00e1o c\u00e1 th\u1ec3 h\u00f3a li\u1ec1u gonadotropin theo \u0111\u00e1p \u1ee9ng d\u1ef1 ki\u1ebfn.",
          "Poor responder: t\u0103ng li\u1ec1u r\u1ea5t cao th\u01b0\u1eddng KH\u00d4NG \u0111\u1ea3m b\u1ea3o t\u0103ng no\u00e3n t\u01b0\u01a1ng x\u1ee9ng.",
          "High responder: GI\u1ea2M li\u1ec1u + antagonist + agonist trigger + freeze-all \u2192 gi\u1ea3m OHSS.",
          "PMID: 32395637"]),

    # --- 5.1 Đánh giá trước KTBT ---
    sec("II.5.1", "\u0110\u00e1nh gi\u00e1 tr\u01b0\u1edbc k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng", ""),

    checklist("Si\u00eau \u00e2m tr\u01b0\u1edbc KTBT \u2014 Checklist",
              ["\u0110\u1ebfm s\u1ed1 nang th\u1ee9 c\u1ea5p (AFC)",
               "C\u00f3 nang t\u1ed3n d\u01b0 hay kh\u00f4ng?",
               "C\u00f3 b\u1ea5t th\u01b0\u1eddng bu\u1ed3ng tr\u1ee9ng? (nang l\u1ea1c n\u1ed9i m\u1ea1c t\u1eed cung...)",
               "C\u00f3 b\u1ea5t th\u01b0\u1eddng t\u1eed cung?",
               "\u0110\u00e1nh gi\u00e1 \u0111\u01b0\u1eddng ti\u1ebfp c\u1eadn bu\u1ed3ng tr\u1ee9ng cho ch\u1ecdc h\u00fat"]),

    content("Nang l\u1ea1c n\u1ed9i m\u1ea1c t\u1eed cung",
            ["C\u00f3 th\u1ec3 m\u1ed9t ho\u1eb7c nhi\u1ec1u nang, k\u00edch th\u01b0\u1edbc kh\u00e1c nhau.",
             "Ranh gi\u1edbi r\u00f5, \u00e2m vang kh\u00f4ng \u0111\u1ec1u.",
             "N\u1ebfu kh\u00f4ng \u1ea3nh h\u01b0\u1edfng \u0111\u1ebfn ch\u1ecdc h\u00fat no\u00e3n \u2192 KH\u00d4NG nh\u1ea5t thi\u1ebft ch\u1ecdc h\u00fat tr\u01b0\u1edbc KTBT.",
             "N\u1ebfu nang to, t\u1ed3n t\u1ea1i nhi\u1ec1u chu k\u1ef3 \u2192 C\u00c2N NH\u1eaeC ch\u1ecdc h\u00fat tr\u01b0\u1edbc KTBT."]),

    content("Nang t\u1ed3n d\u01b0 bu\u1ed3ng tr\u1ee9ng",
            ["L\u00e0 c\u00e1c nang c\u00f3 k\u00edch th\u01b0\u1edbc to nh\u1ecf kh\u00e1c nhau.",
             "N\u1ebfu c\u00f3 nang k\u00edch th\u01b0\u1edbc tr\u00ean 18 mm \u2192 c\u1ea7n ch\u1ecdc h\u00fat nang HO\u1eb6C ch\u1edd sang chu k\u1ef3 ti\u1ebfp theo.",
             "Trong th\u1eddi gian ch\u1edd: c\u00f3 th\u1ec3 kh\u00f4ng d\u00f9ng thu\u1ed1c ho\u1eb7c d\u00f9ng vi\u00ean tr\u00e1nh thai k\u1ebft h\u1ee3p."]),

    content("\u0110\u00e1nh gi\u00e1 t\u1eed cung tr\u01b0\u1edbc KTBT",
            ["C\u1ea7n lo\u1ea1i tr\u1eeb c\u00e1c b\u1ea5t th\u01b0\u1eddng c\u00f3 th\u1ec3 \u1ea3nh h\u01b0\u1edfng k\u1ebft qu\u1ea3 c\u00f3 thai.",
             "T\u1eed cung ng\u1ea3 sau + kh\u00f4ng di \u0111\u1ed9ng khi \u1ea5n \u0111\u1ea7u d\u00f2 \u2192 th\u01b0\u1eddng do D\u00cdNH (L\u1ea1c n\u1ed9i m\u1ea1c t\u1eed cung).",
             "Ti\u00ean l\u01b0\u1ee3ng KH\u00d4NG T\u1ed0T trong qu\u00e1 tr\u00ecnh KTBT.",
             "C\u1ea7n ph\u00e1t hi\u1ec7n: u x\u01a1 c\u01a1, polyp, v\u00e1ch ng\u0103n \u2192 c\u00f3 th\u1ec3 c\u1ea7n tr\u00ec ho\u00e3n chuy\u1ec3n ph\u00f4i."]),

    # --- 5.2 Theo dõi trong quá trình KTBT ---
    sec("II.5.2", "Theo d\u00f5i trong qu\u00e1 tr\u00ecnh k\u00edch th\u00edch", ""),

    content("4 m\u1ee5c \u0111\u00edch c\u1ee7a theo d\u00f5i",
            ["1) \u0110\u00e1nh gi\u00e1 hi\u1ec7u qu\u1ea3 \u1ee9c ch\u1ebf tuy\u1ebfn y\u00ean (down-regulation) trong ph\u00e1c \u0111\u1ed3 d\u00e0i.",
             "2) Theo d\u00f5i \u0111\u00e1p \u1ee9ng bu\u1ed3ng tr\u1ee9ng \u0111\u1ec3 THAY \u0110\u1ed4I LI\u1ec0U n\u1ebfu c\u1ea7n.",
             "3) X\u00e1c \u0111\u1ecbnh th\u1eddi \u0111i\u1ec3m d\u00f9ng ANTAGONIST trong ph\u00e1c \u0111\u1ed3 \u0111\u1ed1i v\u1eadn linh ho\u1ea1t.",
             "4) X\u00e1c \u0111\u1ecbnh th\u1eddi \u0111i\u1ec3m TRIGGER v\u00e0 ph\u00e1t hi\u1ec7n s\u1edbm OHSS."]),

    content("C\u1eadp nh\u1eadt: Checklist theo d\u00f5i si\u00eau \u00e2m",
         ["M\u1ed7i l\u1ea7n si\u00eau \u00e2m n\u00ean ghi:",
          "S\u1ed1 nang theo NH\u00d3M K\u00cdCH TH\u01af\u1edaC.",
          "Nang l\u1edbn nh\u1ea5t HAI B\u00caN.",
          "\u0110\u1ed9 d\u00e0y / h\u00ecnh th\u00e1i N\u1ed8I M\u1ea0C.",
          "Kh\u1ea3 n\u0103ng TI\u1ebeP C\u1eacN bu\u1ed3ng tr\u1ee9ng khi ch\u1ecdc h\u00fat.",
          "D\u1ea5u nguy c\u01a1 OHSS.",
          "K\u1ebf ho\u1ea1ch: fresh transfer hay freeze-all.",
          "N\u1ed9i ti\u1ebft (E2/LH/P4): KH\u00d4NG nh\u1ea5t thi\u1ebft m\u1ecdi l\u1ea7n, nh\u01b0ng h\u1eefu \u00edch khi nghi OHSS / \u0111\u00e1p \u1ee9ng b\u1ea5t th\u01b0\u1eddng / LH surge / P4 t\u0103ng s\u1edbm."]),

    # --- 5.3 Theo dõi sự đáp ứng ---
    sec("II.5.3", "Theo d\u00f5i s\u1ef1 \u0111\u00e1p \u1ee9ng", ""),

    content("Si\u00eau \u00e2m theo t\u1eebng ph\u00e1c \u0111\u1ed3",
            ["Long protocol: sau GnRH agonist 10-12 ng\u00e0y, ki\u1ec3m tra \u1ee9c ch\u1ebf ho\u00e0n to\u00e0n.",
             "Ti\u00eau ch\u00ed \u1ee9c ch\u1ebf: LH < 5 IU/L, E2 < 50 pg/mL, si\u00eau \u00e2m KH\u00d4NG c\u00f3 nang t\u1ed3n d\u01b0.",
             "Sau \u0111\u00f3 b\u1eaft \u0111\u1ea7u FSH ngo\u1ea1i sinh + duy tr\u00ec agonist li\u1ec1u gi\u1ea3m 1/2.",
             "Antagonist / flare up: b\u1eaft \u0111\u1ea7u FSH t\u1eeb ng\u00e0y 2-3 khi si\u00eau \u00e2m kh\u00f4ng c\u00f3 nang t\u1ed3n d\u01b0 v\u00e0 b\u1ea5t th\u01b0\u1eddng."]),

    content("L\u1ecbch si\u00eau \u00e2m trong theo d\u00f5i",
            ["Si\u00eau \u00e2m ti\u1ebfp theo: ng\u00e0y 6 ho\u1eb7c 7 d\u00f9ng FSH.",
             "\u0110\u1ebfm v\u00e0 \u0111o k\u00edch th\u01b0\u1edbc T\u1ea4T C\u1ea2 nang hai b\u00ean + \u0111\u1ed9 d\u00e0y ni\u00eam m\u1ea1c.",
             "Sau \u0111\u00f3: si\u00eau \u00e2m c\u00e1ch 2 ho\u1eb7c 1 ng\u00e0y t\u00f9y k\u00edch th\u01b0\u1edbc nang.",
             "T\u1ed1c \u0111\u1ed9 ph\u00e1t tri\u1ec3n nang \u01b0\u1edbc \u0111o\u00e1n: 1-2 mm/ng\u00e0y.",
             "Fixed antagonist: KH\u00d4NG c\u1ea7n si\u00eau \u00e2m s\u1edbm (antagonist ng\u00e0y c\u1ed1 \u0111\u1ecbnh).",
             "Flexible antagonist: B\u1eaeT BU\u1ed8C si\u00eau \u00e2m ng\u00e0y 6 \u0111\u1ec3 quy\u1ebft \u0111\u1ecbnh antagonist."]),

    content("C\u00e1ch \u0111o k\u00edch th\u01b0\u1edbc nang",
            ["\u0110o t\u1eeb B\u1edc TRONG b\u00ean n\u00e0y \u0111\u1ebfn B\u1edc TRONG b\u00ean \u0111\u1ed1i di\u1ec7n.",
             "Nang tr\u00f2n \u0111\u1ec1u: ch\u1ec9 c\u1ea7n \u0111o M\u1ed8T chi\u1ec1u.",
             "Nang kh\u00f4ng tr\u00f2n: \u0111o HAI chi\u1ec1u (l\u1edbn nh\u1ea5t v\u00e0 b\u00e9 nh\u1ea5t) \u2192 l\u1ea5y GI\u00c1 TR\u1eca TRUNG B\u00ccNH."]),

    content("Di\u1ec5n bi\u1ebfn k\u00edch th\u01b0\u1edbc nang theo th\u1eddi gian",
            ["\u0110\u1ea7u chu k\u1ef3: nang th\u1ee9 c\u1ea5p 2-9 mm.",
             "Ng\u00e0y 6-7: nang v\u01b0\u1ee3t tr\u1ed9i \u2265 12 mm, t\u1ed1c \u0111\u1ed9 trung b\u00ecnh 2 mm/ng\u00e0y.",
             "Nang 14-24 mm: t\u1ef7 l\u1ec7 thu no\u00e3n v\u00e0 th\u1ee5 tinh T\u1ed0I \u01afU.",
             "Nang > 24 mm: s\u1ed1 no\u00e3n thu \u0111\u01b0\u1ee3c GI\u1ea2M.",
             "C\u00f3 th\u1ec3 quan s\u00e1t G\u00d2 NO\u00c3N b\u00ean trong nang tr\u01b0\u1edbc ph\u00f3ng no\u00e3n."]),

    content("Bu\u1ed3ng tr\u1ee9ng nhi\u1ec1u nang / PCOS",
            ["Bu\u1ed3ng tr\u1ee9ng \u00edt nang: \u0111o v\u00e0 \u0111\u1ebfm kh\u00f4ng qu\u00e1 kh\u00f3.",
             "Bu\u1ed3ng tr\u1ee9ng NHI\u1ec0U NANG (PCOS): c\u00e1c nang ph\u00e1t tri\u1ec3n kh\u00f4ng \u0111\u1ec1u \u2192 d\u1ec5 B\u1ece S\u00d3T ho\u1eb7c \u0110\u1ebeM L\u1eb6P.",
             "C\u1ea7n ng\u01b0\u1eddi c\u00f3 KINH NGHI\u1ec6M \u0111\u1ec3 si\u00eau \u00e2m.",
             "M\u00e1y si\u00eau \u00e2m 3D v\u1edbi \u0111\u1ea7u d\u00f2 \u00e2m \u0111\u1ea1o: l\u1eadp \u1ea3nh 3D, m\u1ed7i nang hi\u1ec3n th\u1ecb m\u00e0u kh\u00e1c nhau \u2192 h\u1ea1n ch\u1ebf sai s\u1ed1.",
             "Nh\u01b0ng gi\u00e1 th\u00e0nh CAO \u2192 kh\u00f4ng ph\u1ea3i c\u01a1 s\u1edf n\u00e0o c\u0169ng c\u00f3."]),

    content("\u0110\u00e1nh gi\u00e1 ni\u00eam m\u1ea1c t\u1eed cung",
            ["\u0110o \u1edf v\u1ecb tr\u00ed D\u00c0Y NH\u1ea4T tr\u00ean \u0111\u01b0\u1eddng c\u1eaft d\u1ecdc.",
             "\u0110\u1eb7t con tr\u1ecf \u1edf v\u1ecb tr\u00ed TI\u1ebeP GI\u00c1P ni\u00eam m\u1ea1c \u2013 c\u01a1 t\u1eed cung, \u0111o VU\u00d4NG G\u00d3C v\u1edbi \u0111\u01b0\u1eddng ni\u00eam m\u1ea1c.",
             "C\u00f3 3 lo\u1ea1i h\u00ecnh th\u00e1i:",
             "D\u1ea1ng 1 (BA L\u00c1, h\u00ecnh h\u1ea1t c\u00e0 ph\u00ea): 3 \u0111\u01b0\u1eddng t\u0103ng \u00e2m + 2 \u0111\u01b0\u1eddng gi\u1ea3m \u00e2m \u2192 THU\u1eacN L\u1ee2I nh\u1ea5t cho l\u00e0m t\u1ed5.",
             "D\u1ea1ng 2: T\u0102NG \u00c2M TO\u00c0N B\u1ed8, kh\u00f4ng c\u00f3 v\u00f9ng gi\u1ea3m \u00e2m \u2192 KH\u00d4NG thu\u1eadn l\u1ee3i.",
             "D\u1ea1ng 3: TRUNG GIAN gi\u1eefa d\u1ea1ng 1 v\u00e0 2."]),

    content("Ni\u00eam m\u1ea1c t\u1eed cung \u2014 Khi n\u00e0o \u0111o c\u00f3 \u00fd ngh\u0129a?",
            ["Theo d\u00f5i ni\u00eam m\u1ea1c M\u1ed6I L\u1ea6N si\u00eau \u00e2m l\u00e0 KH\u00d4NG th\u1ef1c s\u1ef1 c\u1ea7n thi\u1ebft.",
             "CH\u1ec8 C\u1ea6N \u0111o v\u00e0o NG\u00c0Y TR\u01af\u1edeNG TH\u00c0NH NO\u00c3N.",
             "M\u1ee5c \u0111\u00edch: t\u01b0 v\u1ea5n c\u01a1 h\u1ed9i c\u00f3 thai + quy\u1ebft \u0111\u1ecbnh chuy\u1ec3n ph\u00f4i T\u01af\u01a0I hay \u0110\u00d4NG PH\u00d4I."]),

    content("Vai tr\u00f2 c\u1ee7a x\u00e9t nghi\u1ec7m n\u1ed9i ti\u1ebft",
            ["Si\u00eau \u00e2m + x\u00e9t nghi\u1ec7m E2, LH, P4: \u0111\u00e1nh gi\u00e1 ch\u1ea5t l\u01b0\u1ee3ng nang no\u00e3n.",
             "LH t\u0103ng ho\u1eb7c P4 t\u0103ng s\u1edbm \u2192 \u1ea3nh h\u01b0\u1edfng ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n.",
             "Tuy nhi\u00ean: \u0111\u1ecbnh l\u01b0\u1ee3ng hormon KH\u00d4NG c\u1ea3i thi\u1ec7n t\u1ef7 l\u1ec7 c\u00f3 thai so v\u1edbi KH\u00d4NG \u0111\u1ecbnh l\u01b0\u1ee3ng.",
             "KHUY\u1ebeN C\u00c1O: KH\u00d4NG c\u1ea7n \u0111\u1ecbnh l\u01b0\u1ee3ng hormon cho T\u1ea4T C\u1ea2 c\u00e1c b\u1ec7nh nh\u00e2n.",
             "E2 c\u00f3 gi\u00e1 tr\u1ecb trong tr\u01b0\u1eddng h\u1ee3p QU\u00c1 K\u00cdCH BU\u1ed2NG TR\u1ee8NG.",
             "LH: t\u00f9y thu\u1ed9c v\u00e0o t\u1eebng b\u1ec7nh nh\u00e2n c\u1ee5 th\u1ec3, KH\u00d4NG c\u1ea7n theo d\u00f5i h\u1ec7 th\u1ed1ng.",
             "Ng\u01b0\u1eddi c\u00f3 kinh nghi\u1ec7m: c\u00f3 th\u1ec3 GI\u1ea2M s\u1ed1 l\u1ea7n si\u00eau \u00e2m + kh\u00f4ng \u0111\u1ecbnh l\u01b0\u1ee3ng hormon \u2192 gi\u1ea3m chi ph\u00ed."]),

    content("Si\u00eau \u00e2m 3D v\u00e0 Doppler",
            ["Si\u00eau \u00e2m 3D v\u00e0 Doppler: KH\u00d4NG th\u1ef1c s\u1ef1 c\u1ea7n thi\u1ebft cho T\u1ea4T C\u1ea2 b\u1ec7nh nh\u00e2n.",
             "Ch\u1ec9 n\u00ean \u00e1p d\u1ee5ng cho m\u1ed9t s\u1ed1 b\u1ec7nh nh\u00e2n nh\u1ea5t \u0111\u1ecbnh.",
             "\u0110\u1eb7c bi\u1ec7t: b\u1ec7nh nh\u00e2n GI\u1ea2M D\u1ef0 TR\u1eee ho\u1eb7c \u0110\u00c1P \u1ee8NG K\u00c9M."]),

    content("Guideline ESHRE \u2014 C\u00e1 th\u1ec3 h\u00f3a",
            ["ESHRE 2020: guideline n\u1ec1n v\u1ec1 ch\u1ecdn ph\u00e1c \u0111\u1ed3, li\u1ec1u FSH, trigger cho IVF/ICSI.",
             "ESHRE 2025/2026: b\u1ea3n c\u1eadp nh\u1eadt m\u1edf r\u1ed9ng.",
             "C\u00e1c khuy\u1ebfn c\u00e1o c\u1ea7n hi\u1ec3u theo h\u01b0\u1edbng: C\u00c1 TH\u1ec2 H\u00d3A v\u00e0 C\u1eacP NH\u1eacT THEO GUIDELINE M\u1edaI NH\u1ea4T."]),

    # ═══ II.6. TRƯỞNG THÀNH NOÃN ═══
    sec("II.6", "Ti\u00eau chu\u1ea9n v\u00e0 ph\u00e1c \u0111\u1ed3 tr\u01b0\u1edfng th\u00e0nh no\u00e3n",
        "Trigger \u2014 hCG \u2014 GnRH agonist \u2014 Dual/Double"),

    # --- 6.1 Tiêu chuẩn ---
    sec("II.6.1", "Ti\u00eau chu\u1ea9n tr\u01b0\u1edfng th\u00e0nh no\u00e3n", ""),

    content("Ti\u00eau chu\u1ea9n trigger",
            ["\u00cdt nh\u1ea5t 3 nang tr\u00ean 17 mm HO\u1eb6C 2 nang tr\u00ean 18 mm.",
             "T\u1ed1i thi\u1ec3u 1/2 t\u1ed5ng s\u1ed1 nang c\u00f3 k\u00edch th\u01b0\u1edbc tr\u00ean 14 mm.",
             "Th\u1eddi gian KTBT trung b\u00ecnh: 8-12 ng\u00e0y.",
             "E2 trung b\u00ecnh cho m\u1ed7i nang: kho\u1ea3ng 150-200 pg/mL (m\u1ed9t s\u1ed1 th\u1ef1c h\u00e0nh).",
             "hCG trigger: li\u1ec1u 5.000-10.000 \u0111\u01a1n v\u1ecb ho\u1eb7c hCG t\u00e1i t\u1ed5 h\u1ee3p 250 mcg (\u2248 6.500 \u0111\u01a1n v\u1ecb).",
             "Ch\u1ecdc h\u00fat no\u00e3n: 34-36 GI\u1edc sau trigger, qua \u0111\u01b0\u1eddng \u00e2m \u0111\u1ea1o."]),

    content("C\u1eadp nh\u1eadt: Ti\u00eau chu\u1ea9n trigger linh ho\u1ea1t",
         ["Ti\u00eau chu\u1ea9n trigger THAY \u0110\u1ed4I theo ph\u00e1c \u0111\u1ed3 v\u00e0 m\u1ee5c ti\u00eau trung t\u00e2m.",
          "N\u00ean xem s\u1ed1 nang theo NHI\u1ec0U NH\u00d3M k\u00edch th\u01b0\u1edbc thay v\u00ec ch\u1ec9 nh\u00ecn 1 nang l\u1edbn nh\u1ea5t.",
          "Tr\u01b0\u1edbc trigger c\u1ea7n ki\u1ec3m tra: nguy c\u01a1 OHSS, k\u1ebf ho\u1ea1ch fresh/freeze-all, lo\u1ea1i trigger, th\u1eddi \u0111i\u1ec3m ch\u1ecdc h\u00fat, h\u1ed7 tr\u1ee3 ho\u00e0ng th\u1ec3."]),

    checklist("Trigger checklist",
              ["S\u1ed1 nang theo nh\u00f3m k\u00edch th\u01b0\u1edbc \u0111\u00e3 \u0111\u1ee7 ch\u01b0a?",
               "C\u00f3 bao nhi\u00eau nang nguy c\u01a1 \u0111\u00f3ng g\u00f3p OHSS?",
               "N\u1ed9i m\u1ea1c v\u00e0 P4 c\u00f2n ph\u00f9 h\u1ee3p fresh transfer?",
               "Chu k\u1ef3 antagonist c\u00f3 th\u1ec3 d\u00f9ng agonist trigger?",
               "Gi\u1edd ch\u1ecdc h\u00fat 34-36h sau trigger \u0111\u00e3 l\u00ean l\u1ecbch?",
               "K\u1ebf ho\u1ea1ch h\u1ed7 tr\u1ee3 ho\u00e0ng th\u1ec3 \u0111\u00e3 r\u00f5?"]),

    # --- 6.2 hCG trigger ---
    sec("II.6.2", "Tr\u01b0\u1edfng th\u00e0nh no\u00e3n b\u1eb1ng hCG", ""),

    content("hCG trigger \u2014 C\u01a1 ch\u1ebf v\u00e0 \u01b0u \u0111i\u1ec3m",
            ["hCG c\u00f3 c\u1ea5u tr\u00fac T\u01af\u01a0NG T\u1ef0 LH \u2192 thay th\u1ebf LH trong tr\u01b0\u1edfng th\u00e0nh no\u00e3n.",
             "hCG g\u1eafn c\u00f9ng th\u1ee5 th\u1ec3 LH/hCG.",
             "Th\u1eddi gian B\u00c1N H\u1ee6Y K\u00c9O D\u00c0I h\u01a1n LH \u2192 t\u00e1c d\u1ee5ng ho\u00e0ng th\u1ec3 h\u00f3a v\u00e0 nguy c\u01a1 OHSS K\u00c9O D\u00c0I h\u01a1n.",
             "Li\u1ec1u: 5.000-10.000 \u0111\u01a1n v\u1ecb.",
             "Urinary hCG ho\u1eb7c recombinant hCG: k\u1ebft qu\u1ea3 T\u01af\u01a0NG \u0110\u01af\u01a0NG.",
             "Nguy c\u01a1 OHSS: c\u00f3 th\u1ec3 GI\u1ea2M LI\u1ec0U xu\u1ed1ng 5.000 \u0111\u01a1n v\u1ecb v\u00e0 d\u00f9ng hCG t\u00e1i t\u1ed5 h\u1ee3p (b\u00e1n h\u1ee7y ng\u1eafn h\u01a1n)."]),

    # --- 6.3 GnRH agonist trigger ---
    sec("II.6.3", "Tr\u01b0\u1edfng th\u00e0nh no\u00e3n b\u1eb1ng GnRH agonist", ""),

    content("GnRH agonist trigger \u2014 C\u01a1 ch\u1ebf",
            ["D\u1ef1a tr\u00ean t\u00e1c d\u1ee5ng FLARE UP c\u1ee7a GnRH agonist \u2192 t\u1ea1o \u0111\u1ec9nh LH N\u1ed8I SINH.",
             "\u0110\u1ec9nh LH n\u1ed9i sinh c\u00f3 t\u00e1c d\u1ee5ng tr\u01b0\u1edfng th\u00e0nh no\u00e3n T\u01af\u01a0NG T\u1ef0 hCG.",
             "\u01afu \u0111i\u1ec3m c\u1ee7a \u0111\u1ec9nh LH n\u1ed9i sinh:",
             "- Gi\u1ed1ng chu k\u1ef3 t\u1ef1 nhi\u00ean h\u01a1n.",
             "- Xu\u1ea5t hi\u1ec7n s\u1edbm, bi\u00ean \u0111\u1ed9 TH\u1ea4P, gi\u1ea3m NHANH h\u01a1n.",
             "- \u2192 GI\u1ea2M nguy c\u01a1 OHSS s\u1edbm."]),

    content("GnRH agonist trigger \u2014 Nh\u01b0\u1ee3c \u0111i\u1ec3m",
            ["L\u00e0m SUY HO\u00c0NG TH\u1ec2.",
             "Gi\u1ea3m kh\u1ea3 n\u0103ng TI\u1ebeP NH\u1eacN NI\u00caM M\u1ea0C t\u1eed cung.",
             "\u2192 GI\u1ea2M t\u1ef7 l\u1ec7 c\u00f3 thai n\u1ebfu CHUY\u1ec2N PH\u00d4I T\u01af\u01a0I.",
             "CH\u1ec8 \u0110\u1ecaNH: nguy c\u01a1 OHSS cao, nhi\u1ec1u nang, E2 r\u1ea5t cao.",
             "K\u1ebft h\u1ee3p: \u0110\u00d4NG PH\u00d4I TO\u00c0N B\u1ed8 \u2192 chuy\u1ec3n chu k\u1ef3 sau.",
             "Thu\u1ed1c d\u00f9ng: buserelin ho\u1eb7c Decapeptyl, ti\u00eam d\u01b0\u1edbi da b\u1ee5ng."]),

    content("Trigger failure \u2014 Nguy c\u01a1 c\u1ea7n nh\u1edb",
            ["Sau GnRH agonist trigger: v\u1eabn c\u00f3 th\u1ec3 TH\u1ea4T B\u1ea0I trigger.",
             "Ho\u1eb7c thu \u0111\u01b0\u1ee3c R\u1ea4T \u00cdT no\u00e3n / no\u00e3n KH\u00d4NG nh\u01b0 k\u1ef3 v\u1ecdng.",
             "\u0110\u1eb7c bi\u1ec7t khi: tuy\u1ebfn y\u00ean b\u1ecb \u1ee9c ch\u1ebf QU\u00c1 M\u1ea0NH ho\u1eb7c \u0111\u00e1p \u1ee9ng LH KH\u00d4NG \u0110\u1ee6.",
             "C\u1ea7n c\u00f3 quy tr\u00ecnh KI\u1ec2M TRA v\u00e0 C\u1ee8U V\u00c3N chu k\u1ef3 t\u00f9y trung t\u00e2m.",
             "C\u00f3 th\u1ec3 d\u00f9ng hCG \u0111\u1ec3 C\u1ee8U V\u00c3N v\u00e0 ch\u1ecdc h\u00fat \u0111\u01b0\u1ee3c no\u00e3n."]),

    content("Khi n\u00e0o KH\u00d4NG d\u00f9ng agonist trigger?",
            ["Long protocol: tuy\u1ebfn y\u00ean \u0111\u00e3 b\u1ecb \u1ee8C CH\u1ebe HO\u00c0N TO\u00c0N \u2192 KH\u00d4NG c\u00f3 ch\u1ec9 \u0111\u1ecbnh agonist trigger.",
             "Antagonist cycle + agonist trigger: c\u1ea7n l\u01b0u \u00fd th\u1eddi gian t\u1eeb m\u0169i antagonist cu\u1ed1i \u0111\u1ebfn trigger KH\u00d4NG D\u01af\u1edaI 10 GI\u1edc.",
             "M\u1ee5c \u0111\u00edch: \u0111\u1ea3m b\u1ea3o tuy\u1ebfn y\u00ean KH\u00d4NG c\u00f2n b\u1ecb \u1ee9c ch\u1ebf."]),

    content("C\u1eadp nh\u1eadt: Chi\u1ebfn l\u01b0\u1ee3c gi\u1ea3m OHSS",
         ["D\u00f9ng ANTAGONIST thay v\u00ec agonist d\u00e0i \u1edf nh\u00f3m nguy c\u01a1.",
          "GnRH AGONIST TRIGGER trong chu k\u1ef3 antagonist.",
          "GI\u1ea2M li\u1ec1u FSH.",
          "FREEZE-ALL.",
          "SINGLE EMBRYO TRANSFER khi ph\u00f9 h\u1ee3p.",
          "PMID: 26597569"]),

    # --- 6.4 Trưởng thành noãn kép ---
    sec("II.6.4", "Tr\u01b0\u1edfng th\u00e0nh no\u00e3n k\u00e9p", ""),

    content("Dual trigger & Double trigger",
            ["Tr\u01b0\u1edfng th\u00e0nh no\u00e3n k\u00e9p: s\u1eed d\u1ee5ng C\u1ea2 hCG v\u00e0 agonist.",
             "M\u1ee5c \u0111\u00edch: v\u1eeba GI\u1ea2M OHSS v\u1eeba GI\u1eee t\u1ef7 l\u1ec7 c\u00f3 thai cao.",
             "V\u1ec1 sau: m\u1edf r\u1ed9ng cho \u0111\u00e1p \u1ee9ng k\u00e9m, ti\u1ec1n s\u1eed trigger k\u1ebft qu\u1ea3 k\u00e9m.",
             "Nghi\u00ean c\u1ee9u ph\u00e2n t\u00edch g\u1ed9p c\u1ee7a Ding v\u00e0 cs: c\u1ea3i thi\u1ec7n s\u1ed1 no\u00e3n ho\u1eb7c t\u1ef7 l\u1ec7 c\u00f3 thai."]),

    twocol("Dual vs Double trigger",
           "Dual trigger", ["hCG + GnRH agonist C\u00d9NG TH\u1edcI \u0110I\u1ec2M", "Ph\u1ed1i h\u1ee3p t\u00edn hi\u1ec7u tr\u01b0\u1edfng th\u00e0nh no\u00e3n", "C\u00e2n nh\u1eafc OHSS n\u1ebfu c\u00f3 hCG"],
           "Double trigger", ["GnRH agonist TR\u01af\u1edaC, hCG SAU", "D\u00f9ng trong \u0111\u00e1p \u1ee9ng k\u00e9m / ti\u1ec1n s\u1eed trigger k\u00e9m", "KH\u00d4NG n\u00ean d\u00f9ng routine"]),

    content("Nghi\u00ean c\u1ee9u c\u1ee7a H\u1ed3 S\u1ef9 H\u00f9ng",
            ["So s\u00e1nh tr\u01b0\u1edfng th\u00e0nh no\u00e3n k\u00e9p v\u1edbi hCG \u0111\u01a1n thu\u1ea7n.",
             "\u0110\u1ed1i t\u01b0\u1ee3ng: b\u1ec7nh nh\u00e2n GI\u1ea2M D\u1ef0 TR\u1eee BU\u1ed2NG TR\u1ee8NG.",
             "K\u1ebft qu\u1ea3: tr\u01b0\u1edfng th\u00e0nh no\u00e3n k\u00e9p l\u00e0m T\u0102NG T\u1ef6 L\u1ec6 NO\u00c3N MII so v\u1edbi nh\u00f3m rhCG \u0111\u01a1n thu\u1ea7n."]),

    # ═══ II.7. ĐÔNG PHÔI TOÀN BỘ ═══
    sec("II.7", "\u0110\u00f4ng ph\u00f4i to\u00e0n b\u1ed9 (freeze-all)", ""),

    content("\u01afu \u0111i\u1ec3m c\u1ee7a k\u1ef9 thu\u1eadt \u0111\u00f4ng ph\u00f4i th\u1ee7y tinh h\u00f3a",
            ["K\u1ef9 thu\u1eadt \u0111\u00f4ng ph\u00f4i TH\u1ee6Y TINH H\u00d3A cho t\u1ef7 l\u1ec7 s\u1ed1ng sau r\u00e3 \u0111\u00f4ng CAO.",
             "Ch\u1ea5t l\u01b0\u1ee3ng ph\u00f4i KH\u00d4NG THAY \u0110\u1ed4I tr\u01b0\u1edbc v\u00e0 sau r\u00e3 \u0111\u00f4ng.",
             "T\u1ef7 l\u1ec7 c\u00f3 thai chu k\u1ef3 chuy\u1ec3n ph\u00f4i tr\u1eef l\u1ea1nh KH\u00d4NG THUA K\u00c9M chu k\u1ef3 chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i.",
             "\u2192 Freeze-all \u0111\u01b0\u1ee3c ch\u1ec9 \u0111\u1ecbnh TH\u01af\u1edcNG QUY trong c\u00e1c chu k\u1ef3 c\u00f3 ch\u1ec9 \u0111\u1ecbnh."]),

    content("Ch\u1ec9 \u0111\u1ecbnh freeze-all",
            ["Nguy c\u01a1 qu\u00e1 k\u00edch bu\u1ed3ng tr\u1ee9ng (OHSS).",
             "Chu k\u1ef3 t\u0103ng progesterone s\u1edbm.",
             "Chu k\u1ef3 c\u00f3 ni\u00eam m\u1ea1c t\u1eed cung KH\u00d4NG thu\u1eadn l\u1ee3i.",
             "B\u1ea5t c\u1ee9 l\u00fd do n\u00e0o c\u1ea7n TR\u00cc HO\u00c3N chuy\u1ec3n ph\u00f4i.",
             "Chu k\u1ef3 tr\u01b0\u1edfng th\u00e0nh no\u00e3n b\u1eb1ng GnRH agonist (suy ho\u00e0ng th\u1ec3).",
             "Chu k\u1ef3 random start (n\u1ed9i m\u1ea1c kh\u00f4ng \u0111\u1ed3ng b\u1ed9).",
             "Chu k\u1ef3 PPOS (n\u1ed9i m\u1ea1c kh\u00f4ng \u0111\u1ed3ng b\u1ed9 v\u1edbi tu\u1ed5i ph\u00f4i)."]),

    content("C\u1eadp nh\u1eadt: Freeze-all \u2014 C\u00e1 th\u1ec3 h\u00f3a",
         ["Freeze-all \u0111\u1eb7c bi\u1ec7t h\u1ee3p l\u00fd khi: OHSS, P4 t\u0103ng s\u1edbm, PPOS, random start, agonist trigger, n\u1ed9i m\u1ea1c kh\u00f4ng thu\u1eadn l\u1ee3i.",
          "Tuy nhi\u00ean: freeze-all KH\u00d4NG n\u00ean \u0111\u01b0\u1ee3c hi\u1ec3u l\u00e0 LU\u00d4N T\u1ed0T H\u01a0N fresh transfer cho M\u1eccI b\u1ec7nh nh\u00e2n.",
          "Quy\u1ebft \u0111\u1ecbnh c\u1ea7n C\u00c1 TH\u1ec2 H\u00d3A theo nguy c\u01a1 v\u00e0 m\u1ee5c ti\u00eau \u0111i\u1ec1u tr\u1ecb."]),

    # ═══ III. KẾT LUẬN ═══
    sec("III", "K\u1ebft lu\u1eadn",
        "Si\u00eau \u00e2m l\u00e0 c\u00f4ng c\u1ee5 kh\u00f4ng th\u1ec3 thay th\u1ebf trong theo d\u00f5i KTBT"),

    content("T\u00f3m t\u1eaft vai tr\u00f2 c\u1ee7a KTBT v\u00e0 theo d\u00f5i",
            ["KTBT l\u00e0 b\u01b0\u1edbc quan tr\u1ecdng trong IVF, quy\u1ebft \u0111\u1ecbnh t\u1ea1o \u0111\u01b0\u1ee3c NHI\u1ec0U no\u00e3n v\u1edbi CH\u1ea4T L\u01af\u1ee2NG t\u1ed1t hay kh\u00f4ng.",
             "Theo d\u00f5i trong KTBT: \u0111i\u1ec1u ch\u1ec9nh k\u1ecbp th\u1eddi, quy\u1ebft \u0111\u1ecbnh trigger, ph\u00e1t hi\u1ec7n s\u1edbm OHSS.",
             "Ph\u01b0\u01a1ng ph\u00e1p ch\u00ednh: SI\u00caU \u00c2M \u0111\u01b0\u1eddng \u00e2m \u0111\u1ea1o + X\u00c9T NGHI\u1ec6M HORMON.",
             "Si\u00eau \u00e2m l\u00e0 ph\u01b0\u01a1ng ph\u00e1p \u0110\u01a0N GI\u1ea2N, KH\u00d4NG X\u00c2M NH\u1eacP v\u00e0 KH\u00d4NG TH\u1ec2 THAY TH\u1ebe."]),

    content("B\u1ea3ng c\u1eadp nh\u1eadt \u2014 Quy\u1ebft \u0111\u1ecbnh nhanh trong th\u1ef1c h\u00e0nh",
         ["\u0110\u00e1p \u1ee9ng TH\u1ea4P \u2192 ki\u1ec3m tra tu\u1ed5i, AMH/AFC, li\u1ec1u \u0111ang d\u00f9ng, s\u1ed1 nang th\u1ef1c s\u1ef1 ph\u00e1t tri\u1ec3n; c\u00e2n nh\u1eafc KH\u00d4NG t\u0103ng li\u1ec1u qu\u00e1 m\u1ee9c.",
          "\u0110\u00e1p \u1ee9ng CAO \u2192 \u01b0u ti\u00ean ph\u00f2ng OHSS b\u1eb1ng gi\u1ea3m li\u1ec1u / antagonist / agonist trigger / freeze-all.",
          "Progesterone T\u0102NG S\u1edaM ho\u1eb7c PPOS \u2192 KH\u00d4NG chuy\u1ec3n t\u01b0\u01a1i.",
          "Nghi ch\u1ecdc h\u00fat KH\u00d3 \u2192 ghi r\u00f5 v\u1ecb tr\u00ed bu\u1ed3ng tr\u1ee9ng v\u00e0 chu\u1ea9n b\u1ecb th\u1ee7 thu\u1eadt."]),

    yesno("Decision: \u0110\u00e1p \u1ee9ng th\u1ea5p",
          "\u00cdt nang ph\u00e1t tri\u1ec3n h\u01a1n k\u1ef3 v\u1ecdng?",
          ["Ki\u1ec3m tra tu\u1ed5i, AMH/AFC, FSH", "Xem ti\u1ec1n s\u1eed v\u00e0 s\u1ed1 nang th\u1eadt", "T\u01b0 v\u1ea5n k\u1ef3 v\u1ecdng; kh\u00f4ng t\u0103ng li\u1ec1u v\u00f4 h\u1ea1n"],
          ["Ti\u1ebfp t\u1ee5c theo protocol", "Theo d\u00f5i s\u00e1t"]),

    yesno("Decision: \u0110\u00e1p \u1ee9ng cao",
          "Nhi\u1ec1u nang v\u00e0 nguy c\u01a1 OHSS?",
          ["Gi\u1ea3m nguy c\u01a1", "E2 n\u1ebfu c\u1ea7n", "Antagonist + agonist trigger", "Freeze-all"],
          ["Ti\u1ebfp t\u1ee5c k\u1ebf ho\u1ea1ch", "Theo d\u00f5i s\u00e1t"]),

    yesno("Decision: P4 / n\u1ed9i m\u1ea1c",
          "Fresh transfer c\u00f2n ph\u00f9 h\u1ee3p?",
          ["Fresh n\u1ebfu P4, n\u1ed9i m\u1ea1c v\u00e0 OHSS risk \u0111\u1ec1u \u1ed5n"],
          ["C\u00e2n nh\u1eafc freeze-all", "Ghi r\u00f5 l\u00fd do"]),

    yesno("Decision: Ch\u1ecdc h\u00fat kh\u00f3",
          "Bu\u1ed3ng tr\u1ee9ng xa \u0111\u1ea7u d\u00f2 ho\u1eb7c nghi d\u00ednh?",
          ["Ghi v\u1ecb tr\u00ed, h\u01b0\u1edbng ti\u1ebfp c\u1eadn", "T\u00ecm v\u1eadt c\u1ea3n (ru\u1ed9t, m\u1ea1ch m\u00e1u)", "B\u00e1o tr\u01b0\u1edbc ekip"],
          ["Theo d\u00f5i th\u01b0\u1eddng quy", "V\u1eabn ghi access n\u1ebfu thay \u0111\u1ed5i"]),

    summary("Take-home messages",
            ["1. Reserve \u2260 Response: AMH/AFC d\u1ef1 \u0111o\u00e1n s\u1ed1 no\u00e3n; tu\u1ed5i d\u1ef1 \u0111o\u00e1n ch\u1ea5t l\u01b0\u1ee3ng.",
             "2. Si\u00eau \u00e2m l\u00e0 tr\u1ee5c ch\u00ednh: ghi checklist m\u1ed7i l\u1ea7n, kh\u00f4ng ch\u1ec9 nh\u00ecn nang l\u1edbn nh\u1ea5t.",
             "3. Antagonist \u0111\u01b0\u1ee3c \u01b0u ti\u00ean: ng\u1eafn, an to\u00e0n, cho ph\u00e9p agonist trigger.",
             "4. Trigger l\u00e0 quy\u1ebft \u0111\u1ecbnh AN TO\u00c0N: c\u00e2n b\u1eb1ng to\u00e0n cohort, kh\u00f4ng t\u1ed1i \u01b0u m\u1ed9t nang.",
             "5. Freeze-all l\u00e0 c\u00f4ng c\u1ee5 c\u00e1 th\u1ec3 h\u00f3a: kh\u00f4ng ph\u1ea3i m\u1eb7c \u0111\u1ecbnh t\u1ed1t h\u01a1n fresh."]),

    refs("T\u00e0i li\u1ec7u tham kh\u1ea3o \u0111\u00e3 verify",
         ["ESHRE guideline: ovarian stimulation for IVF/ICSI. PMID: 32395637.",
          "ESHRE guideline: ovarian stimulation for IVF/ICSI: an update in 2025. PMID: 41732035.",
          "Testing and interpreting measures of ovarian reserve: a committee opinion. PMID: 33280722.",
          "Association between the number of eggs and live birth in IVF treatment. PMID: 21558332.",
          "Consensus statement on prevention and detection of ovarian hyperstimulation syndrome. PMID: 26597569."]),
]

deck = {"meta": {"title": "Si\u00eau \u00e2m theo d\u00f5i k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng", "author": "B\u00e1c s\u0129 Ng\u1ecdc H\u01b0ng", "subtitle": "Deck h\u1ecdc c\u00e1 nh\u00e2n \u2014 engine slider3636"}, "slides": slides}
OUT.write_text(json.dumps(deck, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {OUT} ({len(slides)} slides)")
