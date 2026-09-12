"""depth_check.py - Gate script kiểm tra độ sâu bài học y khoa.

Mục đích: đảm bảo mỗi bài daily lesson đạt MINIMUM quality standard trước khi publish.
Fail-closed depth contract gate per profile (foundation/disease/pharmacology).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from profile_check import check_profile_content


# ============================================================
# CONFIG — threshold cho mỗi dimension & profile
# ============================================================
@dataclass
class DepthConfig:
    """Base threshold cho depth check."""

    profile_name: str = "disease"
    min_total_words: int = 6000
    min_total_lines: int = 600  # nonblank lines
    min_subsections_total: int = 14
    min_mechanism_chains: int = 4
    min_examples: int = 8
    min_misconceptions: int = 8
    min_checkpoints: int = 5
    min_cases_with_solutions: int = 3
    min_tips_bullets: int = 12

    # Section structure
    required_section_keywords: list = field(default_factory=lambda: [
        "TỔNG QUAN",
        "ĐỊNH NGHĨA",
        "CƠ CHẾ",
        "CHẨN ĐOÁN",
        "ĐIỀU TRỊ",
        "THEO DÕI",
        "TÓM TẮT",
        "TIPS",
        "BẰNG CHỨNG",
        "TÀI LIỆU THAM KHẢO",
    ])
    min_main_sections: int = 10
    min_markdown_tables: int = 2
    min_papers_in_refs: int = 1
    min_unique_pmids: int = 1
    min_guideline_mentions: int = 5
    guideline_keywords: list = field(default_factory=lambda: [
        "ACOG", "RCOG", "ASRM", "ESHRE", "ISUOG", "SMFM", "SOGC", "FIGO",
        "NICE", "WHO", "CDC", "AAP", "KHA", "MFM",
        "ESC", "ACC", "AHA", "ACCP", "HRS", "VSH", "VNHA",
        "ACG", "AGA", "CAG", "VNAGE", "BSG", "ESGE", "WGO", "AASLD", "EASL", "APASL",
        "IDSA", "SHEA", "CDC",
        "ADA", "EASD", "JBDS", "Endocrine Society", "NOGG", "ISCD", "USPSTF",
        "KDIGO", "KDOQI", "ERA", "EDTA",
        "ATS", "ERS", "GINA", "GOLD",
        "ACR", "EULAR",
        "AAN", "ESO",
    ])

    require_vietnam_section: bool = False
    vietnam_keywords: list = field(default_factory=lambda: [
        "Việt Nam", "VN", "BYT", "tuyến tỉnh", "tuyến trung ương",
        "BV TƯ", "BVPS",
    ])

    min_vietnamese_ratio: float = 0.80

    require_pmid_near_specific_claim: bool = True
    pmid_proximity_chars: int = 600

    min_total_chars: int = 12000
    require_epi_in_overview: bool = False
    epi_keywords: list = field(default_factory=lambda: [
        "tỷ lệ", "tỉ lệ", "%", "prevalence", "incidence",
        "tần suất", "triệu", "/1000", "/100",
    ])

    require_drug_dosage: bool = False
    min_drug_dosage_patterns: int = 5
    drug_dosage_re: str = (
        r"\d+\.?\d*\s*(?:\\text\{\s*)?(?:mg|g|μg|mcg|IU|UI|mmol)\s*[/×x]\s*(?:ngày|tuần|tháng|năm|lần|liều|kg|day|week|month|year|dose)"
    )

    require_basic_concepts: bool = False
    min_basic_concepts: int = 5
    basic_concept_re: str = (
        r"\*{0,2}[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠƯẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼẾỀỂỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴÝỶỸ]"
        r"[^\n*]{2,60}\*{0,2}"
        r"\s+(?:là\s+(?:gì\s*[?？]|một\s+|quá\s+trình\s+|trạng\s+thái\s+|hội\s+chứng\s+|chỉ\s+số\s+|dấu\s+|thuốc\s+|cơ\s+chế\s+|tình\s+trạng\s+|bệnh\s+|phản\s+ứng\s+|enzyme\s+|hormone\s+|tế\s+bào\s+|cơ\s+quan\s+|chất\s+|ký\s+hiệu\s+|viết\s+tắt\s+|đơn\s+vị\s+|thông\s+số\s+|phép\s+đo\s+|ước\s+tính\s+|chỉ\s+tiêu\s+|marker\s+|dấu\s+ấn\s+|xét\s+nghiệm\s+|hệ\s+thống\s+|phức\s+hợp\s+|con\s+đường\s+|vòng\s+|chu\s+kỳ\s+|khái\s+niệm\s+|thuật\s+ngữ\s+)|được\s+định\s+nghĩa\s+(?:là\s+|bởi\s+|theo\s+)|có\s+nghĩa\s+là\s+|nghĩa\s+là\s+|được\s+xác\s+định\s+khi\s+|được\s+tính\s+(?:bằng|theo|từ)\s+|được\s+đo\s+(?:bằng|qua|theo)\s+)"
    )

    require_section10_depth: bool = False
    min_section10_lines: int = 15


@dataclass
class FoundationConfig(DepthConfig):
    """Foundation profile configuration."""

    profile_name: str = "foundation"
    min_total_words: int = 5000
    min_total_lines: int = 500
    min_subsections_total: int = 12
    min_mechanism_chains: int = 3
    min_examples: int = 6
    min_misconceptions: int = 6
    min_checkpoints: int = 4
    min_cases_with_solutions: int = 2
    min_tips_bullets: int = 10

    required_section_keywords: list = field(default_factory=lambda: [
        "TỔNG QUAN",
        "ĐỊNH NGHĨA",
        "CƠ CHẾ",
        "CHẨN ĐOÁN",
        "THEO DÕI",
        "TÓM TẮT",
        "TIPS",
        "TÀI LIỆU THAM KHẢO",
    ])
    min_main_sections: int = 10
    min_markdown_tables: int = 2
    min_papers_in_refs: int = 1
    min_unique_pmids: int = 1
    min_guideline_mentions: int = 0

    # Foundation profile does not mandate drug dosage if topic is drug-free (e.g. ECG physiology)
    require_drug_dosage: bool = False
    require_basic_concepts: bool = True
    require_section10_depth: bool = True


@dataclass
class DiseaseConfig(DepthConfig):
    """Disease profile configuration."""

    profile_name: str = "disease"
    min_total_words: int = 6000
    min_total_lines: int = 600
    min_subsections_total: int = 14
    min_mechanism_chains: int = 4
    min_main_sections: int = 10
    min_markdown_tables: int = 2
    min_papers_in_refs: int = 1
    min_unique_pmids: int = 1
    min_guideline_mentions: int = 0


@dataclass
class PharmacologyConfig(DepthConfig):
    """Pharmacology profile configuration."""

    profile_name: str = "pharmacology"
    min_total_words: int = 6000
    min_total_lines: int = 600
    min_subsections_total: int = 14
    min_mechanism_chains: int = 5
    min_examples: int = 8
    min_misconceptions: int = 8
    min_checkpoints: int = 5
    min_cases_with_solutions: int = 3
    min_tips_bullets: int = 12

    required_section_keywords: list = field(default_factory=lambda: [
        "TỔNG QUAN",
        "BẢN ĐỒ NHÓM THUỐC",
        "KHÁNG LỢI TIỂU",
        "KÊ ĐƠN THỰC HÀNH",
        "THEO DÕI",
        "TỔNG KẾT",
        "TIPS",
        "TÀI LIỆU THAM KHẢO",
    ])
    min_main_sections: int = 8
    min_markdown_tables: int = 2
    min_papers_in_refs: int = 1
    min_unique_pmids: int = 1
    min_guideline_mentions: int = 0


def get_depth_config(profile: str) -> DepthConfig:
    if profile == "foundation":
        return FoundationConfig()
    elif profile == "pharmacology":
        return PharmacologyConfig()
    else:
        return DiseaseConfig()


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
    informational: bool = False


@dataclass
class DepthReport:
    file: str
    passed: bool
    results: list = field(default_factory=list)
    failed_count: int = 0

    def add(self, name, passed, value, threshold, message="", informational=False):
        r = CheckResult(name, passed, value, threshold, message, informational)
        self.results.append(r)
        if not passed and not informational:
            self.failed_count += 1

    def print(self):
        print(f"\n{'='*60}")
        print(f"DEPTH CHECK: {self.file}")
        print(f"{'='*60}")
        for r in self.results:
            if r.passed:
                icon = "[OK]"
            elif r.informational:
                icon = "[INFO]"
            else:
                icon = "[FAIL]"
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
    """Đếm section chính (## X. ...) và check đủ required keywords."""
    section_pattern = re.compile(r"^##\s+\d*\.?\s*(.+)$", re.MULTILINE)
    sections = section_pattern.findall(content)
    section_upper = [s.upper().strip() for s in sections]
    section_joined = " || ".join(section_upper)
def check_sections(content: str, cfg: DepthConfig) -> tuple[bool, int, int, list]:
    """Đếm section chính (## X. ...) và check đủ required keywords."""
    section_pattern = re.compile(r"^##\s+\d*\.?\s*(.+)$", re.MULTILINE)
    sections = section_pattern.findall(content)
    section_count = len(sections)
    section_upper = [s.upper().strip() for s in sections]
    section_joined = " || ".join(section_upper)

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
        "BẢN ĐỒ NHÓM THUỐC": ["BẢN ĐỒ NHÓM THUỐC", "DRUG MAP", "PHÂN LOẠI THUỐC"],
        "KHÁNG LỢI TIỂU": ["KHÁNG LỢI TIỂU", "RESISTANCE", "ĐƠN THỦY"],
        "KÊ ĐƠN THỰC HÀNH": ["KÊ ĐƠN THỰC HÀNH", "PRESCRIBING", "LIỀU DÙNG VÀ KÊ ĐƠN"],
    }

    found_keywords = []
    missing_keywords = []
    for kw in cfg.required_section_keywords:
        aliases = keyword_aliases.get(kw, [kw])
        if any(alias in section_joined for alias in aliases):
            found_keywords.append(kw)
        else:
            missing_keywords.append(kw)

    passed = len(missing_keywords) == 0 and section_count >= cfg.min_main_sections
    return passed, section_count, len(found_keywords), missing_keywords
def check_total_size(content: str, cfg: DepthConfig) -> tuple[bool, int, int]:
    """Check total word count and nonblank line count."""
    words = len(content.split())
    nonblank_lines = len([ln for ln in content.splitlines() if ln.strip()])
    passed = words >= cfg.min_total_words and nonblank_lines >= cfg.min_total_lines
    return passed, words, nonblank_lines

def check_subsections(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm subsection (### X.Y. ...)."""
    sub_pattern = re.compile(r"^###\s+.", re.MULTILINE)
    subs = sub_pattern.findall(content)
    passed = len(subs) >= cfg.min_subsections_total
    return passed, len(subs)


def check_mechanism_chains(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Count reasoning/mechanism chains (arrow chains >=4 nodes or Tầng 1..5 blocks)."""
    # 1. Arrow chains with >=3 arrows (meaning >=4 nodes)
    arrow_pattern = re.compile(
        r"(?:[^\n→\->⇒\n]+(?:\s*(?:→|->|-->|⇒)\s*)){3,}[^\n→\->⇒\n]+",
        re.MULTILINE,
    )
    arrow_chains = arrow_pattern.findall(content)

    # 2. Structural Tầng 1..5 / Kênh 1..5 blocks
    tang_pattern = re.compile(
        r"(?:Tầng|Kênh)\s+1[\s\S]+?(?:Tầng|Kênh)\s+5",
        re.IGNORECASE,
    )
    tang_blocks = tang_pattern.findall(content)

    total = len(arrow_chains) + len(tang_blocks)
    passed = total >= cfg.min_mechanism_chains
    return passed, total


def check_examples(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Count illustrative examples."""
    matches = re.findall(
        r"\b(?:ví\s+dụ|Ví\s+dụ|VÍ\s+DỤ|VD\s*:|vd\s*:|Example|example)\b",
        content,
    )
    count = len(matches)
    passed = count >= cfg.min_examples
    return passed, count


def check_misconceptions(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Count traps, misconceptions, counter-examples, common student errors."""
    matches = re.findall(
        r"\b(?:bẫy|Bẫy|BẪY|học\s+viên\s+hay\s+nhầm|học\s+viên\s+rất\s+hay\s+nhầm|phản\s+ví\s+dụ|nhầm\s+lẫn|sai\s+lầm|cạm\s+bẫy|lỗi\s+thường\s+gặp|pitfall|Pitfall|common\s+mistake)\b",
        content,
        re.IGNORECASE,
    )
    count = len(matches)
    passed = count >= cfg.min_misconceptions
    return passed, count


def check_checkpoints(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Count self-check checkpoints."""
    matches = re.findall(
        r"\b(?:checkpoint|Checkpoint|CHECKPOINT|tự\s+kiểm\s+tra|câu\s+hỏi\s+tự\s+kiểm\s+tra|kiểm\s+tra\s+nhanh|self-check|Self-check)\b",
        content,
        re.IGNORECASE,
    )
    count = len(matches)
    passed = count >= cfg.min_checkpoints
    return passed, count


def check_cases_with_solutions(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Count clinical cases that include full solutions/explanations."""
    case_blocks = re.findall(
        r"^###?\s*(?:Case|Ca\s+lâm\s+sàng)[^\n]*\n([\s\S]+?)(?=^#{2,3}\s+|\Z)",
        content,
        re.MULTILINE | re.IGNORECASE,
    )

    solution_kw = ["lời giải", "giải thích", "đáp án", "phân tích", "xử trí", "bàn luận", "hướng xử trí", "phương án"]
    count = 0
    if case_blocks:
        for block in case_blocks:
            if any(kw in block.lower() for kw in solution_kw):
                count += 1
    else:
        all_cases = re.findall(r"\b(?:Case|Ca\s+lâm\s+sàng)\s*\d+", content, re.IGNORECASE)
        solutions = re.findall(r"\b(?:lời\s+giải|giải\s+thích|đáp\s+án)\b", content, re.IGNORECASE)
        count = min(len(all_cases), len(solutions))

    passed = count >= cfg.min_cases_with_solutions
    return passed, count


def check_tables(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm markdown table (có header row + separator row)."""
    table_pattern = re.compile(
        r"^\|.+\|\s*\n\|[\s\-:|]+\|\s*\n",
        re.MULTILINE,
    )
    tables = table_pattern.findall(content)
    passed = len(tables) >= cfg.min_markdown_tables
    return passed, len(tables)


def check_guidelines(content: str, cfg: DepthConfig) -> tuple[bool, int, list]:
    """Đếm tổng số lần xuất hiện guideline keywords HOẶC tier 0 guideline citation."""
    total = 0
    found = []
    for kw in cfg.guideline_keywords:
        count = len(re.findall(rf"\b{re.escape(kw)}\b", content))
        if count > 0:
            total += count
            found.append(f"{kw}({count})")

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
    ref_match = re.search(
        r"##\s+\d*\.?\s*TÀI LIỆU THAM KHẢO(.+)$",
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not ref_match:
        return False, 0

    ref_section = ref_match.group(1)
    items_bold = re.findall(r"^\d+\.\s+\*\*", ref_section, re.MULTILINE)
    items_plain = re.findall(r"^\d+\.\s+[A-Z]", ref_section, re.MULTILINE)
    items = items_bold if len(items_bold) >= len(items_plain) else items_plain
    passed = len(items) >= cfg.min_papers_in_refs
    return passed, len(items)


def check_tips(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm bullet tips trong section TIPS THỰC HÀNH."""
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
    """DISABLED — không cần data Việt Nam."""
    return True, 0, []


def check_diacritics(content: str, cfg: DepthConfig) -> tuple[bool, float]:
    """Tỉ lệ từ tiếng Việt có dấu."""
    vn_with_diac = set("ăâđêôơưĂÂĐÊÔƠƯáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỳÁÀẢÃẠẮẰẲẴẶẤẦẨẪẬÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌỐỒỔỖỘỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ")
    latin_ext = set("àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉÈẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐđ")

    words = re.findall(r"[a-zA-ZàáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÈÉÈẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴĐđ]+", content)
    if not words:
        return False, 0.0

    vn_diac = 0
    vn_no_diac = 0
    for w in words:
        if any(c in vn_with_diac for c in w):
            vn_diac += 1
        elif any(c in latin_ext for c in w):
            vn_no_diac += 1

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
    passed = found >= 3
    return passed, found


def check_specific_claim_near_pmid(content: str, cfg: DepthConfig) -> tuple[bool, int, int]:
    """Mỗi số liệu cụ thể (RR/CI/%/n=) phải có PMID trong vòng 600 chars."""
    if not cfg.require_pmid_near_specific_claim:
        return True, 0, 0

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

    pmid_positions = []
    for m in re.finditer(r"PMID[:\s]+\d{6,9}", content):
        pmid_positions.append(m.start())
    for m in re.finditer(r"\[PMID\s*\d{6,9}\]", content):
        pmid_positions.append(m.start())
    for m in re.finditer(r"\(PMID\s*\d{6,9}\)", content):
        pmid_positions.append(m.start())
    for m in re.finditer(r"\.\s*PMID[:\s]+\d{6,9}", content):
        pmid_positions.append(m.start())

    if not pmid_positions:
        return False, 0, len(claims)

    covered = 0
    uncovered = 0
    proximity = 600
    for claim in claims:
        pos = claim.start()
        has_pmid = any(abs(p - pos) <= proximity for p in pmid_positions)
        if has_pmid:
            covered += 1
        else:
            uncovered += 1

    if covered + uncovered == 0:
        return True, 0, 0
    coverage_ratio = covered / (covered + uncovered)
    passed = coverage_ratio >= 0.55
    return passed, covered, uncovered


def check_drug_dosage(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm số pattern liều thuốc trong toàn bài."""
    if not getattr(cfg, "require_drug_dosage", False):
        return True, -1
    matches = re.findall(getattr(cfg, "drug_dosage_re", r""), content, re.IGNORECASE)
    count = len(matches)
    passed = count >= cfg.min_drug_dosage_patterns
    return passed, count


def check_basic_concepts(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đếm số khái niệm nền tảng được giải thích rõ ràng."""
    if not getattr(cfg, "require_basic_concepts", False):
        return True, -1
    pattern_matches = re.findall(getattr(cfg, "basic_concept_re", r""), content, re.IGNORECASE)
    count = len(pattern_matches)
    passed = count >= cfg.min_basic_concepts
    return passed, count


def check_section10_depth(content: str, cfg: DepthConfig) -> tuple[bool, int]:
    """Đo độ dài thực của section 0.1 (Nền tảng tối thiểu cần dùng ngay)."""
    if not getattr(cfg, "require_section10_depth", False):
        return True, -1
    m = re.search(r"^###\s+0\.1[\s.]", content, re.MULTILINE)
    if not m:
        return False, 0
    start = m.end()
    next_heading = re.search(r"^#{2,3}\s", content[start:], re.MULTILINE)
    block = content[start: start + next_heading.start()] if next_heading else content[start:]
    non_empty = [ln for ln in block.splitlines() if ln.strip() and ln.strip() != "---"]
    count = len(non_empty)
    passed = count >= cfg.min_section10_lines
    return passed, count


def check_placeholders(content: str) -> tuple[bool, int, list[str]]:
    """Detect leftover placeholders."""
    patterns = [
        r"\[(?:Mục\s+tiêu|Tên|Nội\s+dung|Tiêu\s+đề|Điền|insert|TODO|TBD|Tên\s+bài|Cần\s+bổ\s+sung|xxx|XXX)[^\]]*\]",
        r"\[[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠƯẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼẾỀỂỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪỬỮỰỲỴÝỶỸ\s]*\.\.\.[^\]]*\]",
        r"\b(?:TODO|TBD|FIXME)\b",
        r"\[\s*\.\.\.\s*\]",
    ]
    found = []
    for pat in patterns:
        matches = re.findall(pat, content, re.IGNORECASE)
        found.extend(matches)
    found_unique = sorted(set(found))
    count = len(found)
    passed = count == 0
    return passed, count, found_unique


def check_padding_and_duplicates(content: str) -> tuple[bool, int, list[str]]:
    """Detect verbatim padding/repeats, template-pattern line repeats, and overly short main sections."""
    lines = [ln.strip() for ln in content.splitlines() if ln.strip()]

    candidates = [
        ln for ln in lines
        if len(ln) >= 25
        and not ln.startswith("#")
        and not ln.startswith("```")
        and not ln.startswith("|---")
    ]

    # 1. Exact verbatim repeated non-trivial lines
    seen = set()
    verbatim_duplicates = set()
    for ln in candidates:
        if ln in seen:
            verbatim_duplicates.add(ln[:60] + "...")
        else:
            seen.add(ln)

    # 2. Template-line repeats (same string pattern with only numbers changing)
    normalized_counts: dict[str, int] = {}
    normalized_samples: dict[str, str] = {}
    for ln in candidates:
        norm = re.sub(r"\d+", "N", ln)
        normalized_counts[norm] = normalized_counts.get(norm, 0) + 1
        if norm not in normalized_samples:
            normalized_samples[norm] = ln[:60] + "..."

    template_duplicates = set()
    for norm, count in normalized_counts.items():
        if count >= 3:
            template_duplicates.add(f"Template repeat ({count}x): {normalized_samples[norm]}")

    # 3. Short sections (main heading ## with <3 non-empty lines before next heading)
    short_sections = []
    heading_matches = list(re.finditer(r"^##\s+(.+)$", content, re.MULTILINE))
    for i, m in enumerate(heading_matches):
        start = m.end()
        end = heading_matches[i + 1].start() if i + 1 < len(heading_matches) else len(content)
        sec_body = content[start:end]
        sec_title = m.group(1).strip()
        sec_lines = [ln.strip() for ln in sec_body.splitlines() if ln.strip() and ln.strip() != "---"]
        if "THAM KHẢO" in sec_title.upper() or "REFERENCES" in sec_title.upper():
            continue
        if len(sec_lines) < 3:
            short_sections.append(f"Section '## {sec_title}' has only {len(sec_lines)} lines")

    issues = list(verbatim_duplicates) + list(template_duplicates) + short_sections
    passed = len(verbatim_duplicates) == 0 and len(template_duplicates) == 0 and len(short_sections) == 0
    return passed, len(issues), issues


# ============================================================
# MAIN RUNNER
# ============================================================
def run_depth_check(md_path: Path, cfg: DepthConfig = None) -> DepthReport:
    if cfg is None:
        cfg = DepthConfig()

    if not md_path.exists():
        print(f"ERROR: file not found: {md_path}", file=sys.stderr)
        sys.exit(2)

    content = md_path.read_text(encoding="utf-8")
    report = DepthReport(file=str(md_path), passed=True)

    # 1. Structural profile check (headings + markers)
    profile_failures = check_profile_content(cfg.profile_name, content)
    report.add(
        f"Profile structural markers ({cfg.profile_name})",
        len(profile_failures) == 0,
        f"{len(profile_failures)} issues",
        "0 issues",
        "; ".join(profile_failures) if profile_failures else "",
    )

    # 2. Sections
    passed, sec_count, found_count, missing = check_sections(content, cfg)
    report.add(
        f"Main sections count (##) & keywords",
        passed,
        f"{sec_count} sections ({found_count}/{len(cfg.required_section_keywords)} keywords)",
        f"≥{cfg.min_main_sections} sections ({len(cfg.required_section_keywords)} keywords)",
        f"Missing keywords: {missing}" if missing else "",
    )

    # 3. Subsections (###)
    passed, count = check_subsections(content, cfg)
    report.add("Subsections (### X.Y)", passed, count, cfg.min_subsections_total)

    # 4. Total size (word count & nonblank lines)
    passed, words, lines = check_total_size(content, cfg)
    report.add(
        "Total size (words / nonblank lines)",
        passed,
        f"{words} words / {lines} lines",
        f"{cfg.min_total_words} words / {cfg.min_total_lines} lines",
    )

    # 5. Mechanism chains
    passed, count = check_mechanism_chains(content, cfg)
    report.add("Mechanism chains (→ / Tầng 1..5)", passed, count, cfg.min_mechanism_chains)

    # 6. Examples
    passed, count = check_examples(content, cfg)
    report.add("Examples (ví dụ / VD)", passed, count, cfg.min_examples)

    # 7. Misconceptions / traps
    passed, count = check_misconceptions(content, cfg)
    report.add("Misconceptions / traps (bẫy / hay nhầm)", passed, count, cfg.min_misconceptions)

    # 8. Checkpoints
    passed, count = check_checkpoints(content, cfg)
    report.add("Self-check checkpoints", passed, count, cfg.min_checkpoints)

    # 9. Cases with solutions
    passed, count = check_cases_with_solutions(content, cfg)
    report.add("Clinical cases with solutions", passed, count, cfg.min_cases_with_solutions)

    # 10. Practical tips
    passed, count = check_tips(content, cfg)
    report.add("Tips bullets (Section 7)", passed, count, cfg.min_tips_bullets)

    # 11. Markdown tables (informational)
    passed, count = check_tables(content, cfg)
    report.add("Markdown tables (informational)", passed, count, cfg.min_markdown_tables, informational=True)

    # 12. Guidelines (informational)
    passed, count, found = check_guidelines(content, cfg)
    report.add(
        "Guideline mentions (informational)",
        passed,
        count,
        cfg.min_guideline_mentions,
        f"Found: {', '.join(found)}" if found else "",
        informational=True,
    )

    # 13. PMIDs unique (informational)
    passed, unique, total = check_pmids(content, cfg)
    report.add("Unique PMIDs (informational)", passed, unique, cfg.min_unique_pmids, informational=True)

    # 14. Refs count (informational)
    passed, count = check_refs_count(content, cfg)
    report.add("Papers in References (informational)", passed, count, cfg.min_papers_in_refs, informational=True)

    # 15. Diacritics
    passed, ratio = check_diacritics(content, cfg)
    report.add(
        "Vietnamese diacritics ratio",
        passed,
        f"{ratio:.2%}",
        f"{cfg.min_vietnamese_ratio:.0%}",
    )

    # 16. Specific claim near PMID (informational)
    passed, covered, uncovered = check_specific_claim_near_pmid(content, cfg)
    report.add(
        "Specific claims have PMID nearby (informational)",
        passed,
        f"{covered} covered / {uncovered} uncovered",
        "≥55% covered",
        informational=True,
    )
    # 17. Placeholders
    passed, count, found_placeholders = check_placeholders(content)
    report.add(
        "No leftover placeholders",
        passed,
        f"{count} found",
        "0 found",
        f"Found: {found_placeholders}" if found_placeholders else "",
    )

    # 18. Padding & duplicated text
    passed, count, issues = check_padding_and_duplicates(content)
    report.add(
        "No padding or duplicated sections",
        passed,
        f"{count} issues",
        "0 issues",
        "; ".join(issues[:3]) if issues else "",
    )

    # FOUNDATION / PHARMACOLOGY SPECIFIC CHECKS
    if getattr(cfg, "require_drug_dosage", False):
        passed, count = check_drug_dosage(content, cfg)
        report.add(
            "Drug dosage patterns",
            passed,
            count,
            cfg.min_drug_dosage_patterns,
        )

    if getattr(cfg, "require_basic_concepts", False):
        passed, count = check_basic_concepts(content, cfg)
        report.add(
            "Basic concepts explained",
            passed,
            count,
            cfg.min_basic_concepts,
        )

    if getattr(cfg, "require_section10_depth", False):
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
        help="Check all lesson MD files under Bai hoc y khoa",
    )
    parser.add_argument(
        "--root",
        type=str,
        default=None,
        help="Root folder để scan khi dùng --all",
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
        help="Lesson profile (default: foundation).",
    )
    args = parser.parse_args()
    cfg = get_depth_config(args.profile)

    if args.all:
        project_root = Path(r"F:\DL\mavisresearch\Bai hoc y khoa")
        scan_root = Path(args.root) if args.root else project_root
        if not scan_root.exists():
            print(f"ERROR: scan root not found: {scan_root}", file=sys.stderr)
            sys.exit(2)

        EXCLUDE_DIRS = {
            "10_Script Python", "09_Source - Markdown",
            "80_Legacy_by_format", "99_Inbox", "_duplicates_review",
            "07_Visual Summary - HTML", "08_Anki Deck - apkg",
        }
        EXCLUDE_STEM_SUFFIXES = (
            "_RESEARCH_BRIEF", "_research_brief",
            "_knowledge_check", "_knowledge_check_answer_key",
            "_remediation_gate_report", "_remediation_evidence",
            "_citation_audit", "_gate_report",
        )
        _date_re = re.compile(r"_\d{4}-\d{2}-\d{2}")

        def _is_lesson_file(p: Path) -> bool:
            if any(part in EXCLUDE_DIRS for part in p.parts):
                return False
            name = p.name
            stem = p.stem
            EXCLUDE_NAME_PREFIXES = ("QA-", "case-gia-lap-")
            if any(name.startswith(pfx) for pfx in EXCLUDE_NAME_PREFIXES):
                return False
            if not _date_re.search(stem):
                return False
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
