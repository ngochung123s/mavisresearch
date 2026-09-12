# -*- coding: utf-8 -*-
"""viet_hoa_deck.py — Việt hoá body slide, giữ nguyên notes.

Đọc file deck JSON, thay thế thuật ngữ Anh loanword bằng tiếng Việt
ở các field hiển thị (points, title, headers, rows...), giữ nguyên
field `note` để tra cứu.
"""

import json
import re
from pathlib import Path

SRC = Path(
    r"F:\DL\mavisresearch\Bai hoc y khoa\01_San phu khoa\39_U_xo_tu_cung_ART_Infertility\U_xo_tu_cung_ART_Infertility_2026-07-14_from_md.deck.json"
)
DST = SRC  # ghi đè file gốc


# Thứ tự replace quan trọng: cụm dài trước, ngắn sau
REPLACEMENTS = [
    # Cụm đa từ — thay trước để tránh nuốt mất
    ("chronic endometritis", "viêm nội mạc mạn"),
    ("endometrial receptivity", "khả năng tiếp nhận phôi của nội mạc"),
    ("endometrial scratching", "cào nội mạc"),
    ("frozen embryo transfer", "chuyển phôi đông lạnh (FET)"),
    ("fresh transfer", "chuyển phôi tươi"),
    ("embryo banking", "trữ phôi trước"),
    ("oocyte pick-up", "chọc hút noãn"),
    ("Anti-Mullerian Hormone", "hormone kháng ống Müller (AMH)"),
    ("ovarian stimulation", "kích thích buồng trứng"),
    ("ovarian reserve", "dự trữ buồng trứng"),
    ("ovulation induction", "gây phóng noãn"),
    ("clinical pregnancy", "có thai lâm sàng"),
    ("live birth", "sinh con sống"),
    ("odds ratio", "tỷ số chênh"),
    ("confidence interval", "khoảng tin cậy 95%"),
    ("poor responder", "đáp ứng kém"),
    ("GnRH agonist", "chất đồng vận GnRH"),
    ("GnRH antagonist", "chất đối vận GnRH"),
    ("hysteroscopic myomectomy", "bóc u qua nội soi buồng tử cung"),
    ("laparoscopic myomectomy", "bóc u qua nội soi ổ bụng"),
    ("open myomectomy", "bóc u qua mổ bụng mở"),
    ("robotic myomectomy", "bóc u qua nội soi ổ bụng có robot hỗ trợ"),
    # Đơn từ / viết tắt có giải thích
    ("leiomyoma", "u xơ cơ tử cung"),
    ("leiomyomas", "u xơ cơ tử cung"),
    ("fibroids", "u xơ"),
    ("fibroid", "u xơ"),
    ("myoma", "u xơ"),
    ("myomas", "u xơ"),
    ("myomectomy", "bóc u"),
    ("hysteroscopic", "nội soi buồng tử cung"),
    ("laparoscopic", "nội soi ổ bụng"),
    ("endometrium", "nội mạc tử cung"),
    ("endometrial", "nội mạc tử cung"),
    ("myometrium", "cơ tử cung"),
    ("submucosal", "dưới niêm mạc"),
    ("subserosal", "dưới thanh mạc"),
    ("intramural", "trong cơ"),
    ("adenomyosis", "lạc nội mạc trong cơ"),
    ("hydrosalpinx", "ứ dịch vòi trứng"),
    ("implantation", "làm tổ"),
    ("fertilization", "thụ tinh"),
    ("fertilisation", "thụ tinh"),
    ("fertilization/ICSI", "thụ tinh / tiêm tinh trùng vào bào tương (ICSI)"),
    ("oocyte", "noãn"),
    ("oocytes", "noãn"),
    ("follicle", "nang noãn"),
    ("follicles", "nang noãn"),
    ("antral follicle count", "đếm nang thứ cấp (AFC)"),
    ("estradiol", "estradiol (hormone estrogen chính)"),
    ("progesterone", "progesterone (hormone hoàng thể)"),
    ("estrogen", "estrogen (hormone buồng trứng)"),
    ("androgen", "androgen"),
    ("antral", "thứ cấp"),
    ("morcellation", "cắt nhỏ u trong ổ bụng (morcellation)"),
    ("hysteroscopy có kinh nghiệm", "nội soi buồng tử cung có kinh nghiệm"),
    ("ongoing pregnancy", "thai kỳ diễn tiến (ongoing pregnancy)"),
    ("ongoing pregnancy/live birth", "thai kỳ diễn tiến / sinh con sống"),
    ("điểm cốt lõi thực hành thực hành", "điểm cốt lõi thực hành"),
    ("recurrent implantation failure", "thất bại làm tổ liên tiếp (RIF)"),
    # Cụm từ thường gặp
    ("carneous degeneration", "thoái hoá đỏ"),
    ("red degeneration", "thoái hoá đỏ"),
    ("hyaline degeneration", "thoái hoá kính"),
    ("cystic degeneration", "thoái hoá nang"),
    ("calcific degeneration", "thoái hoá vôi"),
    ("fatty change", "biến đổi mỡ"),
    ("lipoleiomyoma", "u xơ có thành phần mỡ (lipoleiomyoma)"),
    ("cellular leiomyoma", "u xơ tế bào đậm (cellular)"),
    ("mitotically active", "tăng phân bào"),
    ("atypical/symplastic", "dị dạng nhân (atypical)"),
    ("smooth muscle tumor of uncertain malignant potential",
     "u cơ trơn tiềm năng ác tính không chắc chắn (STUMP)"),
    ("trigger", "kích hoạt phóng noãn (trigger)"),
    ("antagonist trigger", "kích hoạt phóng noãn bằng đối vận"),
    ("agonist trigger", "kích hoạt phóng noãn bằng đồng vận"),
    # Cleanup chuỗi lặp do chạy script nhiều lần
    ("cắt nhỏ u trong ổ bụng (cắt nhỏ u trong ổ bụng (morcellation))",
     "cắt nhỏ u trong ổ bụng (morcellation)"),
    ("carneous", "đỏ (carneous)"),
    ("hyaline", "kính (hyaline)"),
    # Cụm tiêu đề còn lại
    ("non-cavity-distorting", "không biến dạng khoang"),
    ("cavity-distorting", "biến dạng khoang"),
    ("cavity", "khoang tử cung"),
    ("obstetric risks", "nguy cơ sản khoa"),
    ("clinical pearls", "điểm cốt lõi thực hành"),
    ("GnRHa", "chất đồng vận GnRH"),
    ("art cycle", "chu kỳ hỗ trợ sinh sản"),
    ("first trimester", "ba tháng đầu thai kỳ"),
    ("gestational age", "tuổi thai"),
]


# Field nào thuộc visible (sẽ được Việt hoá)
VISIBLE_FIELDS = {
    "title",
    "subtitle",
    "part_title",
    "part_subtitle",
    "term",
    "definition",
    "left_title",
    "right_title",
    "question",
    "yes_branch",
    "no_branch",
    "chapters",
    "points",
    "left_points",
    "right_points",
    "headers",
    "rows",
    "items",
    "stats",
    "refs",
    "events",
    "nodes",
}

# Field giữ nguyên tiếng Anh
PROTECTED_FIELDS = {
    "note",        # speaker notes để tra cứu chi tiết
    "type",
    "variant",
    "author",
    "specialty",
    "date",
}


def viet_hoa_text(text: str) -> str:
    """Thay thế thuật ngữ, giữ nguyên PMID, viết tắt chuẩn, số liệu."""
    if not isinstance(text, str):
        return text
    out = text
    for src, dst in REPLACEMENTS:
        # word-boundary, không phân biệt hoa thường để tránh sót 'Leiomyoma', 'FIBROIDS'
        pattern = re.compile(re.escape(src), re.IGNORECASE)
        out = pattern.sub(dst, out)
    return out


def viet_hoa_slide(slide: dict) -> dict:
    new = dict(slide)
    for k, v in list(new.items()):
        if k in PROTECTED_FIELDS:
            continue
        if k in VISIBLE_FIELDS:
            if isinstance(v, list):
                new[k] = [viet_hoa_text(x) for x in v]
            elif isinstance(v, str):
                new[k] = viet_hoa_text(v)
            elif isinstance(v, dict):
                # criteria items dạng [{"text": "...", "points": "..."}]
                inner = {}
                for kk, vv in v.items():
                    if isinstance(vv, list):
                        inner[kk] = [
                            {**item, "text": viet_hoa_text(item.get("text", ""))}
                            if isinstance(item, dict) else viet_hoa_text(item)
                            for item in vv
                        ]
                    else:
                        inner[kk] = vv
                new[k] = inner
    return new


def main():
    import sys
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    deck = json.loads(SRC.read_text(encoding="utf-8"))
    new_slides = [viet_hoa_slide(s) for s in deck["slides"]]
    deck["slides"] = new_slides
    DST.write_text(json.dumps(deck, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] da Viet hoa {len(new_slides)} slides -> {DST}")


if __name__ == "__main__":
    main()
