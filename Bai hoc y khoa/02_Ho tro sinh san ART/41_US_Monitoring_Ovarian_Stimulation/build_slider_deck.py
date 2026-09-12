import json
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "US_Monitoring_Ovarian_Stimulation_slider3636.deck.json"
SRC = "US Monitoring Ovarian Stimulation 2026-07-04 — PMID 41732035; 32395637; 33280722; 21558332; 26597569"


def s(kind, **kw):
    d = {"type": kind}
    d.update(kw)
    return d


def content(title, points):
    return s("content", title=title, points=points, footnote=SRC)


def twocol(title, lt, lp, rt, rp):
    return s("two_column", title=title, left_title=lt, left_points=lp, right_title=rt, right_points=rp, variant="vs_compare", note=SRC)


def sec(n, t, sub=""):
    return s("section", variant="number_block", part_number=n, part_title=t, part_subtitle=sub)


def checklist(title, items):
    return s("criteria", variant="score_points", title=title, items=[{"text": i, "points": "\u2713"} for i in items])


def yesno(title, question, yes, no):
    return s("algorithm", variant="branching_yesno", title=title, question=question, yes_branch=yes, no_branch=no)


def flow(title, steps):
    nodes = []
    for i, t in enumerate(steps):
        nodes.append({"text": t, "type": "start" if i == 0 else "end" if i == len(steps) - 1 else "process"})
    return s("algorithm", variant="linear_flow", title=title, nodes=nodes)


def table(title, headers, rows):
    return s("table", variant="comparison_highlight", title=title, headers=headers, rows=rows)


def big(title, stats):
    return s("big_number", variant="single_hero", title=title, stats=stats)


def summary(title, points):
    return s("summary", variant="takeaways", title=title, points=points)


def refs(title, refs_list):
    return s("references", variant="numbered", title=title, refs=refs_list)


def three(title, cols):
    return s("three_column", title=title, variant="pillars", columns=cols)


def timeline(title, events):
    return s("timeline", variant="horizontal_milestones", title=title, events=[{"date": e[0], "title": e[1], "desc": e[2]} for e in events])


def defin(term, definition):
    return s("definition", variant="term_box", term=term, definition=definition)


slides = [
    s("title", variant="split_dark",
      title="Si\u00eau \u00e2m theo d\u00f5i k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng trong IVF/ICSI",
      subtitle="Deck h\u1ecdc c\u00e1 nh\u00e2n \u2014 t\u1eeb b\u00e0i m\u1eb9 2026-07-04",
      author="B\u00e1c s\u0129 Ng\u1ecdc H\u01b0ng",
      specialty="ART / IVF-ICSI",
      date="2026-07-04"),

    s("outline", variant="numbered", title="N\u1ed9i dung", chapters=[
        "0. T\u1ed5ng quan", "1. Si\u00eau \u00e2m tr\u01b0\u1edbc KTBT", "2. Khung sinh l\u00fd", "3. K\u1ef9 thu\u1eadt \u0111\u1ebfm AFC",
        "4. Theo d\u00f5i theo ph\u00e1c \u0111\u1ed3", "5. K\u1ef9 thu\u1eadt \u0111o nang", "6. Ni\u00eam m\u1ea1c t\u1eed cung",
        "7. N\u1ed9i ti\u1ebft trong theo d\u00f5i", "8. C\u00e1c \u0111i\u1ec3m quy\u1ebft \u0111\u1ecbnh",
        "9. PCOS / \u0111\u00e1p \u1ee9ng cao", "10. \u0110\u00e1p \u1ee9ng th\u1ea5p",
        "11. Nh\u1eadn di\u1ec7n OHSS", "12. Freeze-all", "13. M\u1eabu phi\u1ebfu & checklist",
        "14. Atlas ca l\u00e2m s\u00e0ng", "15. B\u00e0i h\u1ecdc l\u00e2m s\u00e0ng", "TLTK",
    ]),

    # ═══ 0. TỔNG QUAN ═══
    sec("0", "T\u1ed5ng quan", "V\u00ec sao si\u00eau \u00e2m l\u00e0 tr\u1ee5c ch\u00ednh trong theo d\u00f5i KTBT?"),

    content("KTBT l\u00e0 b\u00e0i to\u00e1n \u0111i\u1ec1u khi\u1ec3n \u0111o\u00e0n h\u1ec7 nang",
            ["K\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng c\u00f3 ki\u1ec3m so\u00e1t (COS) l\u00e0 b\u01b0\u1edbc n\u1ec1n t\u1ea3ng c\u1ee7a IVF/ICSI.",
             "M\u1ed7i l\u1ea7n si\u00eau \u00e2m ph\u1ea3i tr\u1ea3 l\u1eddi \u0111\u01b0\u1ee3c m\u1ed9t c\u00e2u h\u1ecfi \u0111i\u1ec1u tr\u1ecb.",
             "Si\u00eau \u00e2m l\u00e0 c\u00f4ng c\u1ee5 ra quy\u1ebft \u0111\u1ecbnh theo th\u1eddi gian th\u1ef1c, kh\u00f4ng ch\u1ec9 \u0111\u1ec3 \u0111o nang."]),

    content("4 m\u1ee5c ti\u00eau c\u1ee7a theo d\u00f5i si\u00eau \u00e2m",
            ["1. \u0110\u00e1nh gi\u00e1 \u0111\u00e1p \u1ee9ng bu\u1ed3ng tr\u1ee9ng: s\u1ed1 nang ph\u00e1t tri\u1ec3n, t\u1ed1c \u0111\u1ed9 l\u1edbn, ph\u00e2n b\u1ed1 k\u00edch th\u01b0\u1edbc.",
             "2. X\u00e1c \u0111\u1ecbnh th\u1eddi \u0111i\u1ec3m d\u00f9ng antagonist (flexible) v\u00e0 th\u1eddi \u0111i\u1ec3m trigger.",
             "3. Ph\u00e1t hi\u1ec7n s\u1edbm nguy c\u01a1 OHSS \u0111\u1ec3 \u0111i\u1ec1u ch\u1ec9nh trigger v\u00e0 k\u1ebf ho\u1ea1ch chuy\u1ec3n ph\u00f4i.",
             "4. \u0110\u00e1nh gi\u00e1 n\u1ed9i m\u1ea1c t\u1eed cung \u0111\u1ec3 quy\u1ebft \u0111\u1ecbnh chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i hay \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9."]),

    content("Nguy\u00ean t\u1eafc c\u1ed1t l\u00f5i",
            ["M\u1ed7i l\u1ea7n si\u00eau \u00e2m k\u1ebft th\u00fac b\u1eb1ng m\u1ed9t K\u1ebeT LU\u1eacN QU\u1ea2N L\u00dd: gi\u1eef li\u1ec1u, \u0111\u1ed5i li\u1ec1u, b\u1eaft antagonist, trigger, \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9, hay chu\u1ea9n b\u1ecb ch\u1ecdc h\u00fat.",
             "Si\u00eau \u00e2m l\u00e0 ph\u01b0\u01a1ng ph\u00e1p KH\u00d4NG X\u00c2M NH\u1eacP, l\u1eb7p l\u1ea1i \u0111\u01b0\u1ee3c, v\u00e0 KH\u00d4NG TH\u1ec2 THAY TH\u1ebe b\u1eb1ng x\u00e9t nghi\u1ec7m n\u1ed9i ti\u1ebft \u0111\u01a1n thu\u1ea7n."]),

    content("ESHRE 2025 v\u1ec1 theo d\u00f5i (PMID 41732035)",
            ["KH\u00d4NG khuy\u1ebfn c\u00e1o \u0111i\u1ec1u ch\u1ec9nh li\u1ec1u FSH gi\u1eefa chu k\u1ef3 th\u01b0\u1eddng quy (conditional).",
             "Nh\u1ea5n m\u1ea1nh t\u1ea7m quan tr\u1ecdng c\u1ee7a vi\u1ec7c ch\u1ecdn \u0111\u00fang li\u1ec1u KH\u1edeI \u0110\u1ea6U.",
             "Si\u00eau \u00e2m \u0111\u00f3ng vai tr\u00f2 X\u00c1C NH\u1eacN \u0111\u00e1p \u1ee9ng h\u01a1n l\u00e0 c\u00f4ng c\u1ee5 \u0111\u1ec3 ch\u1ec9nh li\u1ec1u t\u1eebng ng\u00e0y.",
             "KH\u00d4NG khuy\u1ebfn c\u00e1o \u0111o E2 th\u01b0\u1eddng quy v\u00e0o ng\u00e0y trigger cho chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i cycle (strong).",
             "Khuy\u1ebfn c\u00e1o \u0111o PROGESTERONE v\u00e0o ng\u00e0y trigger cho chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i cycle (conditional)."]),

    timeline("B\u1ea3n \u0111\u1ed3 m\u1ed9t chu k\u1ef3 monitor KTBT",
             [("Baseline", "AFC - t\u1eed cung", "\u0110\u1ecbnh li\u1ec1u FSH, ph\u00e1t hi\u1ec7n nang t\u1ed3n d\u01b0, \u0111\u01b0\u1eddng ch\u1ecdc h\u00fat"),
              ("Start FSH", "Ng\u00e0y 2-4", "B\u1eaft \u0111\u1ea7u gonadotropin theo li\u1ec1u \u0111\u00e3 ch\u1ecdn"),
              ("Day 5-7", "\u0110\u00e1nh gi\u00e1 \u0111\u00e1p \u1ee9ng", "\u0110\u1ecdc t\u1ed1c \u0111\u1ed9 \u0111o\u00e0n h\u1ec7, quy\u1ebft \u0111\u1ecbnh antagonist"),
              ("Day 7-12", "Late stimulation", "Theo d\u00f5i nang, n\u1ed9i m\u1ea1c, OHSS, progesterone"),
              ("Trigger", "Quy\u1ebft \u0111\u1ecbnh cu\u1ed1i", "Ch\u1ecdn lo\u1ea1i trigger, gi\u1edd ch\u1ecdc h\u00fat 34-36h"),
              ("OPU/ET", "Ch\u1ecdc h\u00fat & chuy\u1ec3n ph\u00f4i", "Fresh hay \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9")]),

    # ═══ 1. BASELINE SCAN ═══
    sec("1", "Si\u00eau \u00e2m tr\u01b0\u1edbc k\u00edch th\u00edch", "Baseline scan: AFC, nang t\u1ed3n d\u01b0, t\u1eed cung, \u0111\u01b0\u1eddng ch\u1ecdc h\u00fat"),

    checklist("Baseline ultrasound checklist",
              ["AFC hai bu\u1ed3ng tr\u1ee9ng (nang 2-9 mm t\u1eebng b\u00ean)",
               "Nang t\u1ed3n d\u01b0 / cyst (v\u1ecb tr\u00ed, k\u00edch th\u01b0\u1edbc, t\u00ednh ch\u1ea5t)",
               "Endometrioma (k\u00edch th\u01b0\u1edbc, b\u00ean, quan h\u1ec7 v\u1edbi \u0111\u01b0\u1eddng ch\u1ecdc h\u00fat)",
               "T\u1eed cung: polyp, u x\u01a1 d\u01b0\u1edbi ni\u00eam, v\u00e1ch ng\u0103n, d\u1ecbch l\u00f2ng t\u1eed cung",
               "\u0110\u01b0\u1eddng ti\u1ebfp c\u1eadn bu\u1ed3ng tr\u1ee9ng (kho\u1ea3ng c\u00e1ch, v\u1eadt c\u1ea3n)",
               "T\u1eed cung di \u0111\u1ed9ng (ng\u1ea3 sau, c\u1ed1 \u0111\u1ecbnh \u2192 nghi d\u00ednh/endometriosis)"]),

    content("X\u1eed tr\u00ed nang t\u1ed3n d\u01b0",
            ["Nang \u0111\u01a1n thu\u1ea7n <18 mm, kh\u00f4ng ho\u1ea1t \u0111\u1ed9ng n\u1ed9i ti\u1ebft \u2192 c\u00f3 th\u1ec3 b\u1eaft \u0111\u1ea7u KTBT.",
             "Nang >18 mm \u2192 ch\u1ecdc h\u00fat ho\u1eb7c ch\u1edd sang chu k\u1ef3 ti\u1ebfp theo.",
             "Nang t\u1ed3n t\u1ea1i nhi\u1ec1u chu k\u1ef3, to \u2192 c\u00e2n nh\u1eafc ch\u1ecdc h\u00fat tr\u01b0\u1edbc KTBT.",
             "Nang kh\u00f4ng \u1ea3nh h\u01b0\u1edfng ch\u1ecdc h\u00fat no\u00e3n \u2192 kh\u00f4ng nh\u1ea5t thi\u1ebft can thi\u1ec7p.",
             "C\u00f3 th\u1ec3 d\u00f9ng COCP \u0111\u1ec3 l\u00e0m ti\u00eau nang t\u1ed3n d\u01b0 (kh\u00e1c v\u1edbi COCP pretreatment cho antagonist)."]),

    content("\u0110\u00e1nh gi\u00e1 t\u1eed cung tr\u01b0\u1edbc KTBT",
            ["U x\u01a1 d\u01b0\u1edbi ni\u00eam, polyp, v\u00e1ch ng\u0103n, d\u1ecbch l\u00f2ng t\u1eed cung \u2192 c\u00f3 th\u1ec3 thay \u0111\u1ed5i k\u1ebf ho\u1ea1ch chuy\u1ec3n ph\u00f4i.",
             "M\u1ee5c ti\u00eau tr\u01b0\u1edbc k\u00edch th\u00edch: kh\u00f4ng ch\u1ec9 l\u00e0 bu\u1ed3ng tr\u1ee9ng, m\u00e0 c\u00f2n x\u00e1c \u0111\u1ecbnh chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i c\u00f3 kh\u1ea3 thi kh\u00f4ng.",
             "N\u1ebfu ph\u00e1t hi\u1ec7n b\u1ea5t th\u01b0\u1eddng c\u00f3 \u00fd ngh\u0129a \u2192 k\u00edch th\u00edch v\u00e0 thu ph\u00f4i nh\u01b0ng tr\u00ec ho\u00e3n chuy\u1ec3n ph\u00f4i (\u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9)."]),

    content("Endometrioma tr\u01b0\u1edbc k\u00edch th\u00edch",
            ["Ghi k\u00edch th\u01b0\u1edbc, b\u00ean, s\u1ed1 l\u01b0\u1ee3ng v\u00e0 quan h\u1ec7 v\u1edbi \u0111\u01b0\u1eddng ch\u1ecdc h\u00fat.",
             "N\u1ebfu kh\u00f4ng \u1ea3nh h\u01b0\u1edfng \u0111\u1ebfn ch\u1ecdc h\u00fat no\u00e3n: KH\u00d4NG nh\u1ea5t thi\u1ebft can thi\u1ec7p.",
             "C\u00e2n b\u1eb1ng nguy c\u01a1 gi\u1ea3m d\u1ef1 tr\u1eef sau can thi\u1ec7p v\u1edbi nguy c\u01a1 nhi\u1ec5m/kh\u00f3 ch\u1ecdc h\u00fat.",
             "T\u1eed cung ng\u1ea3 sau c\u1ed1 \u0111\u1ecbnh v\u00e0 \u0111au khi \u1ea5n: g\u1ee3i \u00fd d\u00ednh/endometriosis, ti\u00ean l\u01b0\u1ee3ng kh\u00f4ng t\u1ed1t."]),

    content("Bu\u1ed3ng tr\u1ee9ng xa \u0111\u1ea7u d\u00f2",
            ["G\u1ee3i \u00fd ch\u1ecdc h\u00fat no\u00e3n c\u00f3 th\u1ec3 kh\u00f3 h\u01a1n.",
             "C\u00f3 th\u1ec3 li\u00ean quan d\u00ednh v\u00f9ng ch\u1eadu, endometriosis ho\u1eb7c bu\u1ed3ng tr\u1ee9ng b\u1ecb k\u00e9o cao.",
             "C\u1ea7n ghi h\u01b0\u1edbng ti\u1ebfp c\u1eadn, kho\u1ea3ng c\u00e1ch v\u00e0 nguy c\u01a1 m\u1ea1ch m\u00e1u/ru\u1ed9t xen gi\u1eefa n\u1ebfu th\u1ea5y.",
             "Th\u00f4ng tin n\u00e0y quan tr\u1ecdng NGANG V\u1edaI S\u1ed0 NANG trong planning th\u1ee7 thu\u1eadt."]),

    content("ESHRE 2025 v\u1ec1 d\u1ef1 \u0111o\u00e1n \u0111\u00e1p \u1ee9ng",
            ["AFC ho\u1eb7c AMH \u0111\u1ee7 \u0111\u1ec3 d\u1ef1 \u0111o\u00e1n ovarian response (strong).",
             "FSH n\u1ec1n, E2 n\u1ec1n, LH n\u1ec1n, inhibin B, progesterone n\u1ec1n KH\u00d4NG \u0111\u01b0\u1ee3c khuy\u1ebfn c\u00e1o \u0111\u1ec3 d\u1ef1 \u0111o\u00e1n response (strong, M\u1edaI 2025).",
             "Tu\u1ed5i m\u1eb9 v\u00e0 BMI l\u00e0 predictors c\u1ee7a pregnancy v\u00e0 live birth (strong, M\u1edaI 2025)."]),

    # ═══ 2. KHUNG SINH LÝ ═══
    sec("2", "Khung sinh l\u00fd c\u1ea7n nh\u1edb khi \u0111\u1ecdc si\u00eau \u00e2m", "FSH threshold, FSH window, follicular waves, LH ceiling/floor"),

    defin("FSH threshold (ng\u01b0\u1ee1ng FSH)",
          "N\u1ed3ng \u0111\u1ed9 FSH m\u00e0 tr\u00ean \u0111\u00f3 m\u1ed9t nang c\u00f3 th\u1ec3 ti\u1ebfp t\u1ee5c ph\u00e1t tri\u1ec3n. M\u1ed6I NANG C\u00d3 M\u1ed8T NG\u01af\u1ee0NG RI\u00caNG. FSH ngo\u1ea1i sinh gi\u00fap nhi\u1ec1u nang v\u01b0\u1ee3t ng\u01b0\u1ee1ng h\u01a1n."),

    content("\u00dd ngh\u0129a FSH threshold tr\u00ean si\u00eau \u00e2m",
            ["N\u1ebfu \u0111o\u00e0n h\u1ec7 c\u00f3 nhi\u1ec1u nang nh\u1ecf nh\u01b0ng ch\u1ec9 m\u1ed9t v\u00e0i nang l\u1edbn, c\u00f3 th\u1ec3 do li\u1ec1u FSH ch\u1ec9 v\u1eeba \u0111\u1ee7 cho nh\u00f3m nang nh\u1ea1y nh\u1ea5t.",
             "Nh\u1eefng nang c\u00f2n l\u1ea1i \u0111ang \u1edf d\u01b0\u1edbi ng\u01b0\u1ee1ng \u2192 c\u1ea7n th\u1eddi gian h\u01a1n l\u00e0 t\u0103ng li\u1ec1u."]),

    defin("FSH window (c\u1eeda s\u1ed5 FSH)",
          "Kho\u1ea3ng th\u1eddi gian n\u1ed3ng \u0111\u1ed9 FSH n\u1eb1m tr\u00ean ng\u01b0\u1ee1ng. C\u1eeda s\u1ed5 qu\u00e1 ng\u1eafn \u2192 m\u1ea5t nang nh\u1ecf. C\u1eeda s\u1ed5 qu\u00e1 d\u00e0i \u1edf \u0111\u00e1p \u1ee9ng cao \u2192 qu\u00e1 nhi\u1ec1u nang nh\u1ecf ph\u00e1t tri\u1ec3n \u2192 OHSS."),

    content("Follicular waves (s\u00f3ng nang)",
            ["Kh\u00f4ng ph\u1ea3i m\u1ecdi nang ch\u1ec9 \u0111\u01b0\u1ee3c tuy\u1ec3n m\u1ed9t l\u1ea7n duy nh\u1ea5t v\u00e0o \u0111\u1ea7u chu k\u1ef3.",
             "C\u00f3 b\u1eb1ng ch\u1ee9ng v\u1ec1 nhi\u1ec1u \u0111\u1ee3t s\u00f3ng tuy\u1ec3n nang trong m\u1ed9t chu k\u1ef3.",
             "\u0110\u00e2y l\u00e0 c\u01a1 s\u1edf cho DuoStim v\u00e0 random start.",
             "\u00dd ngh\u0129a: c\u00f3 th\u1ec3 b\u1eaft \u0111\u1ea7u KTBT kh\u00f4ng nh\u1ea5t thi\u1ebft ng\u00e0y 2-3 n\u1ebfu c\u00f3 l\u00fd do.",
             "Nh\u01b0ng khi d\u00f9ng random start, th\u01b0\u1eddng c\u1ea7n \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9 do n\u1ed9i m\u1ea1c kh\u00f4ng \u0111\u1ed3ng b\u1ed9."]),

    twocol("LH ceiling vs LH floor",
           "LH qu\u00e1 cao (surge / ceiling)",
           ["Ho\u00e0ng th\u1ec3 h\u00f3a s\u1edbm", "\u1ee8c ch\u1ebf aromatase, gi\u1ea3m ch\u1ea5t l\u01b0\u1ee3ng no\u00e3n", "\u0110\u00e2y l\u00e0 l\u00fd do d\u00f9ng antagonist"],
           "LH qu\u00e1 th\u1ea5p (floor)",
           ["Gi\u1ea3m s\u1ea3n xu\u1ea5t androgen n\u1ec1n", "Deep suppression t\u1eeb long agonist", "C\u00f3 th\u1ec3 c\u1ea7n th\u00eam LH \u1edf m\u1ed9t s\u1ed1 b\u1ec7nh nh\u00e2n"]),

    # ═══ 3. KỸ THUẬT ĐẾM AFC ═══
    sec("3", "K\u1ef9 thu\u1eadt \u0111\u1ebfm AFC", "Antral Follicle Count \u2014 ch\u1ec9 s\u1ed1 th\u1ef1c h\u00e0nh quan tr\u1ecdng nh\u1ea5t"),

    content("\u0110\u1ecbnh ngh\u0129a v\u00e0 k\u1ef9 thu\u1eadt",
            ["AFC: s\u1ed1 nang th\u1ee9 c\u1ea5p \u0111\u01b0\u1eddng k\u00ednh 2-9 mm (\u0111\u00f4i khi 2-10 mm) \u0111\u1ebfm \u0111\u01b0\u1ee3c v\u00e0o \u0111\u1ea7u chu k\u1ef3.",
             "D\u00f9ng \u0111\u1ea7u d\u00f2 \u00e2m \u0111\u1ea1o t\u1ea7n s\u1ed1 cao (\u22657 MHz) n\u1ebfu c\u00f3 th\u1ec3.",
             "Qu\u00e9t to\u00e0n b\u1ed9 bu\u1ed3ng tr\u1ee9ng theo m\u1ed9t chi\u1ec1u c\u00f3 h\u1ec7 th\u1ed1ng.",
             "\u0110\u1ebfm t\u1eebng nang c\u00f3 b\u1edd trong r\u00f5, d\u1ecbch tr\u1ed1ng \u00e2m.",
             "Ghi ri\u00eang AFC bu\u1ed3ng tr\u1ee9ng ph\u1ea3i v\u00e0 tr\u00e1i."]),

    content("Sai s\u1ed1 th\u01b0\u1eddng g\u1eb7p khi \u0111\u1ebfm AFC",
            ["B\u1ecf s\u00f3t nang nh\u1ecf (2-4 mm): qu\u00e9t ch\u1eadm, t\u0103ng gain nh\u1eb9.",
             "\u0110\u1ebfm l\u1eb7p c\u00f9ng m\u1ed9t nang: gi\u1eef m\u1eb7t c\u1eaft c\u00f3 h\u1ec7 th\u1ed1ng, kh\u00f4ng xoay \u0111\u1ea7u d\u00f2 lung tung.",
             "Nh\u1ea7m m\u1ea1ch m\u00e1u v\u00f9ng ch\u1eadu v\u1edbi nang nh\u1ecf: d\u00f9ng Doppler n\u1ebfu nghi ng\u1edd.",
             "Nh\u1ea7m nang t\u1ed3n d\u01b0 v\u1edbi nang th\u1ee9 c\u1ea5p: nang t\u1ed3n d\u01b0 >10 mm.",
             "Kh\u00f4ng ghi nh\u1eadn bu\u1ed3ng tr\u1ee9ng kh\u00f3 ti\u1ebfp c\u1eadn: lu\u00f4n ghi ch\u00fa n\u1ebfu bu\u1ed3ng tr\u1ee9ng \u1edf v\u1ecb tr\u00ed kh\u00f3."]),

    content("AFC v\u00e0 \u0111\u1ecbnh li\u1ec1u FSH kh\u1edfi \u0111\u1ea7u",
            ["AFC <5 \u2192 Low responder \u2192 225-300 IU/ng. Kh\u00f4ng t\u0103ng qu\u00e1 300 IU.",
             "AFC 5-7 \u2192 Suboptimal \u2192 200-300 IU/ng. C\u00e2n nh\u1eafc t\u00edch l\u0169y.",
             "AFC 8-18 \u2192 Normal responder \u2192 150-225 IU/ng.",
             "AFC >18 \u2192 High responder \u2192 100-150 IU/ng. Nguy c\u01a1 OHSS, \u01b0u ti\u00ean antagonist.",
             "ESHRE 2025: KH\u00d4NG d\u00f9ng >300 IU/ng cho \u0111\u00e1p \u1ee9ng th\u1ea5p (strong)."]),

    content("\u0110\u1ed9 \u0111\u1ed3ng \u0111\u1ec1u c\u1ee7a \u0111o\u00e0n h\u1ec7 nang",
            ["\u0110o\u00e0n h\u1ec7 \u0111\u1ed3ng \u0111\u1ec1u: nang c\u00f3 k\u00edch th\u01b0\u1edbc t\u01b0\u01a1ng t\u1ef1 \u2192 ti\u00ean l\u01b0\u1ee3ng ph\u00e1t tri\u1ec3n \u0111\u1ed3ng b\u1ed9 t\u1ed1t.",
             "\u0110o\u00e0n h\u1ec7 kh\u00f4ng \u0111\u1ed3ng \u0111\u1ec1u: nang to nh\u1ecf xen k\u1ebd \u2192 nguy c\u01a1 l\u1ec7ch pha, kh\u00f3 ch\u1ecdn trigger.",
             "\u0110\u1eebng ch\u1ec9 nh\u00ecn t\u1ed5ng AFC, h\u00e3y quan s\u00e1t c\u1ea3 \u0111\u1ed9 \u0111\u1ed3ng \u0111\u1ec1u c\u1ee7a \u0111o\u00e0n h\u1ec7."]),

    # ═══ 4. THEO DÕI THEO PHÁC ĐỒ ═══
    sec("4", "Theo d\u00f5i theo t\u1eebng lo\u1ea1i ph\u00e1c \u0111\u1ed3", "Long agonist, Antagonist fixed/flexible, PPOS, DuoStim"),

    content("Ph\u00e1c \u0111\u1ed3 Long GnRH Agonist",
            ["M\u1ed1c 1 (sau downregulation): kh\u00f4ng c\u00f3 nang >10 mm, n\u1ed9i m\u1ea1c m\u1ecfng. LH <5 IU/L, E2 <50 pg/mL.",
             "M\u1ed1c 2 (ng\u00e0y 5-7 FSH): \u0111\u00e1nh gi\u00e1 \u0111\u00e1p \u1ee9ng ban \u0111\u1ea7u. Long agonist \u0111\u00e3 ki\u1ec3m so\u00e1t LH surge.",
             "M\u1ed1c 3 (cu\u1ed1i KT, ng\u00e0y 8-12): \u0111o to\u00e0n b\u1ed9 nang, ph\u00e2n nh\u00f3m, n\u1ed9i m\u1ea1c, nguy c\u01a1 qu\u00e1 k\u00edch.",
             "Trigger: B\u1eaeT BU\u1ed8C hCG (kh\u00f4ng d\u00f9ng \u0111\u01b0\u1ee3c GnRH agonist trigger v\u00ec tuy\u1ebfn y\u00ean \u0111\u00e3 b\u1ecb \u1ee9c ch\u1ebf)."]),

    content("Ph\u00e1c \u0111\u1ed3 Antagonist Fixed",
            ["Baseline: nh\u01b0 m\u1ee5c 1.",
             "Ng\u00e0y 5-6 FSH: \u0111\u00e1nh gi\u00e1 \u0111\u00e1p \u1ee9ng. Antagonist b\u1eaft \u0111\u1ea7u theo l\u1ecbch c\u1ed1 \u0111\u1ecbnh.",
             "Fixed \u0111\u01a1n gi\u1ea3n h\u00f3a v\u1eadn h\u00e0nh, gi\u1ea3m nguy c\u01a1 qu\u00ean/mu\u1ed9n antagonist.",
             "Cu\u1ed1i KT: c\u00f3 th\u00eam l\u1ef1a ch\u1ecdn GnRH agonist trigger n\u1ebfu nguy c\u01a1 OHSS.",
             "ESHRE 2025: fixed probably recommended over flexible (conditional, \u2295\u2295\u25ef\u25ef)."]),

    content("Ph\u00e1c \u0111\u1ed3 Antagonist Flexible",
            ["Ng\u00e0y 5-6 FSH: B\u1eaeT BU\u1ed8C si\u00eau \u00e2m.",
             "N\u1ebfu nang l\u1edbn nh\u1ea5t \u226514 mm \u2192 b\u1eaft \u0111\u1ea7u antagonist.",
             "KH\u00d4NG \u0111\u01b0\u1ee3c si\u00eau \u00e2m mu\u1ed9n h\u01a1n ng\u00e0y 7 (nguy c\u01a1 b\u1eaft antagonist tr\u1ec5 \u2192 LH surge).",
             "Flexible gi\u1ea3m s\u1ed1 ng\u00e0y d\u00f9ng antagonist \u1edf m\u1ed9t s\u1ed1 b\u1ec7nh nh\u00e2n.",
             "Nh\u01b0ng \u0111\u00f2i h\u1ecfi si\u00eau \u00e2m \u0111\u00fang th\u1eddi \u0111i\u1ec3m. Kh\u00f4ng ph\u00f9 h\u1ee3p n\u1ebfu logistics kh\u00f3."]),

    content("PPOS v\u00e0 DuoStim / Random Start",
            ["PPOS: theo d\u00f5i si\u00eau \u00e2m t\u01b0\u01a1ng t\u1ef1 antagonist. LU\u00d4N \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9.",
             "DuoStim: 2 \u0111\u1ee3t KTBT trong 1 chu k\u1ef3. Luteal phase stimulation: progesterone n\u1ed9i sinh t\u1ef1 b\u1ea3o v\u1ec7 ch\u1ed1ng LH surge.",
             "Random start: b\u1eaft \u0111\u1ea7u b\u1ea5t k\u1ef3 th\u1eddi \u0111i\u1ec3m n\u00e0o. C\u1ea3 hai \u0111\u1ec1u \u0111i k\u00e8m \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9."]),

    twocol("Fixed vs Flexible Antagonist",
           "Fixed", ["B\u1eaft \u0111\u1ea7u ng\u00e0y 5-6 kh\u00f4ng ph\u1ee5 thu\u1ed9c nang", "D\u1ec5 v\u1eadn h\u00e0nh, \u00edt l\u1ed7i", "ESHRE 2025: probably preferred", "Ph\u00f9 h\u1ee3p trung t\u00e2m \u0111\u00f4ng"],
           "Flexible", ["B\u1eaft khi nang \u226514 mm", "C\u00e1 th\u1ec3 h\u00f3a, \u00edt ng\u00e0y thu\u1ed1c", "C\u1ea7n si\u00eau \u00e2m \u0111\u00fang ng\u00e0y", "Kh\u00f4ng ph\u00f9 h\u1ee3p logistics kh\u00f3"]),

    # ═══ 5. ĐO NANG ═══
    sec("5", "K\u1ef9 thu\u1eadt \u0111o nang no\u00e3n", "\u0110o b\u1edd trong, ph\u00e2n nh\u00f3m k\u00edch th\u01b0\u1edbc, t\u1ed1c \u0111\u1ed9 ph\u00e1t tri\u1ec3n"),

    content("Nguy\u00ean t\u1eafc \u0111o",
            ["\u0110o t\u1eeb B\u1edc TRONG \u0111\u1ebfn B\u1edc TRONG (inner-to-inner). Kh\u00f4ng \u0111o c\u1ea3 th\u00e0nh nang.",
             "\u0110o tr\u00ean m\u1eb7t c\u1eaft l\u1edbn nh\u1ea5t c\u1ee7a nang (\u0111i qua trung t\u00e2m).",
             "Nang tr\u00f2n \u0111\u1ec1u: \u0111o m\u1ed9t \u0111\u01b0\u1eddng k\u00ednh.",
             "Nang kh\u00f4ng tr\u00f2n (b\u1ea7u d\u1ee5c): \u0111o hai \u0111\u01b0\u1eddng k\u00ednh vu\u00f4ng g\u00f3c, l\u1ea5y TRUNG B\u00ccNH."]),

    content("Ph\u00e2n nh\u00f3m k\u00edch th\u01b0\u1edbc nang",
            ["Nh\u1ecf (<10 mm): \u0111ang ph\u00e1t tri\u1ec3n, c\u1ea7n th\u00eam th\u1eddi gian.",
             "Trung b\u00ecnh (10-13 mm): s\u1ebd \u0111\u00f3ng g\u00f3p v\u00e0o \u0111o\u00e0n h\u1ec7 n\u1ebfu c\u00f2n th\u1eddi gian.",
             "G\u1ea7n tr\u01b0\u1edfng th\u00e0nh (14-16 mm): kh\u1ea3 n\u0103ng cao c\u00f3 no\u00e3n.",
             "Tr\u01b0\u1edfng th\u00e0nh (17-18 mm): s\u1eb5n s\u00e0ng trigger.",
             "Qu\u00e1 l\u1edbn (>18 mm, \u0111\u1eb7c bi\u1ec7t >24 mm): nguy c\u01a1 no\u00e3n gi\u00e0 ho\u1eb7c m\u1ea5t no\u00e3n."]),

    content("T\u1ed1c \u0111\u1ed9 ph\u00e1t tri\u1ec3n nang",
            ["Trung b\u00ecnh: 1-2 mm/ng\u00e0y.",
             "C\u00f3 th\u1ec3 t\u0103ng nhanh h\u01a1n \u1edf giai \u0111o\u1ea1n cu\u1ed1i (2-3 mm/ng\u00e0y).",
             "Cohort ch\u1eadm (<1 mm/ng\u00e0y): xem x\u00e9t t\u0103ng li\u1ec1u (trong gi\u1edbi h\u1ea1n) ho\u1eb7c ki\u1ec3m tra tu\u00e2n th\u1ee7.",
             "Cohort nhanh b\u1ea5t th\u01b0\u1eddng (>3 mm/ng\u00e0y): c\u1ea3nh gi\u00e1c high response, \u0111\u1eb7c bi\u1ec7t PCOS."]),

    content("V\u00f9ng k\u1ef3 v\u1ecdng no\u00e3n 14-24 mm",
            ["Nhi\u1ec1u th\u1ef1c h\u00e0nh xem nh\u00f3m 14-24 mm l\u00e0 nh\u00f3m c\u00f3 kh\u1ea3 n\u0103ng \u0111\u00f3ng g\u00f3p no\u00e3n t\u1ed1t nh\u1ea5t.",
             "T\u1ef7 l\u1ec7 thu h\u1ed3i no\u00e3n t\u1eeb nh\u00f3m n\u00e0y kho\u1ea3ng 70-90%.",
             "Nang <14 mm: c\u00f3 th\u1ec3 b\u1eaft k\u1ecbp n\u1ebfu c\u00f2n 2-3 ng\u00e0y.",
             "Nang >24 mm: t\u1ef7 l\u1ec7 thu h\u1ed3i GI\u1ea2M r\u00f5.",
             "C\u00f3 th\u1ec3 th\u1ea5y g\u00f2 no\u00e3n (cumulus) \u1edf nang g\u1ea7n tr\u01b0\u1edfng th\u00e0nh: d\u1ea5u hi\u1ec7u t\u1ed1t cho trigger."]),

    content("PCOS v\u00e0 sai s\u1ed1 \u0111\u1ebfm",
            ["PCOS c\u00f3 th\u1ec3 c\u00f3 20-40+ nang nh\u1ecf m\u1ed7i b\u00ean.",
             "Nguy c\u01a1: b\u1ecf s\u00f3t nang nh\u1ecf (2-5 mm), \u0111\u1ebfm l\u1eb7p do nhi\u1ec1u nang s\u00e1t nhau.",
             "K\u1ef9 thu\u1eadt: qu\u00e9t ch\u1eadm, chia bu\u1ed3ng tr\u1ee9ng th\u00e0nh c\u00e1c v\u00f9ng.",
             "3D ultrasound gi\u00fap \u0111\u1ebfm t\u1ef1 \u0111\u1ed9ng v\u00e0 t\u00f4 m\u00e0u theo k\u00edch th\u01b0\u1edbc, nh\u01b0ng chi ph\u00ed cao.",
             "Sau ng\u00e0y 5-6: t\u1eadp trung v\u00e0o nang \u0111ang ph\u00e1t tri\u1ec3n thay v\u00ec \u0111\u1ebfm t\u1ea5t c\u1ea3 nang nh\u1ecf."]),

    # ═══ 6. NIÊM MẠC TỬ CUNG ═══
    sec("6", "Ni\u00eam m\u1ea1c t\u1eed cung trong chu k\u1ef3 KTBT", "\u0110o \u0111\u00fang, \u0111\u1ecdc h\u00ecnh th\u00e1i, quy\u1ebft \u0111\u1ecbnh fresh/freeze"),

    content("K\u1ef9 thu\u1eadt \u0111o ni\u00eam m\u1ea1c",
            ["M\u1eb7t c\u1eaft d\u1ecdc t\u1eed cung (sagittal).",
             "\u0110o \u1edf v\u1ecb tr\u00ed D\u00c0Y NH\u1ea4T.",
             "\u0110\u1eb7t caliper t\u1ea1i ranh gi\u1edbi ni\u00eam m\u1ea1c \u2013 c\u01a1 t\u1eed cung.",
             "\u0110o VU\u00d4NG G\u00d3C v\u1edbi \u0111\u01b0\u1eddng ni\u00eam m\u1ea1c.",
             "Kh\u00f4ng t\u00ednh d\u1ecbch l\u00f2ng t\u1eed cung (n\u1ebfu c\u00f3)."]),

    content("H\u00ecnh th\u00e1i ni\u00eam m\u1ea1c t\u1eed cung",
            ["D\u1ea1ng 1 \u2014 Ba l\u00e1 (trilaminar): 3 \u0111\u01b0\u1eddng t\u0103ng \u00e2m + 2 v\u00f9ng gi\u1ea3m \u00e2m. THU\u1eacN L\u1ee2I NH\u1ea4T cho l\u00e0m t\u1ed5.",
             "D\u1ea1ng 2 \u2014 T\u0103ng \u00e2m to\u00e0n b\u1ed9: t\u0103ng \u00e2m \u0111\u1ed3ng nh\u1ea5t, kh\u00f4ng c\u00f2n v\u00f9ng gi\u1ea3m \u00e2m. K\u00e9m thu\u1eadn l\u1ee3i, c\u00f3 th\u1ec3 do P4 t\u0103ng s\u1edbm.",
             "D\u1ea1ng 3 \u2014 Trung gian: c\u00f2n \u0111\u01b0\u1eddng t\u0103ng \u00e2m nh\u01b0ng ph\u00e2n l\u1edbp kh\u00f4ng r\u00f5.",]),

    content("Khi n\u00e0o ni\u00eam m\u1ea1c \u1ea3nh h\u01b0\u1edfng quy\u1ebft \u0111\u1ecbnh?",
            ["KH\u00d4NG c\u1ea7n \u0111o n\u1ed9i m\u1ea1c m\u1ed7i l\u1ea7n si\u00eau \u00e2m.",
             "\u0110o c\u00f3 \u00fd ngh\u0129a nh\u1ea5t v\u00e0o NG\u00c0Y TRIGGER ho\u1eb7c 1-2 ng\u00e0y tr\u01b0\u1edbc trigger.",
             "<7 mm th\u01b0\u1eddng \u0111\u01b0\u1ee3c xem l\u00e0 m\u1ecfng.",
             "D\u1ea1ng 2 + progesterone t\u0103ng s\u1edbm \u2192 c\u00e2n nh\u1eafc \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9.",
             "ESHRE 2025: \u0111o progesterone v\u00e0o ng\u00e0y trigger cho chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i cycle (conditional).",
             "Progesterone >1.5 ng/mL ng\u00e0y trigger \u2192 gi\u1ea3m c\u01a1 h\u1ed9i l\u00e0m t\u1ed5 n\u1ebfu chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i."]),

    # ═══ 7. NỘI TIẾT TRONG THEO DÕI ═══
    sec("7", "Vai tr\u00f2 x\u00e9t nghi\u1ec7m n\u1ed9i ti\u1ebft", "Hormone ch\u1ec9 h\u1eefu \u00edch khi l\u00e0m thay \u0111\u1ed5i quy\u1ebft \u0111\u1ecbnh"),

    content("Nguy\u00ean t\u1eafc v\u00e0ng",
            ["Si\u00eau \u00e2m l\u00e0 tr\u1ee5c ch\u00ednh. X\u00e9t nghi\u1ec7m n\u1ed9i ti\u1ebft l\u00e0 c\u00f4ng c\u1ee5 B\u1ed4 SUNG.",
             "Tr\u01b0\u1edbc khi ch\u1ec9 \u0111\u1ecbnh x\u00e9t nghi\u1ec7m: K\u1ebft qu\u1ea3 n\u00e0y c\u00f3 th\u1ec3 l\u00e0m t\u00f4i THAY \u0110\u1ed4I K\u1ebe HO\u1ea0CH h\u00f4m nay kh\u00f4ng?",
             "N\u1ebfu KH\u00d4NG \u2192 kh\u00f4ng l\u00e0m."]),

    content("E2 (Estradiol)",
            ["H\u1eefu \u00edch: nghi high response/OHSS; PCOS c\u1ea7n \u0111\u00e1nh gi\u00e1 nguy c\u01a1; \u0111\u00e1p \u1ee9ng si\u00eau \u00e2m kh\u00f4ng t\u01b0\u01a1ng x\u1ee9ng.",
             "Kh\u00f4ng c\u1ea7n: b\u1ec7nh nh\u00e2n \u0111\u00e1p \u1ee9ng \u0111i\u1ec3n h\u00ecnh, nguy c\u01a1 th\u1ea5p, si\u00eau \u00e2m r\u00f5 r\u00e0ng.",
             "E2 \u0111\u01a1n \u0111\u1ed9c kh\u00f4ng thay th\u1ebf \u0111\u01b0\u1ee3c \u0111\u1ebfm nang."]),

    content("LH v\u00e0 Progesterone",
            ["LH: h\u1eefu \u00edch khi nghi LH surge (flexible antagonist qu\u00ean d\u00f9ng, t\u00e1i kh\u00e1m tr\u1ec5, nang l\u1edbn nhanh).",
             "LH: kh\u00f4ng c\u1ea7n \u1edf fixed antagonist ho\u1eb7c long agonist.",
             "Progesterone: h\u1eefu \u00edch tr\u01b0\u1edbc trigger \u1edf chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i cycle (ESHRE 2025 conditional).",
             "Progesterone >1.5 ng/mL ng\u00e0y trigger: c\u00e2n nh\u1eafc \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9.",
             "Progesterone: kh\u00f4ng c\u00f3 \u00fd ngh\u0129a trong \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9 cycle."]),

    # ═══ 8. CÁC ĐIỂM QUYẾT ĐỊNH ═══
    sec("8", "C\u00e1c \u0111i\u1ec3m quy\u1ebft \u0111\u1ecbnh", "Decision 1-4: li\u1ec1u, \u0111\u1ed1i v\u1eadn, tr\u01b0\u1edfng th\u00e0nh no\u00e3n, lo\u1ea1i tr\u01b0\u1edfng th\u00e0nh no\u00e3n"),

    content("Quy\u1ebft \u0111\u1ecbnh 1 \u2014 Gi\u1eef hay \u0111\u1ed5i li\u1ec1u FSH?",
            ["Cohort \u0111\u1ec1u, t\u1ed1c \u0111\u1ed9 1-2 mm/ng\u00e0y, ng\u00e0y 5-6 c\u00f3 5-12 nang: GI\u1eee NGUY\u00caN li\u1ec1u.",
             "Cohort ch\u1eadm, <3 nang >10 mm ng\u00e0y 7, t\u1ed1c \u0111\u1ed9 <1 mm/ng\u00e0y: xem x\u00e9t T\u0102NG li\u1ec1u nh\u1eb9 (\u226475 IU).",
             "Cohort nhanh, >15 nang >10 mm ng\u00e0y 6, t\u1ed1c \u0111\u1ed9 >2.5 mm/ng\u00e0y: GI\u1ea2M li\u1ec1u, c\u1ea3nh gi\u00e1c OHSS.",
             "L\u01b0u \u00fd: ESHRE 2025 kh\u00f4ng khuy\u1ebfn c\u00e1o \u0111i\u1ec1u ch\u1ec9nh li\u1ec1u gi\u1eefa chu k\u1ef3 TH\u01af\u1edcNG QUY."]),

    yesno("Quy\u1ebft \u0111\u1ecbnh 2 \u2014 B\u1eaft \u0111\u1ea7u \u0111\u1ed1i v\u1eadn?",
          "Nang l\u1edbn nh\u1ea5t \u226514 mm ho\u1eb7c \u0111\u1ebfn ng\u00e0y 7 KTBT?",
          ["B\u1eaft \u0111\u1ea7u antagonist theo ti\u00eau ch\u00ed trung t\u00e2m", "N\u1ebfu nang 14 mm s\u1edbm: b\u1eaft ngay"],
          ["Theo d\u00f5i ti\u1ebfp", "N\u1ebfu \u0111\u1ebfn ng\u00e0y 7 v\u1eabn <14 mm: v\u1eabn b\u1eaft \u0111\u1ec3 an to\u00e0n"]),

    content("Quy\u1ebft \u0111\u1ecbnh 3 \u2014 Khi n\u00e0o tr\u01b0\u1edfng th\u00e0nh no\u00e3n?",
            ["Ti\u00eau chu\u1ea9n th\u1ef1c h\u00e0nh: \u22653 nang \u226517 mm HO\u1eb6C \u22652 nang \u226518 mm. T\u1ed1i thi\u1ec3u 1/2 \u0111o\u00e0n h\u1ec7 \u226514 mm.",
             "Trigger l\u00e0 quy\u1ebft \u0111\u1ecbnh d\u1ef1a tr\u00ean TO\u00c0N B\u1ed8 COHORT.",
             "N\u1ebfu nhi\u1ec1u nang 14-16 mm s\u1eafp b\u1eaft k\u1ecbp: c\u00f3 th\u1ec3 \u0111\u1ee3i th\u00eam 1 ng\u00e0y.",
             "N\u1ebfu nhi\u1ec1u nang >22-24 mm: kh\u00f4ng tr\u00ec ho\u00e3n ch\u1ec9 \u0111\u1ec3 ch\u1edd nang nh\u1ecf.",
             "Nguy c\u01a1 OHSS cao: trigger s\u1edbm h\u01a1n l\u00e0 mu\u1ed9n h\u01a1n.",
             "Progesterone b\u1eaft \u0111\u1ea7u t\u0103ng: kh\u00f4ng tr\u00ec ho\u00e3n \u0111\u1ec3 ch\u1edd chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i.",
             "Sau trigger 34-36 gi\u1edd: ch\u1ecdc h\u00fat no\u00e3n qua \u0111\u01b0\u1eddng \u00e2m \u0111\u1ea1o."]),

    checklist("Trigger checklist",
              ["S\u1ed1 nang theo nh\u00f3m k\u00edch th\u01b0\u1edbc \u0111\u00e3 \u0111\u1ee7?",
               "C\u00f3 bao nhi\u00eau nang nguy c\u01a1 OHSS?",
               "N\u1ed9i m\u1ea1c v\u00e0 progesterone c\u00f2n ph\u00f9 h\u1ee3p chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i?",
               "Chu k\u1ef3 antagonist c\u00f3 th\u1ec3 d\u00f9ng agonist trigger?",
               "Gi\u1edd ch\u1ecdc h\u00fat 34-36h sau trigger \u0111\u00e3 l\u00ean l\u1ecbch?",
               "K\u1ebf ho\u1ea1ch h\u1ed7 tr\u1ee3 ho\u00e0ng th\u1ec3 \u0111\u00e3 r\u00f5?"]),

    twocol("Quy\u1ebft \u0111\u1ecbnh 4 \u2014 Ch\u1ecdn lo\u1ea1i tr\u01b0\u1edfng th\u00e0nh no\u00e3n n\u00e0o?",
           "hCG trigger", ["nguy c\u01a1 qu\u00e1 k\u00edch th\u1ea5p", "C\u1ea3 antagonist v\u00e0 long agonist", "Li\u1ec1u 5.000-10.000 IU", "Fresh ET \u0111\u01b0\u1ee3c"],
           "GnRH agonist trigger", ["nguy c\u01a1 qu\u00e1 k\u00edch cao", "CH\u1ec8 antagonist protocol", "Lu\u00f4n \u0111i k\u00e8m \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9", "Kho\u1ea3ng c\u00e1ch antagonist-trigger >10h", "Nguy c\u01a1 th\u1ea5t b\u1ea1i tr\u01b0\u1edfng th\u00e0nh no\u00e3n"]),

    # ═══ 9. PCOS / ĐÁP ỨNG CAO ═══
    sec("9", "PCOS / \u0110\u00e1p \u1ee9ng cao", "Chi\u1ebfn l\u01b0\u1ee3c theo d\u00f5i v\u00e0 ph\u00f2ng OHSS"),

    content("\u0110\u1eb7c \u0111i\u1ec3m si\u00eau \u00e2m c\u1ee7a PCOS / \u0111\u00e1p \u1ee9ng cao",
            ["AFC cao (>20-24 m\u1ed7i b\u00ean).",
             "Nhi\u1ec1u nang nh\u1ecf 2-5 mm d\u1ea1ng chu\u1ed7i h\u1ea1t ngo\u1ea1i vi.",
             "Th\u1ec3 t\u00edch bu\u1ed3ng tr\u1ee9ng >10 mL m\u1ed7i b\u00ean.",
             "Khi KTBT: nhi\u1ec1u nang nh\u1ecf ph\u00e1t tri\u1ec3n \u0111\u1ed3ng lo\u1ea1t \u2192 nguy c\u01a1 OHSS cao."]),

    content("Chi\u1ebfn l\u01b0\u1ee3c theo d\u00f5i \u1edf \u0111\u00e1p \u1ee9ng cao",
            ["Ch\u1ecdn antagonist protocol (\u01b0u ti\u00ean).",
             "Li\u1ec1u FSH kh\u1edfi \u0111\u1ea7u TH\u1ea4P: 100-150 IU/ng\u00e0y.",
             "Theo d\u00f5i si\u00eau \u00e2m S\u00c1T: ng\u00e0y 5-6, sau \u0111\u00f3 m\u1ed7i 1-2 ng\u00e0y.",
             "E2 c\u00f3 th\u1ec3 h\u1eefu \u00edch nh\u01b0ng kh\u00f4ng b\u1eaft bu\u1ed9c.",
             "\u0110\u1ebfm nang kh\u00f3 h\u01a1n: d\u1ec5 b\u1ecf s\u00f3t ho\u1eb7c \u0111\u1ebfm l\u1eb7p. C\u1ea7n qu\u00e9t c\u00f3 h\u1ec7 th\u1ed1ng."]),

    content("Ph\u00f2ng OHSS \u1edf \u0111\u00e1p \u1ee9ng cao",
            ["Antagonist protocol (kh\u00f4ng d\u00f9ng long agonist).",
             "GnRH agonist trigger thay hCG \u2192 gi\u1ea3m OHSS g\u1ea7n nh\u01b0 tuy\u1ec7t \u0111\u1ed1i.",
             "Freeze-all (kh\u00f4ng chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i).",
             "Cabergoline 0.5 mg/ng\u00e0y x 8 ng\u00e0y t\u1eeb ng\u00e0y trigger (gi\u1ea3m VEGF).",
             "Coasting: ng\u1eebng FSH 1-2 ng\u00e0y tr\u01b0\u1edbc trigger n\u1ebfu E2 qu\u00e1 cao.",
             "Gi\u1ea3m li\u1ec1u hCG (3.000-5.000 IU) n\u1ebfu b\u1eaft bu\u1ed9c d\u00f9ng hCG."]),

    # ═══ 10. ĐÁP ỨNG THẤP ═══
    sec("10", "\u0110\u00e1p \u1ee9ng th\u1ea5p", "Low responder \u2014 ph\u00e2n bi\u1ec7t v\u00e0 chi\u1ebfn l\u01b0\u1ee3c"),

    content("Ph\u00e2n bi\u1ec7t tr\u00ean si\u00eau \u00e2m",
            ["AFC th\u1ea5p \u1edf tr\u01b0\u1edbc k\u00edch th\u00edch.",
             "S\u1ed1 nang ph\u00e1t tri\u1ec3n \u00edt (<4-5 nang), t\u1ed1c \u0111\u1ed9 c\u00f3 th\u1ec3 ch\u1eadm.",
             "Bu\u1ed3ng tr\u1ee9ng nh\u1ecf, kh\u00f3 quan s\u00e1t.",
             "C\u1ea7n ph\u00e2n bi\u1ec7t: d\u1ef1 tr\u1eef th\u1ea5p th\u1eadt s\u1ef1 (AFC <5, AMH th\u1ea5p) hay hypo-response (AFC b\u00ecnh th\u01b0\u1eddng nh\u01b0ng \u0111\u00e1p \u1ee9ng k\u00e9m)."]),

    content("Chi\u1ebfn l\u01b0\u1ee3c theo d\u00f5i \u1edf \u0111\u00e1p \u1ee9ng th\u1ea5p",
            ["Si\u00eau \u00e2m tr\u01b0\u1edbc k\u00edch th\u00edch k\u1ef9: AFC, v\u1ecb tr\u00ed bu\u1ed3ng tr\u1ee9ng (c\u00f3 th\u1ec3 kh\u00f3 ch\u1ecdc h\u00fat).",
             "Theo d\u00f5i kh\u00f4ng c\u1ea7n qu\u00e1 d\u00e0y (m\u1ed7i 2-3 ng\u00e0y).",
             "M\u1ee5c ti\u00eau: kh\u00f4ng b\u1ecf l\u1ee1 trigger (v\u00e0i nang l\u1edbn c\u00f3 th\u1ec3 gi\u00e0 trong khi ch\u1edd nang nh\u1ecf).",
             "C\u00e2n nh\u1eafc \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9 v\u00e0 t\u00edch l\u0169y ph\u00f4i qua nhi\u1ec1u chu k\u1ef3 (oocyte/embryo accumulation)."]),

    content("T\u01b0 v\u1ea5n \u1edf \u0111\u00e1p \u1ee9ng th\u1ea5p",
            ["AMH/AFC th\u1ea5p d\u1ef1 b\u00e1o \u00edt no\u00e3n, nh\u01b0ng KH\u00d4NG d\u1ef1 b\u00e1o tr\u1ef1c ti\u1ebfp live birth n\u1ebfu t\u00e1ch kh\u1ecfi tu\u1ed5i.",
             "B\u1ec7nh nh\u00e2n tr\u1ebb v\u1edbi AFC th\u1ea5p c\u00f3 ti\u00ean l\u01b0\u1ee3ng T\u1ed0T H\u01a0N b\u1ec7nh nh\u00e2n l\u1edbn tu\u1ed5i v\u1edbi c\u00f9ng AFC.",
             "S\u1ed1 no\u00e3n m\u1ee5c ti\u00eau kh\u00f4ng nh\u1ea5t thi\u1ebft l\u00e0 15 \u2014 3-5 no\u00e3n ch\u1ea5t l\u01b0\u1ee3ng t\u1ed1t v\u1eabn c\u00f3 gi\u00e1 tr\u1ecb.",
             "ESHRE 2025: KH\u00d4NG khuy\u1ebfn c\u00e1o >300 IU/ng\u00e0y cho \u0111\u00e1p \u1ee9ng th\u1ea5p (strong)."]),

    # ═══ 11. NHẬN DIỆN OHSS ═══
    sec("11", "Nh\u1eadn di\u1ec7n OHSS tr\u00ean si\u00eau \u00e2m", "D\u1ea5u hi\u1ec7u s\u1edbm \u2192 n\u1eb7ng, ph\u00e2n lo\u1ea1i"),

    content("D\u1ea5u hi\u1ec7u s\u1edbm (tr\u01b0\u1edbc trigger)",
            ["Bu\u1ed3ng tr\u1ee9ng to nhanh (>8 cm m\u1ed7i b\u00ean).",
             ">20 nang \u0111ang ph\u00e1t tri\u1ec3n, nhi\u1ec1u nang k\u00edch th\u01b0\u1edbc trung b\u00ecnh (10-16 mm).",
             "D\u1ecbch t\u1ef1 do t\u00fai c\u00f9ng Douglas (\u00edt, m\u1ee9c \u0111\u1ed9 nh\u1eb9)."]),

    content("D\u1ea5u hi\u1ec7u r\u00f5 (sau trigger 3-7 ng\u00e0y)",
            ["Bu\u1ed3ng tr\u1ee9ng r\u1ea5t to (>10-12 cm), nhi\u1ec1u nang ho\u00e0ng th\u1ec3 h\u00f3a.",
             "D\u1ecbch t\u1ef1 do \u1ed5 b\u1ee5ng l\u01b0\u1ee3ng nhi\u1ec1u (ascites).",
             "C\u00f3 th\u1ec3 c\u00f3 d\u1ecbch m\u00e0ng ph\u1ed5i (pleural effusion)."]),

    content("Ph\u00e2n lo\u1ea1i OHSS nhanh tr\u00ean si\u00eau \u00e2m",
            ["Nh\u1eb9: bu\u1ed3ng tr\u1ee9ng <8 cm, d\u1ecbch t\u1ef1 do \u00edt ho\u1eb7c kh\u00f4ng c\u00f3.",
             "Trung b\u00ecnh: bu\u1ed3ng tr\u1ee9ng 8-12 cm, ascites v\u1eeba.",
             "N\u1eb7ng: bu\u1ed3ng tr\u1ee9ng >12 cm, ascites c\u0103ng, c\u00f3 th\u1ec3 tr\u00e0n d\u1ecbch m\u00e0ng ph\u1ed5i.",
             "(Xem b\u00e0i OHSS Comprehensive \u0111\u1ec3 ph\u00e2n lo\u1ea1i \u0111\u1ea7y \u0111\u1ee7 Golan, RCOG, ASRM 2024.)"]),

    # ═══ 12. FREEZE-ALL ═══
    sec("12", "Freeze-all d\u1ef1a tr\u00ean si\u00eau \u00e2m", "Khi n\u00e0o \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9, khi n\u00e0o chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i?"),

    content("Ra quy\u1ebft \u0111\u1ecbnh \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9 d\u1ef1a tr\u00ean si\u00eau \u00e2m",
            [">20 nang ph\u00e1t tri\u1ec3n, bu\u1ed3ng tr\u1ee9ng >8 cm \u2192 Freeze-all (nguy c\u01a1 qu\u00e1 k\u00edch cao).",
             "Ni\u00eam m\u1ea1c <7 mm ho\u1eb7c d\u1ea1ng 2 ng\u00e0y trigger \u2192 C\u00e2n nh\u1eafc \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9.",
             "Polyp, u x\u01a1 d\u01b0\u1edbi ni\u00eam, d\u1ecbch l\u00f2ng TC m\u1edbi \u2192 Freeze-all.",
             "\u0110\u00e3 d\u00f9ng GnRH agonist trigger \u2192 Freeze-all (tr\u1eeb khi c\u00f3 h\u1ed7 tr\u1ee3 ho\u00e0ng th\u1ec3 \u0111\u1eb7c bi\u1ec7t).",
             "PPOS / Random start \u2192 Freeze-all B\u1eaeT BU\u1ed8C.",
             "P4 >1.5 ng/mL + n\u1ed9i m\u1ea1c d\u1ea1ng 2 \u2192 Freeze-all.",
             "\u0110\u00e1p \u1ee9ng \u0111i\u1ec3n h\u00ecnh, n\u1ed9i m\u1ea1c ba l\u00e1, kh\u00f4ng OHSS \u2192 C\u00f3 th\u1ec3 chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i."]),

    content("T\u01b0 v\u1ea5n b\u1ec7nh nh\u00e2n v\u1ec1 \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9",
            ["Freeze-all KH\u00d4NG c\u00f3 ngh\u0129a l\u00e0 chu k\u1ef3 th\u1ea5t b\u1ea1i.",
             "Vitrification: t\u1ef7 l\u1ec7 s\u1ed1ng sau r\u00e3 \u0111\u00f4ng >95% \u1edf h\u1ea7u h\u1ebft trung t\u00e2m t\u1ed1t.",
             "Chuy\u1ec3n ph\u00f4i chu k\u1ef3 sau v\u1edbi n\u1ed9i m\u1ea1c \u0111\u01b0\u1ee3c chu\u1ea9n b\u1ecb c\u00f3 th\u1ec3 cho t\u1ef7 l\u1ec7 l\u00e0m t\u1ed5 t\u01b0\u01a1ng \u0111\u01b0\u01a1ng ho\u1eb7c t\u1ed1t h\u01a1n chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i."]),

    # ═══ 13. MẪU PHIẾU & CHECKLIST ═══
    sec("13", "M\u1eabu phi\u1ebfu si\u00eau \u00e2m & checklist", "C\u00f4ng c\u1ee5 th\u1ef1c h\u00e0nh h\u00e0ng ng\u00e0y"),

    checklist("Checklist tr\u01b0\u1edbc khi r\u1eddi ph\u00f2ng si\u00eau \u00e2m",
              ["H\u00f4m nay l\u00e0 ng\u00e0y th\u1ee9 m\u1ea5y d\u00f9ng FSH?",
               "T\u1ed1c \u0111\u1ed9 t\u0103ng tr\u01b0\u1edfng nang c\u00f3 ph\u00f9 h\u1ee3p kh\u00f4ng? (so v\u1edbi l\u1ea7n tr\u01b0\u1edbc)",
               "\u0110\u00e3 \u0111\u1ebfn l\u00fac b\u1eaft \u0111\u1ea7u antagonist ch\u01b0a? (v\u1edbi flexible)",
               "C\u00f3 d\u1ea5u hi\u1ec7u OHSS kh\u00f4ng?",
               "C\u00f3 d\u1ea5u hi\u1ec7u LH surge kh\u00f4ng? (P4 t\u0103ng, n\u1ed9i m\u1ea1c thay \u0111\u1ed5i s\u1edbm)",
               "Li\u1ec1u FSH c\u00f3 c\u1ea7n thay \u0111\u1ed5i kh\u00f4ng?",
               "Ng\u00e0y h\u1eb9n ti\u1ebfp theo l\u00e0 khi n\u00e0o?",
               "B\u1ec7nh nh\u00e2n c\u00f3 hi\u1ec3u k\u1ebf ho\u1ea1ch kh\u00f4ng?"]),

    # ═══ 14. ATLAS CA LÂM SÀNG ═══
    sec("14", "Atlas ca l\u00e2m s\u00e0ng", "8 ca \u0111i\u1ec3n h\u00ecnh t\u1eeb th\u1ef1c h\u00e0nh"),

    content("Ca 1 \u2014 AFC th\u1ea5p, \u0111\u00e1p \u1ee9ng ch\u1eadm",
            ["B\u1ec7nh nh\u00e2n 39 tu\u1ed5i, AFC = 4, AMH = 0.6 ng/mL.",
             "Ng\u00e0y 7 FSH 300 IU: 2 nang 11-12 mm, 1 nang 9 mm.",
             "\u2192 Kh\u00f4ng t\u0103ng li\u1ec1u th\u00eam. Ti\u1ebfp t\u1ee5c 300 IU. Si\u00eau \u00e2m l\u1ea1i sau 2 ng\u00e0y.",
             "T\u01b0 v\u1ea5n: c\u00f3 th\u1ec3 ch\u1ec9 thu 2-3 no\u00e3n. B\u00e0n v\u1ec1 oocyte accumulation ho\u1eb7c no\u00e3n hi\u1ebfn."]),

    content("Ca 2 \u2014 PCOS, \u0111\u00e1p \u1ee9ng m\u1ea1nh",
            ["B\u1ec7nh nh\u00e2n 28 tu\u1ed5i, PCOS, AFC >30 m\u1ed7i b\u00ean.",
             "FSH 125 IU/ng\u00e0y, antagonist fixed. Ng\u00e0y 6: >20 nang 6-10 mm m\u1ed7i b\u00ean.",
             "\u2192 Ti\u1ebfp t\u1ee5c li\u1ec1u th\u1ea5p. Theo d\u00f5i S\u00c1T m\u1ed7i 1-2 ng\u00e0y.",
             "L\u00ean k\u1ebf ho\u1ea1ch GnRH agonist trigger + \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9. An to\u00e0n l\u00e0 \u01b0u ti\u00ean s\u1ed1 m\u1ed9t."]),

    content("Ca 3 \u2014 Flexible antagonist, nang 14 mm",
            ["B\u1ec7nh nh\u00e2n 33 tu\u1ed5i, antagonist flexible.",
             "Ng\u00e0y 6 FSH: nang l\u1edbn nh\u1ea5t 14.5 mm, c\u00f3 5 nang 12-13 mm.",
             "\u2192 B\u1eaft \u0111\u1ea7u antagonist NGAY h\u00f4m nay. Ti\u1ebfp t\u1ee5c FSH li\u1ec1u hi\u1ec7n t\u1ea1i. SA l\u1ea1i sau 2 ng\u00e0y."]),

    content("Ca 4 \u2014 Nang l\u1ec7ch pha",
            ["B\u1ec7nh nh\u00e2n 35 tu\u1ed5i. Ng\u00e0y 9 FSH: 2 nang 22-23 mm, 5 nang 13-14 mm, 4 nang 10-11 mm.",
             "Kh\u00f3: nang l\u1edbn \u0111\u00e3 s\u1eb5n s\u00e0ng nh\u01b0ng h\u1ea7u h\u1ebft \u0111o\u00e0n h\u1ec7 c\u00f2n nh\u1ecf.",
             "N\u1ebfu P4 c\u00f2n th\u1ea5p \u2192 c\u00f3 th\u1ec3 \u0111\u1ee3i 1 ng\u00e0y cho nh\u00f3m 10-11 mm.",
             "N\u1ebfu P4 \u0111\u00e3 t\u0103ng \u2192 trigger ngay. Nh\u00f3m l\u1edbn s\u1ebd >24 mm n\u1ebfu \u0111\u1ee3i."]),

    content("Ca 5 \u2014 Progesterone t\u0103ng ng\u00e0y trigger",
            ["B\u1ec7nh nh\u00e2n 31 tu\u1ed5i, \u0111\u00e1p \u1ee9ng t\u1ed1t.",
             "Ng\u00e0y trigger: 12 nang 16-20 mm, n\u1ed9i m\u1ea1c 10 mm d\u1ea1ng 2, P4 = 2.1 ng/mL.",
             "\u2192 \u0110\u00e3 c\u00f3 l\u1ec7ch pha n\u1ed9i m\u1ea1c. D\u00f9 nang \u0111\u1eb9p, chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i kh\u1ea3 n\u0103ng th\u1ea5p.",
             "T\u01b0 v\u1ea5n \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9. Trigger b\u00ecnh th\u01b0\u1eddng, ch\u1ecdc h\u00fat, \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9."]),

    content("Ca 6 \u2014 Bu\u1ed3ng tr\u1ee9ng kh\u00f3 ti\u1ebfp c\u1eadn",
            ["B\u1ec7nh nh\u00e2n 34 tu\u1ed5i, ti\u1ec1n s\u1eed m\u1ed5 b\u00f3c endometrioma bu\u1ed3ng tr\u1ee9ng tr\u00e1i.",
             "Si\u00eau \u00e2m: bu\u1ed3ng tr\u1ee9ng tr\u00e1i n\u1eb1m sau t\u1eed cung, c\u00e1ch \u0111\u1ea7u d\u00f2 ~4 cm, c\u00f3 quai ru\u1ed9t xen gi\u1eefa.",
             "\u2192 Ghi r\u00f5 v\u1ecb tr\u00ed, kho\u1ea3ng c\u00e1ch, v\u1eadt c\u1ea3n. B\u00e1o tr\u01b0\u1edbc ekip ch\u1ecdc h\u00fat.",
             "C\u00f3 th\u1ec3 c\u1ea7n \u1ea5n b\u1ee5ng/thay \u0111\u1ed5i t\u01b0 th\u1ebf. Kh\u00f4ng h\u1ee7y chu k\u1ef3 v\u00ec access kh\u00f3."]),

    content("Ca 7 \u2014 Nang t\u1ed3n d\u01b0 tr\u01b0\u1edbc k\u00edch th\u00edch",
            ["B\u1ec7nh nh\u00e2n 29 tu\u1ed5i. Baseline: AFC = 12, c\u00f3 1 nang \u0111\u01a1n thu\u1ea7n 22 mm bu\u1ed3ng tr\u1ee9ng ph\u1ea3i.",
             "N\u1ebfu E2 v\u00e0 P4 th\u1ea5p \u2192 nang kh\u00f4ng ho\u1ea1t \u0111\u1ed9ng. C\u00f3 th\u1ec3 b\u1eaft \u0111\u1ea7u KTBT.",
             "N\u1ebfu E2 t\u0103ng \u2192 nang ho\u1ea1t \u0111\u1ed9ng: ch\u1ecdc h\u00fat ho\u1eb7c d\u00f9ng COCP 7-10 ng\u00e0y.",
             "N\u1ebfu c\u00f3 ch\u1ec9 \u0111\u1ecbnh g\u1ea5p (b\u1ea3o t\u1ed3n sinh s\u1ea3n): ch\u1ecdc h\u00fat nang r\u1ed3i b\u1eaft \u0111\u1ea7u FSH."]),

    content("Ca 8 \u2014 Nghi th\u1ea5t b\u1ea1i tr\u01b0\u1edfng th\u00e0nh no\u00e3n sau GnRHa",
            ["B\u1ec7nh nh\u00e2n antagonist cycle, GnRHa trigger (triptorelin 0.2 mg).",
             "Sau trigger 12h: LH <15 IU/L (n\u1ebfu x\u00e9t nghi\u1ec7m).",
             "\u2192 Nghi th\u1ea5t b\u1ea1i tr\u01b0\u1edfng th\u00e0nh no\u00e3n.",
             "\u0110o LH sau trigger 8-12h. N\u1ebfu LH kh\u00f4ng t\u0103ng r\u00f5: rescue b\u1eb1ng hCG 5.000-10.000 IU.",
             "Ch\u1ecdc h\u00fat theo l\u1ecbch hCG (34-36h sau m\u0169i rescue)."]),

    # ═══ 15. CLINICAL PEARLS ═══
    sec("15", "B\u00e0i h\u1ecdc l\u00e2m s\u00e0ng", "10 \u0111i\u1ec3m c\u1ed1t l\u00f5i \u0111\u1ec3 th\u1ef1c h\u00e0nh t\u1ed1t h\u01a1n"),

    content("Pearl 1-5",
            ["1. AFC kh\u00f4ng ph\u1ea3i l\u00e0 cu\u1ed9c thi \u0111\u1ebfm. \u0110\u1ed9 \u0111\u1ed3ng \u0111\u1ec1u v\u00e0 ghi nh\u1eadn bu\u1ed3ng tr\u1ee9ng kh\u00f3 ti\u1ebfp c\u1eadn quan tr\u1ecdng kh\u00f4ng k\u00e9m con s\u1ed1 AFC.",
             "2. Ng\u00e0y 5-7 l\u00e0 M\u1ed0C QUAN TR\u1eccNG NH\u1ea4T. \u0110\u00e1nh gi\u00e1 \u0111\u00e1p \u1ee9ng ban \u0111\u1ea7u v\u00e0 quy\u1ebft \u0111\u1ecbnh antagonist.",
             "3. Kh\u00f4ng tr\u00ec ho\u00e3n trigger ch\u1ec9 \u0111\u1ec3 ch\u1edd v\u00e0i nang nh\u1ecf. M\u1ea5t 2 no\u00e3n non c\u00f2n h\u01a1n h\u1ecfng c\u1ea3 chu k\u1ef3.",
             "4. PCOS: \u0111o\u00e1n tr\u01b0\u1edbc OHSS, \u0111\u1eebng \u0111\u1ee3i th\u1ea5y d\u1ecbch m\u1edbi lo. N\u1ebfu >20 nang, l\u00ean k\u1ebf ho\u1ea1ch GnRHa + \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9 t\u1eeb tr\u01b0\u1edbc.",
             "5. N\u1ed9i m\u1ea1c ch\u1ec9 c\u1ea7n \u0111o c\u00f3 \u00fd ngh\u0129a khi g\u1ea7n trigger. \u0110o m\u1ed7i l\u1ea7n g\u00e2y lo l\u1eafng kh\u00f4ng c\u1ea7n thi\u1ebft."]),

    content("Pearl 6-10",
            ["6. Fixed antagonist d\u1ec5 v\u1eadn h\u00e0nh h\u01a1n flexible. Trung t\u00e2m \u0111\u00f4ng, b\u1ec7nh nh\u00e2n kh\u00f3 t\u00e1i kh\u00e1m \u0111\u00fang h\u1eb9n \u2192 ch\u1ecdn fixed.",
             "7. Bu\u1ed3ng tr\u1ee9ng kh\u00f3 ch\u1ecdc h\u00fat: ghi ngay t\u1eeb tr\u01b0\u1edbc k\u00edch th\u00edch, c\u1eadp nh\u1eadt m\u1ed7i l\u1ea7n si\u00eau \u00e2m.",
             "8. Progesterone l\u00e0 \u0111\u00e8n v\u00e0ng cho chuy\u1ec3n ph\u00f4i t\u01b0\u01a1i. P4 >1.5 ng/mL \u2192 \u0111\u00f4ng ph\u00f4i to\u00e0n b\u1ed9 th\u01b0\u1eddng an to\u00e0n h\u01a1n.",
             "9. S\u1ed1 no\u00e3n m\u1ee5c ti\u00eau kh\u00f4ng ph\u1ea3i c\u00e0ng nhi\u1ec1u c\u00e0ng t\u1ed1t. ~15 no\u00e3n l\u00e0 t\u1ed1i \u01b0u. Tr\u00ean 20: OHSS t\u0103ng m\u00e0 live birth kh\u00f4ng t\u0103ng (PMID 21558332).",
             "10. K\u1ebft th\u00fac m\u1ed7i l\u1ea7n si\u00eau \u00e2m b\u1eb1ng m\u1ed9t K\u1ebe HO\u1ea0CH R\u00d5 R\u00c0NG. B\u1ec7nh nh\u00e2n c\u1ea7n bi\u1ebft: li\u1ec1u, ng\u00e0y h\u1eb9n, b\u01b0\u1edbc ti\u1ebfp theo."]),

    # ═══ REFERENCES ═══
    refs("T\u00e0i li\u1ec7u tham kh\u1ea3o \u0111\u00e3 verify",
         ["ESHRE guideline ovarian stimulation 2025 update. PMID: 41732035.",
          "ESHRE guideline ovarian stimulation for IVF/ICSI. PMID: 32395637.",
          "ASRM: testing and interpreting measures of ovarian reserve. PMID: 33280722.",
          "Sunkara: number of eggs and live birth in IVF (400,135 cycles). PMID: 21558332.",
          "OHSS prevention and detection consensus. PMID: 26597569.",
          "ASRM 2024: prevention of moderate and severe OHSS. PMID: 38099867.",
          "Humaidan 2011: GnRH agonist vs HCG for oocyte triggering. PMID: 21450755.",
          "HERA Delphi consensus: AMH/AFC thresholds for hyperresponse risk. PMID: 39603489."]),
]

deck = {"meta": {"title": "Si\u00eau \u00e2m theo d\u00f5i k\u00edch th\u00edch bu\u1ed3ng tr\u1ee9ng", "author": "B\u00e1c s\u0129 Ng\u1ecdc H\u01b0ng", "subtitle": "Deck h\u1ecdc c\u00e1 nh\u00e2n t\u1eeb b\u00e0i m\u1eb9 2026-07-04"}, "slides": slides}
OUT.write_text(json.dumps(deck, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {OUT} ({len(slides)} slides)")
