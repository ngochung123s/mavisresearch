"""
build_master_ped_decks.py
Tạo bộ thẻ Anki Master kết hợp hoàn chỉnh cho PED-46 và PED-47:
- Track 1: [🏛️ BAREM GỐC Y THÁI BÌNH] (Bản 1 - Học thuộc lòng để ăn trọn điểm thi tự luận Bộ môn)
- Track 2: [🔬 EBM HIỆN ĐẠI & LÂM SÀNG] (Bản 2 - Phản xạ chẩn đoán lâm sàng, cờ đỏ cấp cứu và guideline quốc tế)
- Xuất file .cards.v2.json và file .apkg nhị phân thực thụ cho Anki.
- Cập nhật data.js cho PedViewer.
"""
import json
import genanki
from pathlib import Path

BASE_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa")
PED46_DIR = BASE_DIR / "04_Tieu_hoa_va_Dinh_duong" / "PED-46_Tiep_can_gan_to"
PED47_DIR = BASE_DIR / "06_Than_Tim_mach_Noi_tiet" / "PED-47_Tiep_can_dai_mau"

CSS_STYLE = """
.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #e2e8f0;
  background-color: #090e17;
  padding: 18px;
  max-width: 680px;
  margin: 0 auto;
}
.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 12px;
}
.badge-barem {
  background-color: rgba(245, 158, 11, 0.15);
  color: #fbbf24;
  border: 1px solid rgba(245, 158, 11, 0.4);
}
.badge-ebm {
  background-color: rgba(6, 182, 212, 0.15);
  color: #22d3ee;
  border: 1px solid rgba(6, 182, 212, 0.4);
}
.question {
  font-size: 16px;
  font-weight: 600;
  color: #f8fafc;
  margin-bottom: 10px;
}
.cloze {
  font-weight: 700;
  color: #38bdf8;
  border-bottom: 2px solid #0284c7;
  padding: 0 2px;
}
.extra-box {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.04);
  border-left: 3px solid #38bdf8;
  font-size: 14px;
  color: #cbd5e1;
}
.extra-box-barem {
  border-left-color: #fbbf24;
}
.extra-title {
  font-weight: 700;
  color: #38bdf8;
  margin-bottom: 4px;
}
.extra-title-barem {
  color: #fbbf24;
}
"""

CLOZE_MODEL = genanki.Model(
    1709132001,
    'PedMed_Master_Cloze',
    model_type=genanki.Model.CLOZE,
    fields=[
        {'name': 'Text'},
        {'name': 'Extra'},
        {'name': 'Badge'},
        {'name': 'BadgeClass'},
        {'name': 'Title'},
    ],
    templates=[{
        'name': 'Cloze Master',
        'qfmt': '<div class="badge {{BadgeClass}}">{{Badge}}</div><div class="question">{{cloze:Text}}</div>',
        'afmt': '<div class="badge {{BadgeClass}}">{{Badge}}</div><div class="question">{{cloze:Text}}</div><hr id="answer"><div class="extra-box {{BadgeClass}}"><div class="extra-title {{BadgeClass}}">💡 {{Title}}:</div>{{Extra}}</div>',
    }],
    css=CSS_STYLE
)

def create_deck_and_json(deck_id, deck_name, cards_list, json_path, apkg_path):
    # Write JSON
    payload = {
        "topic": deck_name,
        "version": "master_combo_v1",
        "date": "2026-09-13",
        "total_cards": len(cards_list),
        "cards": cards_list
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  [JSON] Đã lưu {len(cards_list)} thẻ: {json_path}")

    # Build APKG
    deck = genanki.Deck(deck_id, deck_name)
    for c in cards_list:
        is_barem = c.get("track") == "barem_goc"
        badge_text = "🏛️ BAREM GIÁO TRÌNH GỐC (ÔN THI)" if is_barem else "🔬 LẬP LUẬN EBM & THỰC HÀNH LÂM SÀNG"
        badge_class = "badge-barem" if is_barem else "badge-ebm"
        title_text = "Barem Giáo trình gốc YTB" if is_barem else "Giải thích lâm sàng & EBM"

        note = genanki.Note(
            model=CLOZE_MODEL,
            fields=[c["text"], c.get("extra", ""), badge_text, badge_class, title_text],
            tags=c.get("tags", [])
        )
        deck.add_note(note)

    genanki.Package(deck).write_to_file(apkg_path)
    print(f"  [APKG] Đã xuất {len(cards_list)} thẻ ra: {apkg_path}")

# ==============================================================================
# BỘ THẺ PED-46: TIẾP CẬN GAN TO (COMBO BAREM GỐC + EBM)
# ==============================================================================
cards_ped46 = [
    # --- TRACK 1: BAREM GỐC GIÁO TRÌNH (TRANG 37 - 44) ---
    {
        "id": "PED46-B01",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Bờ trên của gan bình thường được xác định trên lâm sàng bằng cách gõ đục nằm tại vị trí {{c1::khoang liên sườn 5}} trên đường giữa xương đòn phải.",
        "extra": "Văn bản gốc: Bờ trên gõ thấy ở khoang liên sườn 5 trên đường giữa xương đòn phải.",
        "tags": ["PED-46", "Barem-goc", "Kham-gan", "Bo-tren"]
    },
    {
        "id": "PED46-B02",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Bờ dưới của gan bình thường sờ thấy dưới bờ sườn phải không quá {{c1::2 cm}} đối với trẻ nhỏ và không quá {{c1::1 cm}} với trẻ lớn.",
        "extra": "Văn bản gốc: Bờ dưới của gan sờ thấy dưới bờ sườn phải không quá 2cm đối với trẻ nhỏ và không quá 1cm với trẻ lớn.",
        "tags": ["PED-46", "Barem-goc", "Kham-gan", "Bo-duoi"]
    },
    {
        "id": "PED46-B03",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Theo giáo trình, kích thước trung bình của gan thay đổi: Trẻ 1 tuần tuổi là {{c1::4,5 – 5 cm}}, trẻ nhỏ là {{c1::6 – 7 cm}}, lúc 12 tuổi là {{c1::7 – 8 cm}}.",
        "extra": "Văn bản gốc: Kích thước trung bình của gan thay đổi: Trẻ 1 tuần tuổi 4,5-5cm; Trẻ nhỏ 6-7cm; Trẻ lớn hơn lúc 12 tuổi 7-8cm.",
        "tags": ["PED-46", "Barem-goc", "Kich-thuoc-gan", "Tuoi"]
    },
    {
        "id": "PED46-B04",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Công thức Nelson 1996 tính kích thước gan ở trẻ trai > 12 tuổi là: Kích thước gan (cm) = {{c1::0,032 × W (pound) + 0,18 × H (inch) - 7,86}}.",
        "extra": "Văn bản gốc: Trẻ trai: Kích thước gan (cm) = 0,032. W (pound) + 0,18. H (inch) - 7,86.",
        "tags": ["PED-46", "Barem-goc", "Nelson-1996", "Tre-trai"]
    },
    {
        "id": "PED46-B05",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Công thức Nelson 1996 tính kích thước gan ở trẻ gái > 12 tuổi là: Kích thước gan (cm) = {{c1::0,027 × W (pound) + 0,22 × H (inch) - 10,75}}.",
        "extra": "Văn bản gốc: Trẻ gái: Kích thước gan (cm) = 0,027. W (pound) + 0,22. H (inch) - 10,75.",
        "tags": ["PED-46", "Barem-goc", "Nelson-1996", "Tre-gai"]
    },
    {
        "id": "PED46-B06",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Phân loại nguyên nhân gan to trong giáo trình gồm 6 nhóm cơ chế: (1) Viêm nhiễm; (2) Ứ chất (storage); (3) Thâm nhiễm; (4) Tăng kích thước khoang mạch; (5) {{c1::Ứ mật}}; (6) Nội tại gan.",
        "extra": "Văn bản gốc: Bảng phân loại 6 cơ chế bệnh sinh tại trang 38 giáo trình.",
        "tags": ["PED-46", "Barem-goc", "6-co-che"]
    },
    {
        "id": "PED46-B07",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Theo giáo trình, nhóm cơ chế Tăng kích thước khoang mạch gồm: Tắc tĩnh mạch trong gan (Budd-Chiari, bịt TM gan) và Trên gan do {{c1::suy tim sung huyết, bệnh màng ngoài tim, viêm màng ngoài tim co thắt}}.",
        "extra": "Văn bản gốc: Trên gan: suy tim sung huyết, bệnh màng ngoài tim, viêm màng ngoài tim co thắt.",
        "tags": ["PED-46", "Barem-goc", "Khoang-mach", "Suy-tim"]
    },
    {
        "id": "PED46-B08",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Khi khám thực thể, gan đổ sau làm diện đục của gan {{c1::nhỏ hơn bình thường}}, gan đổ trước làm diện đục của gan {{c1::rộng hơn bình thường}}.",
        "extra": "Văn bản gốc: Gan đổ sau: diện đục nhỏ hơn bình thường; Gan đổ trước: diện đục rộng hơn bình thường. Do đó chỉ dựa vào sờ bờ gan không thể kết luận.",
        "tags": ["PED-46", "Barem-goc", "Kham-gan", "Vi-tri"]
    },
    {
        "id": "PED46-B09",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Nghiệm pháp Rung gan dương tính khi người bệnh đau, có khi rất đau, thường gặp kinh điển trong bệnh {{c1::áp xe gan}}.",
        "extra": "Văn bản gốc: Bàn tay trái đặt lên vùng gan, tay phải chặt nhẹ vào tay trái, (+) khi đau, thường gặp trong bệnh áp xe gan.",
        "tags": ["PED-46", "Barem-goc", "Rung-gan", "Ap-xe-gan"]
    },
    {
        "id": "PED46-B10",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Nghiệm pháp Ấn kẽ sườn dùng ngón tay ấn vào các kẽ sườn vùng trước gan, nếu đau là nghiệm pháp dương tính gặp trong {{c1::áp xe gan}}.",
        "extra": "Văn bản gốc: Thầy thuốc dùng ngón tay ấn vào các kẽ sườn vùng trước gan. Nếu đau là nghiệm pháp dương tính, thường gặp trong áp xe gan.",
        "tags": ["PED-46", "Barem-goc", "An-ke-suon", "Ap-xe-gan"]
    },
    {
        "id": "PED46-B11",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Nghiệm pháp Phản hồi gan tĩnh mạch cảnh dương tính (+) khi ấn gan làm tĩnh mạch cảnh nổi rõ dần lên, gặp trong {{c1::gan ứ máu do suy tim phải}} (khi gan xơ nghiệm pháp này âm tính).",
        "extra": "Văn bản gốc: Gặp trong gan ứ máu do suy tim phải. Khi gan xơ thì nghiệm pháp này âm tính.",
        "tags": ["PED-46", "Barem-goc", "Phan-hoi-gan-TMC", "Suy-tim-phai"]
    },
    {
        "id": "PED46-B12",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Nghiệm pháp Murphy dương tính khi bệnh nhân hít vào cơ hoành đẩy túi mật xuống chạm đầu ngón tay làm bệnh nhân {{c1::đau và ngừng thở ngay}}, gặp trong viêm túi mật xơ teo.",
        "extra": "Văn bản gốc: Nếu túi mật bị tổn thương thì bệnh nhân sẽ đau và ngừng thở ngay như vậy là dấu hiệu Murphy (+). Gặp trong viêm túi mật xơ teo.",
        "tags": ["PED-46", "Barem-goc", "Murphy", "Viem-tui-mat"]
    },
    {
        "id": "PED46-B13",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Chú ý an toàn khi làm nghiệm pháp Murphy: Chỉ làm khi nhìn thấy túi mật {{c1::không to}}, vì nếu túi mật to ấn vào có thể gây {{c1::vỡ túi mật, mật vào ổ bụng gây viêm phúc mạc}}.",
        "extra": "Văn bản gốc: Chỉ làm khi nhìn thấy túi mật không to vì nếu túi mật to ấn vào có thể gây vỡ túi mật, mật vào ổ bụng gây viêm phúc mạc.",
        "tags": ["PED-46", "Barem-goc", "Murphy", "Canh-bao-nguy-hiem"]
    },
    {
        "id": "PED46-B14",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong hội chứng gan to đơn thuần, Ung thư gan nguyên phát có đặc điểm lâm sàng: Gan to không đều, lổn nhổn, mật độ {{c1::cứng và lồi lõm}}, không đau, tiến triển nhanh suy sụp nhanh.",
        "extra": "Văn bản gốc: Gan to không đều, lổn nhổn; Mật độ cứng và lồi lõm; Không đau; Tiến triển nhanh, toàn trạng suy sụp nhanh.",
        "tags": ["PED-46", "Barem-goc", "Ung-thu-gan", "K-gan"]
    },
    {
        "id": "PED46-B15",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Gan to có vàng da do u đầu tụy - u bóng Vanter (Vater) có đặc điểm: Gan to đều, mềm, mặt nhẵn, không đau, không sốt, {{c1::túi mật to}} và dấu hiệu tắc mật rõ.",
        "extra": "Văn bản gốc: Gan to đều; Mềm, mặt nhẵn; Không đau, không sốt; Túi mật to; Dấu hiệu tắc mật rõ.",
        "tags": ["PED-46", "Barem-goc", "U-dau-tuy", "Bong-Vater"]
    },
    {
        "id": "PED46-B16",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Gan to có vàng da do sán lá gan có đặc điểm: Gan to ít và đều, mềm và nhẵn, đi kèm yếu tố dịch tễ là tiền sử {{c1::ăn gỏi cá}}.",
        "extra": "Văn bản gốc: Gan to do sán lá gan: Gan to ít và đều; Mềm và nhẵn; Tiền sử ăn gỏi cá.",
        "tags": ["PED-46", "Barem-goc", "San-la-gan", "Goi-ca"]
    },
    {
        "id": "PED46-B17",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong nhóm gan to kèm lách to, Hội chứng Banti được mô tả gồm: Lách to và cường lách, hội chứng tăng áp lực tĩnh mạch cửa, gan to ít và đều, {{c1::chắc và nhẵn}}, xơ gan, cổ trướng, tuần hoàn bàng hệ.",
        "extra": "Văn bản gốc: Hội chứng Banti: Lách to và cường lách, hội chứng tăng áp lực tĩnh mạch cửa; Gan to ít và đều; Chắc và nhẵn; Không đau; Xơ gan; Lách to, cổ trướng, tuần hoàn bàng hệ.",
        "tags": ["PED-46", "Barem-goc", "Hoi-chung-Banti", "Gan-lach-to"]
    },
    {
        "id": "PED46-B18",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Bệnh Hanot trong giáo trình kinh điển biểu hiện bằng tam chứng: {{c1::Gan to đều, Lách to, Vàng da từng đợt ngày càng tăng lên}}, mật độ gan chắc và không đau.",
        "extra": "Văn bản gốc: Bệnh Hanot: Gan to, lách to, vàng da từng đợt ngày càng tăng lên; Gan to đều; Chắc và không đau.",
        "tags": ["PED-46", "Barem-goc", "Benh-Hanot", "Gan-lach-to"]
    },
    {
        "id": "PED46-B19",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Hội chứng Gan to + Lách to + Hạch to thường liên quan tới hệ thống liên võng nội mô hoặc cơ quan tạo máu: {{c1::Leucemie cấp – kinh, Hodgkin, Lymphosarcome}}.",
        "extra": "Văn bản gốc: Thường liên quan tới hệ thống liên võng nội mô hoặc hệ thống cơ quan tạo máu: Leucemie cấp – kinh, Hodgkin, Lymphosarcome.",
        "tags": ["PED-46", "Barem-goc", "Gan-lach-hach-to", "Leukemia"]
    },
    {
        "id": "PED46-B20",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Về cận lâm sàng, khi {{c1::alpha-fetoprotein (AFP) tăng và kháng nguyên carcinoembryonic (CEA) tăng cao}} thì phải nghĩ tới bệnh lý ác tính ở gan.",
        "extra": "Văn bản gốc: Khi alpha-fetoprotein tăng và kháng nguyên carcinoembryonic tăng cao thì phải nghĩ tới bệnh ác tính ở gan.",
        "tags": ["PED-46", "Barem-goc", "Tumor-markers", "AFP-CEA"]
    },

    # --- TRACK 2: LẬP LUẬN LÂM SÀNG & EBM HIỆN ĐẠI ---
    {
        "id": "PED46-E01",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Tiêu chuẩn chẩn đoán Suy gan cấp trẻ em (PALF) bao gồm bằng chứng tổn thương gan cấp tính, không có xơ gan mạn và rối loạn đông máu với ngưỡng INR {{c1::> 1.5}} khi có bệnh não gan.",
        "extra": "Nếu trẻ chưa có bệnh não gan, ngưỡng chẩn đoán PALF là INR > 2.0 không hồi phục sau tiêm Vitamin K. Chống chỉ định tuyệt đối sinh thiết gan qua da vì nguy cơ xuất huyết tử vong.",
        "tags": ["PED-46", "EBM", "PALF", "INR"]
    },
    {
        "id": "PED46-E02",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Dấu hiệu phân ly men gan - bilirubin (AST/ALT giảm nhanh đột ngột trong khi Bilirubin tiếp tục tăng vọt) ở trẻ viêm gan cấp phản ánh tình trạng {{c1::hoại tử tế bào gan ồ ạt}} báo hiệu nguy cơ tử vong rất cao.",
        "extra": "Cơ chế: Tế bào gan bị phá hủy gần hết nên không còn enzyme để giải phóng vào máu, chứ không phải bệnh thuyên giảm.",
        "tags": ["PED-46", "EBM", "Phan-ly-men-gan", "PALF"]
    },
    {
        "id": "PED46-E03",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Nguyên nhân hàng đầu gây gan to và tăng men gan mạn tính liên quan đến ứ đọng lipid ở trẻ em học đường hiện nay là {{c1::MASLD}} (Bệnh gan nhiễm mỡ liên quan chuyển hóa do béo phì).",
        "extra": "Thuật ngữ MASLD chính thức thay thế NAFLD từ năm 2023, phản ánh đại dịch béo phì ở trẻ em đô thị.",
        "tags": ["PED-46", "EBM", "MASLD", "Beo-phi"]
    },
    {
        "id": "PED46-E04",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Khối u gan ác tính nguyên phát thường gặp nhất ở trẻ nhỏ dưới 3 tuổi với đặc trưng nồng độ AFP tăng cực kỳ cao (> 100.000 ng/mL) là {{c1::U nguyên bào gan (Hepatoblastoma)}}.",
        "extra": "Khác với Carcinoma tế bào gan (HCC) thường gặp ở trẻ lớn > 10 tuổi trên nền viêm gan B mạn hoặc rối loạn chuyển hóa.",
        "tags": ["PED-46", "EBM", "Hepatoblastoma", "AFP"]
    },
    {
        "id": "PED46-E05",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Bệnh lý ngoại khoa gây gan to và vàng da ứ mật ở trẻ sơ sinh bắt buộc phải phẫu thuật Kasai trước thời điểm {{c1::60 ngày tuổi}} là Teo đường mật bẩm sinh (Biliary Atresia).",
        "extra": "Mổ sau 60 ngày tỷ lệ thành công lưu thông mật giảm mạnh; sau 90 ngày gan đã xơ hóa không hồi phục và hầu hết phải ghép gan.",
        "tags": ["PED-46", "EBM", "Teo-duong-mat", "Kasai-60-ngay"]
    },
    {
        "id": "PED46-E06",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Ở trẻ từ 1 – 10 tuổi có gan to hoặc tăng men gan kéo dài không rõ nguyên nhân, xét nghiệm sàng lọc đầu tay để tầm soát bệnh Wilson là định lượng {{c1::Ceruloplasmin máu}} (ngưỡng < 20 mg/dL).",
        "extra": "Kết hợp tìm vòng Kayser-Fleischer tại rìa giác mạc và định lượng đồng niệu 24h tăng cao.",
        "tags": ["PED-46", "EBM", "Wilson", "Ceruloplasmin"]
    },
    {
        "id": "PED46-E07",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Thuật ngữ 'Hội chứng Banti' trong giáo trình cũ bản chất theo EBM hiện đại thuộc nhóm {{c1::Tăng áp lực tĩnh mạch cửa không do xơ gan (NCPF)}} mà nguyên nhân hàng đầu ở trẻ nhỏ là Huyết khối tạo hang TM cửa.",
        "extra": "Huyết khối tĩnh mạch cửa dạng hang (Portal cavernoma) thường là di chứng sau đặt catheter tĩnh mạch rốn thời kỳ sơ sinh.",
        "tags": ["PED-46", "EBM", "Banti-NCPF", "Exam-bridge"]
    },
    {
        "id": "PED46-E08",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Thuật ngữ 'Bệnh Hanot' (Xơ gan mật nguyên phát - PBC) thực tế {{c1::hầu như không bao giờ gặp ở trẻ em}}; ở trẻ có hội chứng tương tự cần nghĩ đến Viêm đường mật xơ hóa (PSC), Viêm gan tự miễn (AIH) hoặc PFIC.",
        "extra": "PBC là bệnh tự miễn của phụ nữ trung niên. Ở trẻ vị thành niên gan to kèm viêm loét đại tràng (IBD) phải tầm soát PSC.",
        "tags": ["PED-46", "EBM", "Hanot-PSC", "Exam-bridge"]
    }
]

# ==============================================================================
# BỘ THẺ PED-47: TIẾP CẬN ĐÁI MÁU (COMBO BAREM GỐC + EBM)
# ==============================================================================
cards_ped47 = [
    # --- TRACK 1: BAREM GỐC GIÁO TRÌNH (TRANG 18 - 23) ---
    {
        "id": "PED47-B01",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Đái máu vi thể được xác định bằng soi kính hiển vi khi soi nước tiểu tươi giữa dòng có {{c1::≥ 5 hồng cầu/ml}} hoặc có {{c1::trên 3 hồng cầu/vi trường}} trong mẫu quay ly tâm 10ml nước tiểu tươi.",
        "extra": "Văn bản gốc: Khi soi nước tiểu tươi giữa dòng có 5 hồng cầu/ml hoặc có trên 3 hồng cầu trong mẫu quay ly tâm 10ml nước tiểu tươi lấy giữa dòng.",
        "tags": ["PED-47", "Barem-goc", "Dinh-nghia", "Dai-mau-vi-the"]
    },
    {
        "id": "PED47-B02",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Cơ chế đái máu không do cầu thận: Hồng cầu vào nước tiểu trực tiếp mà không phải qua lỗ màng đáy cho nên hồng cầu vẫn {{c1::giữ nguyên hình dạng và kích thước giống như hồng cầu máu ngoại vi}}.",
        "extra": "Văn bản gốc: Do hồng cầu vào nước tiểu trực tiếp mà không phải qua lỗ màng đáy cho nên hồng cầu vẫn giữ nguyên hình dạng và kích thước giống như hồng cầu máu ngoại vi.",
        "tags": ["PED-47", "Barem-goc", "Co-che", "Ngoai-cau-than"]
    },
    {
        "id": "PED47-B03",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Đái máu đại thể: Đái máu đầu bãi gặp trong tổn thương {{c1::niệu đạo}}, đái máu cuối bãi gặp trong tổn thương {{c1::bàng quang}}, đái máu toàn bãi gặp trong tổn thương cầu thận, niệu quản, bàng quang, bệnh máu.",
        "extra": "Văn bản gốc: Đái máu đầu bãi gặp trong tổn thương niệu đạo, đái máu cuối bãi gặp trong tổn thương bàng quang. Đái máu toàn bãi gặp trong viêm cầu thận...",
        "tags": ["PED-47", "Barem-goc", "Nghiem-phap-3-coc", "Vi-tri"]
    },
    {
        "id": "PED47-B04",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Đái máu đỏ tươi, {{c1::có máu cục}} là dấu hiệu lâm sàng gợi ý nguyên nhân chảy máu đường tiết niệu (ngoài cầu thận).",
        "extra": "Văn bản gốc: Đái máu đỏ tươi, có máu cục gợi ý nguyên nhân chảy máu đường tiết niệu.",
        "tags": ["PED-47", "Barem-goc", "Mau-cuc", "Duong-tiet-nieu"]
    },
    {
        "id": "PED47-B05",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Đánh giá mức độ phù theo % cân nặng cơ thể: Phù nhẹ khi cân nặng tăng {{c1::dưới 10%}}, phù vừa khi cân nặng tăng {{c1::10 – 20%}}, phù nặng khi cân nặng tăng {{c1::trên 20%}}.",
        "extra": "Văn bản gốc: Phù nhẹ: Cân nặng tăng &lt; 10%; Phù vừa: Cân nặng tăng từ 10-20%; Phù nặng: Cân nặng tăng &gt; 20%.",
        "tags": ["PED-47", "Barem-goc", "Phu", "Phan-do-can-nang"]
    },
    {
        "id": "PED47-B06",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Đau khớp trong đái máu do Lupus ban đỏ có đặc điểm: Đau chuyển khớp, {{c1::không cứng khớp buổi sáng, không sưng nóng đỏ đau, không biến dạng khớp}}.",
        "extra": "Văn bản gốc: Đau khớp đơn thuần hoặc nhiều khớp nhỏ các chi... không cứng khớp buổi sáng, không sưng nóng đỏ đau, không biến dạng khớp là dấu hiệu hay gặp trong đái máu do lupus.",
        "tags": ["PED-47", "Barem-goc", "Lupus", "Dau-khop"]
    },
    {
        "id": "PED47-B07",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Đái máu kèm theo xuất huyết cẳng chân dạng {{c1::đi bốt}} (xuất huyết hoại tử đối xứng) nghĩ nhiều đến bệnh Schonlein Henoch.",
        "extra": "Văn bản gốc: Xuất huyết cẳng chân dạng đi bốt nghĩ nhiều đến Schonlein Henoch.",
        "tags": ["PED-47", "Barem-goc", "Schonlein-Henoch", "Xuat-huyet"]
    },
    {
        "id": "PED47-B08",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Đái máu đại thể tái phát kết hợp với nhiễm trùng đường hô hấp trên thường là: {{c1::Bệnh thận do IgA, bệnh màng đáy mỏng hay hội chứng Alport}}.",
        "extra": "Văn bản gốc: Đái máu đại thể tái phát kết hợp với nhiễm trùng đường hô hấp trên thường là bệnh thận do IgA, bệnh màng đáy mỏng hay hội chứng Alport.",
        "tags": ["PED-47", "Barem-goc", "Tai-phat", "Ho-hap"]
    },
    {
        "id": "PED47-B09",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Chỉ định sinh thiết thận số 1 trong giáo trình: Khi Protein niệu đạt ngưỡng {{c1::> 1 g/1,73 m²/ngày}}.",
        "extra": "Văn bản gốc: 5.4. Sinh thiết thận: Protein niệu > 1g/1.73 m2/ngày.",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than", "Chi-dinh-1"]
    },
    {
        "id": "PED47-B10",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Chỉ định sinh thiết thận số 2 trong giáo trình: Khi nồng độ Bổ thể C3 thấp kéo dài {{c1::trên 3 tháng}}.",
        "extra": "Văn bản gốc: 5.4. Sinh thiết thận: Bổ thể C3 thấp kéo dài trên 3 tháng.",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than", "Chi-dinh-2"]
    },
    {
        "id": "PED47-B11",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Chỉ định sinh thiết thận số 3 trong giáo trình: Khi mức lọc cầu thận giảm kéo dài {{c1::< 80 ml/phút/1,73 m²}}.",
        "extra": "Văn bản gốc: 5.4. Sinh thiết thận: Mức lọc cầu thận giảm < 80ml/phút/1.73m2.",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than", "Chi-dinh-3"]
    },
    {
        "id": "PED47-B12",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Chỉ định sinh thiết thận số 7 (chỉ định tâm lý/tiên lượng): Đái máu do cầu thận mà {{c1::gia đình thiết tha muốn biết nguyên nhân và tiên lượng}} của bệnh mặc dù protein niệu không cao.",
        "extra": "Văn bản gốc: Đái máu do cầu thận mà gia đình thiết tha muốn biết nguyên nhân và tiên lượng của bệnh mặc dù protein niệu không cao.",
        "tags": ["PED-47", "Barem-goc", "Sinh-thiet-than", "Chi-dinh-7"]
    },
    {
        "id": "PED47-B13",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong sơ đồ tiếp cận 5 bước: Bước 1 que thử (+) nhưng soi tươi (-) thì hướng chẩn đoán là {{c1::tìm huyết sắc tố niệu}}.",
        "extra": "Văn bản gốc: Sơ đồ thuật toán Bước 1: Soi tươi (-) + Que thử (+) -> Tìm huyết sắc tố niệu.",
        "tags": ["PED-47", "Barem-goc", "Thuat-toan", "Buoc-1"]
    },
    {
        "id": "PED47-B14",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong sơ đồ tiếp cận: Bước 2 tìm các triệu chứng của viêm cầu thận cấp gồm tam chứng lâm sàng là {{c1::phù, cao huyết áp, đái ít}}.",
        "extra": "Văn bản gốc: Bước 2: Tìm các triệu chứng của viêm cầu thận cấp: phù, cao huyết áp, đái ít.",
        "tags": ["PED-47", "Barem-goc", "Thuat-toan", "Buoc-2"]
    },
    {
        "id": "PED47-B15",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong sơ đồ tiếp cận: Bước 3 đối với đái máu đại thể phải loại trừ do {{c1::thể dục thể thao}}; đái máu vi thể đơn độc làm lại xét nghiệm nước tiểu hàng tuần trong {{c1::2 tuần}}.",
        "extra": "Văn bản gốc: Bước 3: Đái máu đại thể: loại trừ do thể dục thể thao. Đái máu vi thể đơn độc: làm lại xét nghiệm nước tiểu hàng tuần trong 2 tuần.",
        "tags": ["PED-47", "Barem-goc", "Thuat-toan", "Buoc-3"]
    },
    {
        "id": "PED47-B16",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong sơ đồ tiếp cận: Bước 4 phân định nguyên nhân tại cầu thận khi có bộ ba: {{c1::Hồng cầu biến đổi hình thái, Protein niệu (+), Trụ (+)}}.",
        "extra": "Văn bản gốc: Nhánh 1: Nguyên nhân tại cầu thận: Hồng cầu biến đổi hình thái, protein niệu (+), trụ (+).",
        "tags": ["PED-47", "Barem-goc", "Thuat-toan", "Buoc-4"]
    },
    {
        "id": "PED47-B17",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong sơ đồ tiếp cận Bước 5: Tìm nguyên nhân không ở cầu thận bằng canxi/creatinine niệu, cấy nước tiểu tìm vi khuẩn và {{c1::tìm adenovirus}}.",
        "extra": "Văn bản gốc: Bước 5: Canxi/creatinine niệu, Cấy NT – Cấy tìm adenovirus, Siêu âm, Doppler thận...",
        "tags": ["PED-47", "Barem-goc", "Thuat-toan", "Buoc-5"]
    },
    {
        "id": "PED47-B18",
        "track": "barem_goc",
        "card_type": "cloze",
        "text": "[Barem gốc] Trong sơ đồ tiếp cận Bước 5: Chụp MRI mạch thận được chỉ định khi nghi ngờ {{c1::hội chứng Nutcracker}} (kẹp tĩnh mạch thận).",
        "extra": "Văn bản gốc: Chụp MRI mạch (nếu nghi ngờ hội chứng nutcracker).",
        "tags": ["PED-47", "Barem-goc", "Nutcracker", "MRI-mach"]
    },

    # --- TRACK 2: LẬP LUẬN LÂM SÀNG & EBM HIỆN ĐẠI ---
    {
        "id": "PED47-E01",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Theo khuyến cáo của Viện Hàn lâm Nhi khoa Hoa Kỳ (AAP), đái máu vi thể bệnh lý chỉ được xác nhận khi có ≥ 3 hồng cầu/vi trường (HPF) trên {{c1::ít nhất 2 trong 3 mẫu nước tiểu độc lập}} lấy cách nhau 1 – 2 tuần.",
        "extra": "Quy tắc 3 lần (The Rule of Persistence) giúp tránh làm xét nghiệm máu và hình ảnh thừa thãi ở 10 - 15% trẻ em có đái máu vi thể thoáng qua sau sốt virus hay gắng sức.",
        "tags": ["PED-47", "EBM", "AAP", "Rule-of-persistence"]
    },
    {
        "id": "PED47-E02",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Thành phần cặn lắng nước tiểu có giá trị đặc hiệu 100% khẳng định nguồn gốc viêm cầu thận là {{c1::trụ hồng cầu (RBC casts)}}.",
        "extra": "Hình thành do hồng cầu kết tụ với mạng lưới protein Tamm-Horsfall trong lòng ống lượn xa. Ngược lại, có cục máu đông loại trừ nguồn gốc cầu thận.",
        "tags": ["PED-47", "EBM", "Tru-hong-cau", "Pathognomonic"]
    },
    {
        "id": "PED47-E03",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Hình thái hồng cầu biến dạng có giá trị đặc hiệu cao nhất cho tổn thương cầu thận là {{c1::Acanthocyte}} (hồng cầu hình nhẫn có chồi) khi chiếm > 5% tổng số hồng cầu.",
        "extra": "Hồng cầu biến dạng > 80% hoặc Acanthocyte > 5% giúp loại trừ chỉ định nội soi bàng quang hoặc chụp CT không cần thiết ở trẻ em.",
        "tags": ["PED-47", "EBM", "Acanthocyte", "Dac-hieu"]
    },
    {
        "id": "PED47-E04",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Bổ thể C3 giảm sâu trong đợt cấp và bắt buộc hồi phục sau 6 – 8 tuần trong bệnh {{c1::Viêm cầu thận cấp hậu liên cầu (APSGN)}}; nếu C3 hoàn toàn bình thường khi đái máu đại thể bùng phát sau sốt 1 – 2 ngày thì chẩn đoán là {{c1::Bệnh thận IgA}}.",
        "extra": "C3 là dấu ấn miễn dịch chìa khóa phân biệt giữa APSGN và Bệnh thận IgA trên lâm sàng.",
        "tags": ["PED-47", "EBM", "C3", "APSGN-vs-IgA"]
    },
    {
        "id": "PED47-E05",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Hội chứng Alport di truyền liên kết X do đột biến gen {{c1::COL4A5}} mã hóa chuỗi collagen type IV alpha-5, biểu hiện bằng đái máu tiến triển kết hợp giảm thính lực tiếp nhận và biến dạng thể thủy tinh hình nón.",
        "extra": "Ngược lại, Bệnh màng đáy mỏng (Benign Familial Hematuria) do đột biến COL4A3/A4 có tiên lượng lành tính suốt đời, chức năng thận bình thường.",
        "tags": ["PED-47", "EBM", "Alport", "COL4A5"]
    },
    {
        "id": "PED47-E06",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Nguyên nhân ngoài cầu thận phổ biến nhất gây đái máu vi thể cô lập ở trẻ em là {{c1::Tăng canxi niệu vô căn}}, chẩn đoán khi tỷ lệ UCa/UCr mẫu ngẫu nhiên > 0,2 mg/mg ở trẻ > 2 tuổi.",
        "extra": "Vi tinh thể canxi oxalate cọ xát vi mạch ống thận gây đái máu. Cần cho trẻ uống nhiều nước và hạn chế ăn mặn.",
        "tags": ["PED-47", "EBM", "Tang-canxi-nieu", "UCa-UCr"]
    },
    {
        "id": "PED47-E07",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Hội chứng Nutcracker gây đái máu do tĩnh mạch thận trái bị kẹp giữa {{c1::động mạch chủ bụng và động mạch mạc treo tràng trên (SMA)}}, thường gặp ở trẻ vị thành niên gầy cao kèm giãn tĩnh mạch thừng tinh trái.",
        "extra": "Chẩn đoán hình ảnh đầu tay là Siêu âm Doppler mạch thận so sánh tỷ lệ vận tốc dòng chảy trước và sau điểm kẹp (> 4:1).",
        "tags": ["PED-47", "EBM", "Nutcracker", "SMA"]
    },
    {
        "id": "PED47-E08",
        "track": "ebm_hien_dai",
        "card_type": "cloze",
        "text": "[EBM Lâm sàng] Theo nguyên lý ALARA trong Thận học Nhi, chỉ định chẩn đoán hình ảnh đầu tay ưu tiên số 1 là {{c1::Siêu âm Doppler hệ tiết niệu}} thay vì chụp X-quang KUB hay CT nhằm tránh bức xạ ion hóa nguy hại cho trẻ.",
        "extra": "Sỏi ở trẻ em thường là sỏi không cản quang, siêu âm có độ nhạy vượt trội trong việc phát hiện sỏi, ứ nước và dị tật đường niệu.",
        "tags": ["PED-47", "EBM", "ALARA", "Sieu-am-Doppler"]
    }
]

def main():
    print("=" * 60)
    print("BIÊN TẬP MASTER COMBO DECKS (JSON + APKG) CHO PED-46 & PED-47")
    print("=" * 60)

    # 1. PED-46
    p46_json = PED46_DIR / "PED-46_Tiep_can_gan_to_MASTER_v1.cards.v2.json"
    p46_apkg = PED46_DIR / "PED-46_Tiep_can_gan_to_MASTER_v1.apkg"
    create_deck_and_json(
        deck_id=1709132046,
        deck_name="NhiKhoa::PED-46_Tiep_can_gan_to::MASTER_v1",
        cards_list=cards_ped46,
        json_path=p46_json,
        apkg_path=p46_apkg
    )

    # 2. PED-47
    p47_json = PED47_DIR / "PED-47_Tiep_can_dai_mau_MASTER_v1.cards.v2.json"
    p47_apkg = PED47_DIR / "PED-47_Tiep_can_dai_mau_MASTER_v1.apkg"
    create_deck_and_json(
        deck_id=1709132047,
        deck_name="NhiKhoa::PED-47_Tiep_can_dai_mau::MASTER_v1",
        cards_list=cards_ped47,
        json_path=p47_json,
        apkg_path=p47_apkg
    )

    print("\nHoàn tất tạo Master Decks cho cả 2 chuyên đề!")

if __name__ == "__main__":
    main()
