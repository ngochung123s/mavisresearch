#!/usr/bin/env python3
"""Offline, occurrence-based citation audit for medical lesson releases.

The audit consumes ``--evidence-bundle`` only: no provider call or cache fallback
is allowed. It preserves every citation occurrence, applies provider-neutral
identity/topic/claim/integrity gates, then maps journal quality and guideline
registry policy. Any BLOCK or WARN exits 2 for fail-closed release semantics.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path
from typing import Optional

from evidence_bundle import BundleError, load_bundle, seven_gate_check

try:
    from docx import Document
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False

# ============================================================
# CONFIG
# ============================================================
SCRIPT_DIR = Path(__file__).parent
JOURNAL_QUARTILE_FILE = SCRIPT_DIR / "journal_quartile.json"
GUIDELINE_REGISTRY_FILE = SCRIPT_DIR / "guideline_registry.json"
EVIDENCE_BUNDLE_REQUIRED = True

# Specific number claim patterns (for strictness mode)
SPECIFIC_CLAIM_PATTERNS = [
    (r'\bRR\s*[=:]?\s*\d+\.?\d*', 'RR'),
    (r'\bOR\s*[=:]?\s*\d+\.?\d*', 'OR'),
    (r'\bHR\s*[=:]?\s*\d+\.?\d*', 'HR'),
    (r'\b95%?\s*CI\b', 'CI'),
    (r'\bp\s*[=<>]\s*0?\.\d+', 'p-value'),
    (r'\(n\s*=\s*\d+\)', 'sample n'),
    (r'\bn\s*=\s*\d{2,}', 'n=NNN'),
    (r'\d+\.?\d*\s*-\s*\d+\.?\d*', 'range'),
    (r'\d+\.?\d*\s*%', 'percent'),
    (r'>\s*\d+%', 'gt-percent'),
    (r'<\s*\d+%', 'lt-percent'),
    (r'\d+\s*-\s*\d+\s*mm', 'mm range'),
    (r'\d+\s*IU[/\s]', 'IU'),
    (r'\d+\s*mg/dl', 'mg/dL'),
    (r'\d+\s*pg/mL', 'pg/mL'),
    (r'\d+\s*ng/mL', 'ng/mL'),
    (r'\d+\s*mIU/mL', 'mIU/mL'),
    (r'giảm\s+\d+\s*%', 'VN-giam %'),
    (r'tăng\s+\d+\s*%', 'VN-tang %'),
    (r'\d+\s*-\s*\d+\s*tuần', 'VN-tuan'),
    (r'\d+\s*năm', 'VN-nam'),
    (r'\d+\.\d+\s*-\s*\d+\.\d+', 'CI decimal'),
]

# Society patterns
SOCIETIES = ['ASRM', 'ACOG', 'RCOG', 'ESHRE', 'ISUOG', 'NICE', 'FIGO', 'WHO', 'SOGC', 'RANZCOG', 'SMFM', 'AIUM', 'VSH/VNHA', 'ESC', 'AHA/ACC', 'ADA/EASD', 'ADA', 'JBDS']

# ============================================================
# MAIN CLASS
# ============================================================
class CitationAuditor:
    def __init__(self, journal_quartile_file=None, guideline_registry_file=None, verbose=True, evidence_bundle=None):
        self.journal_file = journal_quartile_file or JOURNAL_QUARTILE_FILE
        self.guideline_file = guideline_registry_file or GUIDELINE_REGISTRY_FILE
        self.verbose = verbose
        self.journal_table = self._load_json(self.journal_file)
        self.guideline_table = self._load_json(self.guideline_file)
        self.journal_map = self._build_journal_map()
        self.aliases = self.journal_table.get('ALIASES', {})
        if evidence_bundle is None:
            raise BundleError("--evidence-bundle is required")
        self.bundle = load_bundle(Path(evidence_bundle))
    def _load_json(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _build_journal_map(self):
        """Build flat journal -> quartile map."""
        jmap = {}
        for q_key in ['Q1', 'Q2', 'Q3', 'Q4_AVOID']:
            for jname, info in self.journal_table.get(q_key, {}).items():
                if isinstance(info, dict) and 'if' in info:
                    jmap[jname] = {'quartile': q_key, 'tier': self._quartile_to_tier(q_key), **info}
        return jmap

    def _quartile_to_tier(self, q):
        return {'Q1': 1, 'Q2': 2, 'Q3': 3, 'Q4_AVOID': 4}.get(q, 3)

    def read_file(self, file_path):
        p = Path(file_path)
        if p.suffix.lower() == '.docx':
            if not HAS_DOCX:
                return None, "python-docx not installed"
            doc = Document(str(p))
            text = '\n'.join([para.text for para in doc.paragraphs])
            for table in doc.tables:
                for row in table.rows:
                    for cell in row.cells:
                        text += '\n' + cell.text
            return text, None
        elif p.suffix.lower() in ('.md', '.txt'):
            return p.read_text(encoding='utf-8', errors='ignore'), None
        else:
            return None, f"Unsupported file extension: {p.suffix}"

    def extract_citations(self, text):
        """Extract all PMIDs and guideline citations from text."""
        citations = []

        # 1. Extract PMIDs (variants: PMID: 12345, PMID 12345, (PMID 12345))
        for m in re.finditer(r'PMID[:\s]*(\d{6,9})', text, re.IGNORECASE):
            citations.append({
                'type': 'pmid',
                'value': m.group(1),
                'span': m.span(),
                'raw': m.group(0),
            })

        # 2. Extract guideline citations [SOCIETY ...]
        for society in SOCIETIES:
            # Patterns:
            #   [ASRM 2023 - ...]
            #   [ACOG PB #175]
            #   [RCOG GTG-75]
            #   [NICE NG137]
            patterns = [
                rf'\[{society}\s+\d{{4}}\s*-\s*[^\]]+\]',  # [SOCIETY YYYY - ...]
                rf'\[{society}\s+(?:PB\s*#?\s*\d+|GTG-?\d+|CO\s*#?\s*\d+|NG\d+)(?:\s*[^\]]*)?\]',  # [SOCIETY PB#175]
            ]
            for pat in patterns:
                for m in re.finditer(pat, text):
                    citations.append({
                        'type': 'guideline',
                        'society': society,
                        'value': m.group(0),
                        'span': m.span(),
                        'raw': m.group(0),
                    })

        # Sort by position
        citations.sort(key=lambda c: c['span'][0])

        # Keep every occurrence: release verification is occurrence-based.
        return citations

    def detect_specific_claim(self, text, span, window=300):
        """Check if citation is in a context with specific numbers (RR, CI, %, n=)."""
        start = max(0, span[0] - window)
        end = min(len(text), span[1] + window)
        context = text[start:end]
        matches = []
        for pattern, label in SPECIFIC_CLAIM_PATTERNS:
            if re.search(pattern, context, re.IGNORECASE):
                matches.append(label)
        return (len(matches) > 0), matches

    def verify_pmid(self, pmid):
        """Read normalized metadata from the already validated bundle."""
        item = self.bundle.record_for_pmid(pmid)
        if not item or item.get('exists') is not True:
            return {'pmid': pmid, 'status': 'NOT_FOUND'}
        if item.get('conflicts'):
            return {'pmid': pmid, 'status': 'ERROR', 'error': '; '.join(item['conflicts'])}
        return {
            'pmid': pmid,
            'status': 'OK',
            'year': item.get('year', 'NA'),
            'title': item.get('title', 'NA'),
            'author': item.get('author', 'NA'),
            'journal': item.get('journal', 'NA'),
            'article_type': ', '.join(item.get('publication_types', [])[:2]),
            'pubtypes': item.get('publication_types', []),
        }

    @staticmethod
    def classify_evidence(pmid_info):
        """Classify evidence hierarchy: study design, GRADE equivalent, evidence level.
        
        Returns dict with:
          - study_design: RCT, Meta-Analysis, Systematic Review, Cohort, Case-Control, 
                          Case Report, Review, Guideline, Editorial, Other
          - evidence_level: 1a (SR/MA of RCTs), 1b (RCT), 2a (SR of cohorts), 
                            2b (Cohort), 3 (Case-Control), 4 (Case Series), 
                            5 (Expert Opinion)
          - is_guideline: bool
          - is_systematic_review: bool
        """
        pubtypes = [p.lower() for p in pmid_info.get('pubtypes', [])]
        title = pmid_info.get('title', '').lower()
        atype = pmid_info.get('article_type', '').lower()
        
        evidence = {
            'study_design': 'Other',
            'evidence_level': 5,
            'is_guideline': False,
            'is_meta_analysis': False,
            'is_systematic_review': False,
            'is_rct': False,
        }
        
        # Guideline detection
        if 'practice guideline' in atype or 'guideline' in atype:
            evidence['study_design'] = 'Guideline'
            evidence['evidence_level'] = 1
            evidence['is_guideline'] = True
            return evidence
        
        if 'guideline' in title or 'consensus' in title:
            evidence['study_design'] = 'Guideline/Consensus'
            evidence['evidence_level'] = 1 if 'guideline' in title else 3
            evidence['is_guideline'] = 'guideline' in title
            return evidence
        
        # Meta-Analysis
        if 'meta-analysis' in atype or 'meta-analysis' in title:
            evidence['study_design'] = 'Meta-Analysis'
            evidence['evidence_level'] = 1
            evidence['is_meta_analysis'] = True
            return evidence
        
        # Systematic Review
        if 'systematic review' in atype or 'systematic review' in title:
            evidence['study_design'] = 'Systematic Review'
            evidence['evidence_level'] = 1
            evidence['is_systematic_review'] = True
            return evidence
        
        # RCT
        if 'randomized controlled trial' in atype or 'randomized' in title:
            evidence['study_design'] = 'RCT'
            evidence['evidence_level'] = 2
            evidence['is_rct'] = True
            return evidence
        
        # Review
        if 'review' in atype:
            evidence['study_design'] = 'Review'
            evidence['evidence_level'] = 5
            return evidence
        
        # Editorial / Opinion
        if 'editorial' in atype or 'comment' in atype:
            evidence['study_design'] = 'Editorial/Opinion'
            evidence['evidence_level'] = 5
            return evidence
        
        # Cohort / Observational
        if 'journal article' in atype:
            # Check title for clues
            if 'cohort' in title or 'retrospective' in title:
                evidence['study_design'] = 'Cohort (Retrospective)'
                evidence['evidence_level'] = 4
            elif 'prospective' in title:
                evidence['study_design'] = 'Cohort (Prospective)'
                evidence['evidence_level'] = 3
            elif 'case-control' in title:
                evidence['study_design'] = 'Case-Control'
                evidence['evidence_level'] = 4
            elif 'case report' in title or 'case series' in title:
                evidence['study_design'] = 'Case Report/Series'
                evidence['evidence_level'] = 5
            else:
                evidence['study_design'] = 'Observational'
                evidence['evidence_level'] = 4
            return evidence
        
        # Case Reports
        if 'case reports' in atype:
            evidence['study_design'] = 'Case Report'
            evidence['evidence_level'] = 5
            return evidence
        
        # Clinical Trial (not specified as RCT)
        if 'clinical trial' in atype:
            evidence['study_design'] = 'Clinical Trial'
            evidence['evidence_level'] = 2
            return evidence
        
        return evidence

    def resolve_journal(self, journal_str):
        """Resolve journal name to tier."""
        if not journal_str or journal_str == 'NA':
            return None, 'No journal name'
        # Check direct match
        if journal_str in self.journal_map:
            entry = self.journal_map[journal_str]
            return entry, f"{entry['quartile']} (IF {entry.get('if', 'NA')})"
        # Check aliases
        canonical = self.aliases.get(journal_str, self.aliases.get(journal_str.lower(), journal_str))
        if canonical in self.journal_map:
            entry = self.journal_map[canonical]
            return entry, f"{entry['quartile']} (IF {entry.get('if', 'NA')})"
        # Check case-insensitive match in journal_map
        for jname, entry in self.journal_map.items():
            if jname.lower() == journal_str.lower() or jname.lower() == canonical.lower():
                return entry, f"{entry['quartile']} (IF {entry.get('if', 'NA')})"
        return None, f"Unknown journal: {journal_str}"

    def match_guideline(self, citation_text):
        """Try to match a guideline citation to registry entry.
        Strategy:
        1. Exact match (preferred)
        2. Starts-with match (longest gl_id wins)
        3. No fuzzy char-prefix (can cause false matches)
        """
        clean = citation_text.strip('[]').strip()
        # Collect all candidate gl_ids sorted by length descending
        candidates = []
        for society_key, society_data in self.guideline_table.items():
            if society_key == '_meta' or not isinstance(society_data, dict):
                continue
            if 'guidelines' not in society_data:
                continue
            for gl_id, gl_data in society_data['guidelines'].items():
                candidates.append((gl_id, gl_data, society_data))
        # Sort by gl_id length desc (longest first = most specific)
        candidates.sort(key=lambda x: -len(x[0]))

        # 1. Exact match
        for gl_id, gl_data, society in candidates:
            if clean == gl_id:
                return gl_id, gl_data, society

        # 2. Starts-with match (longest wins)
        for gl_id, gl_data, society in candidates:
            if clean.startswith(gl_id):
                return gl_id, gl_data, society

        return None, None, None

    def check_supersede(self, gl_data):
        """Check if guideline is superseded."""
        if 'superseded_by' in gl_data:
            return True, gl_data['superseded_by']
        return False, None

    def audit_citation(self, citation, text):
        """Audit a single citation."""
        has_specific, patterns = self.detect_specific_claim(text, citation['span'])
        entry = {
            'citation': citation['raw'],
            'type': citation['type'],
            'has_specific_claim': has_specific,
            'specific_patterns': patterns,
            'tier': None,
            'tier_reason': '',
            'verdict': '',
            'severity': 'pass',  # pass | warn | block
            'details': {},
        }

        if citation['type'] == 'pmid':
            pmid_info = self.verify_pmid(citation['value'])
            entry['details']['pmid_info'] = pmid_info
            
            # Add evidence hierarchy
            evidence = self.classify_evidence(pmid_info)
            entry['details']['evidence'] = evidence

            if pmid_info.get('status') == 'NOT_FOUND':
                entry['verdict'] = 'NOT_FOUND (PMID không tồn tại)'
                entry['severity'] = 'block'
                entry['tier'] = 5
                entry['tier_reason'] = 'PMID invalid'
                return entry
            if pmid_info.get('status') == 'ERROR':
                entry['verdict'] = f"BLOCK: {pmid_info.get('error', 'provider conflict')}"
                entry['severity'] = 'block'
                entry['tier'] = None
                entry['tier_reason'] = 'bundle identity conflict'
                return entry
            # Extract claim context around the citation occurrence (symmetric window)
            context_start = max(0, citation['span'][0] - 300)
            context_end = min(len(text), citation['span'][1] + 300)
            evidence_gates = seven_gate_check(
                self.bundle.record_for_pmid(citation['value']),
                claim=text[context_start:context_end],
            )
            failed_gates = [name for name, gate in evidence_gates.items() if gate['status'] != 'PASS']
            if failed_gates:
                entry['verdict'] = f"BLOCK evidence gates: {', '.join(failed_gates)}"
                entry['severity'] = 'block'
                entry['tier_reason'] = 'provider-neutral evidence gate failure'
                return entry

            journal_entry, reason = self.resolve_journal(pmid_info['journal'])
            if journal_entry:
                tier = journal_entry['tier']
                entry['tier'] = tier
                entry['tier_reason'] = reason
                entry['details']['journal'] = pmid_info['journal']
                entry['details']['quartile'] = journal_entry['quartile']
                entry['details']['if'] = journal_entry.get('if', 'NA')
            else:
                tier = 3  # Unknown journal default
                entry['tier'] = tier
                entry['tier_reason'] = reason
                entry['details']['journal'] = pmid_info['journal']
                entry['details']['quartile'] = 'UNKNOWN'

            # Apply strictness
            if tier == 4:  # Q4_AVOID
                if has_specific:
                    entry['verdict'] = 'BLOCK (Q4 + specific claim)'
                    entry['severity'] = 'block'
                else:
                    entry['verdict'] = 'WARN (Q4 paper, direction only)'
                    entry['severity'] = 'warn'
            elif tier in (1, 2) and has_specific:
                entry['verdict'] = 'WARN (Q1/Q2 + specific claim, cần verify full text)'
                entry['severity'] = 'warn'
            elif tier == 3 and has_specific:
                if 'UNKNOWN' in entry.get('details', {}).get('quartile', ''):
                    entry['verdict'] = 'WARN (Unknown journal + specific claim - VERIFY TOPIC RELEVANCE!)'
                else:
                    entry['verdict'] = 'WARN (Q3 + specific claim, nên tìm Q1/Q2 source)'
                entry['severity'] = 'warn'
            elif tier == 3:
                if 'UNKNOWN' in entry.get('details', {}).get('quartile', ''):
                    entry['verdict'] = 'WARN (Unknown journal - verify relevance)'
                else:
                    entry['verdict'] = 'OK (Q3, direction only)'
                entry['severity'] = 'warn' if 'UNKNOWN' in entry.get('details', {}).get('quartile', '') else 'pass'
            elif tier in (1, 2):
                entry['verdict'] = 'OK'
                entry['severity'] = 'pass'
            else:
                entry['verdict'] = f'OK (tier {tier})'
                entry['severity'] = 'pass'


        elif citation['type'] == 'guideline':
            gl_id, gl_data, society = self.match_guideline(citation['value'])
            if gl_id:
                entry['tier'] = 0
                entry['tier_reason'] = f"Guideline: {gl_id} ({society['society']})"
                entry['details']['guideline_id'] = gl_id
                entry['details']['society'] = society['society']
                entry['details']['year'] = gl_data.get('year', 'NA')
                entry['details']['title'] = gl_data.get('title', 'NA')
                superseded, replacement = self.check_supersede(gl_data)
                if superseded:
                    entry['verdict'] = f'SUPERSEDED → dùng {replacement}'
                    entry['severity'] = 'warn'
                else:
                    entry['verdict'] = 'OK (Tier 0 guideline)'
                    entry['severity'] = 'pass'
            else:
                entry['tier'] = None
                entry['tier_reason'] = 'Guideline không có trong registry'
                entry['verdict'] = 'UNKNOWN_GUIDELINE (verify thủ công hoặc thêm vào registry)'
                entry['severity'] = 'warn'
        return entry

    def audit_file(self, file_path):
        """Run full audit on a file."""
        text, err = self.read_file(file_path)
        if err:
            return {'error': err, 'file': str(file_path), 'summary': {'total': 0, 'pass': 0, 'warn': 0, 'block': 1}, 'citations': []}

        citations = self.extract_citations(text)
        if self.verbose:
            print(f"[citation_audit] {file_path}: {len(citations)} citation occurrences", file=sys.stderr)

        results = []
        for cit in citations:
            entry = self.audit_citation(cit, text)
            results.append(entry)

        summary = {
            'total': len(results),
            'pass': sum(1 for r in results if r['severity'] == 'pass'),
            'warn': sum(1 for r in results if r['severity'] == 'warn'),
            'block': sum(1 for r in results if r['severity'] == 'block'),
        }

        return {
            'file': str(file_path),
            'summary': summary,
            'citations': results,
        }

    def print_console_report(self, result):
        """Print human-readable report to console."""
        s = result['summary']
        print()
        print('=' * 80)
        print(f"  CITATION AUDIT: {result['file']}")
        print('=' * 80)
        print()
        print(f"  Total: {s['total']}  |  Pass: {s['pass']}  |  Warn: {s['warn']}  |  BLOCK: {s['block']}")
        print()

        if not result['citations']:
            print("  (khong co citation nao de audit)")
            return

        for i, c in enumerate(result['citations'], 1):
            v = c['verdict']
            t = c.get('tier')
            tr = c.get('tier_reason', '')
            sc = ' [SPECIFIC CLAIM]' if c.get('has_specific_claim') else ''

            icon = {'pass': '✓', 'warn': '!', 'block': 'X'}.get(c['severity'], '?')

            print(f"  [{icon}] #{i}  {v}")
            print(f"      Citation: {c['citation']}")
            print(f"      Tier: {t} - {tr}{sc}")

            if c.get('details', {}).get('pmid_info'):
                pi = c['details']['pmid_info']
                if pi.get('status') == 'OK':
                    print(f"      Paper: {pi.get('title', '')[:90]}")
                    print(f"      Journal: {pi.get('journal', '')} ({pi.get('year', '')})")
                    print(f"      Author: {pi.get('author', '')}")

            if c.get('details', {}).get('title'):
                print(f"      Guideline title: {c['details']['title'][:90]}")
                print(f"      Year: {c['details']['year']}")

            if c.get('specific_patterns'):
                print(f"      Specific patterns detected: {', '.join(c['specific_patterns'])}")

            print()


def format_markdown_report(result):
    """Format audit result as markdown."""
    s = result['summary']
    md = f"""# Citation Audit Report

**File:** `{result['file']}`

## Summary

| Metric | Count |
|---|---|
| Total citations | {s['total']} |
| Pass (OK) | {s['pass']} |
| Warn | {s['warn']} |
| **Block** | **{s['block']}** |

## Citations

| # | Citation | Type | Tier | Specific? | Verdict |
|---|---|---|---|---|---|
"""
    for i, c in enumerate(result['citations'], 1):
        cite_short = c['citation'].replace('|', '\\|')[:60]
        sc = '✓' if c.get('has_specific_claim') else ''
        v_icon = {'pass': '✓', 'warn': '⚠️', 'block': '❌'}.get(c['severity'], '?')
        md += f"| {i} | `{cite_short}` | {c['type']} | {c.get('tier', '?')} | {sc} | {v_icon} {c['verdict']} |\n"

    if any(c.get('details', {}).get('pmid_info') for c in result['citations']):
        md += "\n## Paper Details\n\n"
        for i, c in enumerate(result['citations'], 1):
            pi = c.get('details', {}).get('pmid_info', {})
            if pi.get('status') == 'OK':
                md += f"- **#{i} PMID {pi.get('pmid', '')}** ({pi.get('year', '')}): {pi.get('title', '')[:100]} — *{pi.get('journal', '')}* — {pi.get('author', '')}\n"

    md += f"\n---\n*Generated by citation_audit.py at {time.strftime('%Y-%m-%d %H:%M:%S')}*\n"
    return md


def main():
    parser = argparse.ArgumentParser(description="Offline occurrence-based citation audit")
    parser.add_argument("file", type=Path)
    parser.add_argument("--evidence-bundle", required=True, type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    try:
        auditor = CitationAuditor(verbose=not args.quiet, evidence_bundle=args.evidence_bundle)
        result = auditor.audit_file(args.file)
    except BundleError as exc:
        result = {'file': str(args.file), 'error': str(exc), 'summary': {'total': 0, 'pass': 0, 'warn': 0, 'block': 1}, 'citations': []}
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif not args.quiet:
        auditor.print_console_report(result)
    if args.out:
        args.out.write_text(format_markdown_report(result), encoding='utf-8')
    return 0 if result['summary']['block'] == 0 and result['summary']['warn'] == 0 else 2

if __name__ == '__main__':
    raise SystemExit(main())
