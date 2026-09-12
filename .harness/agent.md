---
name: mavisresearch
description: Medical research project harness for ART/IVF, OB/GYN, reproductive medicine deep-dives
---

# mavisresearch — Medical Research Harness

This harness is mounted at `F:\DL\mavisresearch\`. It provides a team of medical-research specialists:

- `medical-researcher` — clinical evidence extraction with PMID discipline
- `guideline-analyst` — secondary research of society guidelines
- `mechanism-reviewer` — reproductive biology deep-dive with test-verified mermaid
- `medical-synthesis-writer` — final deep-report with coverage matrix + decision aid

## Folder layout
```
F:\DL\mavisresearch\
  daily_lessons\          # 18:00 daily lessons
  deep_dives\<topic>\     # per-topic deliverables (clinical-evidence.md, guideline-review.md, mechanism-review.md, final-report.md)
  papers\pubmed_cache\    # PubMed MCP cache
  papers\pdf\             # downloaded full-text PDFs
  notes\raw\<topic>\      # raw notes, URL bookmarks
  notes\synthesis\<topic>\ # synthesis summary after each deep-dive
  agents\configs\         # agent config snapshots
  agents\sessions_archive\ # archived session logs
  tools\                  # custom scripts
```

## Workflow
1. Orchestrator (Mavis) spawns team plan
2. 3 parallel research tracks (medical-researcher + guideline-analyst + mechanism-reviewer)
3. medical-synthesis-writer consumes upstream files, produces final-report.md
4. Verifier checks each track
