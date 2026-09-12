"""Shared, fail-closed parsing and evidence helpers for lesson verification."""
from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass
from pathlib import Path

VERIFICATION_TAGS = (
    "FETCHED",
    "ABSTRACT VERIFIED",
    "DATA VERIFIED",
    "FULL TEXT VERIFIED",
    "GUIDELINE VERIFIED",
)
TAG_RE = re.compile(r"\[(" + "|".join(re.escape(tag) for tag in VERIFICATION_TAGS) + r")\]", re.IGNORECASE)
LEGACY_TAG_RE = re.compile(
    r"\[(?:ABSTRACT MATCH|FULL VERIFIED|DIRECTION ONLY|TEXTBOOK|Thông tin cơ bản\s*[-–]\s*LLM verified)\]",
    re.IGNORECASE,
)
PMID_RE = re.compile(r"PMID\s*:?\s*\*{0,2}(\d{7,8})\*{0,2}", re.IGNORECASE)
BARE_PMID_RE = re.compile(r"^\d{7,8}$")
CLAIM_REF_RE = re.compile(r"\{claim\s*:\s*([A-Za-z0-9_.-]+)\}", re.IGNORECASE)
NUMERIC_RE = re.compile(
    r"(?:\b(?:RR|OR|HR|aOR|AOR|SMD|WMD|MD)\s*[=:]?\s*-?\d+(?:[.,]\d+)?|"
    r"95\s*%\s*CI|\bn\s*[=:]\s*[\d,]+|\bp\s*[<>=]\s*\d+(?:[.,]\d+)?|"
    r"\d+(?:[.,]\d+)?\s*(?:%|mg(?:/kg)?\b|mcg\b|µg\b|g\b|kg\b|mL\b|mmol/L\b|IU\b|UI\b|tuần\b|ngày\b|giờ\b|"
    r"Hz\b|kHz\b|mm/s\b|mm/mV\b|mV\b|ms\b|\bs\b))",
    re.IGNORECASE,
)
NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)?")


@dataclass(frozen=True)
class Claim:
    claim_id: str
    claim_text: str
    source_id: str
    verification: str
    quote: str
    line: int
    population: str = ""
    intervention_comparator: str = ""
    outcome: str = ""
    timepoint: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_tag(value: str) -> str:
    match = TAG_RE.search(value)
    return match.group(1).upper() if match else ""


def has_numeric_data(text: str) -> bool:
    return bool(NUMERIC_RE.search(text))


def extract_numbers(text: str) -> list[str]:
    return [match.group(0).replace(",", ".") for match in NUMBER_RE.finditer(text)]


def extract_claim_numbers(text: str) -> list[str]:
    """Extract only numbers attached to a clinical metric/unit, not years or PMIDs."""
    numbers: list[str] = []
    for metric in NUMERIC_RE.finditer(text):
        numbers.extend(extract_numbers(metric.group(0)))
    return numbers


def extract_metric_tokens(text: str) -> list[str]:
    """Extract normalized metric tokens (number + unit/symbol) for clinical metric checking."""
    tokens: list[str] = []
    for match in NUMERIC_RE.finditer(text):
        token = " ".join(match.group(0).lower().replace(",", ".").split())
        tokens.append(token)
    return tokens

def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return []
    return [cell.strip().replace("\\|", "|") for cell in re.split(r"(?<!\\)\|", stripped[1:-1])]


def _section(text: str, heading_pattern: str) -> tuple[str, int]:
    match = re.search(heading_pattern, text, re.IGNORECASE | re.MULTILINE)
    if not match:
        return "", 0
    tail = text[match.end():]
    next_heading = re.search(r"^##\s+", tail, re.MULTILINE)
    body = tail[:next_heading.start()] if next_heading else tail
    return body, text[:match.end()].count("\n") + 1


def extract_brief_claims(text: str) -> list[Claim]:
    """Parse every claim row under the locked claims section; never deduplicate by PMID."""
    body, first_line = _section(text, r"^##\s+\d+\.\s+Claims?[^\n]*$")
    if not body:
        return []

    claims: list[Claim] = []
    header: list[str] | None = None
    for offset, line in enumerate(body.splitlines(), 1):
        cells = split_markdown_row(line)
        if not cells:
            continue
        lowered = [cell.casefold() for cell in cells]
        if any("claim" in cell for cell in lowered) and any("pmid" in cell or "source" in cell for cell in lowered):
            header = lowered
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if header is None or len(cells) < 4:
            continue

        def first_index(predicate) -> int | None:
            return next((index for index, name in enumerate(header) if predicate(name)), None)

        def value_at(index: int | None) -> str:
            return cells[index].strip() if index is not None and index < len(cells) else ""

        claim_index = first_index(lambda name: "claim" in name and "id" not in name)
        source_index = first_index(lambda name: "pmid" in name or "source" in name or "nguồn" in name)
        tag_index = first_index(lambda name: "verification" in name or "tag" in name)
        quote_index = first_index(lambda name: "quote" in name or "trích" in name)
        id_index = first_index(lambda name: "claim" in name and "id" in name)
        claim_text = value_at(claim_index)
        source = value_at(source_index)
        tag_cell = value_at(tag_index)
        quote = value_at(quote_index)
        if not claim_text or not source:
            continue
        pmid_match = PMID_RE.search(source)
        source_id = pmid_match.group(1) if pmid_match else source.strip()
        if not BARE_PMID_RE.fullmatch(source_id):
            continue
        claim_id = value_at(id_index) or f"C-{len(claims) + 1:03d}"
        claims.append(Claim(
            claim_id=claim_id,
            claim_text=claim_text,
            source_id=source_id,
            verification=normalize_tag(tag_cell),
            quote=quote.strip(' "'),
            line=first_line + offset,
            population=value_at(first_index(lambda name: "population" in name or "quần thể" in name)),
            intervention_comparator=value_at(first_index(lambda name: any(term in name for term in ("intervention", "can thiệp", "comparator", "đối chứng")))),
            outcome=value_at(first_index(lambda name: "outcome" in name or "kết cục" in name)),
            timepoint=value_at(first_index(lambda name: "timepoint" in name or "thời điểm" in name)),
        ))
    return claims


def extract_lesson_claims(text: str) -> list[Claim]:
    """Return one claim occurrence per PMID mention outside the reference section, using its containing line."""
    claims: list[Claim] = []
    lines = text.splitlines()

    ref_match = re.search(r"^##\s+(\d+\.\s+)?(Tài liệu tham khảo|References?)[^\n]*$", text, re.IGNORECASE | re.MULTILINE)
    ref_start_line = text[:ref_match.start()].count("\n") + 1 if ref_match else len(lines) + 1

    for line_num, line in enumerate(lines, 1):
        if line_num >= ref_start_line:
            break
        line_str = line.strip()
        if not line_str:
            continue
        pmid_matches = list(PMID_RE.finditer(line_str))
        if not pmid_matches:
            continue

        for occurrence, match in enumerate(pmid_matches, 1):
            prev_end = pmid_matches[occurrence - 2].end() if occurrence > 1 else 0
            next_start = pmid_matches[occurrence].start() if occurrence < len(pmid_matches) else len(line_str)
            segment = line_str[prev_end:next_start]

            ref_match_claim = CLAIM_REF_RE.search(segment) or CLAIM_REF_RE.search(line_str)
            tag_match = TAG_RE.search(segment) or TAG_RE.search(line_str)

            claims.append(Claim(
                claim_id=ref_match_claim.group(1) if ref_match_claim else f"L{line_num}-{occurrence}",
                claim_text=line_str,
                source_id=match.group(1),
                verification=tag_match.group(1).upper() if tag_match else "",
                quote="",
                line=line_num,
            ))
    return claims


def validate_tag_policy(claim: Claim, source_kind: str) -> list[str]:
    failures: list[str] = []
    numeric = has_numeric_data(claim.claim_text)
    if not claim.verification:
        failures.append("missing one of the five canonical verification tags")
        return failures
    if claim.verification == "FETCHED" and numeric:
        failures.append("[FETCHED] cannot authorize a numeric claim")
    if claim.verification == "ABSTRACT VERIFIED" and numeric:
        failures.append("numeric claims require [DATA VERIFIED] or [FULL TEXT VERIFIED]")
    if claim.verification == "DATA VERIFIED" and source_kind not in {"abstract", "full_text"}:
        failures.append("[DATA VERIFIED] requires an abstract/full-text evidence source")
    if claim.verification == "FULL TEXT VERIFIED" and source_kind != "full_text":
        failures.append("[FULL TEXT VERIFIED] requires full text")
    if claim.verification == "GUIDELINE VERIFIED" and source_kind != "guideline":
        failures.append("[GUIDELINE VERIFIED] requires the guideline evidence pipeline")
    return failures
