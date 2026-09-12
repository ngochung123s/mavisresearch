"""Provider-neutral evidence bundle validation and seven offline release gates."""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA_VERSION = "1.0"
METADATA_MAX_AGE_HOURS = 72
RETRACTION_MAX_AGE_HOURS = 24
PMID_RE = re.compile(r"PMID\s*:?\s*\*{0,2}(\d{7,8})\*{0,2}", re.I)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
WORD_RE = re.compile(r"[A-Za-zÀ-ỹ0-9]{4,}")
NUMERIC_RE = re.compile(r"(?:\b(?:RR|OR|HR|CI|n)\s*[=:]?\s*\d|\d+(?:[.,]\d+)?\s*(?:\\?%|mg|g|kg|mm|cm|mL|L|mmol/L|mg/dL|Hz|ms|mV)\b)", re.I)
NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:[.,]\d+)?")
GUIDELINE_TYPES = {"guideline", "practice guideline", "consensus statement", "clinical practice guideline"}


BLOCKING_INTEGRITY = {"retracted", "expression_of_concern"}

class BundleError(ValueError):
    pass


def canonical_document_type(value: Any) -> str:
    """Normalize a document type for semantic comparison without rewriting provenance."""
    return " ".join(str(value or "").split()).casefold()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def content_hash(bundle: dict) -> str:
    payload = dict(bundle)
    payload.pop("content_hash", None)
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_time(value: str, field: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        raise BundleError(f"invalid {field}: {value!r}") from exc
    if parsed.tzinfo is None:
        raise BundleError(f"{field} must include timezone")
    return parsed.astimezone(timezone.utc)


def age_hours(value: str, now: datetime | None = None) -> float:
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    return (current - parse_time(value, "timestamp")).total_seconds() / 3600


def extract_pmids(text: str) -> list[str]:
    return list(dict.fromkeys(PMID_RE.findall(text)))


def meaningful_words(text: str) -> set[str]:
    stop = {"with", "from", "that", "this", "were", "have", "been", "trong", "được", "những", "claim", "pmid", "verified"}
    return {word.casefold() for word in WORD_RE.findall(text) if word.casefold() not in stop and not word.isdigit()}


def overlap_ratio(left: str, right: str) -> float:
    words = meaningful_words(left)
    return 1.0 if not words else len(words & meaningful_words(right)) / len(words)


@dataclass(frozen=True)
class EvidenceBundle:
    path: Path
    data: dict
    records: dict[str, dict]

    def record_for_pmid(self, pmid: str) -> dict | None:
        return self.records.get(f"pmid:{pmid}")

    def record_for_doi(self, doi: str) -> dict | None:
        wanted = doi.casefold()
        return next((record for record in self.records.values() if str(record.get("identifiers", {}).get("doi") or "").casefold() == wanted), None)

    def record_for_official_id(self, official_id: str) -> dict | None:
        direct = self.records.get(f"official:{official_id}")
        if direct:
            return direct
        return next((record for record in self.records.values() if str(record.get("identifiers", {}).get("official_id") or "") == official_id), None)


def load_bundle(path: Path | str, *, now: datetime | None = None, require_fresh: bool = True) -> EvidenceBundle:
    bundle_path = Path(path).resolve()
    try:
        data = json.loads(bundle_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BundleError(f"cannot read evidence bundle: {exc}") from exc
    required = {"schema_version", "created_at", "records", "raw_objects", "content_hash", "providers"}
    missing = sorted(required - data.keys())
    if missing:
        raise BundleError(f"bundle missing fields: {missing}")
    if data["schema_version"] != SCHEMA_VERSION:
        raise BundleError(f"unsupported schema_version {data['schema_version']!r}")
    expected = content_hash(data)
    if data["content_hash"] != expected:
        raise BundleError("bundle content hash mismatch")
    if not isinstance(data["records"], dict) or not isinstance(data["raw_objects"], list):
        raise BundleError("records/raw_objects have invalid types")
    base = bundle_path.parent
    raw_hashes: set[str] = set()
    for row in data["raw_objects"]:
        for field in ("provider", "retrieved_at", "sha256", "path", "media_type", "license"):
            if field not in row:
                raise BundleError(f"raw object missing {field}")
        cache_root_value = data.get("cache_root")
        cache_root = Path(cache_root_value).resolve() if cache_root_value else base
        raw_path = (cache_root / row["path"]).resolve()
        try:
            raw_path.relative_to(cache_root)
        except ValueError as exc:
            raise BundleError("raw object escapes cache root") from exc
        if not raw_path.is_file() or sha256_file(raw_path) != row["sha256"]:
            raise BundleError(f"raw hash mismatch: {row['path']}")
        raw_hashes.add(row["sha256"])
    for key, record in data["records"].items():
        if not isinstance(record, dict) or not record.get("providers"):
            raise BundleError(f"record {key} has no provider provenance")
        if record.get("exists") is True:
            providers = set(record.get("providers", []))
            identifiers = record.get("identifiers", {})
            if identifiers.get("pmid") and not {"europe_pmc_metadata", "openalex"}.issubset(providers):
                raise BundleError(f"record {key} lacks Europe PMC/OpenAlex corroboration")
            if identifiers.get("pmid") and identifiers.get("doi") and "crossref_retraction_watch" not in providers:
                raise BundleError(f"record {key} lacks Crossref/Retraction Watch corroboration")
            integrity_provider = record.get("integrity", {}).get("provider")
            if integrity_provider not in {"crossref_retraction_watch", "official_source"}:
                raise BundleError(f"record {key} has untrusted integrity provider")
        for digest in record.get("raw_sha256", []):
            if digest not in raw_hashes:
                raise BundleError(f"record {key} references unknown raw hash")
        if require_fresh:
            if age_hours(record.get("metadata_checked_at", ""), now) > METADATA_MAX_AGE_HOURS:
                raise BundleError(f"stale metadata for {key}")
            integrity = record.get("integrity", {})
            if age_hours(integrity.get("checked_at", ""), now) > RETRACTION_MAX_AGE_HOURS:
                raise BundleError(f"stale retraction/correction status for {key}")
    return EvidenceBundle(bundle_path, data, data["records"])


def expected_identity(context: str) -> tuple[str | None, str | None]:
    doi = DOI_RE.search(context)
    title = None
    for marker in ("Title:", "Tiêu đề:", "Expected title:"):
        if marker.casefold() in context.casefold():
            tail = re.split(re.escape(marker), context, maxsplit=1, flags=re.I)[1]
            title = tail.split("|")[0].splitlines()[0].strip(" *`.-")
            break
    return (doi.group(0).rstrip(".,;)").casefold() if doi else None, title)


def seven_gate_check(record: dict | None, *, claim: str = "", expected_doi: str | None = None,
                     expected_title: str | None = None, topic: str | None = None,
                     verification: str = "") -> dict[str, dict]:
    gates: dict[str, dict] = {}
    exists = bool(record and record.get("exists") is True)
    gates["existence"] = {"status": "PASS" if exists else "BLOCK", "reason": "record exists" if exists else "no exact provider record"}
    if not exists:
        for name in ("exact_identity", "topic_relevance", "claim_abstract", "numeric_full_text", "guideline_authority", "integrity_freshness"):
            gates[name] = {"status": "BLOCK", "reason": "existence gate failed"}
        return gates
    conflicts = record.get("conflicts", [])
    identifiers = record.get("identifiers", {})
    identity_failures = list(conflicts)
    if expected_doi and identifiers.get("doi", "").casefold() != expected_doi.casefold():
        identity_failures.append("PMID-DOI conflict")
    if expected_title and overlap_ratio(expected_title, record.get("title", "")) < 0.65:
        identity_failures.append("title mismatch")
    gates["exact_identity"] = {"status": "BLOCK" if identity_failures else "PASS", "reason": "; ".join(identity_failures) or "identifiers agree"}
    topic_text = " ".join([record.get("title", ""), record.get("abstract", ""), " ".join(record.get("topics", []))])
    relevance_target = topic or claim
    relevant = bool(relevance_target) and overlap_ratio(relevance_target, topic_text) >= (0.12 if topic else 0.08)
    gates["topic_relevance"] = {"status": "PASS" if relevant else "BLOCK", "reason": f"overlap={overlap_ratio(relevance_target, topic_text):.2f}"}
    abstract = record.get("abstract", "")
    claim_match = bool(abstract) and (not claim or overlap_ratio(claim, abstract) >= 0.08)
    gates["claim_abstract"] = {"status": "PASS" if claim_match else "BLOCK", "reason": "abstract supports claim tokens" if claim_match else "missing/irrelevant abstract"}
    numeric = bool(NUMERIC_RE.search(claim))
    full = record.get("full_text", {})
    quote = record.get("claim_quote", "")
    evidence_text = quote or abstract
    claim_numbers = {value.replace(",", ".") for value in NUMBER_RE.findall(claim)}
    evidence_numbers = {value.replace(",", ".") for value in NUMBER_RE.findall(evidence_text)}
    numeric_source_ok = bool(evidence_text) and claim_numbers.issubset(evidence_numbers)
    if verification.upper() == "FULL TEXT VERIFIED":
        numeric_source_ok = numeric_source_ok and bool(full.get("available")) and bool(full.get("reuse_suitable"))
    numeric_ok = not numeric or numeric_source_ok
    gates["numeric_full_text"] = {"status": "PASS" if numeric_ok else "BLOCK", "reason": "not numeric" if not numeric else "exact numbers require abstract evidence or suitably licensed full text"}
    guideline = verification.upper() == "GUIDELINE VERIFIED"
    pubtypes = {canonical_document_type(value) for value in record.get("publication_types", [])}
    authority = record.get("official_source", {})
    translation_ok = not authority.get("translation_of") or authority.get("endorsement_status") == "endorsed"
    current = authority.get("superseded_by") in {None, "", False} and authority.get("current_version", True) is True
    guideline_ok = not guideline or (
        bool(pubtypes & GUIDELINE_TYPES)
        and authority.get("authority_verified") is True
        and canonical_document_type(authority.get("document_type")) in GUIDELINE_TYPES
        and translation_ok
        and current
    )
    authority_reason = "not a guideline claim" if not guideline else "official, current, endorsed guideline authority/document type required"
    gates["guideline_authority"] = {"status": "PASS" if guideline_ok else "BLOCK", "reason": authority_reason}
    integrity = record.get("integrity", {})
    state = integrity.get("status", "unknown")
    corrections = integrity.get("corrections", [])
    unresolved = [row for row in corrections if row.get("requires_adjudication", True) and row.get("adjudication") not in {"unaffected", "resolved"}]
    fresh = age_hours(integrity.get("checked_at", "")) <= RETRACTION_MAX_AGE_HOURS
    integrity_ok = fresh and state not in BLOCKING_INTEGRITY and not unresolved
    gates["integrity_freshness"] = {"status": "PASS" if integrity_ok else "BLOCK", "reason": f"status={state}; fresh={fresh}; unresolved_corrections={len(unresolved)}"}
    return gates


def document_checks(text: str, bundle: EvidenceBundle, *, topic: str | None = None) -> list[dict]:
    rows = []
    for match in PMID_RE.finditer(text):
        line_start = text.rfind("\n", 0, match.start()) + 1
        line_end = text.find("\n", match.end())
        context = text[line_start: len(text) if line_end < 0 else line_end]
        verification_match = re.search(r"\[(FETCHED|ABSTRACT VERIFIED|DATA VERIFIED|FULL TEXT VERIFIED|GUIDELINE VERIFIED)\]", context, re.I)
        doi, title = expected_identity(context)
        gates = seven_gate_check(bundle.record_for_pmid(match.group(1)), claim=context, expected_doi=doi, expected_title=title, topic=topic, verification=verification_match.group(1) if verification_match else "")
        rows.append({"pmid": match.group(1), "context": context, "gates": gates, "status": "PASS" if all(g["status"] == "PASS" for g in gates.values()) else "BLOCK"})
    return rows
