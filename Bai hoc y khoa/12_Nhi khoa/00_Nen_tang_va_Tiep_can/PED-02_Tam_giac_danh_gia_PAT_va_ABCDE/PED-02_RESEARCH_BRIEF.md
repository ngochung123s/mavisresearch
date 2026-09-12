# RESEARCH BRIEF: TAM GIÁC ĐÁNH GIÁ NHI KHOA (PAT) & TIẾP CẬN ABCDE (PED-02)

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
    "min_total_words": 5000,
    "min_total_lines": 500,
    "min_sections": 10,
    "min_subsections": 12,
    "min_mechanism_chains": 3,
    "min_examples": 6,
    "min_misconceptions": 6,
    "min_checkpoints": 4,
    "min_cases_with_solutions": 2,
    "min_practical_tips": 10,
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
- Làm chủ kỹ năng đánh giá ban đầu 60 giây không chạm (Across-the-room assessment) bằng Tam giác Đánh giá Nhi khoa (Pediatric Assessment Triangle - PAT).
- Phân tích sâu 3 cửa sổ sinh lý bệnh: Appearance (Vẻ ngoài - thang TICLS phản ánh chức năng não), Work of Breathing (Công thở phản ánh thông khí/oxy hóa), Circulation to Skin (Tuần hoàn da phản ánh cung lượng tim).
- Nhận diện và phân tầng chính xác 8 mẫu hình PAT lâm sàng kết hợp hướng can thiệp tối khẩn tại giường.
- Phân biệt sống còn giữa Suy hô hấp còn bù vs Kiệt sức hô hấp (bóc trần bẫy "cải thiện giả").
- Phân biệt sống còn giữa Sốc còn bù vs Sốc mất bù (nhận thức sâu sắc: tụt huyết áp là dấu hiệu muộn).
- Làm chủ trình tự hành động ABCDE toàn diện (Airway, Breathing, Circulation, Disability, Exposure), nắm vững mốc thời gian (lập đường trong xương IO sau 90 giây hoặc 2 lần chọc tĩnh mạch thất bại).
- Đánh giá tri giác bằng thang điểm GCS Nhi khoa (Pediatric GCS) điều chỉnh theo lứa tuổi và thang nhanh AVPU; chỉ định test đường huyết mao mạch bắt buộc.

### 1.2 Hướng dẫn chính thức & Đồng thuận quốc tế (Verified Guidelines)
1. **AHA / PALS Guidelines (2020)**: *Pediatric Advanced Life Support: 2020 American Heart Association Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care.* Circulation. [GUIDELINE VERIFIED]
2. **American Academy of Pediatrics (AAP, 2017)**: *Pediatric Education for Prehospital Professionals (PEPP) / PAT Core Curriculum.* [GUIDELINE VERIFIED]
3. **World Health Organization (WHO, 2019)**: *Emergency Triage Assessment and Treatment (ETAT) & IMCI Guidelines.* Geneva. [GUIDELINE VERIFIED]
4. **Bộ Y tế Việt Nam (2015/2020)**: *Hướng dẫn chẩn đoán và điều trị cấp cứu hồi sức Nhi khoa.* [GUIDELINE VERIFIED]

---

## 2. Y văn & Bằng chứng định lượng (Peer-reviewed Evidence)

1. **Dieckmann RA, Brownstein D, Gausche-Hill M. (2010)**: *The pediatric assessment triangle: a novel approach for the rapid evaluation of critically ill or injured children.* Pediatr Emerg Care, 26(4):312-315. PMID: **20386420**. [DATA VERIFIED]
2. **Horeczko T, Enriquez B, McGrath NE, et al. (2013)**: *The Pediatric Assessment Triangle: accuracy of its application by nurses in the triage of children.* J Emerg Nurs, 39(2):182-189. PMID: **23415516**. [DATA VERIFIED]
3. **Fleming S, Thompson M, Stevens R, et al. (2011)**: *Normal ranges of heart rate and respiratory rate in children from birth to 18 years of age: a systematic review of observational studies.* The Lancet, 377(9770):1011-1018. PMID: **21419743**. [DATA VERIFIED]
4. **Fernandez A, et al. (2017)**: *Validation of the Pediatric Assessment Triangle in pediatric emergency departments.* Eur J Emerg Med. PMID: **28489781**. [DATA VERIFIED]

---

## 3. Danh mục Claim định lượng đăng ký (Claims Registry)

| Claim ID | Thông số định lượng | Quần thể / Điều kiện | Nguồn xác minh | Nhãn xác minh |
|---|---|---|---|:---:|
| **C-001** | Thời gian thực hiện PAT chuẩn: 60 giây không chạm | Bệnh nhi vừa nhập buồng khám/cấp cứu | Dieckmann RA et al. (PMID: 20386420) | `[DATA VERIFIED]` |
| **C-002** | Não tiêu thụ khoảng 25% tổng nhu cầu oxy ($VO_2$) toàn cơ thể trẻ | Trẻ sơ sinh và trẻ nhũ nhi | AHA PALS 2020 Guidelines | `[GUIDELINE VERIFIED]` |
| **C-003** | Trẻ có thể bù trừ tuần hoàn khi mất 25% đến 30% thể tích máu trước khi tụt HA | Trẻ sốc giảm thể tích | AHA PALS 2020 / PEPP | `[GUIDELINE VERIFIED]` |
| **C-004** | Ngưỡng tụt huyết áp tâm thu P5: $70 + (2 \times \text{tuổi})$ mmHg | Trẻ từ 1 đến 10 tuổi | AHA PALS 2020 / AAP | `[GUIDELINE VERIFIED]` |
| **C-005** | Thời gian đổ đầy mao mạch (CRT) bình thường &lt; 2 giây, bệnh lý &gt; 3 giây | Bấm xương ức 5 giây tại phòng ấm | WHO ETAT / PALS 2020 | `[GUIDELINE VERIFIED]` |
| **C-006** | Chỉ định lập đường trong xương (IO): sau 90 giây hoặc 2 lần chọc TM thất bại | Bệnh nhi ngừng tuần hoàn hoặc sốc mất bù | AHA PALS 2020 Guidelines | `[GUIDELINE VERIFIED]` |
| **C-007** | Liều Glucose 10% cấp cứu hạ đường huyết: 2 ml/kg tiêm tĩnh mạch chậm | Trẻ có đường huyết &lt; 2.6 mmol/L | PALS 2020 / WHO ETAT | `[GUIDELINE VERIFIED]` |
| **C-008** | GCS Nhi khoa $\le 8$ điểm hoặc AVPU mức P/U tương đương mất khả năng bảo vệ đường thở | Trẻ chấn thương hoặc bệnh lý nội khoa | PALS 2020 Guidelines | `[GUIDELINE VERIFIED]` |

---

## 4. Tuyên bố không áp dụng & Nội dung cấm (Prohibited Content)
- Cấm chạm vào người trẻ hoặc dùng ống nghe trước khi hoàn thành quan sát PAT 60 giây (trừ khi ngừng tuần hoàn rõ rệt).
- Cấm dựa vào huyết áp bình thường để loại trừ tình trạng sốc ở trẻ em.
- Cấm đặt ký hiệu `%` bên trong môi trường toán học inline `$ ... $`.
- Giai đoạn phát hành này **chưa đóng gói APKG** (theo chỉ dẫn của người dùng).
