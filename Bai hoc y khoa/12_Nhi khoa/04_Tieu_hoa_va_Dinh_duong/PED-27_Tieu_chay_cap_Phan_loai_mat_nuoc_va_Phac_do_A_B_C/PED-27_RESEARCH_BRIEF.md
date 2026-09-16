# RESEARCH BRIEF: TIÊU CHẢY CẤP — PHÂN LOẠI MẤT NƯỚC & PHÁC ĐỒ A - B - C (PED-27)

## 0. Lesson profile & release contract

```json
{
  "profile": "foundation",
  "mode": "L3_BEGINNER",
  "required_gates": [
    "depth_foundation",
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

## 1. Phạm vi, mục tiêu & văn bản hướng dẫn cốt lõi (Guidelines)

### 1.1 Mục tiêu đào tạo
- Làm chủ chẩn đoán xác định Tiêu chảy cấp ở trẻ em: đại tiện phân lỏng hoặc tóe nước $\ge 3$ lần trong 24 giờ, thời gian kéo dài $< 14$ ngày.
- Nắm vững 4 chuỗi sinh lý bệnh 5 tầng: (1) Cơ chế tiêu chảy xuất tiết qua độc tố ruột và kênh CFTR; (2) Cơ chế đồng vận chuyển Na⁺-Glucose qua protein SGLT-1 làm cơ sở khoa học cho dung dịch ORS; (3) Cơ chế tiêu chảy thẩm thấu do tổn thương diềm bàn chải và thiếu men Lactase thứ phát; (4) Sinh lý bệnh sốc giảm thể tích, toan chuyển hóa mất kiềm qua phân và suy thận cấp trước thận.
- Thành thạo phân loại 3 mức độ mất nước theo chuẩn 4 dấu hiệu của WHO: Không mất nước, Có mất nước (Mất nước nhẹ - trung bình), và Mất nước nặng.
- Thực hành chuẩn xác Phác đồ A (điều trị tại nhà, phòng ngừa mất nước): 4 nguyên tắc chăm sóc, liều lượng ORS áp lực thẩm thấu thấp (245 mOsm/L) sau mỗi lần đi ngoài, duy trì bú mẹ và dinh dưỡng đầy đủ, nhận diện các dấu hiệu nguy hiểm cần tái khám ngay.
- Thực hành chuẩn xác Phác đồ B (bù nước tại cơ sở y tế): tính thể tích ORS $75\text{ ml/kg}$ trong 4 giờ, kỹ thuật cho uống từng thìa nhỏ, theo dõi nôn trớ, đánh giá lại sau 4 giờ để chuyển phác đồ phù hợp.
- Thực hành cấp cứu Phác đồ C (bù dịch tĩnh mạch trong mất nước nặng và sốc giảm thể tích): chọn lựa dịch truyền đầu tay (Ringer Lactat), tổng liều $100\text{ ml/kg}$, phân bổ 2 bước tốc độ truyền chuẩn xác theo nhóm tuổi (< 12 tháng vs $\ge 12$ tháng), theo dõi mạch, tri giác, nếp véo da mỗi 15–30 phút.
- Chỉ định và hướng dẫn sử dụng Kẽm (Zinc) đủ 10–14 ngày theo lứa tuổi để phục hồi niêm mạc ruột và giảm tỷ lệ tái phát.
- Phân biệt tiêu chảy cấp phân nước vs hội chứng lỵ (phân nhầy máu) và nắm vững chỉ định kháng sinh hợp lý, tránh lạm dụng thuốc cầm tiêu chảy nguy hiểm.

### 1.2 Hướng dẫn chính thức & Đồng thuận chuyên gia (Verified Guidelines)
1. **World Health Organization (WHO, 2019/2022)**: *The treatment of diarrhoea: a manual for physicians and other senior health workers (4th rev) & Pocket Book of Hospital Care for Children: Guidelines for the Management of Common Childhood Illnesses (2nd edition) - Chapter 5: Diarrhoea.* Geneva: World Health Organization. [GUIDELINE VERIFIED]
2. **Bộ Y tế Việt Nam (Quyết định số 4121/QĐ-BYT)**: *Hướng dẫn chẩn đoán và điều trị tiêu chảy ở trẻ em.* Hà Nội: Bộ Y tế. [GUIDELINE VERIFIED]
3. **Bệnh viện Nhi Đồng 1 & Bệnh viện Nhi Đồng 2 (2020/2021)**: *Phác đồ điều trị Nhi khoa — Tiêu chảy cấp & Xử trí mất nước.* TP. Hồ Chí Minh: NXB Y học. [GUIDELINE VERIFIED]
4. **European Society for Paediatric Gastroenterology, Hepatology, and Nutrition / European Society for Paediatric Infectious Diseases (ESPGHAN/ESPID, 2014)**: *Evidence-based Guidelines for the Management of Acute Gastroenteritis in Children in Europe: Update 2014.* J Pediatr Gastroenterol Nutr, 59(1):132–152. PMID: **24739189**. [GUIDELINE VERIFIED]
5. **Centers for Disease Control and Prevention (CDC, 2003)**: *Managing Acute Gastroenteritis Among Children: Oral Rehydration, Maintenance, and Nutritional Therapy.* MMWR Recomm Rep, 52(RR-16):1–16. PMID: **14627948**. [GUIDELINE VERIFIED]
6. **Nelson Textbook of Pediatrics (21st Edition, 2020)**: *Chapter 366: Acute Gastroenteritis in Children.* Philadelphia: Elsevier. [GUIDELINE VERIFIED]

---

## 2. Y văn & Bằng chứng định lượng (Peer-reviewed Evidence)

1. **Hahn S, Kim Y, Garner P. (Cochrane Review, 2002)**: *Reduced osmolarity oral rehydration solution for treating dehydration caused by acute diarrhoea in children.* Cochrane Database Syst Rev, 2002(1):CD002847. PMID: **11869639**. [DATA VERIFIED]
2. **Lazzerini M, Wanzira H. (Cochrane Review, 2016)**: *Oral zinc for treating diarrhoea in children.* Cochrane Database Syst Rev, 2016(12):CD005436. PMID: **27996088**. [DATA VERIFIED]
3. **Houston KA, Gibb DM, Maitland K. (GASTRO Trial, 2019)**: *Gastroenteritis aggressive versus slow treatment for rehydration (GASTRO): a phase II rehydration trial for severe dehydration: WHO plan C versus slow rehydration.* Wellcome Open Res, 2019;4:122. PMID: **31256761**. [DATA VERIFIED]
4. **Guarino A, Ashkenazi S, Gendrel D, et al. (ESPGHAN/ESPID Guidelines, 2014)**: *European Society for Paediatric Gastroenterology, Hepatology, and Nutrition/European Society for Paediatric Infectious Diseases evidence-based guidelines for the management of acute gastroenteritis in children in Europe: update 2014.* J Pediatr Gastroenterol Nutr, 2014;59(1):132-152. PMID: **24739189**. [GUIDELINE VERIFIED]
5. **King CK, Glass R, Bresee JS, Duggan C. (CDC MMWR, 2003)**: *Managing acute gastroenteritis among children: oral rehydration, maintenance, and nutritional therapy.* MMWR Recomm Rep, 2003;52(RR-16):1-16. PMID: **14627948**. [DATA VERIFIED]

---

## 3. Claims — Danh mục Claim định lượng đăng ký (Claims Registry)

| Claim ID | Claim text | Population | Source (PMID) | Verification Tag |
|---|---|---|---|:---:|
| **C-001** | Dung dịch ORS áp lực thẩm thấu thấp (Reduced osmolarity oral rehydration solution for acute diarrhoea) có tổng áp lực thẩm thấu 245 mOsm/L (Na⁺ 75 mmol/L, Glucose 75 mmol/L) | Trẻ tiêu chảy cấp mất nước | PMID: 11869639 | [DATA VERIFIED] |
| **C-002** | Liều ORS uống sau mỗi lần đi ngoài trong Phác đồ A (Managing acute gastroenteritis among children oral rehydration therapy): Trẻ < 2 tuổi uống 50–100 ml; Trẻ 2–10 tuổi uống 100–200 ml; Trẻ ≥ 10 tuổi uống theo nhu cầu | Trẻ tiêu chảy không mất nước điều trị tại nhà | PMID: 14627948 | [DATA VERIFIED] |
| **C-003** | Tổng thể tích dịch truyền tĩnh mạch cấp cứu trong Phác đồ C (WHO plan C rapid rehydration trial for severe dehydration secondary to gastroenteritis using Ringer's lactate) là 100 ml/kg | Trẻ mất nước nặng do tiêu chảy cấp | PMID: 31256761 | [DATA VERIFIED] |
| **C-004** | Tổng thời gian truyền tĩnh mạch Phác đồ C (WHO plan C rehydration for severe dehydration): Trẻ < 12 tháng truyền trong 6 giờ; Trẻ ≥ 12 tháng truyền trong 3 giờ | Trẻ mất nước nặng | PMID: 31256761 | [DATA VERIFIED] |
| **C-005** | Liều bổ sung Kẽm (Oral zinc supplementation for treating children with acute diarrhoea): Trẻ < 6 tháng uống 10 mg/ngày; Trẻ ≥ 6 tháng uống 20 mg/ngày, dùng liên tục 10–14 ngày | Trẻ tiêu chảy cấp | PMID: 27996088 | [DATA VERIFIED] |
| **C-006** | Thuật toán bù dịch phân loại 3 mức (ESPGHAN evidence-based guidelines for the management of acute gastroenteritis in children): Phác đồ A tại nhà, Phác đồ B ORS 75 ml/kg trong 4 giờ, Phác đồ C truyền TM 100 ml/kg | Trẻ tiêu chảy cấp mất nước | PMID: 24739189 | [GUIDELINE VERIFIED] |
| **C-007** | Bảng phân loại mất nước lâm sàng (clinical dehydration assessment in children with acute gastroenteritis): Toàn trạng tri giác, Mắt trũng, Uống nước, Nếp véo da | Đánh giá trẻ mất nước | PMID: 24739189 | [GUIDELINE VERIFIED] |
| **C-008** | Dịch truyền tĩnh mạch ưu tiên lựa chọn hàng đầu cho Phác đồ C là dung dịch Ringer Lactat (rapid rehydration using Ringer's lactate in severe dehydration); nếu không có Ringer Lactat mới dùng Natri Clorid 0.9% | Hồi sức mất nước nặng do tiêu chảy | PMID: 31256761 | [DATA VERIFIED] |
| **C-009** | Phác đồ C bước 1 cho trẻ ≥ 12 tháng (WHO plan C rehydration 30 ml/kg bolus given over 30 min): Truyền tĩnh mạch 30 ml/kg trong 30 phút đầu tiên | Trẻ ≥ 12 tháng mất nước nặng | PMID: 31256761 | [DATA VERIFIED] |
| **C-010** | Phác đồ C bước 2 cho trẻ ≥ 12 tháng (WHO plan C rehydration 100 ml/kg over 3 h remainder 70 ml/kg over 2.5 h): Truyền tĩnh mạch 70 ml/kg trong 2.5 giờ tiếp theo | Trẻ ≥ 12 tháng mất nước nặng | PMID: 31256761 | [DATA VERIFIED] |
| **C-011** | Phác đồ C bước 1 cho trẻ < 12 tháng (WHO plan C rehydration bolus 30 ml/kg given over 60 min if < 1 year): Truyền tĩnh mạch 30 ml/kg trong 1 giờ đầu tiên | Trẻ < 12 tháng mất nước nặng | PMID: 31256761 | [DATA VERIFIED] |
| **C-012** | Phác đồ C bước 2 cho trẻ < 12 tháng (WHO plan C rehydration 100 ml/kg over 6 h remainder 70 ml/kg over 5 h): Truyền tĩnh mạch 70 ml/kg trong 5 giờ tiếp theo | Trẻ < 12 tháng mất nước nặng | PMID: 31256761 | [DATA VERIFIED] |

---

## 4. Tuyên bố không áp dụng & Nội dung cấm (Prohibited Content)
- Tuyệt đối CẤM kê đơn thuốc làm giảm nhu động ruột (Loperamide, Diphenoxylate, Atropine, Opiates) cho trẻ em: gây liệt ruột, trướng bụng hoại tử, nhiễm độc toàn thân và ức chế hô hấp.
- Tuyệt đối CẤM pha ORS sai tỷ lệ thể tích nước (pha quá đặc gây ngộ độc Natri thẩm thấu dẫn đến xuất huyết não; pha quá loãng không đủ hiệu quả bù nước điện giải).
- Tuyệt đối CẤM chỉ định kháng sinh thường quy cho tiêu chảy phân nước cấp tính (trừ trường hợp nghi ngờ Tả có mất nước nặng, hoặc tiêu chảy phân nhầy máu/Hội chứng lỵ do Shigella).
- Tuyệt đối CẤM bắt trẻ nhịn ăn hoặc kiêng khem sữa mẹ/thức ăn giàu năng lượng trong đợt tiêu chảy cấp.
- Cấm đặt ký hiệu `%` bên trong môi trường toán học inline `$ ... $`.
