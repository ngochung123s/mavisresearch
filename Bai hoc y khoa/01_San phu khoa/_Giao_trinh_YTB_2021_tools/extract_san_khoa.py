"""
extract_san_khoa.py — trích lại Giáo trình Sản phụ khoa ĐHYD Thái Bình 2021 từ bản .docx (do convert_doc.py tạo).

Khác bản cũ (build_san_khoa_library.py, đọc file .txt phẳng):
  - Giải mã THEO FONT của từng run: .VnTime/.VnArial… = TCVN3, .VnTimeH/.VnArialH = TCVN3 chữ hoa,
    Symbol/Wingdings = ký hiệu (β, µ, ≤, ≥, ±, →, •). Chữ Unicode (Times New Roman) giữ nguyên
    → hết lỗi "đó→đú", "tiêm→tiờm", "phút→phỳt", "- → ư", "tuÇn lÔ thø", "β-hCG → òưhCG".
  - Giữ BẢNG (bảng Markdown), HÌNH (ảnh nén ≤150 KB, ≤1200 px), danh sách, cấp tiêu đề.
  - Tách bài theo tiêu đề đứng ngay trước "Mục tiêu" (lesson_specs.json giữ mã SK-xx/thư mục/tên file).

Xuất ra OUT_DIR: <chương>/<SK-xx_slug>.md + .json, media/SK-xx/*.jpg, index.json, CATALOG_BAI_GIANG.md,
FULL_TEXT_BOOK_UNICODE.txt, extract_report.json.
"""
from __future__ import annotations

import difflib
import io
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from PIL import Image

HERE = Path(__file__).resolve().parent
WORK = Path(r"F:\DL\san_khoa_reextract")  # bản .docx 32 MB (không đưa vào git) do convert_doc.py tạo
DOCX = WORK / "BG_SAN_KHOA_2021.docx"
# Dùng: python extract_san_khoa.py <thư mục ra>  → kiểm tra xong mới thay F:\DL\Giao_trinh_San_khoa_Y_Thai_Binh_2021,
# rồi chạy 12_Nhi khoa/build_unified_med_library.py (đưa bài + ảnh lên web).
OUT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else WORK / "out"
SPECS = json.loads((HERE / "lesson_specs.json").read_text(encoding="utf-8"))

# ---------------------------------------------------------------- giải mã font
_TC = ("µ¸¶·¹" "¨»¾¼½Æ" "©ÇÊÈÉË" "®" "ÌÐÎÏÑ" "ªÒÕÓÔÖ" "×ÝØÜÞ" "ßãáâä" "«åèæçé" "¬êíëìî" "ïóñòô" "\xadõøö÷ù" "úýûüþ"
       "¡¢§£¤¥¦")
_UNI = ("àáảãạ" "ăằắẳẵặ" "âầấẩẫậ" "đ" "èéẻẽẹ" "êềếểễệ" "ìíỉĩị" "òóỏõọ" "ôồốổỗộ" "ơờớởỡợ" "ùúủũụ" "ưừứửữự" "ỳýỷỹỵ"
        "ĂÂĐÊÔƠƯ")
assert len(_TC) == len(_UNI), (len(_TC), len(_UNI))
TCVN3 = str.maketrans(dict(zip(_TC, _UNI)))

SYMBOL = {0x61: "α", 0x62: "β", 0x63: "χ", 0x64: "δ", 0x65: "ε", 0x66: "φ", 0x67: "γ", 0x68: "η", 0x69: "ι", 0x6A: "ϕ",
          0x6B: "κ", 0x6C: "λ", 0x6D: "µ", 0x6E: "ν", 0x6F: "ο", 0x70: "π", 0x71: "θ", 0x72: "ρ", 0x73: "σ", 0x74: "τ",
          0x75: "υ", 0x77: "ω", 0x78: "ξ", 0x79: "ψ", 0x7A: "ζ", 0x41: "Α", 0x42: "Β", 0x44: "Δ", 0x47: "Γ", 0x4C: "Λ",
          0x50: "Π", 0x53: "Σ", 0x57: "Ω", 0x46: "Φ", 0x51: "Θ", 0x59: "Ψ", 0x2D: "−", 0x2B: "+", 0x3D: "=", 0x3C: "<",
          0x3E: ">", 0xA3: "≤", 0xB3: "≥", 0xB1: "±", 0xB4: "×", 0xB8: "÷", 0xAE: "→", 0xAC: "←", 0xAD: "↑", 0xAF: "↓",
          0xAB: "↔", 0xDE: "⇒", 0xDB: "⇔", 0xB7: "•", 0xB0: "°", 0xBB: "≈", 0xB9: "≠", 0xBA: "≡", 0xA5: "∞", 0xD6: "√",
          0xBE: "—", 0xA2: "′", 0xB2: "″", 0x25: "%", 0x28: "(", 0x29: ")", 0x20: " ", 0xD7: "·", 0xC5: "⊕", 0xC4: "⊗"}
WINGDINGS = {0xFC: "✓", 0xFB: "✗", 0xD8: "➢", 0xA7: "▪", 0x6C: "●", 0x6E: "■", 0x71: "❑", 0x76: "❖", 0xE0: "→",
             0xE8: "➔", 0xF0: "⇨", 0x9F: "•", 0xA8: "◻", 0x77: "◆", 0xD9: "⮙", 0x46: "☞"}


def font_kind(font: str | None) -> str:
    f = (font or "").lower().replace(" ", "")
    if f.startswith("symbol"):
        return "symbol"
    if f.startswith("wingdings"):
        return "wingdings"
    if f.startswith(".vn") or (f.startswith("vn") and not f.startswith("vni")):
        return "tcvn3h" if f.endswith("h") else "tcvn3"
    return "unicode"


def decode(text: str, kind: str) -> str:
    if kind in ("symbol", "wingdings"):
        table = SYMBOL if kind == "symbol" else WINGDINGS
        out = []
        for ch in text:
            code = ord(ch) - 0xF000 if 0xF000 <= ord(ch) <= 0xF0FF else ord(ch)
            out.append(table.get(code, "•" if kind == "wingdings" else ch))
        return "".join(out)
    if kind.startswith("tcvn3"):
        s = text.translate(TCVN3)
        return s.upper() if kind == "tcvn3h" else s
    # soft hyphen trong font Unicode = vô hình; tài liệu gõ ß thay β, Ð/ð (Eth) thay Đ/đ
    text = re.sub(r"[\uf000-\uf0ff]", "•", text)  # ký hiệu Symbol/Wingdings lọt vào font Unicode → gạch đầu dòng
    return text.replace("\xad", "").replace("ß", "β").replace("Ð", "Đ").replace("ð", "đ")


# ---------------------------------------------------------------- đọc docx
doc = Document(str(DOCX))
STYLE_FONT: dict[str, str | None] = {}


def style_font(style) -> str | None:
    key = style.style_id if style is not None else ""
    if key in STYLE_FONT:
        return STYLE_FONT[key]
    s, found = style, None
    while s is not None and found is None:
        rpr = s.element.rPr
        if rpr is not None and rpr.rFonts is not None:
            found = rpr.rFonts.get(qn("w:ascii")) or rpr.rFonts.get(qn("w:hAnsi"))
        s = s.base_style
    STYLE_FONT[key] = found
    return found


def run_font(r, para_font):
    rpr = r.find(qn("w:rPr"))
    if rpr is not None:
        rf = rpr.find(qn("w:rFonts"))
        if rf is not None:
            f = rf.get(qn("w:ascii")) or rf.get(qn("w:hAnsi")) or rf.get(qn("w:cs"))
            if f:
                return f
        rs = rpr.find(qn("w:rStyle"))
        if rs is not None:
            try:
                f = style_font(doc.styles.get_by_id(rs.get(qn("w:val")), 1))
                if f:
                    return f
            except (KeyError, ValueError):
                pass
    return para_font


def is_bold(r) -> bool:
    rpr = r.find(qn("w:rPr"))
    if rpr is None:
        return False
    b = rpr.find(qn("w:b"))
    return b is not None and b.get(qn("w:val")) not in ("0", "false")


BLIP = qn("a:blip"), qn("r:embed")
IMAGEDATA = "{urn:schemas-microsoft-com:vml}imagedata", qn("r:id")
TXBX = qn("w:txbxContent")


def para_content(p_el, para_style):
    """→ (text, bold_ratio, [rId ảnh]) — bỏ chữ trong text box của hình, lấy ảnh ở mọi chỗ."""
    para_font = style_font(para_style)
    parts, bold_chars, chars, images = [], 0, 0, []
    for r in p_el.iter(qn("w:r")):
        anc = r.getparent()
        inside_box = False
        while anc is not None and anc is not p_el:
            if anc.tag == TXBX:
                inside_box = True
                break
            anc = anc.getparent()
        if inside_box:
            continue
        kind = font_kind(run_font(r, para_font))
        bold = is_bold(r)
        for ch in r:
            if ch.tag == qn("w:t"):
                t = decode(ch.text or "", kind)
            elif ch.tag == qn("w:tab"):
                t = "\t"
            elif ch.tag in (qn("w:br"), qn("w:cr")):
                t = "\n" if ch.get(qn("w:type")) not in ("page", "column") else " "
            elif ch.tag == qn("w:sym"):
                code = int(ch.get(qn("w:char")), 16)
                t = decode(chr(code), font_kind(ch.get(qn("w:font"))))
            elif ch.tag == qn("w:noBreakHyphen"):
                t = "-"
            else:
                t = ""
            if t:
                parts.append(t)
                n = len(t.strip())
                chars += n
                bold_chars += n if bold else 0
        for el in r.iter(BLIP[0], IMAGEDATA[0]):
            rid = el.get(BLIP[1]) or el.get(IMAGEDATA[1])
            if rid and rid not in images:
                images.append(rid)
    text = unicodedata.normalize("NFC", "".join(parts))
    return text, (bold_chars / chars if chars else 0.0), images


def _pstyle(p_el):
    ppr = p_el.find(qn("w:pPr"))
    if ppr is None:
        return None
    ps = ppr.find(qn("w:pStyle"))
    return ps.get(qn("w:val")) if ps is not None else None


def _style_of(p_el):
    sid = _pstyle(p_el)
    return doc.styles.get_by_id(sid, 1) if sid else doc.styles["Normal"]


def iter_blocks():
    """Khối theo đúng thứ tự thân văn bản: ('p', style, text, bold, images) / ('table', rows)."""
    for el in doc.element.body.iterchildren():
        if el.tag == qn("w:p"):
            style = _style_of(el)
            text, bold, imgs = para_content(el, style)
            yield ("p", style.name if style is not None else "Normal", text, bold, imgs)
        elif el.tag == qn("w:tbl"):
            rows = []
            for tr in el.iter(qn("w:tr")):
                cells = []
                for tc in tr.iter(qn("w:tc")):
                    if tc.getparent() is not tr:
                        continue
                    tcpr = tc.find(qn("w:tcPr"))
                    gs = tcpr.find(qn("w:gridSpan")) if tcpr is not None else None
                    texts, imgs = [], []
                    for p in tc.iter(qn("w:p")):
                        t, _, im = para_content(p, _style_of(p))
                        if t.strip():
                            texts.append(clean_inline(t))
                        imgs += im
                    cells.append({"text": "<br>".join(texts), "images": imgs,
                                  "span": int(gs.get(qn("w:val"))) if gs is not None else 1})
                if cells:
                    rows.append(cells)
            yield ("table", rows)


def clean_inline(t: str) -> str:
    t = t.replace("\t", " ").replace("\u00a0", " ")
    t = re.sub(r"[ \u2002\u2003]{2,}", " ", t)
    t = re.sub(r" +([,.;:)])", r"\1", t)
    t = re.sub(r"\( +", "(", t)
    return t.strip()


# ---------------------------------------------------------------- ảnh
def save_image(rid: str, lesson_id: str, n: int, media_dir: Path, report: Counter) -> str | None:
    try:
        part = doc.part.related_parts[rid]
    except KeyError:
        report["image_missing_rel"] += 1
        return None
    try:
        im = Image.open(io.BytesIO(part.blob))
        im.load()
    except Exception:  # WMF/EMF không đọc được
        report["image_unreadable"] += 1
        return None
    if im.width < 40 or im.height < 40:
        report["image_tiny_skipped"] += 1
        return None
    if im.mode in ("P", "LA", "RGBA"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    elif im.mode != "RGB":
        im = im.convert("RGB")
    im.thumbnail((1200, 1200))
    media_dir.mkdir(parents=True, exist_ok=True)
    out = media_dir / f"{lesson_id}_fig{n:02d}.jpg"
    buf = io.BytesIO()
    while True:  # ≤150 KB: hạ chất lượng, rồi thu nhỏ dần
        for q in (82, 72, 62, 52):
            buf = io.BytesIO()
            im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
            if buf.tell() <= 150_000:
                break
        if buf.tell() <= 150_000 or max(im.size) < 400:
            break
        im = im.resize((int(im.width * 0.8), int(im.height * 0.8)), Image.LANCZOS)
    out.write_bytes(buf.getvalue())
    report["images_saved"] += 1
    return out.name


# ---------------------------------------------------------------- dựng Markdown
BULLET_RE = re.compile(r"^\s*([-–—+•▪●➢✓❖◆*_·])\s*")
# "2.1. Tên", "2.1 Tên", "3. Tên", "3) Tên" — chữ đứng sau số. KHÔNG bắt "1: …", "1610: …", "0,5 cm", "3 giờ sau…"
NUM_HEAD_RE = re.compile(r"^(\d+(?:\.\d+)+)\.?\s*(?=[^\W\d_])(.*)$|^(\d+)[.)]\s*(?=[^\W\d_(\"“])(.*)$")
CHAPTER_RE = re.compile(r"^CHƯƠNG\s+(?:[IVX]+|\d+)\b")
ROMAN_RE = re.compile(r"^(?:X{0,3})(?:IX|IV|V?I{0,3})\.\s+\S")
H2_WORDS = re.compile(r"^(?:[IVX]+\.\s*)?(?:MỤC TIÊU|CÂU HỎI|TÀI LIỆU THAM KHẢO|LƯỢNG GIÁ)", re.U | re.I)
AUTHOR_RE = re.compile(r"^(?:Th[Ss]|TS|PGS|GS|BS|Bs|ThS|BSCK|Ths|SCK)\b[\s.,]")


def upper_ratio(t: str) -> float:
    letters = [c for c in t if c.isalpha()]
    return sum(c.isupper() for c in letters) / len(letters) if letters else 0.0


def classify(text: str, style: str, bold: float) -> tuple[str, str]:
    t = clean_inline(text)
    if not t:
        return "empty", ""
    if style.lower().startswith("toc"):
        return "toc", t
    if CHAPTER_RE.match(t) and upper_ratio(t) > 0.6:
        return "toc", t  # vạch chia chương giữa 2 bài, không thuộc bài nào
    if H2_WORDS.match(t) and len(t) < 60:
        return "h2", t
    if ROMAN_RE.match(t) and len(t) < 120 and upper_ratio(t) > 0.6:
        return "h2", t.upper()
    m = NUM_HEAD_RE.match(t)
    num, rest = (m.group(1) or m.group(3), m.group(2) if m.group(1) else m.group(4)) if m else (None, None)
    if m and rest and len(t) < 130 and not t.endswith((":", ";")):
        depth = num.count(".") + 1
        m_rest = rest
        heading_like = (style.startswith("Heading") or bold > 0.6 or upper_ratio(m_rest) > 0.7)
        if depth == 1 and (upper_ratio(m_rest) > 0.6 or (heading_like and len(t) < 80 and not t.endswith("."))):
            # "DÂY rỐn" (lẫn font) → "DÂY RỐN"
            return "h2", f"{num}. {m_rest.upper() if upper_ratio(m_rest) > 0.6 else m_rest}"
        if depth >= 2 and heading_like or depth >= 2 and len(t) < 70 and not t.endswith("."):
            return f"h{min(depth + 1, 5)}", f"{num}. {m_rest}"
        return "olist", f"{num}. {m_rest}"
    if m and rest:
        return "olist", f"{num}. {rest}"
    b = BULLET_RE.match(t)
    if b and len(t) > len(b.group(0)):
        return ("ulist2" if b.group(1) == "+" else "ulist"), t[b.end():]
    return "para", t


def md_escape_line(t: str) -> str:
    return re.sub(r"^([#>])", r"\\\1", t)


def table_md(rows) -> str:
    width = max(sum(c["span"] for c in r) for r in rows)
    if width == 1:  # bảng 1 cột (khung chữ) → đoạn văn
        return "\n\n".join(r[0]["text"] for r in rows if r[0]["text"])
    lines = []
    for i, r in enumerate(rows):
        cells = []
        for c in r:
            cells.append((c["text"] or " ").replace("|", "\\|"))
            cells.extend([""] * (c["span"] - 1))
        cells += [""] * (width - len(cells))
        lines.append("| " + " | ".join(cells) + " |")
        if i == 0:
            lines.append("|" + "---|" * width)
    return "\n".join(lines)


def _norm_title(t: str) -> str:
    t = unicodedata.normalize("NFD", t.upper())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn").replace("Đ", "D")
    return re.sub(r"[^A-Z0-9]+", " ", t).strip()


def anchored_titles(blocks, toc_end):
    """Đầu bài thật = tiêu đề viết hoa ngay trước đoạn 'Mục tiêu' (lùi qua dòng tác giả, gộp tiêu đề 2 dòng)."""
    paras = [(i, clean_inline(b[2])) for i, b in enumerate(blocks) if b[0] == "p" and clean_inline(b[2])]
    out = []
    for k, (i, t) in enumerate(paras):
        if i <= toc_end or len(t) > 40 or not re.match(r"(?i)^(?:[IVX]+\.\s*)?mục tiêu", t):
            continue
        for j in range(k - 1, max(k - 6, -1), -1):
            tj = paras[j][1]
            if AUTHOR_RE.match(tj) or len(tj) > 110 or upper_ratio(tj) <= 0.6:
                continue
            start, title = paras[j][0], tj
            if j > 0 and upper_ratio(paras[j - 1][1]) > 0.6 and len(paras[j - 1][1]) < 80 \
                    and not AUTHOR_RE.match(paras[j - 1][1]) and paras[j][0] - paras[j - 1][0] <= 2:
                start, title = paras[j - 1][0], paras[j - 1][1] + " " + tj  # tiêu đề xuống 2 dòng
            out.append((start, title))
            break
    return out


def find_starts(blocks):
    """Mốc đầu bài: ưu tiên tiêu đề có 'Mục tiêu' ngay sau; bài không có 'Mục tiêu' thì dò regex trong khoảng trống."""
    toc_end = max((i for i, b in enumerate(blocks) if b[0] == "p" and b[1].lower().startswith("toc")), default=0)
    anchors = anchored_titles(blocks, toc_end)
    used, starts = set(), {}
    for spec in SPECS:
        want = _norm_title(spec["title"])
        pat = re.compile(spec["regex"], re.I)
        best = None
        for a, (i, t) in enumerate(anchors):
            if a in used:
                continue
            nt = _norm_title(t)
            score = 1.0 if (pat.search(t.upper()) or want in nt or (nt in want and len(nt) > 8)) else \
                difflib.SequenceMatcher(None, want, nt).ratio()
            if score >= 0.72 and (best is None or score > best[0]):
                best = (score, a, i)
        if best:
            used.add(best[1])
            starts[spec["id"]] = best[2]
    order = [s["id"] for s in SPECS]
    for k, spec in enumerate(SPECS):
        if spec["id"] in starts:
            continue
        lo = max([starts[x] for x in order[:k] if x in starts], default=toc_end) + 1
        hi = min([starts[x] for x in order[k + 1:] if x in starts], default=len(blocks))
        pat = re.compile(spec["regex"], re.I)
        for i in range(lo, hi):
            b = blocks[i]
            t = clean_inline(b[2]) if b[0] == "p" else ""
            if t and len(t) <= 90 and not BULLET_RE.match(t) and not t.startswith(("Hình", "Bảng")) and pat.search(t.upper()):
                starts[spec["id"]] = i
                break
        else:
            raise SystemExit(f"[BLOCK] không tìm thấy đầu bài {spec['id']} {spec['title']} trong khoảng {lo}-{hi}")
    seq = [starts[x] for x in order]
    if seq != sorted(seq):
        bad = [(order[i], seq[i]) for i in range(1, len(seq)) if seq[i] < seq[i - 1]]
        raise SystemExit(f"[BLOCK] thứ tự bài không tăng dần: {bad}")
    leftovers = [(i, t) for a, (i, t) in enumerate(anchors) if a not in used and i not in seq]
    if leftovers:
        raise SystemExit(f"[BLOCK] có đầu bài trong tài liệu chưa khai trong lesson_specs.json: {leftovers}")
    return seq


NUM_RE = re.compile(r"\b\d+(?:[.,]\d+)?\s*(?:tuần|tháng|ngày|giờ|phút|ml|mL|g|kg|mg|mcg|µg|UI|IU|mmHg|cm|mm|%)(?![\w])", re.I)
DRUG_RE = re.compile(r"\b(?:oxytocin|misoprostol|magnesium sulfat[e]?|methyldopa|nifedipin[e]?|labetalol|hydralazin[e]?|"
                     r"betamethason[e]?|dexamethason[e]?|ergometrin[e]?|carboprost|amoxicillin|ampicillin|gentamicin|"
                     r"cefotaxim[e]?|ceftriaxon[e]?|dinoproston[e]?|prostaglandin|methotrexat[e]?|progesteron[e]?|"
                     r"estrogen|clomiphen[e]?|metronidazol[e]?|acyclovir|insulin|heparin|corticoid|sulfat magie)\b", re.I)


def norm_num(s: str) -> str:
    m = re.match(r"(\d+(?:[.,]\d+)?)\s*(\S+)", s)
    return f"{m.group(1)} {m.group(2)}" if m else s


def render(spec, seg, report) -> tuple[str, str, int]:
    lid = spec["id"]
    media_dir = OUT_DIR / "media" / lid
    out, fig_n, plain, skipped_head = [], 0, [], 0
    for b in seg:
        if b[0] == "table":
            for r in b[1]:
                for c in r:
                    for rid in c["images"]:
                        fig_n += 1
                        name = save_image(rid, lid, fig_n, media_dir, report)
                        if name:
                            out.append(("img", f"![{lid} hình {fig_n}](media/{lid}/{name})"))
            md = table_md(b[1])
            if md.strip():
                out.append(("table", md))
                report["tables"] += 1
                plain.append(md)
            continue
        _, style, text, bold, imgs = b
        for rid in imgs:
            fig_n += 1
            name = save_image(rid, lid, fig_n, media_dir, report)
            if name:
                out.append(("img", f"![{lid} hình {fig_n}](media/{lid}/{name})"))
        for line in text.split("\n"):
            kind, t = classify(line, style, bold)
            if kind in ("empty", "toc"):
                continue
            # vài dòng đầu: tên bài + tác giả (đã in ở phần đầu trang)
            if skipped_head < 3 and kind in ("para", "h2") and (upper_ratio(t) > 0.6 or AUTHOR_RE.match(t)) \
                    and not H2_WORDS.match(t):
                skipped_head += 1
                continue
            skipped_head = 3
            out.append((kind, t))
            plain.append(t)
    md_lines = [f"# {spec['title'].upper()}", "",
                f"**Mã bài:** `{lid}` | **Chương:** {spec['chapter']} | **Giảng viên:** {spec['author']}  ",
                "**Nguồn tài liệu:** Giáo trình Bài giảng Đại học Bộ môn Phụ Sản — ĐHYD Thái Bình (2021)", "", "---", ""]
    prev = None
    for kind, t in out:
        is_list = kind in ("ulist", "ulist2", "olist")
        if not (is_list and prev in ("ulist", "ulist2", "olist")) and md_lines[-1] != "":
            md_lines.append("")
        if kind.startswith("h"):
            md_lines += ["#" * int(kind[1]) + " " + t, ""]
        elif kind == "ulist":
            md_lines.append("- " + t)
        elif kind == "ulist2":
            md_lines.append(("  - " if prev in ("ulist", "ulist2") else "- ") + t)
        elif kind == "olist":
            md_lines.append(t)
        elif kind in ("table", "img"):
            md_lines += [t, ""]
        else:
            md_lines.append(md_escape_line(t))
        prev = kind if is_list else None
    md_text = re.sub(r"\n{3,}", "\n\n", "\n".join(md_lines)).strip() + "\n"
    return md_text, "\n".join(plain), fig_n


def main() -> int:
    report = Counter()
    blocks = list(iter_blocks())
    starts = find_starts(blocks)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    catalog, full = [], []
    for k, spec in enumerate(SPECS):
        seg = blocks[starts[k]: starts[k + 1] if k + 1 < len(starts) else len(blocks)]
        md_text, body, fig_n = render(spec, seg, report)
        lid = spec["id"]
        words = len(body.split())
        nums = sorted({norm_num(x) for x in NUM_RE.findall(body)},
                      key=lambda s: (float(re.match(r"[\d.,]+", s).group(0).replace(",", ".").rstrip(".")), s))
        drugs = sorted({d.lower() for d in DRUG_RE.findall(body)})
        (OUT_DIR / spec["folder"]).mkdir(parents=True, exist_ok=True)
        name = spec["basename"]
        (OUT_DIR / spec["folder"] / f"{name}.md").write_text(md_text, encoding="utf-8")
        meta = {"id": lid, "chapter": spec["chapter"], "folder": spec["folder"], "title": spec["title"],
                "author": spec["author"], "word_count": words, "figures": fig_n, "key_numbers": nums[:24],
                "key_drugs": drugs, "source": "BG_ĐAI_HỌC_BM_4_12_2021 (.doc → .docx, giải mã theo font)"}
        (OUT_DIR / spec["folder"] / f"{name}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
        catalog.append({"id": lid, "chapter": spec["chapter"], "folder": spec["folder"], "title": spec["title"],
                        "author": spec["author"], "word_count": words, "figures": fig_n,
                        "md_path": f"{spec['folder']}/{name}.md", "json_path": f"{spec['folder']}/{name}.json"})
        full.append(md_text)
        print(f"[{lid}] {spec['title'][:42]:<42} {words:>5} từ · {fig_n:>2} hình")
    (OUT_DIR / "index.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    cat = ["# MỤC LỤC GIÁO TRÌNH SẢN PHỤ KHOA (ĐHYD THÁI BÌNH 2021)", "",
           f"Trích lại từ bản .doc gốc (giải mã theo font, giữ bảng và hình) — {len(catalog)} bài.", "",
           "| Mã bài | Chương | Tên bài | Giảng viên | Số từ | Hình | File |", "|---|---|---|---|---|---|---|"]
    cat += [f"| **{c['id']}** | {c['chapter']} | {c['title']} | {c['author']} | {c['word_count']:,} | {c['figures']} | [md]({c['md_path']}) |"
            for c in catalog]
    (OUT_DIR / "CATALOG_BAI_GIANG.md").write_text("\n".join(cat) + "\n", encoding="utf-8")
    (OUT_DIR / "FULL_TEXT_BOOK_UNICODE.txt").write_text("\n\n".join(full), encoding="utf-8")
    (OUT_DIR / "extract_report.json").write_text(json.dumps(dict(report), indent=2), encoding="utf-8")
    print(dict(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
