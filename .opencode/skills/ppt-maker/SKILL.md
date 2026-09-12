---
name: ppt-maker
description: Create medical PPTX presentations from verified medical lessons. Use ONLY when user asks for PowerPoint slides, PPTX, slide y khoa, bài giảng PowerPoint, or presentation. Supports 25 medical slide types with medical palettes.
---

# PPT Maker — Medical Slide Generator

## When to use

User says: "tạo slide", "làm PowerPoint", "PPTX", "bài giảng", "slide y khoa", "presentation".

## Hard rules

- Read repo context first: `AGENTS.md`, `Bai hoc y khoa/WORKFLOW.md`, `Bai hoc y khoa/.mavis/AGENTS.md`, then `Bai hoc y khoa/10_Script Python/slidemaker_prompt.txt`.
- PPTX is optional. Only create it when the user explicitly asks for slides/PowerPoint.
- Do not write output to `C:\` or the repo root. Put both deck JSON and PPTX in the relevant lesson folder under `F:\DL\mavisresearch\Bai hoc y khoa\`.
- Filename/folder names: no Vietnamese diacritics. Slide content: Vietnamese with full diacritics.
- Difficult English terms must be introduced as `tiếng Việt (English)` the first time.
- Do not invent citations, PMID, guideline versions, numbers, timing, dose, route, or protocol sequence. Preserve verified PMID/guideline tags from the source lesson.

## Workflow

### 0. Determine source and output folder

Prefer an existing lesson folder containing a verified `.md` source. Use that folder for output:

```text
Bai hoc y khoa/XX_Chuyen_khoa/XX_Ten_bai/
  Ten_bai_YYYY-MM-DD.md
  Ten_bai_YYYY-MM-DD.deck.json
  Slides - Ten_bai - YYYY-MM-DD.pptx
```

If the user gives only a new topic/text, create slides only from provided/verified facts. For medical claims with RR/CI/%/n= or protocol details, verify evidence before using them.

### 1. Read the prompt reference

Read `Bai hoc y khoa/10_Script Python/slidemaker_prompt.txt` — full spec of **25 slide types × 53 variants** with JSON format and decision table.

### 2. Compose JSON deck

```json
{
  "meta": {"title": "...", "author": "Bác sĩ Ngọc Hưng", "subtitle": "..."},
  "slides": [
    {"type": "title", "variant": "split_dark", "title": "...", "subtitle": "...", "author": "..."},
    {"type": "objectives", "variant": "icon_check", "objectives": ["..."]},
    ...
  ]
}
```

**CRITICAL RULES**: `type` REQUIRED for every slide. All fields at TOP LEVEL (never nested). No trailing commas. Use concise slide text; move long explanations to speaker `note`.

Recommended deck rhythm for medical lessons:

```text
title -> objectives -> key_message -> section -> mechanism/criteria/algorithm/case/evidence -> summary -> references
```

Avoid a deck made only of `content/bullets`. Mix visual slide types to keep the presentation readable.

### 3. Validate

```bash
python "Bai hoc y khoa/10_Script Python/slider3636.py" --deck "path\to\Ten_bai_YYYY-MM-DD.deck.json" --validate
```

### 4. Render

```bash
python "Bai hoc y khoa/10_Script Python/slider3636.py" --deck "path\to\Ten_bai_YYYY-MM-DD.deck.json" -o "path\to\Slides - Ten_bai - YYYY-MM-DD.pptx" --palette "Medical Teal"
```

### 5. QA before returning

```bash
python -c "from pptx import Presentation; p=Presentation(r'path\to\Slides - Ten_bai - YYYY-MM-DD.pptx'); print(len(p.slides)); assert len(p.slides)>0"
```

Also inspect warnings from `--validate`. Fix any overlong or overpacked slide instead of relying on autofit.

### 6. Quick type reference

| Content | type | variant |
|---|---|---|
| Bia | title | split_dark |
| Muc tieu | objectives | icon_check |
| Phan chuong | section | number_block |
| Danh sach | content | bullets |
| So sanh | two_column | vs_compare / cards |
| Dinh nghia | definition | term_box |
| So lieu noi bat | big_number | single_hero / multi_kpi |
| Thong diep | key_message | dark_hero |
| Co che | mechanism | horizontal_steps / cycle_loop |
| Phac do | algorithm | linear_flow / branching_yesno |
| Tieu chuan CD | criteria | major_minor |
| Thang diem | criteria | score_points |
| Ca lam sang | case | full_3zone / mini_vignette |
| Thuoc | medication | full_profile / quick_reference |
| Khuyen cao | evidence | class_level / recommendation_box |
| Dien tien/tien luong | timeline | vertical_history |
| Bien chung | complications | severity_tree |
| Tien luong | prognosis | survival_stats |
| MCQ | qa_clinical | mcq_5option |
| Tom tat | summary | takeaways |
| Tai lieu | references | numbered / categorized |
| Muc luc | outline | tree |
| Chuyen tiep | transition | chapter_close |

### 7. Palettes

- `"Medical Teal"` (default — y khoa chinh thong)
- `"International Blue"` (hoi nghi quoc te)
- `"Mayo Dark"` (toi gian)
- `"Academic Purple"` (hoc thuat)
- `"Clinical Red"` (cap cuu)

### 8. Deck structure (recommended)

```
1. title (bia)
2. objectives (muc tieu)
3. key_message (nguyen tac vang)
4. section (phan 1)
5. definition (dinh nghia)
6. content (dich te)
7. mechanism (co che)
8. criteria (tieu chuan)
9. algorithm (phac do)
10. medication (thuoc)
11. evidence (khuyen cao)
12. case (ca lam sang)
13. complications (bien chung)
14. summary (ket luan)
15. references (tai lieu)
```

Adjust based on content. Not all types needed.

### 9. Tips

- 1 message per slide, max 8 points
- Bullets: 10-22 words each; use speaker notes for detail
- LaTeX formulas: `$\\ge 90\\%$`, `$p < 0.001$`
- Add `key_message` between long sections
- For quick reference: `medication/quick_reference`
- For scoring: `criteria/score_points`
- Use `mechanism`, `algorithm`, `case`, `evidence`, and `chart` when the source supports them; they look better than dense bullet slides.
