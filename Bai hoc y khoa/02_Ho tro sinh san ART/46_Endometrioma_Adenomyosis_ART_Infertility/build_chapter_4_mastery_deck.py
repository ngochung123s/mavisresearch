# -*- coding: utf-8 -*-
"""build_chapter_4_mastery_deck.py — Build Chapter 4 standalone master slide deck with pure unnumbered bullet points."""
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

pure_bullet_chapter_4 = {
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
            "title": "CHƯƠNG 4: KÍCH THÍCH BUỒNG TRỨNG & AN TOÀN CHỌC HÚT NOÃN",
            "subtitle": "Phác Đồ Antagonist, PPOS, Kích Thích Kép DuoStim & An Toàn Thủ Thuật OPU",
            "author": "Giáo Trình Master Chuyên Sâu — Phần 4",
            "specialty": "Hỗ Trợ Sinh Sản & Phụ Khoa",
            "date": "2026"
        },
        # Slide 2: Key Message
        {
            "type": "key_message",
            "variant": "dark_hero",
            "kicker": "TRIẾT LÝ KÍCH TRỨNG TRONG OMA",
            "message": "Cá Thể Hóa Phác Đồ Kích Trứng Theo Dự Trữ Buồng Trứng\nVà Đảm Bảo An Toàn Tuyệt Đối Trong Thủ Thuật Chọc Hút Noãn"
        },
        # Slide 3: Objectives
        {
            "type": "objectives",
            "variant": "numbered_circles",
            "title": "Mục Tiêu Học Tập Chương 4",
            "objectives": [
                "Thấu hiểu khuyến cáo ESHRE 2022 về tính tương đương của phác đồ GnRH Antagonist và Agonist dài.",
                "Làm chủ phác đồ PPOS trong chiến lược Freeze-all và phác đồ kích thích kép DuoStim cho bệnh nhân DOR.",
                "Nắm vững nguyên tắc phối hợp rFSH + hMG và liều khởi đầu Gonadotropin ở buồng trứng có OMA.",
                "Thực hành đúng quy trình khử khuẩn âm đạo, dùng kháng sinh dự phòng và kịch bản xử trí khi chọc nhầm vào nang OMA."
            ]
        },
        # Slide 4: Khuyến cáo ESHRE 2022
        {
            "type": "content",
            "variant": "bullets",
            "title": "Khuyến Cáo Chính Thức ESHRE 2022 Về Phác Đồ Kích Thích Buồng Trứng",
            "points": [
                "Khuyến cáo chính thức ESHRE 2022 (PMID: 35350465): Không có phác đồ ART cụ thể nào vượt trội hơn hẳn về tỷ lệ có thai hoặc tỷ lệ sinh sống ở bệnh nhân lạc nội mạc tử cung (Weak recommendation).",
                "Lựa chọn phác đồ: Cả hai phác đồ GnRH Antagonist và GnRH Agonist dài đều có thể được chỉ định dựa trên sự lựa chọn của bệnh nhân và bác sĩ.",
                "Tính an toàn của ART: ESHRE 2022 khẳng định việc kích thích buồng trứng làm ART không làm tăng nguy cơ tái phát bệnh lạc nội mạc tử cung (Somigliana et al., 2019 - PMID: 31086989).",
                "Xu hướng lâm sàng hiện đại: Phác đồ GnRH Antagonist được ưu tiên rộng rãi do thời gian tiêm ngắn hơn, giảm nguy cơ OHSS khi dùng Agonist Trigger."
            ]
        },
        # Slide 5: Phác đồ GnRH Antagonist linh hoạt
        {
            "type": "content",
            "variant": "bullets",
            "title": "Phác Đồ GnRH Antagonist Linh Hoạt (Flexible Antagonist Protocol)",
            "points": [
                "Lộ trình thực hiện: Bắt đầu tiêm Gonadotropin từ ngày 2 hoặc 3 chu kỳ kinh nguyệt.",
                "Khởi động thuốc đối vận: Bắt đầu tiêm GnRH Antagonist (Ganirelix hoặc Cetrorelix 0.25 mg/ngày) khi nang vượt trội đạt đường kính ≥ 14 mm hoặc E2 > 500 pg/mL.",
                "Mục tiêu: Ức chế chọn lọc và tức thì thụ thể GnRH tuyến yên, ngăn chặn hoàn toàn đỉnh LH sớm mà không gây hiện tượng bùng phát (flare-up).",
                "Trưởng thành noãn (Trigger) an toàn: Sử dụng GnRH Agonist Trigger (Triptorelin 0.2 mg) thay thế hCG để triệt tiêu nguy cơ quá kích buồng trứng (OHSS)."
            ]
        },
        # Slide 6: Vai trò phối hợp rFSH + hMG
        {
            "type": "content",
            "variant": "bullets",
            "title": "Cơ Sở Sinh Học Của Việc Phối Hợp rFSH + hMG Trong Buồng Trứng OMA",
            "points": [
                "Tình trạng giảm nhạy cảm thụ thể: Nhu mô buồng trứng có u OMA bị xơ hóa mô vỏ và viêm mạn tính làm giảm số lượng và độ nhạy của thụ thể FSH.",
                "Mô hình 2 tế bào - 2 Gonadotropin: Bổ sung hoạt tính LH từ hMG kích thích tế bào vỏ (theca) sản xuất đủ tiền chất Androgen sinh lý.",
                "Hỗ trợ tế bào hạt: Lượng Androgen nội tại kích hoạt enzyme Aromatase trong tế bào hạt chuyển hóa thành Estrogen, giúp nang noãn phát triển đồng đều hơn.",
                "Liều khởi đầu Gonadotropin: Thường cần liều khởi đầu cao hơn người bình thường (225 - 300 IU/ngày tùy theo AMH, AFC, tuổi và BMI) do tình trạng kháng kích thích tương đối."
            ]
        },
        # Slide 7: Phác đồ PPOS
        {
            "type": "content",
            "variant": "bullets",
            "title": "Phác Đồ PPOS (Progestin-Primed Ovarian Stimulation) Trong Chiến Lược Freeze-All",
            "points": [
                "Nguyên lý phác đồ: Sử dụng Progestin đường uống (Medroxyprogesterone acetate - MPA 10 mg/ngày; các nghiên cứu sau này mở rộng thêm với Dydrogesterone 20 mg/ngày) uống liên tục từ ngày đầu kích trứng cùng Gonadotropin (Kuang et al., 2015 - PMID: 25956370).",
                "Cơ chế ức chế LH: Nồng độ Progestin ngoại sinh tác động lên trục dưới đồi - tuyến yên ngăn chặn hoàn toàn đỉnh LH sớm qua đường uống.",
                "Ưu thế lâm sàng: Giảm đáng kể số mũi tiêm đối vận và thuận tiện hơn cho người bệnh.",
                "Bằng chứng trên bệnh nhân OMA: Nghiên cứu của Boynukalin et al. (Front Endocrinol 2025 - PMID: 40698246) trên 543 bệnh nhân OMA chứng minh PPOS cho số lượng noãn thu được và kết cục sau FET tương đương với phác đồ Antagonist."
            ]
        },
        # Slide 8: Phác đồ DuoStim
        {
            "type": "content",
            "variant": "bullets",
            "title": "Phác Đồ Kích Thích Kép (DuoStim) — Gom Noãn Khẩn Cấp Trong 1 Tháng Cho DOR",
            "points": [
                "Cơ sở sinh học: Dựa trên hiện tượng chiêu mộ nang noãn nhiều làn sóng trong một chu kỳ kinh nguyệt (Multiple follicular waves).",
                "Lộ trình 2 đợt kích trứng: Đợt 1 ở pha nang noãn (FPS) → Chọc hút noãn OPU-1 → Nghỉ 2-5 ngày → Đợt 2 kích trứng lại ở pha hoàng thể (LPS) → Chọc hút noãn OPU-2.",
                "Bằng chứng mốc (Ubaldi 2016 - PMID: 27020168): Tỷ lệ tạo phôi nang nguyên bội (euploid blastocysts) tương đương nhau giữa 2 pha (46.9% so với 44.8%).",
                "Giá trị trong Lạc nội mạc tử cung: Giải pháp cứu cánh cho bệnh nhân OMA có suy giảm dự trữ buồng trứng nặng (DOR) hoặc lớn tuổi (nhóm POSEIDON), giúp gom tối đa số noãn/phôi trong 1 tháng."
            ]
        },
        # Slide 9: Nguyên tắc an toàn OPU
        {
            "type": "content",
            "variant": "bullets",
            "title": "Thủ Thuật Chọc Hút Noãn (OPU) An Toàn — Nguyên Tắc Tiếp Cận Nang Noãn",
            "points": [
                "Nguyên tắc 'Vàng': Luôn tìm đường chọc kim trực tiếp vào các nang noãn lành, tuyệt đối không đâm kim xuyên qua nang u lạc nội mạc buồng trứng.",
                "Tránh tổn thương ruột: Đối chiếu kỹ bản đồ siêu âm IDEA trước thủ thuật; khi có dính khoang sau (#Enzian C), phải xác định rõ ranh giới trực tràng để không đâm kim vào ruột.",
                "Đo lường nang noãn cẩn trọng: Đo kích thước nang noãn trên 2 mặt cắt trực giao, tránh nhầm lẫn nang noãn lành với các thùy phụ của khối u OMA.",
                "Tối ưu hóa áp lực hút: Duy trì áp lực hút ổn định từ 100 đến 140 mmHg để bảo vệ phức hợp noãn - tế bào hạt (COC)."
            ]
        },
        # Slide 10: Dự phòng nhiễm trùng OPU
        {
            "type": "content",
            "variant": "bullets",
            "title": "Dự Phòng Nhiễm Trùng & Áp Xe Buồng Trứng Sau Chọc Hút Noãn",
            "points": [
                "Kháng sinh dự phòng theo ESHRE 2022 (GPP): ESHRE 2022 ghi nhận nguy cơ áp xe buồng trứng sau chọc hút là thấp nhưng cho phép bác sĩ lâm sàng cân nhắc sử dụng kháng sinh dự phòng (GPP); phác đồ tiêm tĩnh mạch phổ rộng (Ceftriaxone 1g + Metronidazole 500mg) là thực hành thường quy tại các trung tâm IVF.",
                "Quy trình khử khuẩn âm đạo đúng cách: Sát trùng âm đạo bằng dung dịch Povidone-iodine pha loãng kỹ lưỡng.",
                "BẮT BUỘC rửa sạch bằng nước muối: Phải dùng nước muối sinh lý ấm (NaCl 0.9%) rửa sạch hoàn toàn Povidone-iodine trước khi chọc kim (vì Povidone-iodine có tính độc noãn cực mạnh).",
                "Phòng ngừa áp xe buồng trứng: Dịch nang OMA là môi trường nuôi cấy vi khuẩn yếm khí cực tốt nếu bị kim mang vi khuẩn từ âm đạo đâm vào."
            ]
        },
        # Slide 11: Xử trí chọc nhầm OMA
        {
            "type": "content",
            "variant": "bullets",
            "title": "Kịch Bản Xử Trí Sự Cố Khi Vô Tình Chọc Kim Vào Nang OMA (Clinical Pearl)",
            "points": [
                "Hành động tức thì: TUYỆT ĐỐI KHÔNG ĐƯỢC hút dịch sô-cô-la lẫn vào ống nghiệm chứa dịch hút noãn.",
                "Ngừng hút áp lực âm ngay lập tức: Rút kim chọc hút ra ngoài buồng trứng.",
                "Thay kim hoặc súc rửa kỹ: Thay kim chọc hút mới hoặc súc rửa kỹ lòng kim bằng môi trường nuôi cấy chuyên dụng.",
                "Chuyển hướng tiếp cận: Chuyển đầu dò sang chọc các nang noãn lành ở buồng trứng đối diện trước.",
                "Bơm rửa khoang chậu sau OPU: Nếu nghi ngờ có dịch u OMA rò rỉ vào ổ bụng, tiến hành bơm rửa sạch túi cùng Douglas bằng nước muối sinh lý ấm để ngừa viêm phúc mạc hóa học."
            ]
        },
        # Slide 12: Tóm tắt Chương 4
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tóm Tắt Cốt Lõi Chương 4 (Thông Điệp Master)",
            "points": [
                "Khuyến cáo ESHRE 2022: Antagonist và Agonist dài có tỷ lệ sinh sống tương đương; ART không làm tăng tái phát lạc nội mạc tử cung.",
                "Phác đồ Antagonist & PPOS: Ưu tiên trong chiến lược Freeze-all giúp tối ưu hóa số lượng noãn và giảm nguy cơ OHSS.",
                "Phác đồ DuoStim: Chiến lược gom noãn kép trong 1 tháng cứu cánh cho bệnh nhân OMA có suy giảm dự trữ buồng trứng (DOR).",
                "An toàn thủ thuật OPU: Không đâm kim xuyên qua u OMA; rửa sạch Povidone-iodine bằng nước muối ấm và dùng kháng sinh dự phòng tĩnh mạch.",
                "Xử trí chọc nhầm: Ngừng hút ngay, thay kim mới, không để dịch sô-cô-la nhiễm vào dịch noãn và bơm rửa túi cùng Douglas sau thủ thuật."
            ]
        },
        # Slide 13: References Chương 4
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tài Liệu Tham Khảo Y Học Chứng Cứ Của Chương 4",
            "points": [
                "ESHRE Guideline: Endometriosis. Hum Reprod Open. 2022;2022(2):hoac009. PMID: 35350465.",
                "Kolanska K, Cohen J, et al. Pregnancy outcomes after controlled ovarian hyperstimulation in women with endometriosis: GnRH-agonist versus GnRH-antagonist. J Gynecol Obstet Hum Reprod. 2017; PMID: 28970135.",
                "Kuang Y, Chen Q, et al. Medroxyprogesterone acetate is an effective oral alternative for preventing premature LH surges in women undergoing controlled ovarian hyperstimulation for in vitro fertilization. Fertil Steril. 2015; PMID: 25956370.",
                "Boynukalin FK, Turgut E, et al. A comparative analysis of progestin-primed ovarian stimulation versus GnRH antagonists protocols in patients with endometrioma. Front Endocrinol. 2025; PMID: 40698246.",
                "Ubaldi FM, Capalbo A, et al. Follicular versus luteal phase ovarian stimulation during the same menstrual cycle (DuoStim) in a reduced ovarian reserve population. Fertil Steril. 2016; PMID: 27020168.",
                "Vaiarelli A, Venturella R, et al. Double Stimulation in the Same Ovarian Cycle (DuoStim) to Maximize the Number of Oocytes Retrieved From Poor Prognosis Patients. Front Endocrinol. 2018; PMID: 29963011.",
                "Somigliana E, Vigano P, et al. Association between in vitro fertilization and endometriosis recurrence: a systematic review. Hum Reprod Update. 2019; PMID: 31086989."
            ]
        }
    ]
}

deck_ch4_json = TARGET_DIR / "chapter_4_slider3636_deck.json"
deck_ch4_json.write_text(json.dumps(pure_bullet_chapter_4, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved Chapter 4 deck JSON ({len(pure_bullet_chapter_4['slides'])} slides): {deck_ch4_json}")

slider3636.set_theme("Medical Teal", "Segoe UI", "Standard — mặc định", show_pagenum=False)
out_pptx_ch4 = OUTPUTS_DIR / "Chuong_04_Kich_thich_buong_trung_Mastery.pptx"
out_path, rendered = slider3636.build_presentation(pure_bullet_chapter_4, str(out_pptx_ch4))
print(f"\n🎉 Successfully compiled Chapter 4 Master Deck: {out_pptx_ch4} ({out_pptx_ch4.stat().st_size} bytes, {rendered} slides rendered)")
