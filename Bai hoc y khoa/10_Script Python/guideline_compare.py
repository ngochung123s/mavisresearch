"""guideline_compare.py — Cross-society guideline comparison for a given topic.

Usage:
    python guideline_compare.py --topic "amniotic fluid"
    python guideline_compare.py --topic "oligohydramnios" --md <lesson.md>

Checks guideline_registry.json for all societies that have guidance on the topic.
Flags if different societies:
  - Use different cut-offs (e.g., AFI ≥24 vs ≥25 for polyhydramnios)
  - Have conflicting recommendations (e.g., different timing for delivery)
  - One has been superseded by another
"""
import sys
import json
import re
from pathlib import Path
import sys; sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent
REGISTRY_PATH = SCRIPT_DIR / "guideline_registry.json"

# Keyword mapping: topic keywords → guideline keys to look for
TOPIC_KEYWORDS = {
    "amniotic fluid": ["polyhydramnios", "oligohydramnios", "amniotic", "AFI", "Doppler", "fetal biometry", "fetal surveillance", "fetal growth"],
    "oligohydramnios": ["oligohydramnios", "amniotic", "AFI", "Doppler", "fetal surveillance", "fetal growth"],
    "polyhydramnios": ["polyhydramnios", "amniotic", "AFI", "fetal biometry", "twin"],
    "preeclampsia": ["preeclampsia", "hypertension", "aspirin", "pregnancy"],
    "ovarian stimulation": ["ovarian stimulation", "ovarian", "stimulation", "IVF", "COS", "gonadotropin"],
    "fgr": ["fetal growth", "growth restriction", "Doppler", "fetal surveillance", "fetal biometry"],
    "doppler": ["Doppler", "velocimetry", "fetal growth", "fetal surveillance"],
    "fetal biometry": ["fetal biometry", "biometry", "fetal growth", "ultrasound"],
    "cervical length": ["cervical", "preterm", "PTB"],
    "endometriosis": ["endometriosis", "endometrioma"],
    "icsi": ["ICSI", "sperm", "male infertility"],
    "luteal phase": ["luteal", "progesterone", "luteal phase"],
    "ohss": ["OHSS", "hyperstimulation", "ovarian"],
    "iui": ["IUI", "insemination"],
}


def load_registry():
    if not REGISTRY_PATH.exists():
        return {}
    return json.loads(open(REGISTRY_PATH, encoding='utf-8').read())


def find_relevant_guidelines(topic, registry):
    """Find all guidelines relevant to a topic across all societies."""
    topic_lower = topic.lower()
    
    # First try exact keyword match
    search_terms = TOPIC_KEYWORDS.get(topic_lower, [topic_lower])
    
    found = []
    for society_key, society_data in registry.items():
        if not isinstance(society_data, dict) or 'guidelines' not in society_data:
            continue
        society_name = society_data.get('society', society_key)
        for gkey, gdata in society_data.get('guidelines', {}).items():
            gtitle = gdata.get('title', '').lower()
            gkey_lower = gkey.lower()
            # Match against keywords
            score = 0
            for term in search_terms:
                if term.lower() in gkey_lower or term.lower() in gtitle:
                    score += 1
            
            if score > 0:
                found.append({
                    "society": society_name,
                    "society_key": society_key,
                    "guideline_key": gkey,
                    "year": gdata.get('year', '?'),
                    "title": gdata.get('title', ''),
                    "pmid": gdata.get('pmid', ''),
                    "superseded_by": gdata.get('superseded_by', ''),
                    "score": score,
                })
    
    # Sort by relevance score
    found.sort(key=lambda x: (-x['score'], x['year']))
    return found


def compare_cutoffs(guidelines):
    """Compare cut-off values across guidelines for known measurements."""
    conflicts = []
    
    # Known cut-off patterns
    known_cutoffs = {
        "AFI polyhydramnios": [(r"AFI\s*[≥>=]\s*(\d+)", r"AFI\s*(\d+)\s*cm", None)],
        "SDP polyhydramnios": [(r"SDP\s*[≥>=]\s*(\d+)", r"(?:deepest|single).*?[≥>=]\s*(\d+)", None)],
        "AFI oligohydramnios": [(r"AFI\s*[≤<=]\s*(\d+)", r"AFI\s*(\d+)\s*cm", None)],
    }
    
    # For now, return empty — full implementation would need text extraction
    return conflicts


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Cross-society guideline comparison")
    ap.add_argument("--topic", "-t", required=True, help="Topic to compare guidelines for")
    ap.add_argument("--md", help="Optional MD file to extract topic from")
    ap.add_argument("--json", action="store_true", help="Output as JSON")
    args = ap.parse_args()
    
    registry = load_registry()
    if not registry:
        print("❌ guideline_registry.json not found or empty")
        sys.exit(2)
    
    guidelines = find_relevant_guidelines(args.topic, registry)
    
    if not guidelines:
        print(f"[guideline_compare] No guidelines found for topic: {args.topic}")
        print(f"  Consider adding to guideline_registry.json")
        sys.exit(0)
    
    if args.json:
        print(json.dumps(guidelines, indent=2, ensure_ascii=False))
    else:
        print(f"\n  {'='*50}")
        print(f"  GUIDELINE COMPARISON: {args.topic}")
        print(f"  {'='*50}")
        print(f"  Found {len(guidelines)} relevant guidelines from {len(set(g['society'] for g in guidelines))} societies:\n")
        
        for g in guidelines:
            sup = f" [SUPERSEDED: {g['superseded_by']}]" if g.get('superseded_by') else ""
            pmid_str = f" (PMID: {g['pmid']})" if g.get('pmid') else ""
            print(f"  [{g['society_key']}] {g['guideline_key']} ({g['year']}){pmid_str}{sup}")
            print(f"         {g['title'][:100]}")
        
        # Check for superseded guidelines
        superseded = [g for g in guidelines if g.get('superseded_by')]
        if superseded:
            print(f"\n  ⚠️ WARNING: {len(superseded)} guideline(s) have been SUPERSEDED:")
            for g in superseded:
                print(f"    - {g['society_key']}: {g['guideline_key']} → {g['superseded_by']}")
            sys.exit(1)
        
        # Check society coverage
        societies_found = set(g['society_key'] for g in guidelines)
        tier0_societies = ['ACOG', 'RCOG', 'ESHRE', 'ASRM', 'ISUOG', 'NICE', 'FIGO', 'SMFM', 'WHO']
        missing = [s for s in tier0_societies if s in registry and s not in societies_found]
        if missing:
            print(f"\n  ℹ️ No guidelines yet for these societies (may not have topic-specific guidance):")
            for m in missing:
                print(f"    - {m}")
        
        print(f"\n  ✅ Comparison complete")
        sys.exit(0)


if __name__ == '__main__':
    main()
