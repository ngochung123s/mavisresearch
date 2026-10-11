"""
build_ped30_master_deck.py
Tạo bộ thẻ Anki Master kết hợp hoàn chỉnh cho PED-30:
- Track 1: [🏛️ BAREM GỐC GIÁO TRÌNH (ÔN THI)] (Học thuộc lòng để ăn trọn điểm thi tự luận Bộ môn)
- Track 2: [🔬 LẬP LUẬN EBM & THỰC HÀNH LÂM SÀNG] (Phản xạ chẩn đoán lâm sàng, cờ đỏ cấp cứu và guideline WHO)
- Xuất file .cards.v2.json và file .apkg nhị phân thực thụ cho Anki.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
import genanki

DIR = Path(__file__).resolve().parent

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

def create_deck_and_json(deck_id: int, deck_name: str, cards_list: list[dict], json_path: Path, apkg_path: Path):
    payload = {
        "topic": deck_name,
        "version": "master_combo_v1",
        "date": "2026-10-11",
        "total_cards": len(cards_list),
        "cards": cards_list
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  [JSON] Đã lưu {len(cards_list)} thẻ: {json_path}")

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
# CARDS DEFINITIONS (106 CARDS: B0 - B6)
# ==============================================================================
cards_ped30: list[dict] = []

def add_c(cid: str, track: str, sec: str, text: str, extra: str, tags: list[str]):
    cards_ped30.append({
        "id": cid,
        "track": track,
        "card_type": "cloze",
        "section": sec,
        "text": text,
        "extra": extra,
        "tags": ["PED-30", track, f"Sec-{sec}"] + tags
    })

# ------------------------------------------------------------------------------
# SECTION B0: TỔNG QUAN MÔ HÌNH 4 TRỤC ABCD (10 thẻ: 5 Barem + 5 EBM)
# ------------------------------------------------------------------------------
add_c("PED30-B0-01", "barem_goc", "B0",
      "[Barem gốc] Mô hình 4 trục kinh điển trong thăm khám dinh dưỡng Nhi khoa (ABCD) bao gồm: (1) A là {{c1::Nhân trắc học (Anthropometry)}}; (2) B là {{c1::Cận lâm sàng (Biochemical)}}; (3) C là {{c1::Lâm sàng (Clinical)}}; (4) D là {{c1::Khẩu phần ăn (Dietary)}}.",
      "🎯 Trả lời cốt lõi: 4 trục ABCD tạo nên cẩm nang tiếp cận toàn diện không bỏ sót.<br><br>💡 Giải thích: A (W, H, HC, MUAC), B (Albumin, Sắt, D, Kẽm), C (Khám đầu-chân, phù, mỡ, cơ), D (Hỏi khẩu phần 24h).",
      ["ABCD", "Tong-quan"])

add_c("PED30-B0-02", "barem_goc", "B0",
      "[Barem gốc] 3 mục tiêu học tập cơ bản khi đánh giá suy dinh dưỡng trẻ em: (1) Nắm vững kỹ thuật {{c1::cân đo nhân trắc học chuẩn}}; (2) Phân loại chính xác theo {{c1::Z-score chuẩn WHO}}; (3) Phát hiện được {{c1::dấu hiệu thiếu vi chất}} và bẫy lâm sàng.",
      "🎯 Trả lời cốt lõi: Ba mục tiêu sống còn trong barem thi lý thuyết và lâm sàng Bộ môn Nhi.<br><br>💡 Giải thích: Cần thuộc lòng để làm trọn vẹn bài thi tự luận.",
      ["Muc-tieu", "Barem"])

add_c("PED30-B0-03", "barem_goc", "B0",
      "[Barem gốc] Ba thể suy dinh dưỡng cơ bản theo phân loại hình thái lâm sàng: (1) Thể nhẹ cân: Cân nặng thấp so với {{c1::tuổi (WAZ)}}; (2) Thể thấp còi: Chiều cao thấp so với {{c1::tuổi (HAZ)}}; (3) Thể gầy còm: Cân nặng thấp so với {{c1::chiều cao (WHZ)}}.",
      "🎯 Trả lời cốt lõi: 3 thể hình thái tương ứng 3 chỉ số nhân trắc học trục A.<br><br>💡 Giải thích: WAZ (nhẹ cân), HAZ (thấp còi mạn tính), WHZ (gầy còm cấp tính).",
      ["Phan-loai", "The-benh"])

add_c("PED30-B0-04", "barem_goc", "B0",
      "[Barem gốc] Suy dinh dưỡng thể Thấp còi (Stunting) phản ánh quá trình thiếu hụt dinh dưỡng {{c1::mạn tính, kéo dài trong quá khứ}}, là di chứng tích lũy lâu ngày.",
      "🎯 Trả lời cốt lõi: Chiều cao phản ánh sự phát triển của khung xương theo thời gian dài.<br><br>💡 Giải thích: Khác với thể gầy còm phản ánh sụt cân cấp tính xảy ra gần đây.",
      ["Thap-coi", "HAZ"])

add_c("PED30-B0-05", "barem_goc", "B0",
      "[Barem gốc] Suy dinh dưỡng thể Gầy còm (Wasting) phản ánh tình trạng thiếu hụt dinh dưỡng {{c1::cấp tính, sụt cân gần đây}} do ốm đau, tiêu chảy hoặc thiếu đói cấp.",
      "🎯 Trả lời cốt lõi: Cân nặng theo chiều cao nhạy nhất với biến động dinh dưỡng cấp.<br><br>💡 Giải thích: WHZ là chỉ số sống còn để phát hiện nguy cơ tử vong sớm ở trẻ dưới 5 tuổi.",
      ["Gay-com", "WHZ"])

add_c("PED30-B0-06", "ebm_update", "B0",
      "[EBM Update] Theo Hướng dẫn WHO 2023 về Wasting, Suy dinh dưỡng cấp nặng (SAM) ở trẻ 6–59 tháng tuổi được xác định khi có ít nhất 1 trong 3 tiêu chuẩn: (1) WHZ &lt; {{c1::-3 SD}}; (2) MUAC &lt; {{c1::115 mm}}; (3) {{c1::Có phù dinh dưỡng đối xứng hai bên}}.",
      "🎯 Trả lời cốt lõi: Chỉ cần 1 trong 3 tiêu chuẩn là đủ khẳng định SAM.<br><br>💡 Giải thích: Có phù tự động xếp SAM bất kể chỉ số Z-score (WHO Guideline 2023, PMID: 17076211).",
      ["SAM", "WHO-2023", "Tieu-chuan"])

add_c("PED30-B0-07", "ebm_update", "B0",
      "[EBM Update] Theo WHO 2023, Suy dinh dưỡng cấp vừa (MAM) ở trẻ 6–59 tháng tuổi được xác định khi: {{c1::-3 SD ≤ WHZ &lt; -2 SD}} HOẶC {{c1::115 mm ≤ MUAC &lt; 125 mm}}, và tuyệt đối {{c2::không có phù dinh dưỡng}}.",
      "🎯 Trả lời cốt lõi: MAM nằm giữa ngưỡng -3 SD và -2 SD (hoặc MUAC 115–124 mm).<br><br>💡 Giải thích: Nếu xuất hiện phù thì lập tức chuyển từ MAM sang SAM ngay.",
      ["MAM", "WHO-2023"])

add_c("PED30-B0-08", "ebm_update", "B0",
      "[EBM Update] Khái niệm Z-score (Độ lệch chuẩn) trong nhân trắc học WHO: Z-score biểu thị khoảng cách từ giá trị đo được của trẻ đến {{c1::giá trị trung vị (Median)}} của quần thể chuẩn, tính theo đơn vị {{c2::độ lệch chuẩn (SD)}}.",
      "🎯 Trả lời cốt lõi: Z = (X - Median) / SD (chuẩn hóa theo tuổi và giới tính).<br><br>💡 Giải thích: Khắc phục nhược điểm của phân loại Gomez hay Wellcome theo % cân nặng đơn thuần.",
      ["Z-score", "Nguyen-ly"])

add_c("PED30-B0-09", "ebm_update", "B0",
      "[EBM Update] Nghiên cứu đa trung tâm chuẩn tăng trưởng WHO 2006 (MGRS) chứng minh: Trẻ em thuộc các chủng tộc khác nhau (châu Á, Âu, Phi, Mỹ) đều có {{c1::tiềm năng tăng trưởng thể chất tương đương nhau}} nếu được nuôi dưỡng trong điều kiện tối ưu.",
      "🎯 Trả lời cốt lõi: Mọi trẻ em khỏe mạnh sinh ra đều tăng trưởng theo một quy luật sinh học chung.<br><br>💡 Giải thích: Bác bỏ quan điểm sai lầm cho rằng trẻ em châu Á mặc định phải thấp bé hơn trẻ phương Tây (PMID: 16817681).",
      ["MGRS", "WHO-2006"])

add_c("PED30-B0-10", "ebm_update", "B0",
      "[EBM Update] Gánh nặng kép về dinh dưỡng (Double Burden of Malnutrition) tại Việt Nam: Tỷ lệ trẻ em thấp còi ở vùng sâu vùng xa còn {{c1::khoảng 19–20%}}, trong khi tỷ lệ thừa cân - béo phì ở học sinh đô thị lớn đã vượt {{c2::30–40%}}.",
      "🎯 Trả lời cốt lõi: Tồn tại song hành cả suy dinh dưỡng thiếu hụt lẫn béo phì thừa cân.<br><br>💡 Giải thích: Đòi hỏi bác sĩ thực hành phải nắm vững cả công cụ chẩn đoán gầy còm lẫn sàng lọc béo phì.",
      ["Dich-te", "Viet-Nam"])

# ------------------------------------------------------------------------------
# SECTION B1: KỸ THUẬT NHÂN TRẮC HỌC CHUẨN XÁC (18 thẻ: 9 Barem + 9 EBM)
# ------------------------------------------------------------------------------
add_c("PED30-B1-01", "barem_goc", "B1",
      "[Barem gốc] Quy tắc chọn cân theo lứa tuổi: Trẻ dưới 2 tuổi sử dụng {{c1::cân máng điện tử}}; trẻ từ 2 tuổi trở lên sử dụng {{c1::cân đứng (cân bàn hoặc cân đòn)}}.",
      "🎯 Trả lời cốt lõi: Chọn đúng loại cân phù hợp với khả năng đứng vững của trẻ.<br><br>💡 Giải thích: Cân máng có độ nhạy đến 10g, an toàn cho trẻ nằm hoặc ngồi.",
      ["Can-nang", "Dung-cu"])

add_c("PED30-B1-02", "barem_goc", "B1",
      "[Barem gốc] Nguyên tắc chuẩn bị trẻ trước khi cân: Cởi bỏ hết áo khoác ngoài, giày dép và bắt buộc {{c1::tháo bỏ hoàn toàn tã bỉm}}.",
      "🎯 Trả lời cốt lõi: Bắt buộc tháo bỉm trước khi cân trẻ.<br><br>💡 Giải thích: Một chiếc bỉm ướt đầy nước tiểu nặng tới 300–500g, làm lệch chẩn đoán phân loại Z-score.",
      ["Thao-bim", "Can-chuan"])

add_c("PED30-B1-03", "barem_goc", "B1",
      "[Barem gốc] Quy định tư thế đo chiều dài/chiều cao theo lứa tuổi: Trẻ dưới 24 tháng tuổi bắt buộc đo {{c1::chiều dài nằm}}; trẻ từ 24 tháng tuổi trở lên bắt buộc đo {{c1::chiều cao đứng}}.",
      "🎯 Trả lời cốt lõi: Mốc phân định 24 tháng tuổi (2 tuổi) hoặc mốc 87 cm.<br><br>💡 Giải thích: Trẻ &lt; 24 tháng đo nằm bằng thước hộp Infantometer; trẻ ≥ 24 tháng đo đứng bằng Stadiometer.",
      ["Chieu-dai", "Chieu-cao", "Moc-tuoi"])

add_c("PED30-B1-04", "barem_goc", "B1",
      "[Barem gốc] Dụng cụ chuẩn để đo chiều dài nằm ở trẻ dưới 2 tuổi là {{c1::thước hộp đo nằm (Infantometer)}} có thanh chặn đầu cố định và thanh trượt chân di động; tuyệt đối không dùng {{c2::thước dây mềm}}.",
      "🎯 Trả lời cốt lõi: Thước hộp Infantometer với 2 người đo.<br><br>💡 Giải thích: Thước dây mềm bị co giãn và cong theo nếp gấp cơ thể làm sai số lớn.",
      ["Infantometer", "Dung-cu"])

add_c("PED30-B1-05", "barem_goc", "B1",
      "[Barem gốc] Khi đo chiều cao đứng bằng thước Stadiometer, trẻ phải tiếp xúc với mặt phẳng thẳng đứng của thước tại {{c1::5 điểm chạm}}: (1) Gót chân; (2) Bắp chân; (3) Mông; (4) Bả vai; (5) Ụ chẩm đầu.",
      "🎯 Trả lời cốt lõi: Đủ 5 điểm chạm để đảm bảo trục cơ thể hoàn toàn thẳng đứng.<br><br>💡 Giải thích: Thiếu 1 trong 5 điểm này làm chiều cao đo được ngắn hơn thực tế 1–2 cm.",
      ["5-diem-cham", "Stadiometer"])

add_c("PED30-B1-06", "barem_goc", "B1",
      "[Barem gốc] Mặt phẳng định hướng đầu chuẩn khi đo chiều cao đứng là {{c1::Mặt phẳng Frankfort}}, xác định bằng đường thẳng nối {{c2::bờ dưới ổ mắt}} với {{c2::gờ trên lỗ tai ngoài}} song song với mặt đất.",
      "🎯 Trả lời cốt lõi: Mặt phẳng Frankfort đảm bảo mắt nhìn thẳng ngang tầm.<br><br>💡 Giải thích: Ngửa đầu hoặc cúi đầu làm đỉnh đầu bị lệch hạ thấp chiều cao đo.",
      ["Frankfort", "Tu-the-dau"])

add_c("PED30-B1-07", "barem_goc", "B1",
      "[Barem gốc] Quy tắc chuyển đổi bù trừ bắt buộc: Nếu trẻ ≥ 2 tuổi nhưng bắt buộc phải đo nằm thì lấy kết quả {{c1::trừ đi 0.7 cm}}; nếu trẻ &lt; 2 tuổi nhưng đo đứng thì lấy kết quả {{c2::cộng thêm 0.7 cm}}.",
      "🎯 Trả lời cốt lõi: Đo nằm dài hơn đo đứng trung bình 0.7 cm.<br><br>💡 Giải thích: Trẻ lớn đo nằm phải TRỪ 0.7 cm; trẻ nhỏ đo đứng phải CỘNG 0.7 cm (PMID: 16817681).",
      ["Bu-tru-07cm", "Quy-tac-vang"])

add_c("PED30-B1-08", "barem_goc", "B1",
      "[Barem gốc] Thước dây Shakir đo vòng cánh tay (MUAC) phân loại 3 vùng màu: (1) Màu Đỏ (&lt; 115 mm) là {{c1::Suy dinh dưỡng cấp nặng (SAM)}}; (2) Màu Vàng (115–124 mm) là {{c1::Suy dinh dưỡng cấp vừa (MAM)}}; (3) Màu Xanh (≥ 125 mm) là {{c1::Dinh dưỡng bình thường}}.",
      "🎯 Trả lời cốt lõi: Thang 3 vùng màu đo tại cánh tay trái ở điểm giữa.<br><br>💡 Giải thích: Đỏ &lt; 115mm (nguy cơ tử vong cao), Vàng 115-124mm, Xanh ≥ 125mm.",
      ["Shakir", "3-vung-mau"])

add_c("PED30-B1-09", "barem_goc", "B1",
      "[Barem gốc] Kỹ thuật xác định vị trí đo vòng cánh tay (MUAC): Đo trên tay {{c1::trái}}, gập khuỷu 90 độ, tìm điểm giữa của đường nối giữa {{c2::mỏm cùng vai (Acromion)}} và {{c2::mỏm khuỷu (Olecranon)}}.",
      "🎯 Trả lời cốt lõi: Tay trái, điểm giữa mỏm cùng vai và mỏm khuỷu.<br><br>💡 Giải thích: Khi quấn thước phải thả lỏng tay xuôi thân mình, thước áp sát da không thít chặt mô mềm.",
      ["Vi-tri-MUAC", "Ky-thuat"])

add_c("PED30-B1-10", "ebm_update", "B1",
      "[EBM Update] Lý do sinh lý khiến chiều dài đo nằm dài hơn chiều cao đo đứng 0.7 cm: Khi nằm ngửa, các {{c1::đĩa đệm gian đốt sống}} được giải phóng khỏi áp lực nén của trọng lực và {{c2::độ cong sinh lý cột sống}} được kéo thẳng ra.",
      "🎯 Trả lời cốt lõi: Giải phóng tải trọng trọng lực trên cột sống.<br><br>💡 Giải thích: Khi đứng lên, trọng lực cơ thể nén các đĩa đệm và tăng độ cong ưỡn làm chiều cao giảm 0.7 cm (PMID: 16817681).",
      ["Sinh-ly-cot-song", "07cm"])

add_c("PED30-B1-11", "ebm_update", "B1",
      "[EBM Update] Cơ sở khoa học của việc đo MUAC ở trẻ 6–59 tháng tuổi: Ở lứa tuổi này, chu vi cánh tay của trẻ khỏe mạnh {{c1::hầu như không thay đổi (tăng dưới 1 cm trong 4 năm)}}, nên phản ánh trực tiếp khối cơ và mỡ nạc độc lập với tuổi.",
      "🎯 Trả lời cốt lõi: Chu vi cánh tay tương đối hằng định từ 6 đến 59 tháng.<br><br>💡 Giải thích: Giúp sàng lọc suy dinh dưỡng cấp nhanh chóng ngay cả khi không biết chính xác tuổi của trẻ.",
      ["Co-so-MUAC", "Co-mo"])

add_c("PED30-B1-12", "ebm_update", "B1",
      "[EBM Update] Nghiên cứu Myatt et al. (2006) chứng minh: MUAC kết hợp với khám phù mu chân có {{c1::độ nhạy và giá trị dự báo tử vong cao hơn}} so với chỉ số cân nặng theo chiều cao (WHZ) trong sàng lọc cộng đồng.",
      "🎯 Trả lời cốt lõi: MUAC &lt; 115 mm bắt trúng những trẻ có nguy cơ tử vong cao nhất.<br><br>💡 Giải thích: Dễ thực hiện, độ lặp lại cao, không cần thiết bị cồng kềnh (PMID: 17076211).",
      ["Myatt-2006", "Du-bao-tu-vong"])

add_c("PED30-B1-13", "ebm_update", "B1",
      "[EBM Update] Đo chu vi vòng đầu (OFC) chuẩn: Thước dây đi qua điểm nhô nhất của {{c1::xương chẩm}} ở phía sau và qua {{c1::gờ trên cung mày}} ở phía trước; bất thường khi Z-score &lt; {{c2::-2 SD (tật đầu nhỏ)}} hoặc &gt; {{c2::+2 SD (đầu to/não úng thủy)}}.",
      "🎯 Trả lời cốt lõi: Vòng đầu phản ánh thể tích não bộ trong 2-3 năm đầu đời.<br><br>💡 Giải thích: Đầu nhỏ gợi ý chậm phát triển não hoặc suy dinh dưỡng bào thai nặng; đầu to cần loại trừ u não hoặc tràn dịch não.",
      ["Vong-dau", "OFC"])

add_c("PED30-B1-14", "ebm_update", "B1",
      "[EBM Update] Bẫy lâm sàng khi đo MUAC: Bác sĩ kéo thước quá chặt làm {{c1::lún sâu vào lớp mỡ dưới da}} sẽ làm kết quả giả tạo giảm xuống vùng Đỏ; nếu để thước quá lỏng sẽ bỏ sót SAM.",
      "🎯 Trả lời cốt lõi: Thước phải áp sát chu vi da mà không gây lõm mô mềm.<br><br>💡 Giải thích: Cần luyện tập thành thạo cảm giác tay trên thước dây Shakir.",
      ["Bay-MUAC", "Ky-thuat"])

add_c("PED30-B1-15", "ebm_update", "B1",
      "[EBM Update] Bẫy lâm sàng khi đo Infantometer 1 người: Nếu chỉ có 1 người đo, đầu trẻ dễ bị nghiêng hoặc đầu gối co gập \→ kết quả chiều dài đo được sẽ {{c1::ngắn hơn thực tế}} \→ tính toán chỉ số WHZ bị {{c2::tăng giả tạo (bỏ sót gầy còm)}}.",
      "🎯 Trả lời cốt lõi: Bắt buộc phải có 2 người đo Infantometer.<br><br>💡 Giải thích: 1 người giữ đầu áp sát thanh cố định, 1 người ấn thẳng gối và đẩy thanh trượt chân.",
      ["Bay-Infantometer", "2-nguoi-do"])

add_c("PED30-B1-16", "ebm_update", "B1",
      "[EBM Update] Tác động định lượng của chiếc bỉm ướt: Một trẻ 10 kg có bỉm ướt 400g chiếm {{c1::4% trọng lượng cơ thể}}, đủ để làm thay đổi Z-score cân nặng tới {{c2::0.4 SD}}, biến một trẻ SAM (-3.2 SD) thành MAM (-2.8 SD).",
      "🎯 Trả lời cốt lõi: Cởi bỉm ướt là y lệnh bắt buộc trước khi cân.<br><br>💡 Giải thích: Bỏ sót SAM đồng nghĩa với việc trẻ không được cấp sữa điều trị F-75/RUTF và tăng nguy cơ tử vong.",
      ["Bim-uot", "Dinh-luong"])

add_c("PED30-B1-17", "ebm_update", "B1",
      "[EBM Update] Ví dụ chuyển đổi: Bé trai 26 tháng đo nằm được 84.7 cm. Chiều cao đứng chuẩn hóa để tra Z-score là: 84.7 - 0.7 = {{c1::84.0 cm}}.",
      "🎯 Trả lời cốt lõi: Trẻ ≥ 24 tháng đo nằm phải TRỪ 0.7 cm.<br><br>💡 Giải thích: Nếu không trừ, nhập 84.7 cm sẽ làm chỉ số WHZ bị thấp giả tạo hoặc HAZ cao giả tạo.",
      ["Vi-du-07cm", "Tinh-toan"])

add_c("PED30-B1-18", "ebm_update", "B1",
      "[EBM Update] Ví dụ chuyển đổi: Bé gái 18 tháng tuổi đo đứng được 75.3 cm. Chiều dài nằm chuẩn hóa để tra Z-score là: 75.3 + 0.7 = {{c1::76.0 cm}}.",
      "🎯 Trả lời cốt lõi: Trẻ &lt; 24 tháng đo đứng phải CỘNG 0.7 cm.<br><br>💡 Giải thích: Đưa về đúng chuẩn chiều dài nằm của lứa tuổi dưới 24 tháng theo WHO.",
      ["Vi-du-cong-07", "Tinh-toan"])

# ------------------------------------------------------------------------------
# SECTION B2: Z-SCORE WHO & ĐỘNG HỌC TĂNG TRƯỞNG (18 thẻ: 9 Barem + 9 EBM)
# ------------------------------------------------------------------------------
add_c("PED30-B2-01", "barem_goc", "B2",
      "[Barem gốc] Chỉ số WAZ (Weight-for-Age) phản ánh thể suy dinh dưỡng {{c1::Nhẹ cân (Underweight)}}, chỉ được áp dụng cho trẻ dưới {{c2::10 tuổi}}.",
      "🎯 Trả lời cốt lõi: WAZ đánh giá nhẹ cân ở trẻ &lt; 10 tuổi.<br><br>💡 Giải thích: Từ 10 tuổi trở lên trẻ bước vào dậy thì có sự phân tán lớn về tầm vóc, bắt buộc dùng BAZ.",
      ["WAZ", "Nhe-can", "Duoi-10-tuoi"])

add_c("PED30-B2-02", "barem_goc", "B2",
      "[Barem gốc] Các ngưỡng phân loại của chỉ số WAZ: (1) WAZ &lt; -2 SD là {{c1::Nhẹ cân vừa}}; (2) WAZ &lt; -3 SD là {{c1::Nhẹ cân nặng}}; (3) WAZ &gt; +2 SD cần {{c2::đối chiếu thêm WHZ/BAZ để xác định thừa cân}}.",
      "🎯 Trả lời cốt lõi: Ngưỡng -2 SD và -3 SD chuẩn hóa của WHO.<br><br>💡 Giải thích: WAZ không dùng đơn độc để chẩn đoán béo phì vì trẻ có thể nặng cân do khung xương to cao.",
      ["Nguong-WAZ", "Z-score"])

add_c("PED30-B2-03", "barem_goc", "B2",
      "[Barem gốc] Chỉ số HAZ (Height-for-Age) phản ánh thể suy dinh dưỡng {{c1::Thấp còi (Stunting)}}; ngưỡng HAZ &lt; -2 SD là {{c2::thấp còi vừa}}, HAZ &lt; -3 SD là {{c2::thấp còi nặng}}.",
      "🎯 Trả lời cốt lõi: HAZ đánh giá suy dinh dưỡng mạn tính trường diễn.<br><br>💡 Giải thích: Nếu HAZ &gt; +3 SD cần cảnh giác bất thường u tuyến yên tiết hormon tăng trưởng (GH).",
      ["HAZ", "Thap-coi", "Nguong"])

add_c("PED30-B2-04", "barem_goc", "B2",
      "[Barem gốc] Chỉ số WHZ (Weight-for-Height) áp dụng cho trẻ {{c1::dưới 5 tuổi}} (hoặc chiều cao &lt; 120 cm) nhằm đánh giá thể suy dinh dưỡng {{c2::Gầy còm (Wasting)}}.",
      "🎯 Trả lời cốt lõi: WHZ đánh giá gầy còm cấp tính ở trẻ &lt; 5 tuổi.<br><br>💡 Giải thích: Là chỉ số quan trọng nhất để sàng lọc nguy cơ tử vong cấp trong cộng đồng.",
      ["WHZ", "Gay-com", "Duoi-5-tuoi"])

add_c("PED30-B2-05", "barem_goc", "B2",
      "[Barem gốc] Các ngưỡng phân loại của chỉ số WHZ: (1) WHZ &lt; -2 SD là {{c1::Gầy còm vừa (MAM)}}; (2) WHZ &lt; -3 SD là {{c1::Gầy còm nặng (SAM)}}; (3) WHZ &gt; +2 SD là {{c2::Thừa cân}}; (4) WHZ &gt; +3 SD là {{c2::Béo phì}}.",
      "🎯 Trả lời cốt lõi: Bảng 4 ngưỡng Z-score kinh điển của WHZ.<br><br>💡 Giải thích: Cần thuộc lòng từng ngưỡng để phân loại chuẩn xác khi làm bệnh án thi.",
      ["Nguong-WHZ", "SAM", "MAM", "Beo-phi"])

add_c("PED30-B2-06", "barem_goc", "B2",
      "[Barem gốc] Chỉ số BAZ (BMI-for-Age) là chỉ số bắt buộc áp dụng cho lứa tuổi {{c1::từ 5 đến 19 tuổi}} để đánh giá cả gầy còm lẫn thừa cân - béo phì.",
      "🎯 Trả lời cốt lõi: BAZ thay thế WHZ ở trẻ từ 5 đến 19 tuổi.<br><br>💡 Giải thích: BMI = Cân nặng (kg) / [Chiều cao (m)]² sau đó tra theo biểu đồ BAZ chuẩn WHO 2007 (PMID: 18026621).",
      ["BAZ", "BMI-for-Age", "5-19-tuoi"])

add_c("PED30-B2-07", "barem_goc", "B2",
      "[Barem gốc] Các ngưỡng phân loại của chỉ số BAZ ở trẻ 5–19 tuổi: (1) BAZ &lt; -2 SD là {{c1::Gầy còm vừa}}; (2) BAZ &lt; -3 SD là {{c1::Gầy còm nặng}}; (3) BAZ &gt; +1 SD là {{c2::Thừa cân}}; (4) BAZ &gt; +2 SD là {{c2::Béo phì}}; (5) BAZ &gt; +3 SD là {{c2::Béo phì nặng}}.",
      "🎯 Trả lời cốt lõi: Điểm cắt thừa cân của BAZ là &gt; +1 SD (khác với WHZ là &gt; +2 SD).<br><br>💡 Giải thích: Tại mốc 19 tuổi, +1 SD tương đương BMI 25 kg/m² và +2 SD tương đương BMI 30 kg/m² của người lớn.",
      ["Nguong-BAZ", "Thua-can", "Beo-phi"])

add_c("PED30-B2-08", "barem_goc", "B2",
      "[Barem gốc] Động học tăng trưởng: Đường biểu diễn cân nặng bình thường của trẻ trên biểu đồ WHO phải có hướng {{c1::đi lên và chạy song song với các đường kênh chuẩn}}.",
      "🎯 Trả lời cốt lõi: Tăng trưởng bình thường chạy song song kênh.<br><br>💡 Giải thích: Tốc độ tăng trưởng ổn định phản ánh nạp năng lượng đáp ứng đủ nhu cầu phát triển.",
      ["Dong-hoc", "Binh-thuong"])

add_c("PED30-B2-09", "barem_goc", "B2",
      "[Barem gốc] Hai cờ đỏ động học tăng trưởng báo động suy dinh dưỡng sớm: (1) Đường tăng trưởng {{c1::đi ngang (Flattening)}} liên tục 2–3 tháng; (2) Đường tăng trưởng {{c2::đi xuống hoặc cắt ngang qua các kênh percentiles (Falling)}}.",
      "🎯 Trả lời cốt lõi: Đi ngang hoặc đi xuống cắt kênh là cờ đỏ suy dinh dưỡng sớm.<br><br>💡 Giải thích: Cần can thiệp ngay cả khi chỉ số Z-score lúc đó vẫn nằm trong giới hạn bình thường.",
      ["Co-do", "Flattening", "Falling"])

add_c("PED30-B2-10", "ebm_update", "B2",
      "[EBM Update] Giới hạn của chỉ số WAZ: Không thể phân biệt được một đứa trẻ bị sụt cân cấp do tiêu chảy gần đây hay bị thấp còi teo nhỏ từ nhiều năm trước, vì cả hai trường hợp đều có {{c1::cân nặng thấp so với tuổi}}.",
      "🎯 Trả lời cốt lõi: WAZ chỉ phản ánh khối lượng tổng thể, thiếu tính đặc hiệu.<br><br>💡 Giải thích: Bắt buộc phải kết hợp HAZ và WHZ để bóc tách thể bệnh cấp hay mạn.",
      ["Gioi-han-WAZ", "Phan-biet"])

add_c("PED30-B2-11", "ebm_update", "B2",
      "[EBM Update] Hiện tượng bắt kịp tăng trưởng (Catch-up growth): Khi trẻ suy dinh dưỡng được cung cấp đủ năng lượng và protein, tốc độ tăng cân có thể đạt gấp {{c1::4 đến 5 lần}} bình thường (đạt mức {{c2::≥ 10 g/kg/ngày}}).",
      "🎯 Trả lời cốt lõi: Tốc độ tăng trưởng bắt kịp rất ngoạn mục khi giải tỏa nguyên nhân đói.<br><br>💡 Giải thích: Sự hồi phục cân nặng diễn ra trước (vài tuần), hồi phục chiều cao diễn ra sau (vài tháng).",
      ["Catch-up-growth", "Hoi-phuc"])

add_c("PED30-B2-12", "ebm_update", "B2",
      "[EBM Update] Trục nội tiết chi phối tăng trưởng thể chất: Giai đoạn nhũ nhi phụ thuộc chủ yếu vào {{c1::Insulin và IGF-1}} từ dinh dưỡng; giai đoạn sau 1 tuổi phụ thuộc chính vào {{c2::Hormon tăng trưởng (GH) và hormon tuyến giáp}}.",
      "🎯 Trả lời cốt lõi: Chuyển giao cơ chế nội tiết tăng trưởng theo mốc 1 tuổi.<br><br>💡 Giải thích: Suy giáp bẩm sinh nếu không phát hiện sớm sẽ gây lùn và thiểu năng trí tuệ không hồi phục.",
      ["Noi-tiet", "GH-IGF1"])

add_c("PED30-B2-13", "ebm_update", "B2",
      "[EBM Update] Cơ chế phân tử của suy giảm miễn dịch trong suy dinh dưỡng: Thiếu protein và năng lượng dẫn đến teo tế bào lympho tại {{c1::tuyến ức và hạch lympho}} \→ giảm số lượng và chức năng của {{c2::tế bào lympho T hỗ trợ (CD4)}}.",
      "🎯 Trả lời cốt lõi: Teo tuyến ức gây suy giảm miễn dịch qua trung gian tế bào.<br><br>💡 Giải thích: Tạo vòng xoắn ác tính: Suy dinh dưỡng \→ Nhiễm trùng \→ Kém hấp thu \→ Suy dinh dưỡng nặng hơn.",
      ["Tuyen-uc", "Mien-dich"])

add_c("PED30-B2-14", "ebm_update", "B2",
      "[EBM Update] Đặc điểm nguy hiểm của nhiễm trùng ở trẻ SAM: Trẻ suy dinh dưỡng nặng khi bị viêm phổi nặng hoặc nhiễm trùng huyết thường {{c1::KHÔNG có phản ứng sốt}} và {{c2::bạch cầu máu không tăng}}, mà lại biểu hiện bằng {{c3::hạ thân nhiệt và li bì}}.",
      "🎯 Trả lời cốt lõi: Mất phản ứng viêm và đáp ứng sốt sinh lý.<br><br>💡 Giải thích: Do cơ thể kiệt quệ cytokine (IL-1, TNF-alpha) và năng lượng sinh nhiệt. Bác sĩ thấy không sốt dễ bỏ sót nhiễm trùng huyết tử vong.",
      ["Nhiem-trung-SAM", "Khong-sot", "Ha-than-nhiet"])

add_c("PED30-B2-15", "ebm_update", "B2",
      "[EBM Update] Biến đổi tim mạch trong suy dinh dưỡng nặng: Khối cơ tâm thất trái bị {{c1::teo nhỏ và giảm co bóp}}, cung lượng tim giảm; tim rất nhạy cảm với {{c2::tình trạng quá tải thể tích cấp tính}}.",
      "🎯 Trả lời cốt lõi: Teo cơ tim dẫn đến suy tuần hoàn cung lượng thấp.<br><br>💡 Giải thích: Tuyệt đối không truyền dịch tĩnh mạch nhanh ở trẻ SAM trừ khi có sốc mất nước nguy kịch.",
      ["Teo-co-tim", "Qua-tai-tuan-hoan"])

add_c("PED30-B2-16", "ebm_update", "B2",
      "[EBM Update] Biến đổi tiêu hóa trong suy dinh dưỡng nặng: Nhung mao ruột non bị {{c1::teo đét và cùn phẳng}}, giảm nghiêm trọng diện tích hấp thu và thiếu hụt thứ phát enzym {{c2::Lactase diềm bàn chải}}.",
      "🎯 Trả lời cốt lõi: Teo niêm mạc ruột gây tiêu chảy thẩm thấu khi ăn thức ăn thường.<br><br>💡 Giải thích: Lý do sữa F-75 và F-100 của WHO phải có lượng lactose thấp và áp lực thẩm thấu phù hợp.",
      ["Teo-ruot", "Lactase"])

add_c("PED30-B2-17", "ebm_update", "B2",
      "[EBM Update] Nghiên cứu de Onis et al. (2007) xác lập chuẩn BAZ 5–19 tuổi: Điểm cắt BAZ &gt; +1 SD tại 19 tuổi tương ứng với BMI {{c1::25.4 kg/m² (nam) và 25.0 kg/m² (nữ)}}, trùng khớp với ngưỡng {{c2::thừa cân của người trưởng thành}}.",
      "🎯 Trả lời cốt lõi: Khớp nối hoàn hảo giữa chuẩn nhi khoa và chuẩn người lớn (PMID: 18026621).<br><br>💡 Giải thích: Tương tự, ngưỡng +2 SD tương đương BMI 29.7 kg/m² (ngưỡng béo phì 30 kg/m²).",
      ["deOnis-2007", "BAZ-Adult"])

add_c("PED30-B2-18", "ebm_update", "B2",
      "[EBM Update] Sự khác biệt cơ bản giữa chuẩn tăng trưởng WHO 2006 (Standards) và chuẩn NCHS cũ (References): Chuẩn WHO 2006 mô tả {{c1::trẻ em NÊN tăng trưởng như thế nào (chuẩn mực kê toa)}} thay vì chỉ mô tả {{c2::trẻ em ĐANG tăng trưởng như thế nào (tham chiếu mô tả)}}.",
      "🎯 Trả lời cốt lõi: Chuẩn WHO 2006 là chuẩn quy chuẩn (Prescriptive standard).<br><br>💡 Giải thích: Lấy trẻ bú mẹ hoàn toàn trong điều kiện tối ưu làm chuẩn mực toàn cầu.",
      ["Standards-vs-References", "WHO-2006"])

# ------------------------------------------------------------------------------
# SECTION B3: KHÁM LÂM SÀNG TOÀN DIỆN & VI CHẤT (18 thẻ: 9 Barem + 9 EBM)
# ------------------------------------------------------------------------------
add_c("PED30-B3-01", "barem_goc", "B3",
      "[Barem gốc] Kỹ thuật khám phù dinh dưỡng chuẩn: Dùng mặt ngón tay cái ấn nhẹ nhưng chắc chắn lên {{c1::mặt trước xương chày hoặc mu bàn chân}} của cả hai bên trong vòng {{c2::đúng 3 giây}}.",
      "🎯 Trả lời cốt lõi: Ấn 2 bên đối xứng trong 3 giây tìm vết lõm.<br><br>💡 Giải thích: Động tác 3 giây quyết định chẩn đoán suy dinh dưỡng cấp nặng thể phù.",
      ["Kham-phu", "3-giay"])

add_c("PED30-B3-02", "barem_goc", "B3",
      "[Barem gốc] Quy tắc vàng chẩn đoán phù dinh dưỡng: Phù bắt buộc phải là phù mềm, ấn lõm và xuất hiện {{c1::ĐỐI XỨNG Ở CẢ HAI BÊN CƠ THỂ}}.",
      "🎯 Trả lời cốt lõi: Bắt buộc phải đối xứng 2 bên.<br><br>💡 Giải thích: Phù 1 bên chi là phù do viêm tắc tĩnh mạch, viêm mô tế bào hoặc chấn thương, không phải phù dinh dưỡng.",
      ["Phu-doi-xung", "Quy-tac-vang"])

add_c("PED30-B3-03", "barem_goc", "B3",
      "[Barem gốc] Ba phân độ phù dinh dưỡng trên lâm sàng: (1) Độ 1 (+): Phù nhẹ chỉ ở {{c1::hai mu bàn chân}}; (2) Độ 2 (++): Phù lan lên {{c1::hai cẳng chân, bàn tay, cẳng tay}}; (3) Độ 3 (+++): Phù {{c1::toàn thân, phù mặt, tràn dịch đa màng}}.",
      "🎯 Trả lời cốt lõi: Phân độ 1+, 2+, 3+ theo mức độ lan rộng từ ngoại vi vào trung tâm.<br><br>💡 Giải thích: Phù độ 3 có nguy cơ phù phổi và suy tim rất cao.",
      ["Phan-do-phu", "Do-1-2-3"])

add_c("PED30-B3-04", "barem_goc", "B3",
      "[Barem gốc] Quy tắc phân loại sống còn: Trẻ có phù dinh dưỡng đối xứng hai bên (bất kể độ mấy) {{c1::TỰ ĐỘNG ĐƯỢC XẾP THẲNG VÀO SUY DINH DƯỠNG CẤP NẶNG (SAM)}} mà không cần nhìn chỉ số Z-score.",
      "🎯 Trả lời cốt lõi: Có phù = SAM ngay lập tức.<br><br>💡 Giải thích: Tránh bẫy cân nặng bình thường giả tạo do nước ứ đọng che giấu teo cơ trầm trọng.",
      ["Co-phu-la-SAM", "Quy-tac-vang"])

add_c("PED30-B3-05", "barem_goc", "B3",
      "[Barem gốc] Trình tự giải phẫu mất lớp mỡ dưới da trong suy dinh dưỡng: Mỡ {{c1::bụng}} \→ Mỡ {{c1::chi (đùi, cánh tay)}} \→ Mỡ {{c1::mông}} \→ Cuối cùng là Túi mỡ {{c1::má (Bichat)}}.",
      "🎯 Trả lời cốt lõi: Mỡ má Bichat mất cuối cùng trong suy dinh dưỡng cực nặng.<br><br>💡 Giải thích: Khi mất sạch mỡ má tạo nên vẻ mặt cụ già (Old man face) của thể Marasmus.",
      ["Mat-mo", "Trinh-tu-giai-phau", "Bichat"])

add_c("PED30-B3-06", "barem_goc", "B3",
      "[Barem gốc] Dấu hiệu teo cơ mông trong thể teo đét Marasmus: Khối cơ mông teo nhẽo hoàn toàn, mất nếp lằn mông sinh lý, da vùng mông chùng xuống xếp thành nếp như {{c1::mặc quần lùng bùng (quần quá rộng) / da bọc xương}}.",
      "🎯 Trả lời cốt lõi: Dấu hiệu quần lùng bùng là chỉ điểm teo cơ mông nặng.<br><br>💡 Giải thích: Luôn yêu cầu cởi quần quan sát vùng mông khi khám dinh dưỡng.",
      ["Teo-co-mong", "Quan-lung-bung"])

add_c("PED30-B3-07", "barem_goc", "B3",
      "[Barem gốc] Dấu hiệu tổn thương tóc trong thể Kwashiorkor: Tóc thưa, khô giòn, dễ nhổ, đổi màu hung đỏ hoặc vàng; xuất hiện {{c1::Dấu hiệu cờ (Flag sign)}} gồm các dải tóc nhạt màu xen kẽ sẫm màu.",
      "🎯 Trả lời cốt lõi: Flag sign phản ánh các đợt thiếu protein ngắt quãng.<br><br>💡 Giải thích: Tóc mọc trong giai đoạn thiếu đạm thì mất sắc tố melanin; khi ăn đủ đạm lại có màu đen bình thường.",
      ["Flag-sign", "Dau-hieu-co", "Kwashiorkor"])

add_c("PED30-B3-08", "barem_goc", "B3",
      "[Barem gốc] Tổn thương mắt do thiếu Vitamin A theo thứ tự tiến triển: (1) Quáng gà (nhìn kém chập tối); (2) Vệt {{c1::Bitot (mảng bọt xà phòng kết mạc)}}; (3) Khô kết mạc giác mạc; (4) {{c2::Loét nhuyễn giác mạc (Keratomalacia)}} gây mù lòa cấp tính.",
      "🎯 Trả lời cốt lõi: Loét nhuyễn giác mạc là cấp cứu nhãn khoa khẩn cấp.<br><br>💡 Giải thích: Cần cho uống ngay Vitamin A liều điều trị theo tuổi trong vòng 24 giờ đầu.",
      ["Vitamin-A", "Bitot", "Loet-giac-mac"])

add_c("PED30-B3-09", "barem_goc", "B3",
      "[Barem gốc] Dấu hiệu còi xương do thiếu Vitamin D và Canxi trên hệ xương: (1) Thóp trước rộng, chậm liền sau {{c1::18 tháng}}; (2) Chuỗi hạt {{c2::sườn (Rachitic rosary)}}; (3) Rãnh {{c2::Harrison ở lồng ngực}}; (4) Vòng cổ tay, cổ chân to bè; (5) Chân cong chữ O hoặc chữ X.",
      "🎯 Trả lời cốt lõi: Bộ triệu chứng biến dạng xương kinh điển của còi xương tiến triển.<br><br>💡 Giải thích: Do sụn tiếp hợp phì đại không cốt hóa được khi thiếu canxi/vitamin D.",
      ["Coi-xuong", "Hat-suon", "Harrison", "Vitamin-D"])

add_c("PED30-B3-10", "ebm_update", "B3",
      "[EBM Update] Bốn cờ đỏ đe dọa tử vong trong vòng 24 giờ đầu ở trẻ SAM cần cấp cứu ngay: (1) Hạ thân nhiệt (&lt; {{c1::35.5 °C}} đo nách); (2) Hạ đường huyết (&lt; {{c1::3.0 mmol/L}}); (3) Dấu hiệu {{c2::sốc / chi lạnh ngắt / CRT ≥ 3 giây}}; (4) {{c2::Loét nhuyễn giác mạc}}.",
      "🎯 Trả lời cốt lõi: Bộ 4 cờ đỏ cấp cứu tối khẩn của WHO Pocket Book.<br><br>💡 Giải thích: Phải hồi sức ủ ấm và cho uống nước đường trước khi làm thủ tục khám thường quy.",
      ["Co-do-cap-cuu", "Ha-than-nhiet", "Ha-duong-huyet"])

add_c("PED30-B3-11", "ebm_update", "B3",
      "[EBM Update] Tổn thương da kiểu \"sơn nứt\" (Flaky-paint dermatosis) trong Kwashiorkor: Da xuất hiện các mảng tăng sắc tố sẫm màu, sau đó {{c1::nứt nẻ bong vảy từng mảng lớn}} để lộ lớp biểu bì non đỏ rỉ dịch, hay gặp ở {{c2::vùng bẹn, đùi, mông}}.",
      "🎯 Trả lời cốt lõi: Rất dễ bị nhầm với bỏng nước sôi hoặc hội chứng Stevens-Johnson.<br><br>💡 Giải thích: Hậu quả của thiếu hụt protein nặng, thiếu kẽm và thiếu acid béo thiết yếu.",
      ["Son-nut", "Flaky-paint", "Kwashiorkor"])

add_c("PED30-B3-12", "ebm_update", "B3",
      "[EBM Update] Viêm da đầu chi và quanh các lỗ tự nhiên (Acrodermatitis enteropathica): Biểu hiện tổn thương da đỏ bong vảy, mụn nước quanh miệng, mũi, hậu môn và đầu ngón tay chân là dấu hiệu kinh điển của {{c1::thiếu Kẽm nặng}}.",
      "🎯 Trả lời cốt lõi: Viêm da quanh lỗ tự nhiên gợi ý ngay thiếu Kẽm.<br><br>💡 Giải thích: Bổ sung kẽm liều điều trị tổn thương da sẽ thoái lui nhanh chóng trong 1–2 tuần.",
      ["Thieu-kem", "Acrodermatitis"])

add_c("PED30-B3-13", "ebm_update", "B3",
      "[EBM Update] Dấu hiệu móng tay lõm hình thìa (Koilonychia): Móng tay mỏng, bẹt hoặc lõm lòng chảo ở giữa, gờ móng nhô cao, móng khô giòn dễ gãy là triệu chứng đặc hiệu của {{c1::thiếu máu thiếu Sắt mạn tính nặng}}.",
      "🎯 Trả lời cốt lõi: Koilonychia chỉ điểm thiếu sắt trường diễn.<br><br>💡 Giải thích: Do thiếu enzym chứa sắt tham gia vào quá trình biệt hóa tế bào mầm móng tay.",
      ["Mong-thia", "Koilonychia", "Thieu-sat"])

add_c("PED30-B3-14", "ebm_update", "B3",
      "[EBM Update] Viêm nứt kẽ mép (Cheilosis / Angular stomatitis) và Viêm lưỡi đỏ mất gai (Glossitis): Thường phản ánh tình trạng thiếu hụt đồng thời các vitamin nhóm B gồm: {{c1::Vitamin B2 (Riboflavin), B6 (Pyridoxine), B12 và Folate}}.",
      "🎯 Trả lời cốt lõi: Nứt khóe mép hướng đến B2/B6; lưỡi đỏ nhẵn bóng hướng đến B12/Folate/Sắt.<br><br>💡 Giải thích: Các tế bào biểu mô niêm mạc miệng có tốc độ phân chia nhanh nên nhạy cảm với thiếu vitamin B.",
      ["Nut-mep", "Glossitis", "Vitamin-B"])

add_c("PED30-B3-15", "ebm_update", "B3",
      "[EBM Update] Phân biệt Phù Kwashiorkor vs Phù Hội chứng Thận hư: Phù thận hư thường bắt đầu từ {{c1::mi mắt vào buổi sáng}} và kèm theo {{c2::protein niệu ồ ạt (> 50 mg/kg/ngày)}}; trong khi phù Kwashiorkor bắt đầu từ {{c3::mu bàn chân hai bên}} và luôn có teo cơ đi kèm.",
      "🎯 Trả lời cốt lõi: Vị trí khởi phát và xét nghiệm nước tiểu giúp phân định rạch ròi.<br><br>💡 Giải thích: Kwashiorkor không có protein niệu ngưỡng thận hư; tiền sử ăn dặm toàn bột đường thiếu đạm.",
      ["Phan-biet-phu", "Than-hu", "Kwashiorkor"])

add_c("PED30-B3-16", "ebm_update", "B3",
      "[EBM Update] Vẻ mặt trong hai thể suy dinh dưỡng nặng: Thể Marasmus có vẻ mặt {{c1::cụ già (Old man face)}} do mất túi mỡ má Bichat; thể Kwashiorkor có vẻ mặt {{c2::tròn như mặt trăng rằm (Moon face)}} do phù ứ nước mô mềm.",
      "🎯 Trả lời cốt lõi: Mặt cụ già (Marasmus) vs Mặt trăng rằm (Kwashiorkor).<br><br>💡 Giải thích: Dù mặt tròn trăng rằm nhưng trẻ Kwashiorkor có biểu hiện tâm lý thờ ơ, lãnh đạm, u sầu.",
      ["Ve-mat", "Old-man", "Moon-face"])

add_c("PED30-B3-17", "ebm_update", "B3",
      "[EBM Update] Tâm lý và hành vi khác biệt: Trẻ thể Marasmus thường {{c1::rất thèm ăn, háu ăn, quấy khóc đòi ăn liên tục}}; trong khi trẻ thể Kwashiorkor lại {{c2::rất chán ăn, bỏ bú, thờ ơ, lãnh đạm với xung quanh}}.",
      "🎯 Trả lời cốt lõi: Háo ăn (Marasmus) vs Chán ăn lãnh đạm (Kwashiorkor).<br><br>💡 Giải thích: Trẻ Kwashiorkor chán ăn do rối loạn điện giải, thiếu kali/magie và teo niêm mạc ruột nặng.",
      ["Tam-ly", "Them-an", "Chan-an"])

add_c("PED30-B3-18", "ebm_update", "B3",
      "[EBM Update] Bệnh Scurvy ở trẻ em: Triệu chứng chảy máu chân răng, lợi sưng đỏ bầm tím, xuất huyết dưới màng xương gây đau xương dữ dội khiến trẻ nằm ở tư thế đùi co gập chân ếch (Frog-leg position) do thiếu hụt nghiêm trọng {{c1::Vitamin C (Acid ascorbic)}}.",
      "🎯 Trả lời cốt lõi: Bệnh Scurvy do thiếu Vitamin C làm giảm tổng hợp collagen thành mạch.<br><br>💡 Giải thích: Thường gặp ở trẻ ăn dặm bột nấu quá chín kỹ làm phá hủy toàn bộ vitamin C tự nhiên.",
      ["Scurvy", "Vitamin-C", "Chay-mau-loi"])

# ------------------------------------------------------------------------------
# SECTION B4: SO SÁNH MARASMUS vs KWASHIORKOR (14 thẻ: 7 Barem + 7 EBM)
# ------------------------------------------------------------------------------
add_c("PED30-B4-01", "barem_goc", "B4",
      "[Barem gốc] Khác biệt cốt lõi về cơ chế bệnh sinh: Thể Marasmus do {{c1::thiếu hụt toàn bộ cả Calorie lẫn Protein (đói ăn toàn diện)}}; thể Kwashiorkor do {{c2::thiếu hụt Protein đơn thuần trong khi năng lượng từ tinh bột vẫn cung cấp đủ}}.",
      "🎯 Trả lời cốt lõi: Đói toàn diện (Marasmus) vs Đói đạm đơn thuần (Kwashiorkor).<br><br>💡 Giải thích: Nguồn gốc từ tiếng Ghana: 'Kwashiorkor' nghĩa là 'căn bệnh của đứa trẻ bị thay thế khi mẹ sinh con thứ hai' (phải cai sữa mẹ ăn bột sắn đường).",
      ["Co-che-benh-sinh", "Marasmus", "Kwashiorkor"])

add_c("PED30-B4-02", "barem_goc", "B4",
      "[Barem gốc] Khác biệt về triệu chứng Phù: Thể Marasmus {{c1::HOÀN TOÀN KHÔNG CÓ PHÙ}}; thể Kwashiorkor {{c2::BẮT BUỘC PHẢI CÓ PHÙ ĐỐI XỨNG HAI BÊN}}.",
      "🎯 Trả lời cốt lõi: Phù là tiêu chuẩn phân định sống còn giữa hai thể.<br><br>💡 Giải thích: Nếu trẻ Marasmus xuất hiện thêm phù thì được xếp vào thể phối hợp Marasmic Kwashiorkor.",
      ["Phu", "Tieu-chi-phan-dinh"])

add_c("PED30-B4-03", "barem_goc", "B4",
      "[Barem gốc] Khác biệt về kích thước Gan: Thể Marasmus gan {{c1::bình thường}}; thể Kwashiorkor gan {{c2::sưng to do thoái hóa mỡ (gan ứ mỡ)}}.",
      "🎯 Trả lời cốt lõi: Gan to ứ mỡ là đặc trưng của Kwashiorkor.<br><br>💡 Giải thích: Do thiếu hụt Apolipoprotein B-100 vận chuyển mỡ ra khỏi gan.",
      ["Gan-to", "ApoB100"])

add_c("PED30-B4-04", "barem_goc", "B4",
      "[Barem gốc] Khác biệt về nồng độ Albumin huyết thanh: Thể Marasmus Albumin {{c1::bình thường hoặc giảm nhẹ (> 28 g/L)}}; thể Kwashiorkor Albumin {{c2::giảm rất nặng (&lt; 25 g/L, thậm chí &lt; 15 g/L)}}.",
      "🎯 Trả lời cốt lõi: Albumin giảm sâu làm sụt áp lực keo huyết tương gây phù trong Kwashiorkor.<br><br>💡 Giải thích: Marasmus dị hóa cơ lấy acid amin bù trừ nên gan vẫn duy trì được albumin tương đối.",
      ["Albumin", "Giam-nang"])

add_c("PED30-B4-05", "barem_goc", "B4",
      "[Barem gốc] Khác biệt về lớp mỡ dưới da: Thể Marasmus {{c1::mất sạch hoàn toàn lớp mỡ (mất cả túi mỡ má Bichat)}}; thể Kwashiorkor {{c2::vẫn còn giữ lại một phần lớp mỡ dưới da}}.",
      "🎯 Trả lời cốt lõi: Marasmus tiêu sạch mỡ; Kwashiorkor còn mỡ dưới da.<br><br>💡 Giải thích: Vì Kwashiorkor vẫn nạp thừa tinh bột nên quá trình lipogenesis từ glucose vẫn diễn ra.",
      ["Lop-mo", "Bichat"])

add_c("PED30-B4-06", "barem_goc", "B4",
      "[Barem gốc] Định nghĩa Thể phối hợp (Marasmic Kwashiorkor): Trẻ có đặc điểm của thể teo đét (gầy trơ xương, teo cơ nặng) nhưng đồng thời lại xuất hiện {{c1::triệu chứng phù ở bàn chân/cẳng chân}}.",
      "🎯 Trả lời cốt lõi: Kết hợp teo cơ trơ xương của Marasmus + phù của Kwashiorkor.<br><br>💡 Giải thích: Đây là thể lâm sàng có tiên lượng tử vong cao nhất trong mọi thể suy dinh dưỡng nặng.",
      ["Marasmic-Kwashiorkor", "Phoi-hop", "Tu-vong-cao"])

add_c("PED30-B4-07", "barem_goc", "B4",
      "[Barem gốc] Tiên lượng tử vong: Trong 3 thể suy dinh dưỡng nặng (Marasmus, Kwashiorkor, Marasmic Kwashiorkor), thể có nguy cơ tử vong cao nhất trên thực hành lâm sàng là {{c1::Thể phối hợp (Marasmic Kwashiorkor)}}.",
      "🎯 Trả lời cốt lõi: Marasmic Kwashiorkor có tỷ lệ tử vong cao nhất.<br><br>💡 Giải thích: Cơ thể vừa kiệt quệ hoàn toàn nguồn năng lượng vừa suy sụp protein và hệ thống miễn dịch.",
      ["Tien-luong", "Tu-vong"])

add_c("PED30-B4-08", "ebm_update", "B4",
      "[EBM Update] Cơ chế phân tử của Gan nhiễm mỡ trong Kwashiorkor: Tế bào gan vẫn tổng hợp Triglyceride từ tinh bột thừa nhưng không thể tổng hợp được {{c1::Apolipoprotein B-100 (Apo B-100)}} do thiếu acid amin thiết yếu \→ không đóng gói được {{c2::VLDL}} để xuất bào.",
      "🎯 Trả lời cốt lõi: Thiếu Apo B-100 làm tắc nghẽn xuất bào VLDL gây ứ mỡ tại gan.<br><br>💡 Giải thích: Mỡ bị ứ lại trong bóng mỡ nội bào gan, gan to mềm bờ tù vàng óng.",
      ["ApoB-100", "VLDL", "Gan-u-mo"])

add_c("PED30-B4-09", "ebm_update", "B4",
      "[EBM Update] Cơ chế thích nghi chuyển hóa trong Marasmus: Nồng độ Insulin huyết tương {{c1::giảm rất thấp}} và Cortisol/GH {{c2::tăng cao}} \→ kích hoạt quá trình dị hóa mỡ tạo thể ceton và dị hóa khối cơ giải phóng acid amin nuôi não và gan.",
      "🎯 Trả lời cốt lõi: Đáp ứng nội tiết thích nghi tối đa với nạn đói.<br><br>💡 Giải thích: Nhờ đó gan vẫn tổng hợp được một lượng albumin tối thiểu để duy trì áp lực keo, nên Marasmus không bị phù.",
      ["Thich-nghi-Marasmus", "Insulin-thap"])

add_c("PED30-B4-10", "ebm_update", "B4",
      "[EBM Update] Cơ chế bệnh sinh của Phù trong Kwashiorkor: Không chỉ do giảm áp lực keo vì hạ Albumin, mà còn do: (1) {{c1::Tăng tính thấm thành mạch}} do gốc tự do stress oxy hóa; (2) {{c2::Giảm bài xuất Natri tại thận}} do giảm mức lọc cầu thận.",
      "🎯 Trả lời cốt lõi: Cơ chế đa yếu tố: hạ albumin + tăng tính thấm mao mạch + giữ muối nước.<br><br>💡 Giải thích: Truyền Albumin đơn thuần không giải quyết được phù trong Kwashiorkor nếu không xử trí nhiễm trùng và chống stress oxy hóa.",
      ["Co-che-phu-Kwashiorkor", "Tinh-tham-thanh-mach"])

add_c("PED30-B4-11", "ebm_update", "B4",
      "[EBM Update] Thuyết Stress oxy hóa trong Kwashiorkor (Golden's hypothesis): Thiếu hụt các chất chống oxy hóa bảo vệ (Kẽm, Đồng, Selen, Vitamin E, Glutathione) \→ các gốc tự do peroxide phá hủy màng tế bào \→ gây tổn thương {{c1::da sơn nứt, phù và ứ mỡ gan}}.",
      "🎯 Trả lời cốt lõi: Mất cân bằng giữa gốc tự do và hệ thống phòng ngự chống oxy hóa.<br><br>💡 Giải thích: Giải thích tại sao nhiều trẻ cùng ăn thiếu đạm nhưng chỉ trẻ có nhiễm trùng/thiếu vi chất mới biểu hiện Kwashiorkor.",
      ["Stress-oxy-hoa", "Golden", "Glutathione"])

add_c("PED30-B4-12", "ebm_update", "B4",
      "[EBM Update] Bẫy sụt cân sau điều trị ở thể Kwashiorkor: Trong 5–7 ngày đầu nuôi dưỡng đúng phác đồ, cân nặng của trẻ sẽ {{c1::giảm xuống (sụt cân)}} do lượng nước phù được đào thải ra ngoài; đây là dấu hiệu {{c2::đáp ứng điều trị tốt chứ không phải bệnh nặng lên}}.",
      "🎯 Trả lời cốt lõi: Sụt cân ban đầu là dấu hiệu thoái lui của phù.<br><br>💡 Giải thích: Bác sĩ cần giải thích trước cho người nhà để tránh hoang mang khi thấy cân nặng con bị tụt.",
      ["Sut-can-thoai-phu", "Dap-ung-tot"])

add_c("PED30-B4-13", "ebm_update", "B4",
      "[EBM Update] Nồng độ Albumin trong Marasmus vs Kwashiorkor: Albumin &lt; 25 g/L là tiêu chuẩn kinh điển của {{c1::Kwashiorkor}}; trong khi ở Marasmus, nồng độ Albumin thường {{c2::trên 28 g/L (duy trì tương đối tốt)}}.",
      "🎯 Trả lời cốt lõi: Ngưỡng Albumin &lt; 25 g/L chỉ điểm suy thoái chức năng tổng hợp protein cấp của gan.<br><br>💡 Giải thích: Là một trong các tiêu chuẩn sinh hóa để xác định thể phù dinh dưỡng (PMID: 11989633).",
      ["Nguong-Albumin-25", "Sinh-hoa"])

add_c("PED30-B4-14", "ebm_update", "B4",
      "[EBM Update] Nguy cơ nhiễm trùng huyết vi khuẩn Gram âm trong SAM: Mất hàng rào biểu mô ruột và giảm bài xuất dịch mật \→ {{c1::vi khuẩn đường ruột (E. coli, Klebsiella)}} chuyển vị qua thành ruột trực tiếp vào máu tuần hoàn gây sốc nhiễm khuẩn.",
      "🎯 Trả lời cốt lõi: Chuyển vị vi khuẩn (Bacterial translocation) qua niêm mạc ruột teo đét.<br><br>💡 Giải thích: WHO khuyến cáo bắt buộc dùng kháng sinh phổ rộng thường quy (như Amoxicillin hoặc Ampicillin + Gentamicin) cho mọi trẻ SAM.",
      ["Chuyen-vi-vi-khuan", "Khang-sinh-SAM"])

# ------------------------------------------------------------------------------
# SECTION B5: CẬN LÂM SÀNG DINH DƯỠNG (14 thẻ: 7 Barem + 7 EBM)
# ------------------------------------------------------------------------------
add_c("PED30-B5-01", "barem_goc", "B5",
      "[Barem gốc] Thời gian bán hủy của Albumin huyết thanh là {{c1::20 ngày}}, do đó chỉ có giá trị đánh giá tình trạng dinh dưỡng {{c2::mạn tính kéo dài}}.",
      "🎯 Trả lời cốt lõi: T1/2 = 20 ngày phản ánh mạn tính.<br><br>💡 Giải thích: Không dùng Albumin để theo dõi sự thay đổi dinh dưỡng ngắn hạn trong vài ngày nằm viện.",
      ["Albumin", "T12-20-ngay"])

add_c("PED30-B5-02", "barem_goc", "B5",
      "[Barem gốc] Thời gian bán hủy của Prealbumin (Transthyretin) là {{c1::2 ngày}}, là chỉ số nhạy nhất để theo dõi {{c2::đáp ứng nuôi dưỡng cấp tính}} trong vòng 48–72 giờ.",
      "🎯 Trả lời cốt lõi: T1/2 = 2 ngày phản ánh đáp ứng cấp tính.<br><br>💡 Giải thích: Đạt tiêu chuẩn vàng cận lâm sàng để theo dõi nuôi ăn tĩnh mạch hoặc qua sonde dạ dày (PMID: 11989633).",
      ["Prealbumin", "T12-2-ngay"])

add_c("PED30-B5-03", "barem_goc", "B5",
      "[Barem gốc] Tiêu chuẩn chẩn đoán thiếu máu thiếu sắt trên công thức máu: Hemoglobin giảm kèm hồng cầu nhỏ nhược sắc với: MCV &lt; {{c1::80 fL}}, MCH &lt; {{c1::27 pg}}, và dải phân bố kích thước hồng cầu RDW &gt; {{c2::15%}}.",
      "🎯 Trả lời cốt lõi: Hồng cầu nhỏ nhược sắc không đều (RDW tăng).<br><br>💡 Giải thích: RDW &gt; 15% là chìa khóa phân biệt với Thalassemia thể ẩn (thường có RDW bình thường &lt; 14%).",
      ["Cong-thuc-mau", "MCV", "MCH", "RDW"])

add_c("PED30-B5-04", "barem_goc", "B5",
      "[Barem gốc] Nồng độ Ferritin huyết thanh phản ánh {{c1::lượng sắt dự trữ trong cơ thể}}; ở trẻ em không có phản ứng viêm, nồng độ Ferritin &lt; {{c2::15 ng/mL}} khẳng định chẩn đoán cạn kiệt sắt.",
      "🎯 Trả lời cốt lõi: Ferritin &lt; 15 ng/mL là tiêu chuẩn vàng thiếu sắt (AAP 2010, PMID: 20923825).<br><br>💡 Giải thích: Phản ánh kho sắt dự trữ tại gan và tủy xương.",
      ["Ferritin", "15ng-ml"])

add_c("PED30-B5-05", "barem_goc", "B5",
      "[Barem gốc] Xét nghiệm đánh giá dự trữ Vitamin D chuẩn nhất là định lượng {{c1::25-OH-Vitamin D (Calcidiol)}}; ngưỡng &lt; {{c2::20 ng/mL}} là thiếu vitamin D, ngưỡng &lt; {{c2::12 ng/mL}} là thiếu nặng.",
      "🎯 Trả lời cốt lõi: 25-OH-Vitamin D phản ánh chính xác dự trữ cơ thể (Endocrine Society, PMID: 21646368).<br><br>💡 Giải thích: Không định lượng 1,25-(OH)2-Vitamin D vì dạng này có thời gian bán hủy ngắn và bị PTH bù trừ làm sai lệch.",
      ["25-OH-D", "20ng-ml", "12ng-ml"])

add_c("PED30-B5-06", "barem_goc", "B5",
      "[Barem gốc] Enzym Phosphatase kiềm (ALP - Alkaline Phosphatase) trong máu sẽ {{c1::tăng rất cao}} trong giai đoạn còi xương đang tiến triển do tăng hoạt động của {{c2::nguyên bào tạo xương (Osteoblast)}}.",
      "🎯 Trả lời cốt lõi: ALP tăng cao chỉ điểm còi xương đang hoạt động.<br><br>💡 Giải thích: Khi điều trị vitamin D đủ liều, ALP sẽ giảm dần về bình thường sau vài tuần.",
      ["ALP", "Coi-xuong", "Osteoblast"])

add_c("PED30-B5-07", "barem_goc", "B5",
      "[Barem gốc] Nồng độ Kẽm huyết thanh ở trẻ em bình thường là &gt; {{c1::10.7 µmol/L (tương đương > 70 µg/dL)}} theo chuẩn bách phân vị 2.5 của NHANES II (PMID: 14522734).",
      "🎯 Trả lời cốt lõi: Ngưỡng dưới bình thường của kẽm là 10.7 µmol/L (70 µg/dL).<br><br>💡 Giải thích: Dưới ngưỡng này gây chậm lớn, rụng tóc, tiêu chảy kéo dài và suy giảm miễn dịch.",
      ["Kem-huyet-thanh", "107-umol"])

add_c("PED30-B5-08", "ebm_update", "B5",
      "[EBM Update] Bẫy Ferritin tăng giả tạo trong phản ứng viêm: Ferritin là một {{c1::protein phản ứng viêm giai đoạn cấp (Acute-phase reactant)}}; khi trẻ có nhiễm trùng đi kèm (CRP tăng), điểm cắt chẩn đoán thiếu sắt phải nâng lên &lt; {{c2::30 ng/mL}}.",
      "🎯 Trả lời cốt lõi: Nâng ngưỡng Ferritin lên &lt; 30 ng/mL khi có viêm (AAP 2010, PMID: 20923825).<br><br>💡 Giải thích: Nếu chỉ lấy ngưỡng 15 ng/mL sẽ bỏ sót rất nhiều trẻ thiếu sắt đang bị viêm phổi hoặc tiêu chảy.",
      ["Bay-Ferritin", "Viem-tang-gia", "30ng-ml"])

add_c("PED30-B5-09", "ebm_update", "B5",
      "[EBM Update] Bộ ba điện giải đồ sống còn cần theo dõi để phát hiện Hội chứng Nuôi ăn lại (Refeeding Syndrome): {{c1::Phospho máu (Phosphate)}}, {{c1::Kali máu (Potassium)}} và {{c1::Magie máu (Magnesium)}}.",
      "🎯 Trả lời cốt lõi: Theo dõi bộ ba P, K, Mg nội bào.<br><br>💡 Giải thích: Trong đó hạ Phospho máu là biến đổi nguy hiểm nhất dẫn đến suy tim cấp và tử vong.",
      ["Bo-ba-dien-giai", "P-K-Mg", "Refeeding"])

add_c("PED30-B5-10", "ebm_update", "B5",
      "[EBM Update] Cơ chế hạ Canxi máu bù trừ trong còi xương: Khi thiếu vitamin D, ruột giảm hấp thu canxi \→ tuyến cận giáp tăng tiết {{c1::Hormon cận giáp (PTH)}} \→ huy động canxi từ xương và tăng đào thải phospho qua thận \→ Canxi máu duy trì bình thường nhưng {{c2::Phospho máu giảm sâu}}.",
      "🎯 Trả lời cốt lõi: Canxi máu bình thường nhờ PTH bù trừ, Phospho máu giảm.<br><br>💡 Giải thích: Vì vậy trong còi xương sớm, xét nghiệm canxi máu thường bình thường, không được dùng canxi bình thường để loại trừ còi xương!",
      ["PTH-bu-tru", "Phospho-giam", "Coi-xuong"])

add_c("PED30-B5-11", "ebm_update", "B5",
      "[EBM Update] Phân tầng mức độ hạ Phospho máu trong Hội chứng Refeeding theo ASPEN 2020: (1) Nhẹ: giảm {{c1::10%–20%}}; (2) Vừa: giảm {{c1::20%–30%}}; (3) Nặng: giảm {{c1::> 30%}} hoặc nồng độ Phospho máu &lt; {{c2::0.6 mmol/L (1.8 mg/dL)}}.",
      "🎯 Trả lời cốt lõi: Phân tầng sụt giảm Phospho theo ASPEN (PMID: 32115791).<br><br>💡 Giải thích: Giảm &gt; 30% đòi hỏi phải giảm ngay tốc độ truyền calo và bù phospho tĩnh mạch.",
      ["Phan-tang-Refeeding", "ASPEN-2020", "Phospho"])

add_c("PED30-B5-12", "ebm_update", "B5",
      "[EBM Update] Bẫy lấy máu xét nghiệm kẽm huyết thanh: Kẽm có nồng độ rất cao trong hồng cầu, do đó nếu mẫu máu bị {{c1::tan máu (Hemolysis)}} hoặc để tiếp xúc lâu với kim tiêm kim loại có thể làm nồng độ kẽm đo được {{c2::tăng giả tạo}}.",
      "🎯 Trả lời cốt lõi: Máu tan máu làm tăng kẽm giả tạo.<br><br>💡 Giải thích: Cần lấy máu bằng ống nghiệm chuyên dụng không nhiễm kim loại và ly tâm tách huyết thanh sớm.",
      ["Bay-xet-nghiem-kem", "Tan-mau"])

add_c("PED30-B5-13", "ebm_update", "B5",
      "[EBM Update] Vai trò của xét nghiệm khí máu động mạch ở trẻ SAM: Trẻ suy dinh dưỡng nặng dễ bị {{c1::Toan chuyển hóa (Metabolic acidosis)}} do giảm tưới máu mô, tăng acid lactic và suy giảm khả năng tái hấp thu bicabonate ở ống thận.",
      "🎯 Trả lời cốt lõi: Toan chuyển hóa là dấu hiệu suy kiệt tuần hoàn nặng.<br><br>💡 Giải thích: Toan chuyển hóa làm giảm nhạy cảm của thụ thể cơ tim với catecholamine gây tụt huyết áp kháng trị.",
      ["Khi-mau", "Toan-chuyen-hoa"])

add_c("PED30-B5-14", "ebm_update", "B5",
      "[EBM Update] Bilan đông máu trong Kwashiorkor: Tế bào gan suy thoái giảm tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X) \→ thời gian prothrombin (PT) và tỷ lệ {{c1::INR kéo dài}} \→ nguy cơ xuất huyết tiêu hóa và xuất huyết dưới da.",
      "🎯 Trả lời cốt lõi: Kéo dài INR/PT do suy giảm chức năng tổng hợp gan.<br><br>💡 Giải thích: Cần tiêm bắp Vitamin K1 (1 mg) ngay khi tiếp nhận trẻ suy dinh dưỡng nặng.",
      ["Dong-mau", "Vitamin-K", "PT-INR"])

# ------------------------------------------------------------------------------
# SECTION B6: KHẨU PHẦN 24H & HAI BẪY LÂM SÀNG TỬ VONG (14 thẻ: 7 Barem + 7 EBM)
# ------------------------------------------------------------------------------
add_c("PED30-B6-01", "barem_goc", "B6",
      "[Barem gốc] Phương pháp hỏi khẩu phần 24 giờ qua (24-Hour Dietary Recall): Bác sĩ yêu cầu người nuôi dưỡng kể chi tiết toàn bộ thức ăn, nước uống mà trẻ đã nạp trong vòng {{c1::24 giờ của ngày hôm trước}} từ lúc thức dậy đến sáng hôm nay.",
      "🎯 Trả lời cốt lõi: Thu thập bức tranh thực tế về bữa ăn của trẻ.<br><br>💡 Giải thích: Dùng các vật dụng trực quan (bát con, thìa canh, muỗng cà phê, bình sữa có vạch ml) để định lượng chính xác.",
      ["24h-Recall", "Hoi-khau-phan"])

add_c("PED30-B6-02", "barem_goc", "B6",
      "[Barem gốc] Bốn nhóm chất dinh dưỡng bắt buộc phải có trong mỗi bữa ăn dặm của trẻ: (1) Nhóm Bột đường (Glucid); (2) Nhóm {{c1::Đạm (Protein)}}; (3) Nhóm {{c1::Chất béo (Lipid: dầu/mỡ)}}; (4) Nhóm {{c1::Rau củ quả (Vitamin & Khoáng chất)}}.",
      "🎯 Trả lời cốt lõi: Bắt buộc đủ 4 nhóm chất trong tô cháo/bột.<br><br>💡 Giải thích: Thiếu bất kỳ nhóm nào đều dẫn đến suy dinh dưỡng hoặc thiếu hụt vi chất đặc hiệu.",
      ["4-nhom-chat", "To-chao"])

add_c("PED30-B6-03", "barem_goc", "B6",
      "[Barem gốc] Định lượng chất béo bắt buộc trong mỗi bát bột/cháo của trẻ ăn dặm: Bắt buộc phải cho từ {{c1::5 đến 10 ml dầu ăn hoặc mỡ lợn}} vào mỗi bát cháo khi vừa bắc ra khỏi bếp.",
      "🎯 Trả lời cốt lõi: Mỗi bát cháo cần 5–10 ml dầu mỡ.<br><br>💡 Giải thích: Chất béo cung cấp năng lượng đậm đặc (9 kcal/g) giúp trẻ ăn ít thể tích nhưng đủ calo.",
      ["Dau-mo", "5-10ml"])

add_c("PED30-B6-04", "barem_goc", "B6",
      "[Barem gốc] Sai lầm kinh điển khi nấu cháo nước hầm xương: Nước xương chỉ có tủy mỡ khó tiêu, hoàn toàn {{c1::không có canxi hữu dụng}} và thiếu năng lượng; việc không cho dầu mỡ làm trẻ không hấp thu được các {{c2::vitamin tan trong dầu (A, D, E, K)}}.",
      "🎯 Trả lời cốt lõi: Nước hầm xương không có canxi và gây thiếu vitamin tan trong dầu.<br><br>💡 Giải thích: Hậu quả trực tiếp dẫn đến suy dinh dưỡng thấp còi, còi xương và khô mắt.",
      ["Nuoc-ham-xuong", "Sai-lam"])

add_c("PED30-B6-05", "barem_goc", "B6",
      "[Barem gốc] Bẫy pha sữa công thức quá loãng: Nhiều gia đình hoàn cảnh khó khăn pha sữa quá loãng để tiết kiệm \→ trẻ uống no nước nhưng thiếu năng lượng trầm trọng dẫn đến suy dinh dưỡng thể {{c1::Marasmus (teo đét)}} và biến chứng nguy hiểm là {{c2::Hạ natri máu}}.",
      "🎯 Trả lời cốt lõi: Pha sữa quá loãng gây teo đét và ngộ độc nước hạ natri máu.<br><br>💡 Giải thích: Luôn hỏi chi tiết số muỗng gạt sữa pha với bao nhiêu ml nước.",
      ["Pha-sua-loang", "Ha-natri-mau"])

add_c("PED30-B6-06", "barem_goc", "B6",
      "[Barem gốc] Bẫy lâm sàng số 1 — Cân nặng giả tạo ở thể Kwashiorkor: Trẻ phù toàn thân độ 3 có thể có chỉ số Z-score nằm trong dải {{c1::hoàn toàn bình thường}}, nhưng khi điều trị hết phù, cân nặng thực tế sẽ {{c2::tụt sâu xuống mức suy dinh dưỡng nặng}}.",
      "🎯 Trả lời cốt lõi: Khối lượng nước phù che giấu cân nặng thực tế.<br><br>💡 Giải thích: Tuyệt đối không dựa vào cân nặng bình thường để loại trừ suy dinh dưỡng khi trẻ có phù!",
      ["Can-nang-gia-tao", "Bay-Kwashiorkor"])

add_c("PED30-B6-07", "barem_goc", "B6",
      "[Barem gốc] Bẫy lâm sàng số 2 — Hiểm họa Hội chứng Nuôi ăn lại (Refeeding Syndrome): Xảy ra khi một trẻ bị bỏ đói lâu ngày được nạp một lượng lớn {{c1::Carbohydrate (đường bột)}} đột ngột ngay trong những ngày đầu nhập viện.",
      "🎯 Trả lời cốt lõi: Nạp calo đường bột đột ngột kích hoạt Refeeding Syndrome.<br><br>💡 Giải thích: Có thể làm trẻ ngừng tim và tử vong trong vòng 24–48 giờ đầu nếu không phòng ngừa.",
      ["Refeeding-Syndrome", "Carbohydrate"])

add_c("PED30-B6-08", "ebm_update", "B6",
      "[EBM Update] Chuỗi cơ chế bệnh sinh của Hội chứng Nuôi ăn lại: Nạp Glucose đột ngột \→ Tụy tiết ồ ạt {{c1::Insulin}} \→ Insulin kích hoạt bơm Na-K-ATPase đẩy toàn bộ {{c2::Phospho, Kali, Magie}} từ máu vào trong tế bào \→ Hạ Phospho máu cấp tính \→ {{c3::Suy tim cấp, phù phổi cấp, ngừng tim tử vong}}.",
      "🎯 Trả lời cốt lõi: Bão Insulin kéo Phospho vào nội bào gây suy tim cấp.<br><br>💡 Giải thích: Thiếu phospho làm tế bào không tổng hợp được ATP và hồng cầu mất 2,3-DPG.",
      ["Co-che-Refeeding", "Bao-Insulin", "Ha-Phospho"])

add_c("PED30-B6-09", "ebm_update", "B6",
      "[EBM Update] Nguyên tắc vàng phòng ngừa Hội chứng Nuôi ăn lại (ASPEN 2020): Khởi đầu nuôi ăn ở trẻ có nguy cơ cao với mức năng lượng thấp chỉ từ {{c1::80 đến 100 kcal/kg/ngày}}, chia nhỏ làm {{c2::8 đến 12 cữ ăn}} trong ngày.",
      "🎯 Trả lời cốt lõi: Bắt đầu thấp (80–100 kcal/kg/ngày), đi từ từ (PMID: 32115791).<br><br>💡 Giải thích: Dùng sữa F-75 có tỷ lệ đạm thấp (0.9g/100ml) và áp lực thẩm thấu an toàn.",
      ["Khoi-dau-80-100", "ASPEN", "Phong-ngua"])

add_c("PED30-B6-10", "ebm_update", "B6",
      "[EBM Update] Bổ sung Thiamin (Vitamin B1) trước khi nuôi ăn lại: Bắt buộc cho uống hoặc tiêm Thiamin liều {{c1::50–100 mg}} trước khi nạp carbohydrate để phòng ngừa biến chứng não cấp tính là {{c2::Bệnh não Wernicke}} và toan lactic máu.",
      "🎯 Trả lời cốt lõi: Bổ sung Thiamin trước cữ ăn đầu tiên.<br><br>💡 Giải thích: Thiamin là coenzym bắt buộc của Pyruvate dehydrogenase trong chu trình Krebs chuyển hóa glucose.",
      ["Thiamin", "Vitamin-B1", "Wernicke"])

add_c("PED30-B6-11", "ebm_update", "B6",
      "[EBM Update] Tiêu chí tăng dần năng lượng an toàn trong hồi phục dinh dưỡng: Chỉ tăng năng lượng từ 100 lên 130–150 kcal/kg/ngày khi: (1) Trẻ dung nạp tốt sau {{c1::3–5 ngày}}; (2) {{c1::Hết vẻ mặt u sầu, bắt đầu thèm ăn}}; (3) Điện giải đồ (Phospho, Kali) {{c2::hoàn toàn ổn định}}.",
      "🎯 Trả lời cốt lõi: Đảm bảo 3 điều kiện ổn định trước khi chuyển sang F-100/RUTF.<br><br>💡 Giải thích: Vội vàng chuyển sang sữa năng lượng cao F-100 quá sớm sẽ kích hoạt lại biến chứng Refeeding.",
      ["Chuyen-sang-F100", "On-dinh"])

add_c("PED30-B6-12", "ebm_update", "B6",
      "[EBM Update] Khái niệm RUTF (Ready-to-Use Therapeutic Food): Là sản phẩm dinh dưỡng dạng bột nhão đóng gói ăn liền (gốc đậu phộng, sữa, đường, dầu và khoáng vi lượng), cung cấp khoảng {{c1::500 kcal / gói 92g}}, dùng điều trị {{c2::SAM ngoại trú không biến chứng}}.",
      "🎯 Trả lời cốt lõi: RUTF là cuộc cách mạng giúp điều trị SAM tại nhà.<br><br>💡 Giải thích: Không chứa nước nên không bị nhiễm khuẩn, người nhà bóc gói cho trẻ ăn trực tiếp không cần nấu nướng.",
      ["RUTF", "PlumpyNut", "SAM-ngoai-tru"])

add_c("PED30-B6-13", "ebm_update", "B6",
      "[EBM Update] Test thử cảm giác thèm ăn (Appetite Test) với RUTF: Cho trẻ ngồi ăn thử gói RUTF trong 30 phút ở nơi yên tĩnh; trẻ ăn hết ít nhất {{c1::1/4 đến 1/3 gói}} là Appetite test dương tính \→ đủ tiêu chuẩn {{c2::quản lý ngoại trú}}.",
      "🎯 Trả lời cốt lõi: Appetite test dương tính = đủ điều kiện điều trị ngoại trú.<br><br>💡 Giải thích: Nếu trẻ từ chối ăn hoặc ăn quá ít = thất bại với test ăn \→ bắt buộc nhập viện điều trị nội trú.",
      ["Appetite-test", "RUTF", "Ngoai-tru"])

add_c("PED30-B6-14", "ebm_update", "B6",
      "[EBM Update] Bổ sung Sắt ở trẻ SAM: Tuyệt đối {{c1::KHÔNG bổ sung sắt trong giai đoạn cấp cứu ban đầu (giai đoạn 1)}} vì sắt tự do kích thích vi khuẩn phát triển mạnh gây nhiễm trùng huyết; chỉ bắt đầu bổ sung sắt khi trẻ bước vào {{c2::giai đoạn hồi phục bắt đầu tăng cân}}.",
      "🎯 Trả lời cốt lõi: Trì hoãn bổ sung sắt đến giai đoạn hồi phục.<br><br>💡 Giải thích: Sắt tự do chưa gắn transferrin là nguồn dưỡng chất cho vi khuẩn độc lực cao sinh sôi.",
      ["Tri-hoan-sat", "Giai-doan-cap", "Nhiem-trung-huyet"])

# ==============================================================================
# MAIN BUILDER EXECUTION
# ==============================================================================
def main():
    print("=" * 70)
    print("BUILD MASTER ANKI DECK PED-30: ĐÁNH GIÁ DINH DƯỠNG TRẺ EM WHO")
    print("=" * 70)

    # 1. Verification of card requirements
    print(f"Tổng số thẻ đã định nghĩa: {len(cards_ped30)}")
    assert 90 <= len(cards_ped30) <= 110, f"Total cards must be between 90 and 110, got {len(cards_ped30)}"

    sec_counts = {}
    for c in cards_ped30:
        sec = c["section"]
        sec_counts[sec] = sec_counts.get(sec, 0) + 1

    print("\nPhân bố thẻ theo Section B0 - B6:")
    for s in ["B0", "B1", "B2", "B3", "B4", "B5", "B6"]:
        cnt = sec_counts.get(s, 0)
        print(f"  - Section {s}: {cnt} thẻ")
        assert cnt > 0, f"Section {s} has 0 cards!"

    # 2. Linter rules check
    print("\nKiểm tra Linter quy chuẩn thẻ:")
    unescaped_lt = 0
    latex_matches = 0
    double_escapes = 0
    for idx, c in enumerate(cards_ped30, 1):
        txt = c["text"] + " " + c.get("extra", "")
        # Check unescaped < (only <b, </b, <br, <div, </div, <hr, &lt; allowed)
        raw_lt = re.findall(r"<(?![a-zA-Z/])", txt)
        if raw_lt:
            print(f"  [WARN] Card {c['id']} has unescaped '<': {raw_lt}")
            unescaped_lt += len(raw_lt)
        # Check LaTeX
        if ("$" in txt) or ("\\text{" in txt) or ("\\ge" in txt):
            print(f"  [WARN] Card {c['id']} has LaTeX symbols: '$'")
            latex_matches += 1
        # Check double escapes
        if "&lt;b&gt;" in txt or "&amp;" in txt:
            print(f"  [WARN] Card {c['id']} has double escapes")
            double_escapes += 1

    print(f"  Unescaped '<': {unescaped_lt}")
    print(f"  LaTeX occurrences: {latex_matches}")
    print(f"  Double escapes: {double_escapes}")
    assert unescaped_lt == 0, "Found unescaped '<' in cards!"
    assert latex_matches == 0, "Found LaTeX '$' in cards!"
    assert double_escapes == 0, "Found double escapes in cards!"
    print("  => Linter 100% CLEAN!")

    # 3. Export JSON & APKG
    json_path = DIR / "PED-30_Danh_gia_dinh_duong_MASTER_v1.cards.v2.json"
    apkg_path = DIR / "PED-30_Danh_gia_dinh_duong_MASTER_v1.apkg"
    deck_name = "Nhi khoa Y6::PED-30: Danh gia dinh duong tre em theo chuan WHO"

    create_deck_and_json(17093001, deck_name, cards_ped30, json_path, apkg_path)
    print("\n[SUCCESS] Hoàn thành build Deck Master PED-30!")

if __name__ == "__main__":
    main()