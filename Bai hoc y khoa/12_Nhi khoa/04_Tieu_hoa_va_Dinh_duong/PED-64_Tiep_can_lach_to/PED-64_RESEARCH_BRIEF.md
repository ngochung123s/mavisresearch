# RESEARCH BRIEF: TIẾP CẬN LÁCH TO Ở TRẺ EM (PED-64)

## 0. Lesson profile & release contract

```json
{
  "profile": "disease",
  "mode": "L3_BEGINNER",
  "required_gates": [
    "depth_disease",
    "citation_zero_block",
    "cards_schema",
    "package_diacritics",
    "source_diacritics",
    "candidate_apkg_build"
  ],
  "lesson_depth_contract": {
    "min_total_words": 6000,
    "min_total_lines": 600,
    "min_sections": 10,
    "min_subsections": 14,
    "min_mechanism_chains": 4,
    "min_examples": 8,
    "min_misconceptions": 8,
    "min_checkpoints": 5,
    "min_cases_with_solutions": 3,
    "min_practical_tips": 12,
    "max_placeholder_count": 0,
    "no_padding": true
  },
  "not_applicable": [],
  "approved_exemptions": []
}
```

---

## 1. Phạm vi, mục tiêu & nguồn

### 1.1 Mục tiêu đào tạo
- Track 1 (barem PEDYTB, giáo trình Nhi khoa Y Thái Bình, chương LÁCH TO, trang 100–109): định nghĩa, chức năng lách, nguyên nhân theo 6 nhóm, bệnh sử/thực thể/cận lâm sàng, bảng 3.1 chẩn đoán nguyên nhân, sơ đồ tiếp cận 3.2, điều trị (hạn chế thể thao, cắt lách, OPSI, vacxin, penicillin dự phòng).
- Track 2 (EBM): đo lách bằng siêu âm theo tuổi, cờ đỏ cấp cứu (cơn nhốt máu lách, HLH, vô lách), xử trí EBV và thể thao, cắt lách một phần, dự phòng nhiễm khuẩn hậu cắt lách.

### 1.2 Nguồn y chứng đã truy xuất (Europe PMC, 2026-10-22)
1. Front Pediatr 2021 — Splenomegaly in Children and Adolescents. PMID: **34307263** (PMC8298754). [DATA VERIFIED]
2. Blood Rev 2009 — Splenomegaly: investigation, diagnosis and management. PMID: **19062140**. [ABSTRACT VERIFIED]
3. AJR 1998 — Normal liver, spleen, and kidney dimensions in neonates, infants, and children. PMID: **9843315**. [ABSTRACT VERIFIED]
4. Radiology 2004 — Spleen length in childhood with US: normal values. PMID: **14990814**. [ABSTRACT VERIFIED]
5. Br J Haematol 2011 — Review of guidelines for infection in absent/dysfunctional spleen (BCSH). PMID: **21988145**. [GUIDELINE VERIFIED]
6. Br J Haematol 2012 — Hereditary spherocytosis guidelines 2011 update. PMID: **22055020**. [GUIDELINE VERIFIED]
7. Pathogens 2021 — Role of partial splenectomy in hematologic childhood disorders. PMID: **34832592**. [ABSTRACT VERIFIED]
8. Clin J Sport Med 2023 — AMSSM position statement: mononucleosis and athletic participation. PMID: **37186809**. [ABSTRACT VERIFIED]
9. Clin J Sport Med 2008 — Mononucleosis and athletic participation: evidence-based subject review. PMID: **18614881**. [ABSTRACT VERIFIED]
10. Infect Dis Clin North Am 2007 — Prevention and management of infections in children with asplenia or hyposplenia. PMID: **17826619**. [ABSTRACT VERIFIED]
11. Lancet 2011 — Post-splenectomy and hyposplenic states. PMID: **21474172**. [ABSTRACT VERIFIED]

Artifact: `ncbi_fetch.json`, `abstract_match.jsonl`, `full_verify_table.md` nằm cạnh brief.

### 1.3 Lưu ý khác biệt barem ↔ EBM (đã ghi trong bài ở nhãn "Ngoài barem")
- Barem: "lách là cơ quan tạo máu chính của thai nhi" — thực tế gan là cơ quan tạo máu chủ yếu ở giữa thai kỳ, lách chỉ đóng góp tạm thời (kiến thức nền, không gắn nhãn).
- Barem liệt kê "lách lang thang" trong "lách to tiên phát" — lách lang thang là lách di động lạc vị, không nhất thiết to.
- Barem liệt kê Hodgkin trong chỉ định cắt lách — cắt lách chẩn đoán/xếp giai đoạn không còn là thường quy (kiến thức nền, không gắn nhãn).
