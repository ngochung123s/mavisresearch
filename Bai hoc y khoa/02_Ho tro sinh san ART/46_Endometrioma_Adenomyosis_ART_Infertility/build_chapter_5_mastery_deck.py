# -*- coding: utf-8 -*-
"""build_chapter_5_mastery_deck.py — Build Chapter 5 standalone master slide deck with pure unnumbered bullet points."""
import json
import sys
from pathlib import Path

TARGET_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\02_Ho tro sinh san ART\46_Endometrioma_Adenomyosis_ART_Infertility")
OUTPUTS_DIR = TARGET_DIR / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
SCRIPT_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python")
sys.path.insert(0, str(SCRIPT_DIR))

import slider3636

# Clean footer override (no text, no page number, no divider line)
def clean_empty_footer(slide, left="", page_num=None, total=None):
    pass

slider3636.footer = clean_empty_footer

pure_bullet_chapter_5 = {
    "meta": {
        "title": "",
        "subtitle": "",
        "author": ""
    },
    "slides": [
        # Slide 1: Title
        {
            "type": "title",
            "variant": "split_dark",
            "title": "CHƯƠNG 5: CHUẨN BỊ NIÊM MẠC & CHUYỂN PHÔI ĐÔNG LẠNH CHO ADENOMYOSIS",
            "subtitle": "Chiến Lược Freeze-All, Phác Đồ Ultra-Long GnRHa Cá Thể Hóa & Tối Ưu Hỗ Trợ Hoàng Thể (LPS)",
            "author": "Giáo Trình Master Chuyên Sâu — Phần 5",
            "specialty": "Hỗ Trợ Sinh Sản & Phụ Khoa",
            "date": "2026"
        },
        # Slide 2: Key Message
        {
            "type": "key_message",
            "variant": "dark_hero",
            "kicker": "TRIẾT LÝ CHUYỂN PHÔI TRONG ADENOMYOSIS",
            "message": "Ưu Tiên Đông Phôi Toàn Bộ (Freeze-All)\nHạ Điều Hòa Chọn Lọc & Tái Mở Cửa Sổ Làm Tổ (WOI)"
        },
        # Slide 3: Objectives
        {
            "type": "objectives",
            "variant": "numbered_circles",
            "title": "Mục Tiêu Học Tập Chương 5",
            "objectives": [
                "Giải thích cơ sở sinh học vì sao ưu tiên đông phôi toàn bộ (Freeze-all) thay vì chuyển phôi tươi ở bệnh nhân Adenomyosis.",
                "Phân định rõ khuyến cáo ESHRE 2022 với các bằng chứng chuyên biệt của phác đồ Ultra-long GnRHa trong Adenomyosis lan tỏa.",
                "Thực hành đúng quy trình 5 bước chuẩn bị nội mạc bằng HRT và bước siêu âm đánh giá lại JZ bắt buộc.",
                "Làm chủ chiến lược cá thể hóa (thể khu trú vs thể lan tỏa) và tối ưu hóa hỗ trợ hoàng thể đạt mục tiêu P4 huyết thanh."
            ]
        },
        # Slide 4: Tổng quan chiến lược FET
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tổng Quan Chiến Lược Chuẩn Bị Niêm Mạc Chuyển Phôi Cho Adenomyosis",
            "points": [
                "Thách thức nội mạc trong Adenomyosis: Tình trạng viêm mạn tính, tự sản xuất Estrogen tại chỗ và đề kháng Progesterone làm hỏng quá trình màng rụng hóa.",
                "Chiến lược 2 giai đoạn: Giai đoạn 1 kiểm soát tổn thương cơ tử cung và tái lập nhạy cảm thụ thể → Giai đoạn 2 chuẩn bị nội mạc đón nhận phôi.",
                "Phân tầng theo thể tổn thương: Phân biệt rõ thể khu trú nhỏ (< 2 cm, JZ < 12 mm) với thể lan tỏa nặng (tử cung to > 8 cm, JZ ≥ 12 mm).",
                "Mục tiêu cuối cùng: Tái mở cửa sổ làm tổ (WOI), kiểm soát nhu động cơ tử cung và tối ưu hóa nồng độ Progesterone huyết thanh ngày chuyển phôi."
            ]
        },
        # Slide 5: Tại sao ưu tiên Freeze-all
        {
            "type": "content",
            "variant": "bullets",
            "title": "Cơ Sở Sinh Học Của Việc Ưu Tiên Đông Phôi Toàn Bộ (Freeze-All)",
            "points": [
                "Tác hại của môi trường kích trứng tươi: Nồng độ Estradiol trong chu kỳ tươi tăng vọt lên mức siêu sinh lý (> 3000 - 5000 pg/mL).",
                "Kích hoạt ổ viêm u cơ tuyến: Estrogen siêu cao kích thích trực tiếp các thụ thể hormone trong cơ tử cung, làm các ổ Adenomyosis phù nề và tăng co thắt dữ dội.",
                "Đình trệ màng rụng hóa: Nồng độ Estrogen quá mức làm lệch pha cửa sổ làm tổ (WOI) và làm nặng thêm tình trạng đề kháng Progesterone.",
                "Lợi ích của Freeze-all: Đông toàn bộ phôi ngày 5 giúp đưa cơ thể người bệnh thoát khỏi môi trường kích thích hormone nặng nề, chuẩn bị niêm mạc ở trạng thái cơ tử cung ổn định nhất."
            ]
        },
        # Slide 6: Bằng chứng FET trong Lạc nội mạc tử cung
        {
            "type": "content",
            "variant": "bullets",
            "title": "Bằng Chứng EBM Về Chuyển Phôi Đông Lạnh (FET) Trong Lạc Nội Mạc Tử Cung",
            "points": [
                "Tổng quan hệ thống Han et al. (Front Endocrinol 2025 - PMID: 40438397): Phân tích trên phân nhóm bệnh nhân Lạc nội mạc tử cung.",
                "Tăng tỷ lệ làm tổ: Chiến lược FET mang lại tỷ lệ làm tổ cao hơn rõ rệt so với chuyển phôi tươi (OR = 1.27, 95% CI: 1.05 - 1.54).",
                "Tăng tỷ lệ thai lâm sàng & sinh sống: FET cải thiện tỷ lệ thai lâm sàng (OR = 1.25, 95% CI: 1.11 - 1.40) và tỷ lệ trẻ sinh sống (OR = 1.31, 95% CI: 1.15 - 1.49).",
                "Lưu ý đối với Adenomyosis: Đối với thể u cơ tuyến nặng, kết quả chuyển phôi cần được cá thể hóa dựa trên mức độ tổn thương cơ tử cung và thảo luận cùng người bệnh."
            ]
        },
        # Slide 7: Phân định ESHRE 2022 vs Adenomyosis
        {
            "type": "content",
            "variant": "bullets",
            "title": "Phân Định Khuyến Cáo ESHRE 2022 Với Bằng Chứng Trên Adenomyosis",
            "points": [
                "Khuyến cáo ESHRE 2022 cho Endometriosis nói chung (PMID: 35350465): Không khuyến cáo dùng phác đồ GnRH agonist kéo dài thường quy trước ART vì chưa chứng minh được lợi ích rõ ràng trên nhóm cơ tử cung bình thường (Strong rec, Low certainty).",
                "Bản chất khác biệt trong Adenomyosis: Tổn thương nằm ngay tại lớp cơ và Vùng chuyển tiếp JZ, nơi xuất hiện vòng xoắn tự tạo Estrogen và đề kháng PR-B.",
                "Tổng quan chuyên biệt trên Adenomyosis (Latif et al., EJOGRB 2024 - PMID: 39116480): Hạ điều hòa bằng GnRHa trước FET cải thiện tỷ lệ làm tổ (OR = 1.69) và tỷ lệ thai lâm sàng (OR = 1.42).",
                "Nguyên tắc chỉ định: Áp dụng có chọn lọc cho thể lan tỏa nặng dựa trên thảo luận và chia sẻ quyết định cùng người bệnh (shared decision-making)."
            ]
        },
        # Slide 8: Cơ chế Ultra-long GnRHa
        {
            "type": "content",
            "variant": "bullets",
            "title": "Cơ Chế Phục Hồi Cửa Sổ Làm Tổ Của Phác Đồ Ultra-Long GnRH Agonist",
            "points": [
                "Cắt đứt nguồn Estrogen nuôi dưỡng: GnRHa Depot ức chế thụ thể GnRH tuyến yên (down-regulation), đưa cơ thể về trạng thái mãn kinh tạm thời trong 2-3 tháng.",
                "Thu nhỏ thể tích u cơ tuyến: Cắt nguồn nội tiết làm teo nhỏ các ổ tuyến lạc chỗ và giảm phù nề cơ tử cung.",
                "Ức chế men Aromatase & Viêm: Giảm biểu hiện enzyme Aromatase (CYP19A1), giảm sản xuất Prostaglandin E2 (PGE2) và các cytokine viêm tại chỗ.",
                "Tái thiết lập thụ thể PR-B: Khôi phục độ nhạy của nội mạc tử cung với Progesterone, tái mở cửa sổ làm tổ (WOI) và dập tắt các cơn loạn động cơ tử cung (Dysperistalsis)."
            ]
        },
        # Slide 9: Quy trình 5 bước Ultra-long + HRT
        {
            "type": "content",
            "variant": "bullets",
            "title": "Quy Trình 5 Bước Thực Hiện Phác Đồ Ultra-Long GnRHa + HRT Chuẩn",
            "points": [
                "Bước 1 — Hạ điều hòa tuyến yên: Tiêm bắp GnRH Agonist Depot (Triptorelin hoặc Leuprolide 3.75 mg) từ 1 đến 3 mũi (mỗi mũi cách nhau 28 ngày).",
                "Bước 2 — Siêu âm đánh giá lại (Clinical Pearl): Sau mũi cuối 28 ngày, bắt buộc siêu âm ngả âm đạo đo lại thể tích tử cung và độ dày JZ.",
                "Bước 3 — Chuẩn bị nội mạc bằng Estrogen: Bắt đầu uống Estradiol valerate (Progynova 4 - 6 mg/ngày) tăng dần để kích thích niêm mạc phát triển.",
                "Bước 4 — Bổ sung Progesterone: Khi niêm mạc đạt độ dày ≥ 8 mm và có cấu trúc 3 lá (triple-line), bắt đầu dùng Progesterone.",
                "Bước 5 — Chuyển phôi đông lạnh (FET): Tiến hành chuyển phôi sau đúng 120 giờ tiếp xúc Progesterone đối với phôi nang ngày 5."
            ]
        },
        # Slide 10: Bước siêu âm đánh giá lại JZ
        {
            "type": "content",
            "variant": "bullets",
            "title": "Bước Đánh Giá Lại Cơ Tử Cung Sau Hạ Điều Hòa (Clinical Pearl Sống Còn)",
            "points": [
                "Thời điểm kiểm tra: 28 ngày sau mũi tiêm GnRH Agonist Depot thứ 2 hoặc thứ 3.",
                "Tiêu chuẩn đạt yêu cầu: Thể tích tử cung co nhỏ rõ rệt, cơ tử cung bớt phù nề, bề dày JZ giảm rõ (JZ < 10 - 12 mm trên TVS/3D).",
                "Xử trí khi đáp ứng tốt: Bắt đầu cho bệnh nhân uống Estrogen ngoại sinh (HRT) để chuẩn bị niêm mạc.",
                "Xử trí khi chưa đáp ứng: Nếu tử cung vẫn to và cơ tử cung còn phù nề tăng âm mạnh, cân nhắc tiêm thêm mũi thứ 3 hoặc hội chẩn điều trị bổ trợ trước khi dùng Estrogen."
            ]
        },
        # Slide 11: Cá thể hóa thể khu trú vs lan tỏa
        {
            "type": "content",
            "variant": "bullets",
            "title": "Cá Thể Hóa Phác Đồ Chuẩn Bị Niêm Mạc Theo Mức Độ Tổn Thương",
            "points": [
                "Adenomyosis Thể Nhẹ / Khu Trú Nhỏ (< 2 cm, JZ < 12 mm):",
                "  - Không nhất thiết phải tiêm GnRHa kéo dài 2-3 tháng để tránh tác dụng phụ bốc hỏa và kéo dài thời gian.",
                "  - Chuẩn bị niêm mạc bằng HRT chuẩn hoặc phác đồ chu kỳ tự nhiên cải biên kết hợp Letrozole.",
                "Adenomyosis Thể Lan Tỏa Nặng (JZ ≥ 12 mm, Tử cung to hình cầu > 8 cm):",
                "  - Cân nhắc chỉ định phác đồ Ultra-long GnRHa 2 - 3 tháng sau khi đã tư vấn kỹ lợi ích và nguy cơ cho người bệnh.",
                "  - Kết hợp hỗ trợ hoàng thể đa đường dùng để đạt tỷ lệ trẻ sinh sống tối ưu."
            ]
        },
        # Slide 12: Tối ưu hóa hoàng thể LPS
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tối Ưu Hóa Hỗ Trợ Pha Hoàng Thể (LPS) Trong Chu Kỳ Chuyển Phôi FET",
            "points": [
                "Nhu cầu Progesterone tăng cao: Do tình trạng đề kháng Progesterone nội tại, bệnh nhân Adenomyosis cần chế độ hỗ trợ hoàng thể mạnh mẽ hơn bình thường.",
                "Phối hợp đa đường dùng (Vaginal + Injectable):",
                "  - Progesterone đặt âm đạo: Micro-progesterone 800 mg/ngày (chia 2-4 lần) để tạo nồng độ cao trực tiếp tại mô nội mạc tử cung.",
                "  - KẾT HỢP Progesterone tiêm: Progesterone tiêm bắp 50 mg/ngày hoặc tiêm dưới da (Prolutex 25 mg/ngày) để đảm bảo nồng độ trong máu.",
                "Thời điểm bắt đầu: Bắt đầu dùng Progesterone khi niêm mạc đạt chuẩn ≥ 8 mm cấu trúc 3 lá; chuyển phôi sau đúng 120 giờ tiếp xúc đối với phôi ngày 5."
            ]
        },
        # Slide 13: Mục tiêu Progesterone huyết thanh
        {
            "type": "content",
            "variant": "bullets",
            "title": "Mục Tiêu Nồng Độ Progesterone Huyết Thanh Ngày Chuyển Phôi",
            "points": [
                "Thời điểm xét nghiệm: Định lượng nồng độ Progesterone (P4) trong máu vào buổi sáng ngày chuyển phôi.",
                "Mục tiêu điều trị: Nồng độ P4 huyết thanh phải đạt tối thiểu > 10 - 15 ng/mL (tương đương > 32 - 48 nmol/L).",
                "Xử trí khi P4 dưới ngưỡng (< 10 ng/mL): Tăng ngay liều Progesterone tiêm (bổ sung Prolutex 25 mg SC hoặc Progesterone dầu 50 mg IM) ngay trong ngày chuyển phôi.",
                "Cứu vãn chu kỳ: Đảm bảo nồng độ P4 đạt chuẩn giúp duy trì tỷ lệ làm tổ và giảm thiểu tối đa nguy cơ sảy thai sớm trong 3 tháng đầu."
            ]
        },
        # Slide 14: Tóm tắt Chương 5
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tóm Tắt Cốt Lõi Chương 5 (Thông Điệp Master)",
            "points": [
                "Ưu tiên Freeze-all: Đông toàn bộ phôi ngày 5 để tránh nồng độ Estrogen siêu sinh lý kích hoạt ổ viêm cơ tử cung trong chu kỳ tươi.",
                "Phân định chỉ định ESHRE 2022: Không dùng Ultra-long thường quy cho Lạc nội mạc TC nói chung, nhưng áp dụng chọn lọc cho Adenomyosis thể lan tỏa nặng.",
                "Hiệu quả Ultra-long: Giúp cải thiện tỷ lệ làm tổ (OR = 1.69) và thai lâm sàng (OR = 1.42 theo Latif 2024), tái lập thụ thể PR-B.",
                "Đánh giá lại JZ: Bắt buộc siêu âm kiểm tra tử cung co nhỏ và JZ đạt chuẩn sau 2-3 tháng hạ điều hòa trước khi dùng Estrogen HRT.",
                "Tối ưu hóa hoàng thể LPS: Phối hợp Progesterone âm đạo (800 mg) + tiêm (50 mg), đảm bảo mục tiêu P4 huyết thanh ngày chuyển phôi > 10 - 15 ng/mL."
            ]
        },
        # Slide 15: References Chương 5
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tài Liệu Tham Khảo Y Học Chứng Cứ Của Chương 5",
            "points": [
                "ESHRE Guideline: Endometriosis. Hum Reprod Open. 2022;2022(2):hoac009. PMID: 35350465.",
                "Latif S, Kastora S, Al Wattar BH, et al. The effectiveness of prolonged downregulation with GnRHa in women with adenomyosis undergoing IVF/ICSI. Eur J Obstet Gynecol Reprod Biol. 2024;301:120-128. PMID: 39116480.",
                "Wu Y, Huang J, Zhong G, et al. Long-term GnRH agonist pretreatment before frozen embryo transfer improves pregnancy outcomes in women with adenomyosis. Reprod Biomed Online. 2022;44(2):380-388. PMID: 34895827.",
                "Lan J, Yang H, et al. Prolonged gonadotropin-releasing hormone agonist protocol improves the pregnancy outcomes of in vitro fertilization in patients with adenomyosis. Ann Transl Med. 2021; PMID: 34135858.",
                "Han Y, Liu C, Liu D, et al. Pregnancy outcomes in freeze-all versus fresh embryo transfer cycles of women with adenomyosis and endometriosis. Front Endocrinol. 2025; PMID: 40438397.",
                "Cozzolino M, Tartaglia S, et al. The Effect of Uterine Adenomyosis on IVF Outcomes. Reprod Sci. 2022; PMID: 34981458."
            ]
        }
    ]
}

deck_ch5_json = TARGET_DIR / "chapter_5_slider3636_deck.json"
deck_ch5_json.write_text(json.dumps(pure_bullet_chapter_5, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved Chapter 5 deck JSON ({len(pure_bullet_chapter_5['slides'])} slides): {deck_ch5_json}")

slider3636.set_theme("Medical Teal", "Segoe UI", "Standard — mặc định", show_pagenum=False)
out_pptx_ch5 = OUTPUTS_DIR / "Chuong_05_Chuan_bi_niem_mac_FET_Mastery_v2.pptx"
out_path, rendered = slider3636.build_presentation(pure_bullet_chapter_5, str(out_pptx_ch5))
print(f"\n🎉 Successfully compiled Chapter 5 Master Deck: {out_pptx_ch5} ({out_pptx_ch5.stat().st_size} bytes, {rendered} slides rendered)")
