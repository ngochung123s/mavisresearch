"""knowledge_graph.py — Build cross-reference graph between medical lessons.

Usage:
    python knowledge_graph.py --build       # Scan all MDs, build graph
    python knowledge_graph.py --add <md>    # Add one new lesson to graph
    python knowledge_graph.py --query "Doppler"  # Find lessons related to keyword
    python knowledge_graph.py --mermaid     # Output Mermaid flowchart

Creates: knowledge_graph.json — nodes (lessons) + edges (cross-references).
"""
import sys
import json
import re
from pathlib import Path
from collections import defaultdict
import sys; sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
GRAPH_PATH = SCRIPT_DIR / "knowledge_graph.json"

# Keyword categories for auto-detection
CATEGORIES = {
    "Doppler & Hemodynamics": [
        "Doppler", "UA", "MCA", "CPR", "DV", "PI", "RI", "PSV",
        "uterine artery", "umbilical artery", "middle cerebral", "ductus venosus",
        "cerebroplacental", "brain.sparing", "vasoconstriction", "redistribution"
    ],
    "Fetal Growth & Assessment": [
        "FGR", "IUGR", "SGA", "EFW", "fetal weight", "fetal biometry",
        "growth restriction", "small for gestational", "BPP", "biophysical profile",
        "NST", "non.stress test"
    ],
    "Amniotic Fluid": [
        "amniotic fluid", "AFI", "SDP", "oligohydramnios", "polyhydramnios",
        "anhydramnios", "nước ối", "thiểu ối", "đa ối", "deepest pocket",
        "amniotic fluid index"
    ],
    "Placenta & Preeclampsia": [
        "preeclampsia", "pre-eclampsia", "eclampsia", "HELLP", "aspirin",
        "ASPRE", "placental", "nhau thai", "tiền sản giật", "ISSHP",
        "placental insufficiency", "PLGF", "sFlt"
    ],
    "Preterm Birth & Cervix": [
        "cervical length", "PTB", "preterm", "cervix", "cerclage",
        "progesterone", "sinh non", "cổ tử cung", "PPROM"
    ],
    "ART & Stimulation": [
        "ART", "IVF", "ICSI", "FET", "COS", "GnRH", "FSH", "LH",
        "gonadotropin", "ovarian stimulation", "antagonist", "agonist",
        "PPOS", "OHSS", "trigger", "oocyte", "embryo", "blastocyst",
        "kích trứng", "phác đồ", "stimulation protocol"
    ],
    "Endometrium & Implantation": [
        "endometrial", "endometrium", "ERA", "WOI", "window of implantation",
        "receptivity", "implantation", "RIF", "nội mạc", "làm tổ"
    ],
    "Multiple Pregnancy": [
        "twin", "MCMA", "MCDA", "DCDA", "TTTS", "TAPS", "monochorionic",
        "dichorionic", "song thai", "Quintero"
    ],
    "Endocrinology": [
        "endocrine", "hormone", "HPO", "estrogen", "progesterone", "androgen",
        "testosterone", "DHEA", "AMH", "LH surge", "follicular", "luteal",
        "nội tiết", "buồng trứng", "PCOS"
    ],
    "Genetics & Screening": [
        "aneuploidy", "NIPT", "T21", "T18", "T13", "NT", "first trimester",
        "PGT", "karyotype", "CMA", "microarray", "sàng lọc", "dị tật"
    ],
    "Guidelines & Societies": [
        "ESHRE", "ACOG", "SMFM", "ISUOG", "RCOG", "FIGO", "ASRM", "NICE", "WHO"
    ],
}


def extract_metadata(md_path):
    """Extract title, date, keywords from MD file."""
    text = Path(md_path).read_text(encoding='utf-8')
    lines = text.split('\n')
    
    title = ""
    date = ""
    specialty = ""
    
    for line in lines[:20]:
        s = line.strip()
        if s.startswith('# ') and 'bài học' in s.lower():
            title = s[2:].strip()
        elif 'Chuyên khoa' in s:
            m = re.search(r'\*\*(.+?)\*\*', s)
            if m: specialty = m.group(1)
        elif 'Ngày' in s:
            m = re.search(r'(\d{4}-\d{2}-\d{2})', s)
            if m: date = m.group(1)
            if not date:
                m2 = re.search(r'(\d{2}/\d{2}/\d{4})', s)
                if m2: date = m2.group(1)
    
    # Category matching
    text_lower = text.lower()
    categories = []
    for cat, keywords in CATEGORIES.items():
        score = 0
        for kw in keywords:
            if kw.lower() in text_lower:
                score += 1
        if score >= 2:
            categories.append(cat)
    
    # Extract PMIDs
    pmids = list(set(re.findall(r'PMID:?\s*[*\s]*(\d{7,8})', text)))
    
    return {
        "path": str(md_path),
        "filename": Path(md_path).name,
        "title": title,
        "date": date,
        "specialty": specialty,
        "categories": categories,
        "pmid_count": len(pmids),
    }


def find_cross_references(all_lessons):
    """Find shared keywords between lessons → edges."""
    edges = []
    for i, a in enumerate(all_lessons):
        a_cats = set(a.get('categories', []))
        a_path = Path(a['path'])
        a_text = ""
        try:
            a_text = a_path.read_text(encoding='utf-8').lower()
        except:
            continue
        
        for j in range(i + 1, len(all_lessons)):
            b = all_lessons[j]
            b_cats = set(b.get('categories', []))
            shared = a_cats & b_cats
            
            if shared:
                edges.append({
                    "source": a['filename'],
                    "target": b['filename'],
                    "shared_categories": list(shared),
                    "weight": len(shared),
                })
    
    return edges


def build_graph():
    """Scan all MD files in source directory and build graph."""
    source_dir = PROJECT_ROOT / "09_Source - Markdown"
    if not source_dir.exists():
        print(f"Source directory not found: {source_dir}")
        return None
    
    # Find all MD files recursively
    md_files = list(source_dir.rglob("*.md"))
    # Filter out non-lesson files
    md_files = [f for f in md_files if re.match(r'.*(20\d{2}-\d{2}-\d{2}|2026)', f.name)]
    
    print(f"[knowledge_graph] Scanning {len(md_files)} lesson MD files...")
    
    lessons = []
    for f in md_files:
        try:
            meta = extract_metadata(f)
            lessons.append(meta)
        except Exception as e:
            print(f"  ⚠️ Skipped {f.name}: {e}")
    
    edges = find_cross_references(lessons)
    
    graph = {
        "nodes": lessons,
        "edges": edges,
        "total_lessons": len(lessons),
        "total_connections": len(edges),
    }
    
    with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    print(f"  ✅ Graph built: {len(lessons)} nodes, {len(edges)} edges")
    print(f"  Saved: {GRAPH_PATH}")
    
    return graph


def add_lesson(md_path):
    """Add one lesson to existing graph."""
    if not GRAPH_PATH.exists():
        print("[knowledge_graph] No existing graph — building from scratch")
        return build_graph()
    
    graph = json.loads(GRAPH_PATH.read_text(encoding='utf-8'))
    
    meta = extract_metadata(md_path)
    filename = meta['filename']
    
    # Remove existing entry if present
    graph['nodes'] = [n for n in graph['nodes'] if n['filename'] != filename]
    graph['nodes'].append(meta)
    
    # Rebuild edges
    # Remove edges involving this file
    graph['edges'] = [e for e in graph['edges'] 
                      if e['source'] != filename and e['target'] != filename]
    
    # Add new edges
    a_cats = set(meta.get('categories', []))
    a_text = ""
    try:
        a_text = Path(md_path).read_text(encoding='utf-8').lower()
    except:
        pass
    
    for node in graph['nodes']:
        if node['filename'] == filename:
            continue
        b_cats = set(node.get('categories', []))
        shared = a_cats & b_cats
        if shared:
            graph['edges'].append({
                "source": filename,
                "target": node['filename'],
                "shared_categories": list(shared),
                "weight": len(shared),
            })
    
    graph['total_lessons'] = len(graph['nodes'])
    graph['total_connections'] = len(graph['edges'])
    
    with open(GRAPH_PATH, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    print(f"[knowledge_graph] Added: {filename}")
    print(f"  Nodes: {graph['total_lessons']}, Edges: {graph['total_connections']}")
    print(f"  Categories: {meta.get('categories', [])}")
    
    return graph


def query_graph(keyword):
    """Find lessons related to a keyword."""
    if not GRAPH_PATH.exists():
        print("No graph found — run --build first")
        return
    
    graph = json.loads(GRAPH_PATH.read_text(encoding='utf-8'))
    kw = keyword.lower()
    
    print(f"\n  Lessons related to '{keyword}':")
    found = []
    for node in graph['nodes']:
        score = 0
        for cat in node.get('categories', []):
            if kw in cat.lower():
                score += 1
        # Also check title
        if kw in node.get('title', '').lower():
            score += 2
        if score > 0:
            found.append((score, node))
    
    found.sort(key=lambda x: -x[0])
    for score, node in found:
        print(f"  [{node.get('specialty', '?')}] {node.get('title', node['filename'])[:80]}")
        print(f"         {node.get('date', '?')} | Categories: {', '.join(node.get('categories', []))}")
    
    return found


def output_mermaid():
    """Output Mermaid flowchart of lesson connections."""
    if not GRAPH_PATH.exists():
        print("No graph found — run --build first")
        return
    
    graph = json.loads(GRAPH_PATH.read_text(encoding='utf-8'))
    
    print("```mermaid")
    print("flowchart LR")
    for i, node in enumerate(graph['nodes']):
        short = node.get('title', node['filename'])[:40]
        print(f"  N{i}[\"{short}\"]")
    
    # Only show top connections (weight >= 3)
    for edge in graph['edges']:
        if edge['weight'] >= 3:
            src_idx = next(i for i, n in enumerate(graph['nodes']) if n['filename'] == edge['source'])
            tgt_idx = next(i for i, n in enumerate(graph['nodes']) if n['filename'] == edge['target'])
            print(f"  N{src_idx} --> N{tgt_idx}")
    print("```")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python knowledge_graph.py [--build|--add <md>|--query <kw>|--mermaid]")
        sys.exit(0)
    
    cmd = sys.argv[1]
    if cmd == '--build':
        build_graph()
    elif cmd == '--add' and len(sys.argv) > 2:
        add_lesson(sys.argv[2])
    elif cmd == '--query' and len(sys.argv) > 2:
        query_graph(sys.argv[2])
    elif cmd == '--mermaid':
        output_mermaid()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
