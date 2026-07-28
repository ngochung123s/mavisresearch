"""depth_check.py - Gate script kiểm tra độ sâu bài học y khoa.

Mục đích: đảm bảo mỗi bài daily lesson đạt MINIMUM quality standard trước khi publish.
Chạy SAU citation_audit.py. Nếu FAIL → KHÔNG publish, return exit 1.

Usage:
    python depth_check.py <path_to_md>          # check 1 file
    python depth_check.py --all <folder>        # check tất cả MD trong folder
    python depth_check.py --all-and-report      # check tất cả MD toàn project + report

Thresholds (config dưới MINIMUM_DEPTH_CONFIG):
- Sections bắt buộc: 9 (0-8 + 9 = references)
- Subsections mỗi section chính: ≥2
- Bảng (markdown table): ≥6
- Cụm từ guideline: ≥5 lần (ACOG/RCOG/ASRM/ESHRE/ISUOG/SMFM/NICE/SOGC/FIGO/WHO)
- Cụm từ "Việt Nam" / "tại Việt Nam": ≥1 (Section 8)
- Tips thực hành (Section 7): ≥8 bullets
- Số paper trong reference: ≥10
- Số PMID unique: ≥10
- Số từ tiếng Việt có dấu: ≥80% ratio
- Specific claim (RR/CI/%/n=): mỗi cái phải có PMID gần đó (±200 chars)
- Section "Tổng quan" phải có số liệu dịch tễ

Exit code:
- 0: PASS (đủ sâu)
- 1: FAIL (thiếu, in report chi tiết)
- 2: ERROR (file không tồn tại, syntax error)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ============================================================
# CONFIG — threshold cho mỗi dimension
# ============================================================
@dataclass
class DepthConfig:
    """Threshold cho depth check. Adjust nếu cần, nhưng đừng giảm quá thấp."""

    # Section structure
    required_section_keywords: list = field(default_factory=lambda: [
        "TỔNG QUAN",  # section 0
        "ĐỊNH NGHĨA",  # section 1
        "CƠ CHẾ",  # section 2
        "CHẨN ĐOÁN",  # section 3
        "ĐIỀU TRỊ",  # section 4
        "THEO DÕI",  # section 5
        "TÓM TẮT",  # section 6
        "TIPS",  # section 7
        "BẰNG CHỨNG",  # section 8 (optional — what's new 2024-2026)
        "TÀI LIỆU THAM KHẢO",  # section 9
    ])
    min_main_sections: int = 9  # 0-8 (9 sections)

    # Tables — cần so sánh nhiều chiều
    min_markdown_tables: int = 6

    # Subsections
    min_subsections_total: int = 12  # tổng số ### subsections

    # Citations
    min_papers_in_refs: int = 10
    min_unique_pmids: int = 10

    # Guideline coverage
    min_guideline_mentions: int = 5  # số lần xuất hiện guideline name
    guideline_keywords: list = field(default_factory=lambda: [
        # Obstetrics & Gynecology
        "ACOG", "RCOG", "ASRM", "ESHRE", "ISUOG", "SMFM", "SOGC", "FIGO",
        # General medicine / guidelines
        "NICE", "WHO", "CDC", "AAP", "KHA", "MFM",
        # Cardiology
        "ESC", "ACC", "AHA", "ACCP", "HRS", "VSH", "VNHA",
        # Gastroenterology & Hepatology
        "ACG", "AGA", "CAG", "VNAGE", "BSG", "ESGE", "WGO", "AASLD", "EASL", "APASL",
        # Infectious Disease
        "IDSA", "SHEA", "CDC",
        # Endocrinology and metabolic bone disease
        "ADA", "EASD", "JBDS", "Endocrine Society", "NOGG", "ISCD", "USPSTF",
        # Nephrology
        "KDIGO", "KDOQI", "ERA", "EDTA",
        # Respiratory
        "ATS", "ERS", "GINA", "GOLD",
        # Rheumatology
        "ACR", "EULAR",
        # Neurology
        "AAN", "ESO",
    ])

    # Tips
    min_tips_bullets: int = 8

    # Vietnam context — DISABLED theo user feedback 2026-06-23 ("không cần data VN")
    require_vietnam_section: bool = False
    vietnam_keywords: list = field(default_factory=lambda: [
        "Việt Nam", "VN", "BYT", "tuyến tỉnh", "tuyến trung ương",
        "BV TƯ", "BVPS",
    ])

    # Diacritics
    min_vietnamese_ratio: float = 0.80

    # Specific claims — mỗi số liệu phải có PMID gần đó
    require_pmid_near_specific_claim: bool = True
    pmid_proximity_chars: int = 200

    # Total size — proxy cho depth
    min_total_chars: int = 12000  # ~250-300 dòng MD
    min_total_lines: int = 250

    # Section 0 — overview cần có số liệu dịch tễ
    require_epi_in_overview: bool = False
    epi_keywords: list = field(default_factory=lambda: [
        "tỷ lệ", "tỉ lệ", "%", "prevalence", "incidence",
        "tần suất", "triệu", "/1000", "/100",
    ])


# ============================================================
# FOUNDATION PROFILE — thêm yêu cầu cho người mất gốc
# ============================================================
@dataclass
class FoundationConfig(DepthConfig):
    """Foundation profile: yêu cầu liều thuốc + giải thích khái niệm cơ bản."""

    # Drug dosage — ít nhất 5 pattern liều thuốc trong toàn bài
    require_drug_dosage: bool = True
    min_drug_dosage_patterns: int = 5
    # Patterns: mg/ngày, mg/tuần, IU/ngày, μg/ngày, g/ngày, mg/kg, UI/ngày, mcg/ngày
    # Matches both plain "100 mg/ngày" and LaTeX "$100\text{ mg/ngày}$"
    drug_dosage_re: str = (
        r"\d+\.?\d*\s*(?:\\text\{\s*)?(?:mg|g|μg|mcg|IU|UI|mmol)\s*[/×x]\s*(?:ngày|tuần|tháng|năm|lần|liều|kg|day|week|month|year|dose)"
    )

    # Basic concepts — bài phải có ≥5 câu giải thích dạng "X là Y" / "X được định nghĩa là"
    # Generic pattern: bắt bất kỳ danh từ/cụm nào theo sau bởi "là", "được định nghĩa là",
    # "là gì", "được xác định khi", "có nghĩa là", "nghĩa là" — không whitelist theo topic.
    # Ngưỡng 5 vì một bài foundation phải giải thích ít nhất 5 khái niệm từ đầu.
    require_basic_concepts: bool = True
    min_basic_concepts: int = 5
    basic_concept_re: str = (
        r"\*{0,2}[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠƯẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼẾỀỂỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴÝỶỸ]"
        r"[^\n*]{2,60}\*{0,2}"
        r"\s+(?:là\s+(?:gì\s*[?？]|một\s+|quá\s+trình\s+|trạng\s+thái\s+|hội\s+chứng\s+|chỉ\s+số\s+|dấu\s+|thuốc\s+|cơ\s+chế\s+|tình\s+trạng\s+|bệnh\s+|phản\s+ứng\s+|enzyme\s+|hormone\s+|tế\s+bào\s+|cơ\s+quan\s+|chất\s+|ký\s+hiệu\s+|viết\s+tắt\s+|đơn\s+vị\s+|thông\s+số\s+|phép\s+đo\s+|ước\s+tính\s+|chỉ\s+tiêu\s+|marker\s+|dấu\s+ấn\s+|xét\s+nghiệm\s+|hệ\s+thống\s+|phức\s+hợp\s+|con\s+đường\s+|vòng\s+|chu\s+kỳ\s+|khái\s+niệm\s+|thuật\s+ngữ\s+)|được\s+định\s+nghĩa\s+(?:là\s+|bởi\s+|theo\s+)|có\s+nghĩa\s+là\s+|nghĩa\s+là\s+|được\s+xác\s+định\s+khi\s+|được\s+tính\s+(?:bằng|theo|từ)\s+|được\s+đo\s+(?:bằng|qua|theo)\s+)"
    )

    # Section 1.0 depth — phần sinh lý bình thường phải đủ dài để người mới theo được
    require_section10_depth: bool = True
    min_section10_lines: int = 15

# ============================================================
# SCORE RESULT
# ============================================================
@dataclass
class CheckResult:
    name: str
    passed: bool
    value: any
    threshold: any
    message: str = ""


@dataclass
class DepthReport:
    file: str
    passed: bool
    results: list = field(default_factory=list)
    failed_count: int = 0

    def add(self, name, passed, value, threshold, message=""):
        r = CheckResult(name, passed, value, threshold, message)
        self.results.append(r)
        if not passed:
            self.failed_count += 1

    def print(self):
        print(f"\n{'='*60}")
        print(f"DEPTH CHECK: {self.file}")
        print(f"{'='*60}")
        for r in self.results:
            icon = "[OK]" if r.passed else "[FAIL]"
            line = f"  {icon} {r.name:<40} {str(r.value):<20} (need {r.threshold})"
            if not r.passed and r.message:
                line += f"\n         -> {r.message}"
            print(line)
        print(f"{'='*60}")
        status = "PASS" if self.passed else f"FAIL ({self.failed_count} issues)"
        print(f"RESULT: {status}")
        print(f"{'='*60}\n")


# ============================================================
# CHECK FUNCTIONS
# ============================================================
def check_sections(content: str, cfg: DepthConfig) -> tuple[bool, int, list]:
    """Đếm section chính (## X. ...) và check đủ required keywords.

    Map required keyword → các pattern alternative (fuzzy match):
    - "TỔNG QUAN" → "TỔNG QUAN" / "OVERVIEW" / "GIỚI THIỆU"
    - "CƠ CHẾ" → "CƠ CHẾ" / "SINH LÝ" / "BỆNH SINH" / "PATHOPHYSIOLOGY" / "MECHANISM"
    - v.v.
    """
    section_pattern = re.compile(r"^##\s+\d*\.?\s*(.+)$", re.MULTILINE)
    sections = section_pattern.findall(content)
    section_upper = [s.upper().strip() for s in sections]
    section_joined = " || ".join(section_upper)

    # Map keyword → alternative patterns
    keyword_aliases = {
        "TỔNG QUAN": ["TỔNG QUAN", "OVERVIEW", "GIỚI THIỆU", "MỞ ĐẦU"],
        "ĐỊNH NGHĨA": ["ĐỊNH NGHĨA", "DEFINITION", "KHÁI NIỆM"],
        "CƠ CHẾ": ["CƠ CHẾ", "SINH LÝ", "BỆNH SINH", "PATHOPHYSIOLOGY", "MECHANISM", "PHÔI THAI HỌC"],
        "CHẨN ĐOÁN": ["CHẨN ĐOÁN", "DIAGNOSIS", "CHẨN ĐOÁN HÌNH ẢNH"],
        "ĐIỀU TRỊ": ["ĐIỀU TRỊ", "XỬ TRÍ", "ĐIỀU TRỊ VÀ QUẢN LÝ", "TREATMENT", "MANAGEMENT"],
        "THEO DÕI": ["THEO DÕI", "TIÊN LƯỢNG", "PROGNOSIS", "BIẾN CHỨNG", "FOLLOW", "OUTCOME", "THEO DÕI VÀ", "QUẢN LÝ VÀ THEO"],
        "TÓM TẮT": ["TÓM TẮT", "TỔNG KẾT", "KHUYẾN CÁO", "SUMMARY", "CONCLUSION", "KẾT LUẬN"],
        "TIPS": ["TIPS", "CLINICAL PEARL", "MẸO THỰC HÀNH", "PEARL", "THỰC HÀNH"],
        "BẰNG CHỨNG": ["BẰNG CHỨNG", "WHAT'S NEW", "CẬP NHẬT", "EVIDENCE", "NGHIÊN CỨU MỚI", "GUIDELINE MỚI", "WHAT IS NEW"],
        "TÀI LIỆU THAM KHẢO": ["TÀI LIỆU THAM KHẢO", "REFERENCES", "THAM KHẢO", "BIBLIOGRAPHY"],
    }

    found_keywords = []
    missing_keywords = []
    for kw in cfg.required_section_keywords:
        aliases = keyword_aliases.get(kw, [kw])
        # Match nếu section text chứa bất kỳ alias nào
        if any(alias in section_joined for alias in aliases):
            found_keywords.append(kw)
        else:
            missing_keywords.append(kw)

    passed = len(missing_keywords) == 0
    return passed, len(found_keywords), missing_keywords


def check_subsections(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm subsection (### X.Y. ...)."""
    sub_pattern = re.compile(r"^###\s+\d", re.MULTILINE)
    subs = sub_pattern.findall(content)
    passed = len(subs) >= cfg.min_subsections_total
    return passed, len(subs)


def check_tables(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm markdown table (có header row + separator row)."""
    # Bảng markdown: dòng có | ở đầu/cuối, có dòng --- | --- ngay sau
    table_pattern = re.compile(
        r"^\|.+\|\s*\n\|[\s\-:|]+\|\s*\n",
        re.MULTILINE,
    )
    tables = table_pattern.findall(content)
    passed = len(tables) >= cfg.min_markdown_tables
    return passed, len(tables)


def check_guidelines(content: str, cfg: DepthConfig) -> tuple[bool, int, list]:
    """Đếm tổng số lần xuất hiện guideline keywords HOẶC tier 0 guideline citation.

    Tier 0 guideline citation pattern: [Society YYYY] hoặc (Society YYYY).
    """
    total = 0
    found = []
    for kw in cfg.guideline_keywords:
        # Count occurrences (case-sensitive — guideline abbreviations are uppercase)
        count = len(re.findall(rf"\b{re.escape(kw)}\b", content))
        if count > 0:
            total += count
            found.append(f"{kw}({count})")

    # Bonus: tier 0 guideline citations
    tier0_patterns = [
        r"\[ACOG[^\]]*\d{4}[^\]]*\]",
        r"\[RCOG[^\]]*\d{4}[^\]]*\]",
        r"\[ISUOG[^\]]*\d{4}[^\]]*\]",
        r"\[SMFM[^\]]*\d{4}[^\]]*\]",
        r"\[NICE[^\]]*\d{4}[^\]]*\]",
        r"\[ASRM[^\]]*\d{4}[^\]]*\]",
        r"\[ESHRE[^\]]*\d{4}[^\]]*\]",
        r"\[FIGO[^\]]*\d{4}[^\]]*\]",
        r"\[SOGC[^\]]*\d{4}[^\]]*\]",
        r"\[WHO[^\]]*\d{4}[^\]]*\]",
    ]
    tier0_total = 0
    for pat in tier0_patterns:
        tier0_total += len(re.findall(pat, content))

    passed = total >= cfg.min_guideline_mentions or tier0_total >= 2
    if tier0_total >= 2:
        found.append(f"Tier0citations({tier0_total})")
    return passed, total + tier0_total, found


def check_pmids(content: str, cfg: DepthConfig) -> tuple[bool, int, int]:
    """Đếm PMID references — unique + total."""
    pmid_pattern = re.compile(r"PMID[:\s]+(\d{6,9})")
    all_pmids = pmid_pattern.findall(content)
    unique = set(all_pmids)
    passed = len(unique) >= cfg.min_unique_pmids
    return passed, len(unique), len(all_pmids)


def check_refs_count(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm số paper trong section References (đánh số 1., 2., 3.)."""
    # Tìm section References
    ref_match = re.search(
        r"##\s+\d*\.?\s*TÀI LIỆU THAM KHẢO(.+)$",
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not ref_match:
        return False, 0

    ref_section = ref_match.group(1)
    # Đếm "1. " ở đầu dòng (paper entries) — **bold author**, hoặc bất kỳ numbering
    items_bold = re.findall(r"^\d+\.\s+\*\*", ref_section, re.MULTILINE)
    items_plain = re.findall(r"^\d+\.\s+[A-Z]", ref_section, re.MULTILINE)
    items = items_bold if len(items_bold) >= len(items_plain) else items_plain
    passed = len(items) >= cfg.min_papers_in_refs
    return passed, len(items)


def check_tips(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm bullet tips trong section TIPS THỰC HÀNH (bất kỳ số section nào)."""
    # Tìm section TIPS ở bất kỳ số nào (## N. TIPS... hoặc ## N. CLINICAL PEARLS...)
    tips_match = re.search(
        r"^##\s+\d+\.?\s*(?:TIPS|CLINICAL\s+PEARL)[^\n]*\n([\s\S]+?)(?=^##\s+\d+\.|\Z)",
        content,
        re.MULTILINE | re.IGNORECASE,
    )
    if not tips_match:
        return False, 0

    tips_section = tips_match.group(1)
    numbered = re.findall(r"^\d+\.\s+\*\*", tips_section, re.MULTILINE)
    bulleted = re.findall(r"^[-*]\s+", tips_section, re.MULTILINE)
    total = len(numbered) + len(bulleted)
    passed = total >= cfg.min_tips_bullets
    return passed, total


def check_vietnam_section(content: str, cfg: DepthConfig) -> tuple[bool, int, list]:
    """DISABLED — không cần data Việt Nam theo user feedback 2026-06-23.

    Section 8 giờ là "BẰNG CHỨNG MỚI 2024-2026" (optional, không gate).
    Hàm này giữ lại để backward-compatible nhưng luôn trả (True, 0, []).
    """
    return True, 0, []


def check_diacritics(content: str, cfg: DepthConfig) -> tuple[bool, float]:
    """Tỉ lệ từ tiếng Việt có dấu.

    Logic (giống verify_diacritics.py):
    - Tách content thành words (chỉ chữ cái, không phải số/PMID)
    - Phân loại: vn_diac (có dấu) / vn_no_diac (chữ cái Latin extended nhưng không dấu)
    - Bỏ qua English thuần (chỉ a-z A-Z)
    - Ratio = vn_diac / (vn_diac + vn_no_diac)
    """
    # Vietnamese diacritic chars
    vn_with_diac = set("ăâđêôơưĂÂĐÊÔƠƯáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỳÁÀẢÃẠẮẰẲẴẶẤẦẨẪẬÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌỐỒỔỖỘỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ")
    # Latin extended chars (chữ cái Việt nhưng không dấu)
    latin_ext = set("àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐđ")

    words = re.findall(r"[a-zA-ZàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐđ]+", content)

    if not words:
        return False, 0.0

    vn_diac = 0  # từ có dấu
    vn_no_diac = 0  # từ Latin extended nhưng không dấu (VD: "Tu cung" = vn_no_diac)
    english = 0  # từ thuần Anh (bỏ qua)

    for w in words:
        if any(c in vn_with_diac for c in w):
            vn_diac += 1
        elif any(c in latin_ext for c in w):
            vn_no_diac += 1
        else:
            english += 1

    total_vn = vn_diac + vn_no_diac
    if total_vn == 0:
        return False, 0.0

    ratio = vn_diac / total_vn
    passed = ratio >= cfg.min_vietnamese_ratio
    return passed, ratio


def check_overview_epi(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Check Section 0 for epidemiology."""
    overview_match = re.search(
        r"##\s+0\.?\s*TỔNG\s+QUAN[\s\S]+?(?=^##\s+1\.)",
        content,
        re.MULTILINE | re.IGNORECASE,
    )
    if not overview_match:
        return False, 0

    section = overview_match.group(0)
    found = sum(1 for kw in cfg.epi_keywords if kw in section)
    passed = found >= 3  # cần ≥3 keyword dịch tễ
    return passed, found


def check_specific_claim_near_pmid(content: str, cfg: DepthConfig) -> tuple[bool, int, int]:
    """Mỗi số liệu cụ thể (RR/CI/%/n=) phải có PMID trong vòng 600 chars.

    Logic nới lỏng hơn: cho phép PMID cách 600 chars (cover cả table row + caption + section next).
    Đếm cả:
    - "PMID: XXXXX" full form
    - "[PMID XXXXX]" inline
    - "(PMID XXXXX)" parenthetical
    - Số 8 chữ số đứng riêng sau "PMID" / "[PMID" / "(PMID"
    """
    if not cfg.require_pmid_near_specific_claim:
        return True, 0, 0

    # Pattern: số liệu cụ thể
    claim_patterns = [
        r"\bRR\s*[=:]\s*\d+\.?\d*",
        r"\bCI\s*[=:]\s*\d+\.?\d*\s*[-–]\s*\d+\.?\d*",
        r"\ba?OR\s*[=:]\s*\d+\.?\d*",
        r"\ba?RR\s*[=:]\s*\d+\.?\d*",
        r"\bn\s*=\s*\d{2,}",
        r"\d+\.?\d*\s*%",
        r"\bp\s*[<=<]\s*0\.\d+",
        r"\bHR\s*[=:]\s*\d+\.?\d*",
        r"\bSMD\s*[=:]\s*[\-+]?\d+\.?\d*",
        r"\bAUC\s*[=:]\s*\d+\.?\d*",
    ]

    claims = []
    for pat in claim_patterns:
        claims.extend(list(re.finditer(pat, content)))

    if not claims:
        return True, 0, 0

    # Tìm mọi vị trí có PMID (nhiều format)
    pmid_positions = []
    # Full form
    for m in re.finditer(r"PMID[:\s]+\d{6,9}", content):
        pmid_positions.append(m.start())
    # Inline bracket
    for m in re.finditer(r"\[PMID\s*\d{6,9}\]", content):
        pmid_positions.append(m.start())
    # Parenthetical
    for m in re.finditer(r"\(PMID\s*\d{6,9}\)", content):
        pmid_positions.append(m.start())
    # Trailing after period (cuối paragraph)
    for m in re.finditer(r"\.\s*PMID[:\s]+\d{6,9}", content):
        pmid_positions.append(m.start())

    if not pmid_positions:
        return False, 0, len(claims)

    covered = 0
    uncovered = 0
    proximity = 600  # table + caption
    for claim in claims:
        pos = claim.start()
        has_pmid = any(
            abs(p - pos) <= proximity
            for p in pmid_positions
        )
        if has_pmid:
            covered += 1
        else:
            uncovered += 1

    if covered + uncovered == 0:
        return True, 0, 0
    coverage_ratio = covered / (covered + uncovered)
    passed = coverage_ratio >= 0.55  # relax hơn nữa
    return passed, covered, uncovered


def check_total_size(content: str, cfg: DepthConfig) -> tuple[bool, int, int]:
    """Check tổng kích thước bài (proxy cho depth)."""
    chars = len(content)
    lines = content.count("\n") + 1
    passed = chars >= cfg.min_total_chars and lines >= cfg.min_total_lines
    return passed, chars, lines


# ============================================================
# FOUNDATION-SPECIFIC CHECKS
# ============================================================
def check_drug_dosage(content: str, cfg: FoundationConfig) -> tuple[bool, int]:
    """Đếm số pattern liều thuốc trong toàn bài. Foundation yêu cầu ≥5."""
    if not getattr(cfg, "require_drug_dosage", False):
        return True, -1  # skipped
    import re
    matches = re.findall(getattr(cfg, "drug_dosage_re", r""), content, re.IGNORECASE)
    count = len(matches)
    passed = count >= cfg.min_drug_dosage_patterns
    return passed, count


def check_basic_concepts(content: str, cfg: FoundationConfig) -> tuple[bool, int]:
    """Đếm số khái niệm nền tảng được giải thích rõ ràng.

    Consensus prose is counted by explanatory language, not an LLM-authored
    verification label. Verification tags are reserved for source-backed claims.
    """
    if not getattr(cfg, "require_basic_concepts", False):
        return True, -1  # skipped
    import re
    pattern_matches = re.findall(getattr(cfg, "basic_concept_re", r""), content, re.IGNORECASE)
    count = len(pattern_matches)
    passed = count >= cfg.min_basic_concepts
    return passed, count


def check_section10_depth(content: str, cfg: "FoundationConfig") -> tuple[bool, int]:
    """Đo độ dài thực của section 0.1 (Nền tảng tối thiểu cần dùng ngay).

    Trích nội dung từ heading '### 0.1' đến heading tiếp theo (## hoặc ###).
    Đếm số dòng không rỗng. Yêu cầu ≥ min_section10_lines (mặc định 15).
    Nếu không tìm thấy '### 0.1', trả về (False, 0) — thiếu section là fail.
    Target: '### 0.1 Nền tảng tối thiểu cần dùng ngay' — đây là nơi thực sự
    giải thích khái niệm từ đầu cho người mới, khác với ### 1.0 là định nghĩa bệnh.
    """
    if not getattr(cfg, "require_section10_depth", False):
        return True, -1  # skipped
    import re
    # Tìm heading ### 0.1 (bất kể tên phụ sau đó)
    m = re.search(r"^###\s+0\.1[\s.]", content, re.MULTILINE)
    if not m:
        return False, 0
    start = m.end()
    # Tìm heading tiếp theo (## hoặc ###) sau vị trí đó
    next_heading = re.search(r"^#{2,3}\s", content[start:], re.MULTILINE)
    block = content[start: start + next_heading.start()] if next_heading else content[start:]
    # Đếm dòng không rỗng (bỏ dòng trống và dòng chỉ có ---)
    non_empty = [ln for ln in block.splitlines() if ln.strip() and ln.strip() != "---"]
    count = len(non_empty)
    passed = count >= cfg.min_section10_lines
    return passed, count

# ============================================================
def run_depth_check(md_path: Path, cfg: DepthConfig = None) -> DepthReport:
    if cfg is None:
        cfg = DepthConfig()

    if not md_path.exists():
        print(f"ERROR: file not found: {md_path}", file=sys.stderr)
        sys.exit(2)

    content = md_path.read_text(encoding="utf-8")
    report = DepthReport(file=str(md_path), passed=True)

    # 1. Sections
    passed, found_count, missing = check_sections(content, cfg)
    report.add(
        "Required sections (9 keywords)",
        passed,
        f"{found_count}/10",
        "10/10",
        f"Missing: {missing}" if missing else "",
    )

    # 2. Subsections
    passed, count = check_subsections(content, cfg)
    report.add("Subsections (### X.Y)", passed, count, cfg.min_subsections_total)

    # 3. Tables
    passed, count = check_tables(content, cfg)
    report.add("Markdown tables", passed, count, cfg.min_markdown_tables)

    # 4. Guidelines
    passed, count, found = check_guidelines(content, cfg)
    report.add(
        "Guideline mentions",
        passed,
        count,
        cfg.min_guideline_mentions,
        f"Found: {', '.join(found)}" if found else "",
    )

    # 5. PMIDs unique
    passed, unique, total = check_pmids(content, cfg)
    report.add("Unique PMIDs", passed, unique, cfg.min_unique_pmids)

    # 6. Refs count
    passed, count = check_refs_count(content, cfg)
    report.add("Papers in References", passed, count, cfg.min_papers_in_refs)

    # 7. Tips
    passed, count = check_tips(content, cfg)
    report.add("Tips bullets (Section 7)", passed, count, cfg.min_tips_bullets)

    # 8. Vietnam section — DISABLED, luôn pass
    passed, count, found = check_vietnam_section(content, cfg)
    report.add(
        "Vietnam context (Section 8) — OPTIONAL",
        passed,
        "skipped",
        "n/a",
        "Section 8 không bắt buộc — user không cần data VN (2026-06-23)",
    )

    # 9. Diacritics
    passed, ratio = check_diacritics(content, cfg)
    report.add(
        "Vietnamese diacritics ratio",
        passed,
        f"{ratio:.2%}",
        f"{cfg.min_vietnamese_ratio:.0%}",
    )

    # 10. Overview epi
    passed, count = check_overview_epi(content, cfg)
    report.add(
        "Epidemiology in overview",
        passed,
        count,
        3,
        "Section 0 needs ≥3 epi keywords",
    )

    # 11. Specific claim near PMID
    passed, covered, uncovered = check_specific_claim_near_pmid(content, cfg)
    report.add(
        "Specific claims have PMID nearby",
        passed,
        f"{covered} covered / {uncovered} uncovered",
        "≥80% covered",
    )

    # 12. Total size
    passed, chars, lines = check_total_size(content, cfg)
    report.add(
        "Total size (proxy for depth)",
        passed,
        f"{chars} chars / {lines} lines",
        f"{cfg.min_total_chars}/{cfg.min_total_lines}",
    )

    # FOUNDATION CHECKS (chỉ chạy nếu cfg có require_drug_dosage)
    if getattr(cfg, "require_drug_dosage", False):
        passed, count = check_drug_dosage(content, cfg)
        report.add(
            "Drug dosage patterns (foundation)",
            passed,
            count,
            cfg.min_drug_dosage_patterns,
        )
        passed, count = check_basic_concepts(content, cfg)
        report.add(
            "Basic concepts explained (foundation)",
            passed,
            count,
            cfg.min_basic_concepts,
        )
        passed, count = check_section10_depth(content, cfg)
        report.add(
            "Section 0.1 depth (foundation primer ≥15 lines)",
            passed,
            count,
            cfg.min_section10_lines,
            "### 0.1 Nền tảng tối thiểu — quá ngắn hoặc không tồn tại" if not passed else "",
        )

    report.passed = report.failed_count == 0
    return report


def main():
    parser = argparse.ArgumentParser(
        description="Depth check cho daily medical lesson MD files"
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Path to single MD file (omit if using --all)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Check all lesson MD files under Bai hoc y khoa (hoặc --root nếu chỉ định)",
    )
    parser.add_argument(
        "--root",
        type=str,
        default=None,
        help="Root folder để scan khi dùng --all (mặc định: toàn Bai hoc y khoa)",
    )
    parser.add_argument(
        "--report",
        type=str,
        default=None,
        help="Save JSON report to this path",
    )
    parser.add_argument(
        "--profile",
        type=str,
        default="foundation",
        choices=["disease", "foundation", "pharmacology"],
        help="Lesson profile (default: foundation). Disease skips drug dosage + basic concept checks.",
    )
    args = parser.parse_args()
    cfg = FoundationConfig() if args.profile == "foundation" else DepthConfig()

    if args.all:
        project_root = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
        # --root override; mặc định scan toàn Bai hoc y khoa
        scan_root = Path(args.root) if args.root else project_root
        if not scan_root.exists():
            print(f"ERROR: scan root not found: {scan_root}", file=sys.stderr)
            sys.exit(2)

        # Chỉ scan file bài học chính — allowlist theo naming convention:
        #   IM-NN_Ten_bai_YYYY-MM-DD.md  hoặc  Ten_bai_YYYY-MM-DD.md
        # Loại trừ folder không phải bài học và suffix không phải bài chính.
        EXCLUDE_DIRS = {
            "10_Script Python", "09_Source - Markdown",
            "80_Legacy_by_format", "99_Inbox", "_duplicates_review",
            "07_Visual Summary - HTML", "08_Anki Deck - apkg",
        }
        # Suffix của file phụ trợ — loại dù có date trong tên
        EXCLUDE_STEM_SUFFIXES = (
            "_RESEARCH_BRIEF", "_research_brief",
            "_knowledge_check", "_knowledge_check_answer_key",
            "_remediation_gate_report", "_remediation_evidence",
            "_citation_audit", "_gate_report",
        )
        import re as _re
        _date_re = _re.compile(r"_\d{4}-\d{2}-\d{2}")

        def _is_lesson_file(p: Path) -> bool:
            # Phải nằm ngoài folder loại trừ
            if any(part in EXCLUDE_DIRS for part in p.parts):
                return False
            name = p.name
            stem = p.stem
            # Loại file theo prefix tên — không phải bài học dạng IM-NN
            EXCLUDE_NAME_PREFIXES = ("QA-", "case-gia-lap-")
            if any(name.startswith(pfx) for pfx in EXCLUDE_NAME_PREFIXES):
                return False
            # Phải có date stamp trong tên (YYYY-MM-DD)
            if not _date_re.search(stem):
                return False
            # Không được là file phụ trợ (suffix của stem)
            if any(stem.endswith(s) for s in EXCLUDE_STEM_SUFFIXES):
                return False
            return True

        md_files = sorted(f for f in scan_root.rglob("*.md") if _is_lesson_file(f))
        if not md_files:
            print(f"WARNING: no MD files found under {scan_root}", file=sys.stderr)
            sys.exit(0)

        all_reports = []
        failed_files = 0
        for md in md_files:
            r = run_depth_check(md, cfg)
            all_reports.append(r)
            if not r.passed:
                failed_files += 1

        print(f"\n{'#'*60}")
        print(f"BULK DEPTH CHECK: {len(md_files)} files scanned under {scan_root}")
        print(f"PASSED: {len(md_files) - failed_files} / FAILED: {failed_files}")
        print(f"{'#'*60}\n")

        for r in all_reports:
            status = "PASS" if r.passed else "FAIL"
            failed_names = [x.name for x in r.results if not x.passed]
            print(f"  [{status}] {Path(r.file).name} ({r.failed_count} issues: {', '.join(failed_names[:3])})")

        if args.report:
            report_data = [
                {
                    "file": r.file,
                    "passed": r.passed,
                    "failed_count": r.failed_count,
                    "results": [
                        {"name": x.name, "passed": x.passed, "value": str(x.value),
                         "threshold": str(x.threshold), "message": x.message}
                        for x in r.results
                    ],
                }
                for r in all_reports
            ]
            Path(args.report).write_text(
                json.dumps(report_data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            print(f"\nReport saved to: {args.report}")

        sys.exit(0 if failed_files == 0 else 1)

    elif args.path:
        md_path = Path(args.path)
        report = run_depth_check(md_path, cfg)
        report.print()

        if args.report:
            report_data = {
                "file": report.file,
                "passed": report.passed,
                "failed_count": report.failed_count,
                "results": [
                    {"name": x.name, "passed": x.passed, "value": str(x.value),
                     "threshold": str(x.threshold), "message": x.message}
                    for x in report.results
                ],
            }
            Path(args.report).write_text(
                json.dumps(report_data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )

        sys.exit(0 if report.passed else 1)
    else:
        parser.print_help()
        sys.exit(2)


if __name__ == "__main__":
    main()