# -*- coding: utf-8 -*-
"""build_chapter_6_mastery_deck.py — Build Chapter 6 standalone master slide deck with pure unnumbered bullet points."""
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

pure_bullet_chapter_6 = {
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
            "title": "CHƯƠNG 6: THEO DÕI THAI KỲ & QUẢN LÝ BIẾN CHỨNG SẢN KHOA",
            "subtitle": "Dự Phòng Tiền Sản Giật, Tầm Soát Sinh Non, Rau Cài Răng Lược & Xử Trí Đờ Tử Cung PPH",
            "author": "Giáo Trình Master Chuyên Sâu — Phần 6",
            "specialty": "Hỗ Trợ Sinh Sản & Sản Phụ Khoa",
            "date": "2026"
        },
        # Slide 2: Key Message
        {
            "type": "key_message",
            "variant": "dark_hero",
            "kicker": "TRIẾT LÝ QUẢN LÝ SẢN KHOA TOÀN DIỆN",
            "message": "Đậu Thai Chỉ Là Khởi Đầu — Quản Lý Thai Kỳ Nguy Cơ Cao\nChủ Động Dự Phòng Biến Cứng Để Đảm Bảo An Toàn Cho Mẹ & Con"
        },
        # Slide 3: Objectives
        {
            "type": "objectives",
            "variant": "numbered_circles",
            "title": "Mục Tiêu Học Tập Chương 6",
            "objectives": [
                "Nhận thức rõ các nguy cơ sản khoa đặc thù ở thai phụ có Adenomyosis và Endometriosis.",
                "Thực hành đúng phác đồ dự phòng sảy thai quý 1 và tầm soát sinh non qua chiều dài cổ tử cung (CL) quý 2.",
                "Nắm vững cơ chế khiếm khuyết tái cấu trúc động mạch xoắn và phác đồ dự phòng Tiền sản giật bằng Aspirin.",
                "Hiểu rõ cơ chế enzyme MMPs gây đờ tử cung dẫn đến Băng huyết sau sinh (PPH) và cảnh giác vỡ tử cung."
            ]
        },
        # Slide 4: Lộ trình 3 quý thai kỳ
        {
            "type": "content",
            "variant": "bullets",
            "title": "Lộ Trình Theo Dõi Thai Kỳ Nguy Cơ Cao Qua 3 Tam Cá Nguyệt",
            "points": [
                "Tam cá nguyệt 1 (Tuần 1 - 13): Phòng ngừa dọa sảy thai, duy trì Progesterone hoàng thể đến tuần 10-12, khởi động Aspirin từ tuần 12.",
                "Tam cá nguyệt 2 (Tuần 14 - 27): Siêu âm đo chiều dài kênh cổ tử cung (CL) định kỳ tuần 16-24 ngừa sinh non, khám hình thái học thai nhi.",
                "Tam cá nguyệt 3 (Tuần 28 trở đi): Khảo sát Doppler bánh rau tầm soát Rau tiền đạo và Rau cài răng lược (PAS), theo dõi tăng trưởng thai ngừa FGR.",
                "Chuyển dạ & Hậu sản: Chủ động dự phòng Băng huyết sau sinh (PPH) do đờ tử cung xơ hóa và cảnh giác nguy cơ vỡ tử cung ở bệnh nhân từng bóc u cơ tuyến."
            ]
        },
        # Slide 5: Quý 1 Sảy thai
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tam Cá Nguyệt 1 — Nguy Cơ Sảy Thai Tự Nhiên & Chiến Lược Duy Trì Hoàng Thể",
            "points": [
                "Nguy cơ sảy thai tăng gấp đôi: Các phân tích gộp (Cozzolino 2022 / Vercellini 2014) chứng minh nguy cơ sảy thai quý 1 ở thai phụ Adenomyosis tăng hơn 2 lần (RR ≈ 2.12 - 2.17).",
                "Cơ chế bệnh sinh: Tình trạng viêm mạn tính cơ tử cung, tăng tiết PGE2, loạn động cơ tử cung (Dysperistalsis) và khiếm khuyết màng rụng hóa làm giảm độ bám của gai rau sớm.",
                "Duy trì hỗ trợ hoàng thể: Bắt buộc duy trì Progesterone liên tục đến hết tuần thai thứ 10 - 12 (thời điểm bánh rau tự sản xuất đủ Progesterone thay thế hoàng thể).",
                "Theo dõi hình ảnh siêu âm: Khảo sát định kỳ túi thai và nồng độ P4 để phát hiện sớm các ổ bóc tách màng nuôi hoặc tụ dịch dưới màng đệm."
            ]
        },
        # Slide 6: Quý 2 Sinh non
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tam Cá Nguyệt 2 — Tầm Soát Sinh Non & Đánh Giá Chiều Dài Cổ Tử Cung (CL)",
            "points": [
                "Nguy cơ chuyển dạ sinh non: Tăng từ 1.5 đến 1.8 lần ở thai phụ có Adenomyosis và Lạc nội mạc tử cung sâu.",
                "Cơ chế sinh non: Sự xơ hóa của u cơ tuyến làm giảm tính đàn hồi giãn nở của thân tử cung khi thai lớn, kết hợp các cytokine viêm kích hoạt sớm cơn co chuyển dạ.",
                "Quy trình tầm soát CL: Siêu âm ngả âm đạo đo chiều dài kênh cổ tử cung (Cervical Length - CL) định kỳ mỗi 2 tuần một lần từ tuần thai thứ 16 đến 24.",
                "Can thiệp khi cổ tử cung ngắn (CL < 25 mm): Đặt Progesterone tự nhiên âm đạo liều cao (200 - 400 mg/ngày) liên tục đến tuần 36; cân nhắc đặt vòng nâng pessary hoặc khâu vòng cổ tử cung."
            ]
        },
        # Slide 7: Tiền sản giật & Aspirin
        {
            "type": "content",
            "variant": "bullets",
            "title": "Dự Phòng Tiền Sản Giật (Preeclampsia) & Thai Chậm Tăng Trưởng (FGR)",
            "points": [
                "Cơ chế khiếm khuyết bánh rau: Vùng chuyển tiếp (JZ) bị xơ hóa cản trở nguyên bào nuôi xâm lấn sâu, dẫn đến khiếm khuyết tái cấu trúc động mạch xoắn (Defective deep placentation).",
                "Hậu quả: Động mạch xoắn vẫn hẹp và có sức cản cao, gây thiếu máu cục bộ bánh rau mạn tính dẫn đến Tiền sản giật và Thai chậm tăng trưởng (FGR).",
                "Phác đồ dự phòng bằng Aspirin liều thấp: Uống Aspirin 100 - 150 mg/ngày vào buổi tối trước khi đi ngủ.",
                "Thời điểm vàng: Bắt đầu từ tuần thai thứ 12 (trước tuần 16 để đón đầu đợt xâm lấn thứ 2 của nguyên bào nuôi) và duy trì liên tục đến tuần thứ 36."
            ]
        },
        # Slide 8: Rau tiền đạo & PAS
        {
            "type": "content",
            "variant": "bullets",
            "title": "Bất Thường Bám Bánh Rau: Rau Tiền Đạo & Phổ Bệnh Lý Rau Cài Răng Lược (PAS)",
            "points": [
                "Rau tiền đạo (Placenta Previa): Vùng đáy và thân tử cung xơ hóa kém thuận lợi khiến phôi nang bám thấp xuống đoạn dưới cổ tử cung, tăng nguy cơ rau tiền đạo gấp 2-3 lần.",
                "Phổ bệnh lý Rau cài răng lược (PAS): Khuyết thiếu lớp nội mạc đáy và màng rụng nền khiến các gai rau ăn sâu trực tiếp vào lớp cơ tử cung (Accreta/Increta) hoặc xuyên thủng thanh mạc (Percreta).",
                "Khảo sát siêu âm Doppler chuyên sâu: Siêu âm 2D và Doppler màu ở tuần thai 20-24 và 30-32 để tìm các dấu hiệu: Mất dải giảm âm sau rau, hồ huyết xoáy bất thường (lacunae) trong bánh rau.",
                "Kế hoạch sinh an toàn: Hội chẩn liên chuyên khoa và mổ lấy thai chủ động tại các trung tâm sản khoa lớn có sẵn nguồn máu và phẫu thuật viên giàu kinh nghiệm."
            ]
        },
        # Slide 9: Cơ chế đờ tử cung PPH do MMPs
        {
            "type": "content",
            "variant": "bullets",
            "title": "Cơ Chế Phân Tử Của Đờ Tử Cung & Băng Huyết Sau Sinh (PPH) Ở Adenomyosis",
            "points": [
                "Hiệu ứng 'Nút thắt sống' bình thường: Sau khi sổ rau, các sợi cơ trơn đan chéo co rút mạnh mẽ thắt nghẹt cơ học các mạch máu hở tại diện rau bám để cầm máu sinh lý.",
                "Sự phá hủy của enzyme MMPs: Mô tuyến lạc chỗ trong cơ tiết ra các enzyme tiêu protein (Matrix Metalloproteinases - MMPs) và cytokine viêm phá hủy mạng lưới collagen đàn hồi.",
                "Mất khả năng co rút sinh lý: Cơ tử cung bị xơ hóa cứng đờ, mất hoàn toàn khả năng co rút (Uterine Atony) sau khi sổ rau, dẫn đến chảy máu ồ ạt (Gruber et al., 2026 - PMID: 42453498).",
                "Chiến lược xử trí chủ động: Tiêm thuốc tăng co tích cực ngay sau sổ thai (Oxytocin liều cao, Carbetocin, Misoprostol) và sẵn sàng bóng chèn Bakri hoặc phẫu thuật thắt mạch."
            ]
        },
        # Slide 10: Cảnh giác vỡ tử cung
        {
            "type": "content",
            "variant": "bullets",
            "title": "Cảnh Giác Nguy Cơ Vỡ Tử Cung (Uterine Rupture) & Chiến Lược Đỡ Đẻ An Toàn",
            "points": [
                "Đối tượng nguy cơ cao: Sản phụ có tiền sử phẫu thuật bóc u tuyến cơ tử cung (Adenomyomectomy) trước khi mang thai.",
                "Bản chất sẹo mổ Adenomyosis: Khác với u xơ có vỏ bao rõ, sẹo mổ bóc Adenomyosis nằm trên nền mô cơ bị viêm xơ hóa nên quá trình lành sẹo kém bền vững.",
                "Nguy cơ vỡ tự phát: Tử cung có nguy cơ vỡ tự phát trong 3 tháng cuối thai kỳ hoặc ngay khi xuất hiện những cơn co chuyển dạ đầu tiên mà không có triệu chứng báo trước.",
                "Chiến lược kết thúc thai kỳ: Chỉ định Mổ lấy thai chủ động khi thai đủ tháng (37 đến 38 tuần), tuyệt đối không thử thách sinh đường âm đạo và không dùng thuốc kích thích chuyển dạ."
            ]
        },
        # Slide 11: Tóm tắt Chương 6
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tóm Tắt Cốt Lõi Chương 6 (Thông Điệp Master)",
            "points": [
                "Tam cá nguyệt 1: Duy trì hỗ trợ hoàng thể bằng Progesterone liên tục đến tuần 10-12 ngừa nguy cơ sảy thai tăng gấp đôi (RR ≈ 2.17).",
                "Tam cá nguyệt 2: Đo chiều dài cổ tử cung (CL) định kỳ tuần 16-24 phát hiện sớm nguy cơ sinh non; dùng Aspirin liều thấp (100-150 mg/ngày) từ tuần 12 dự phòng Tiền sản giật.",
                "Tam cá nguyệt 3: Khảo sát Doppler màu phát hiện sớm Rau tiền đạo và Rau cài răng lược (PAS) do khiếm khuyết lớp nội mạc đáy.",
                "Chuyển dạ & Hậu sản: Chủ động phòng ngừa Đờ tử cung gây Băng huyết sau sinh (PPH) do enzyme MMPs phá hủy sợi cơ; mổ lấy thai chủ động ở tuần 37-38 nếu có tiền sử bóc u tuyến cơ."
            ]
        },
        # Slide 12: References Chương 6
        {
            "type": "content",
            "variant": "bullets",
            "title": "Tài Liệu Tham Khảo Y Học Chứng Cứ Của Chương 6",
            "points": [
                "Cozzolino M, Tartaglia S, et al. The Effect of Uterine Adenomyosis on IVF Outcomes: a Systematic Review and Meta-analysis. Reprod Sci. 2022; PMID: 34981458.",
                "Vercellini P, Consonni D, et al. Uterine adenomyosis and in vitro fertilization outcome. Hum Reprod. 2014; PMID: 24622619.",
                "Gruber TM, Ebeling G, Henrich W, et al. Increased risk of postpartum hemorrhage in women with endometriosis and adenomyosis: a prospective cohort study. Front Endocrinol. 2026; PMID: 42453498.",
                "Leone Roberti Maggiore U, Ferrero S, et al. Endometriosis and pregnancy: a systematic review on maternal and neonatal complications. Hum Reprod Update. 2016; PMID: 27154869.",
                "Brosens I, Pijnenborg R, Vercruysse L, et al. The ‘Great Obstetrical Syndromes’ are associated with disorders of deep placentation. Am J Obstet Gynecol. 2011; PMID: 21055714."
            ]
        }
    ]
}

deck_ch6_json = TARGET_DIR / "chapter_6_slider3636_deck.json"
deck_ch6_json.write_text(json.dumps(pure_bullet_chapter_6, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved Chapter 6 deck JSON ({len(pure_bullet_chapter_6['slides'])} slides): {deck_ch6_json}")

slider3636.set_theme("Medical Teal", "Segoe UI", "Standard — mặc định", show_pagenum=False)
out_pptx_ch6 = OUTPUTS_DIR / "Chuong_06_Quan_ly_San_khoa_Mastery.pptx"
out_path, rendered = slider3636.build_presentation(pure_bullet_chapter_6, str(out_pptx_ch6))
print(f"\n🎉 Successfully compiled Chapter 6 Master Deck: {out_pptx_ch6} ({out_pptx_ch6.stat().st_size} bytes, {rendered} slides rendered)")
