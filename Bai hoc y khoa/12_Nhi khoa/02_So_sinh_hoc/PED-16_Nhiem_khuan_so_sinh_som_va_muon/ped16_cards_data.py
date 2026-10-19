# -*- coding: utf-8 -*-
"""ped16_cards_data.py — Thẻ Anki Master PED-16: Nhiễm khuẩn sơ sinh sớm và muộn (Basic-first)."""
import re

_COL = {"r": "#ff6b6b", "y": "#ffd43b", "g": "#51cf66", "b": "#74c0fc"}
_MARK = re.compile(r"\[([rygb])\](.*?)\[/\]", re.S)


def _c(text):
    return _MARK.sub(lambda m: '<span style="color:%s"><b>%s</b></span>' % (_COL[m.group(1)], m.group(2)), text)


CAT = {
    "B0": "Tổng quan & nền tảng",
    "B1": "Định nghĩa & phân loại",
    "B2": "Sinh lý bệnh",
    "B3": "Chẩn đoán & phân tầng nguy cơ",
    "B4": "Xét nghiệm & theo dõi",
    "B5": "Điều trị",
    "B6": "Lưu đồ quyết định",
    "B7": "Dự phòng IAP & biến chứng",
    "B8": "Cạm bẫy lâm sàng",
    "B9": "Checkpoint & ca lâm sàng",
    "B10": "Tips & tóm tắt ca trực",
}

cards_data = []


def B(cid, sec, tier, front, ans, why, extra, algo=False):
    back = "<b>🎯 Trả lời cốt lõi:</b><br>" + "<br>".join("%d) %s" % (i + 1, a) for i, a in enumerate(ans))
    back += "<br><br><b>💡 Giải thích của AI:</b><br>" + why
    card = {
        "id": cid, "type": "basic", "track": "ebm", "section": sec, "category": CAT[sec], "tier": tier,
        "badge": "⚡ THUẬT TOÁN QUYẾT ĐỊNH" if algo else "🔬 EBM HIỆN ĐẠI & LÂM SÀNG",
        "badge_class": "badge-algo" if algo else "badge-ebm",
        "front": _c(front), "back": _c(back), "extra": "📖 Nguồn: " + extra,
        "tags": ["PED-16", sec, "ALGO" if algo else "EBM"],
    }
    cards_data.append(card)


def C(cid, sec, legacy, text, extra):
    cards_data.append({
        "id": cid, "type": "cloze", "section": sec, "text": text,
        "extra": "📖 Nguồn: PED-16 RELEASE v1. " + extra, "legacy_note_id": legacy,
    })


# ============================ B0 TỔNG QUAN & NỀN TẢNG ============================
B("PED16-B0-01", "B0", 1,
  "Nhiễm khuẩn sơ sinh có [y]2 thái cực sai lầm[/] nào trong thực hành, và [r]hậu quả[/] của từng thái cực là gì?",
  ["[r]Overtreatment (lạm dụng kháng sinh):[/] kê kháng sinh phổ rộng hoặc kéo dài [y]7–10 ngày[/] cho mọi trẻ có mẹ vỡ ối sớm/rỉ ối dù trẻ khỏe và xét nghiệm âm tính → loạn khuẩn ruột (Dysbiosis), [r]tăng NEC[/], tăng nhiễm nấm [b]Candida[/] xâm lấn, kéo dài ngày nằm viện, thúc đẩy vi khuẩn đa kháng [b]ESBL, CRE[/].",
   "[r]Undertreatment (bỏ sót, trì hoãn):[/] nhiễm khuẩn huyết sơ sinh [y]hầu như không sốt cao[/]; chỉ có bú kém nhẹ, thân nhiệt dao động hoặc [y]< 36.5 °C[/], cơn ngừng thở thoáng qua, da tái nổi bông, đường huyết không ổn định. Bỏ qua hoặc chờ xét nghiệm (CRP cuống rốn vô giá trị) → can thiệp muộn khi đã [r]sốc nhiễm trùng không hồi phục hoặc viêm màng não mủ[/]."],
  "Hệ miễn dịch sơ sinh (nhất là non tháng) non nớt nên bệnh [r]tiến triển tối cấp[/]: trẻ hồng hào vài giờ sau có thể sốc, suy đa tạng. Bài học này cân bằng giữa không bỏ sót dấu hiệu tinh tế và không dùng kháng sinh thừa.",
  "PED-16 RELEASE v1, phần 0 Tổng quan")

B("PED16-B0-02", "B0", 2,
  "Định nghĩa 5 thuật ngữ nền tảng: [b]EOS[/], [b]LOS[/], [b]IAP[/], [b]Kaiser Sepsis Calculator[/], [b]Rule-out Sepsis[/] và [y]mốc số[/] đi kèm?",
  ["[b]EOS:[/] nhiễm khuẩn huyết [y]< 72 giờ[/] đầu đời, chủ yếu [y]lây truyền dọc[/] từ mẹ trước hoặc trong sinh (AAP và NICE đồng thuận mốc 72 giờ, không dùng mốc 7 ngày cũ).",
   "[b]LOS:[/] nhiễm khuẩn huyết [y]≥ 72 giờ[/] tuổi, chủ yếu [y]lây truyền ngang[/] từ môi trường bệnh viện, tay nhân viên y tế, sữa nhiễm khuẩn, thủ thuật xâm lấn (catheter, ống nội khí quản).",
   "[b]IAP:[/] kháng sinh dự phòng trong chuyển dạ, truyền tĩnh mạch cho sản phụ nguy cơ cao (nhiễm [b]GBS[/]) để ngăn lây sang thai nhi.",
   "[b]Kaiser Sepsis Calculator:[/] công cụ đa biến phối hợp yếu tố nguy cơ tiền sản với lâm sàng thực tế của trẻ để cá thể hóa quyết định dùng kháng sinh, [y]giảm 30–50%[/] kháng sinh lạm dụng.",
   "[b]Rule-out Sepsis:[/] dừng kháng sinh an toàn ở [y]36–48 giờ[/] sau sinh khi cấy máu âm tính, chỉ số viêm bình thường và trẻ hoàn toàn khỏe. Kèm [b]I/T ≥ 0.2[/] là dấu chỉ điểm tủy xương giải phóng ồ ạt tế bào non."],
  "Mốc thời gian không chỉ để phân loại mà quyết định nguồn lây, vi khuẩn và kháng sinh đầu tay, nên phải thuộc trước khi học các phần sau.",
  "PED-16 RELEASE v1, phần 0.1")

B("PED16-B0-03", "B0", 2,
  "[r]BOX ĐỎ cấp cứu sơ sinh:[/] liệt kê [y]6 nhóm dấu hiệu[/] chỉ cần có [y]bất kỳ một[/] là phải dừng khám thường quy, và [g]hành động[/] ngay là gì?",
  ["[r]Thở rên[/] liên tục khi nằm yên, phập phồng cánh mũi, rút lõm lồng ngực nặng.",
   "[r]Cơn ngừng thở[/] kéo dài [y]> 15–20 giây[/], hoặc bất kỳ cơn ngừng thở nào kèm tím tái hoặc nhịp tim [y]< 100 lần/phút[/].",
   "[r]Hạ thân nhiệt < 36.0 °C[/] không hồi phục sau ủ ấm tích cực.",
   "[r]Rối loạn tưới máu:[/] [y]CRT > 3 giây[/], mạch bẹn yếu hoặc không bắt được, da tái xám nổi vân tím (mottling).",
   "[r]Thóp phồng căng, co giật, giảm trương lực toàn thân[/] (mềm oặt như búp bê vải).",
   "[r]Ban xuất huyết hoại tử da[/] hoặc chảy máu không cầm ở vị trí tiêm truyền (cảnh báo [b]DIC[/]).",
   "[g]Hành động:[/] kích hoạt hồi sức sơ sinh, hỗ trợ hô hấp, ủ ấm, [g]cấy máu và tiêm kháng sinh tĩnh mạch trong Giờ vàng đầu tiên[/]."],
  "Nhiễm khuẩn sơ sinh diễn tiến rất nhanh, nên chỉ một dấu hiệu nặng đã đủ ngưỡng cấp cứu; chờ thêm dấu hiệu hoặc chờ xét nghiệm là sai lầm.",
  "PED-16 RELEASE v1, phần 0.1 (Box đỏ)")

# ============================ B1 ĐỊNH NGHĨA & PHÂN LOẠI ============================
B("PED16-B1-01", "B1", 1,
  "Ranh giới [y]72 giờ[/] giữa [b]EOS[/] và [b]LOS[/] phản ánh khác biệt căn bản ở [y]3 điểm[/] nào, và [y]mốc, đường lây, nguồn vi khuẩn[/] của mỗi loại ra sao?",
  ["Mốc 72 giờ phản ánh khác biệt về [b]nguồn lây truyền[/], [b]phổ vi khuẩn gây bệnh[/] và [g]chiến lược điều trị[/].",
   "[b]EOS:[/] [y]< 72 giờ[/] tuổi (đỉnh [y]< 24h[/]); [y]truyền dọc[/] từ mẹ; vi khuẩn từ đường sinh dục mẹ, nước ối.",
   "[b]LOS:[/] [y]≥ 72 giờ[/] tuổi; [y]truyền ngang[/] (bệnh viện); vi khuẩn từ môi trường NICU, da, tay nhân viên."],
  "EOS là bệnh lây từ mẹ nên vi khuẩn là hệ sinh dục mẹ; LOS là nhiễm khuẩn bệnh viện nên vi khuẩn là hệ vi sinh NICU và da.",
  "PED-16 RELEASE v1, phần 1.1 (bảng so sánh)")

B("PED16-B1-02", "B1", 2,
  "So sánh [b]EOS và LOS[/] về [y]vi sinh hàng đầu[/], [r]bệnh cảnh lâm sàng[/] và [g]kháng sinh đầu tay[/]?",
  ["[b]EOS:[/] vi sinh [b]GBS (~40%)[/], [b]E. coli (~30%)[/], [b]Listeria monocytogenes[/]; bệnh cảnh [r]suy hô hấp tối cấp, PPHN, sốc tim-phổi, nhiễm khuẩn huyết bùng phát tức thì[/]; kháng sinh [g]Ampicillin + Gentamicin[/].",
   "[b]LOS:[/] vi sinh [b]CoNS (~50%)[/], [b]S. aureus[/], [b]Klebsiella[/], [b]Pseudomonas[/]; bệnh cảnh [r]âm ỉ: ngừng thở, chướng bụng, vàng da, tụt tiểu cầu, sốc muộn[/]; kháng sinh [g]Oxacillin/Vancomycin + Aminoglycoside/Carbapenem[/]."],
  "Ampicillin vô hiệu với CoNS nên không được dùng phác đồ EOS cho trẻ LOS; chọn đúng nhóm theo tuổi giờ trước khi chọn kháng sinh.",
  "PED-16 RELEASE v1, phần 1.1 và Checkpoint 1")

B("PED16-B1-03", "B1", 2,
  "Đặc điểm [b]EOS[/]: tỷ lệ có triệu chứng trong [y]24 giờ đầu[/], [y]2 đường xâm nhập[/] của vi khuẩn và biểu hiện [r]nổi trội[/] dễ nhầm với bệnh nào?",
  ["Hơn [y]85%[/] ca EOS có triệu chứng ngay trong [y]24 giờ đầu[/] sau sinh.",
   "Đường xâm nhập: (1) lan ngược dòng từ âm đạo, cổ tử cung qua màng ối đã vỡ hoặc còn nguyên (viêm màng ối); (2) qua đường máu từ mẹ qua bánh nhau (kinh điển [b]Listeria monocytogenes[/]).",
   "Thai nhi hít và nuốt nước ối nhiễm khuẩn → biểu hiện nổi trội là [r]hội chứng suy hô hấp cấp (thở rên, thở nhanh, tím tái)[/], dễ nhầm với [b]Bệnh màng trong (RDS)[/] hoặc [b]Thở nhanh thoáng qua (TTN)[/]."],
  "Vì phổi là nơi đầu tiên tiếp xúc nước ối nhiễm khuẩn nên EOS thường mở màn bằng suy hô hấp; nhầm với TTN có thể rất nguy hiểm.",
  "PED-16 RELEASE v1, phần 1.1 mục EOS")

B("PED16-B1-04", "B1", 2,
  "Đặc điểm [b]LOS[/]: [y]đối tượng thường gặp[/], [y]cổng vào[/] của vi khuẩn và [r]bệnh cảnh khởi đầu[/]?",
  ["Thường ở trẻ [y]đẻ non, nhẹ cân[/] nằm điều trị kéo dài tại NICU.",
   "Vi khuẩn xâm nhập qua hàng rào bị phá vỡ: [b]UVC[/] (catheter tĩnh mạch rốn), [b]PICC[/], ống nội khí quản, sonde dạ dày hoặc niêm mạc ruột tổn thương.",
   "Khởi đầu âm ỉ, không đặc hiệu: trẻ bỗng [r]'trông không được khỏe'[/], [r]tăng số cơn ngừng thở[/] trên monitor, [r]kém dung nạp sữa[/] (dịch dạ dày ứ đọng), [r]chướng bụng[/] hoặc [r]tiểu cầu giảm nhanh[/]."],
  "Catheter và thủ thuật xâm lấn mở đường cho vi khuẩn da và môi trường; vì vậy tăng cơn ngừng thở ở trẻ non đang ổn định phải nghĩ tới nhiễm khuẩn.",
  "PED-16 RELEASE v1, phần 1.1 mục LOS")

B("PED16-B1-05", "B1", 1,
  "So sánh [y]3 trường phái[/] tiếp cận nhiễm khuẩn sơ sinh: [b]AAP[/], [b]NICE NG195[/] và [b]WHO[/]?",
  ["[b]AAP (Mỹ):[/] cá thể hóa định lượng bằng [b]Kaiser Sepsis Calculator[/] cho trẻ [y]≥ 34 tuần[/], tính xác suất nguy cơ trên 1000 trẻ sống từ biến số tiền sản và lâm sàng; tránh xét nghiệm đại trà cho trẻ không triệu chứng.",
   "[b]NICE NG195 (Anh):[/] chia [r]Cờ đỏ[/] (cấy máu + kháng sinh TM ngay trong [y]60 phút[/]; gồm nghi nhiễm khuẩn ối mẹ, vỡ ối [y]> 18h[/] ở thai [y]< 37 tuần[/], co giật, suy hô hấp nặng, sốc) và [y]yếu tố nguy cơ[/] (cần [y]≥ 2 yếu tố[/] hoặc [y]1 yếu tố kèm triệu chứng[/] mới cấy máu và dùng kháng sinh).",
   "[b]WHO (tuyến cơ sở, thiếu nguồn lực):[/] dựa [r]dấu hiệu nguy hiểm toàn thân[/] để quyết định chuyển viện hoặc tiêm kháng sinh bắp đầu tay."],
  "Ba trường phái khác nhau về công cụ nhưng cùng mục tiêu: điều trị sớm trẻ thực sự nguy cơ, không điều trị oan trẻ khỏe.",
  "PED-16 RELEASE v1, phần 1.2")

B("PED16-B1-06", "B1", 2,
  "Bộ giải mã nhanh [b]EOS vs LOS[/]: từ [y]tuổi giờ[/] suy ra [b]nguồn lây[/], [b]vi khuẩn[/] và [g]kháng sinh đầu tay[/]?",
  ["[y]< 72 giờ[/] → [b]EOS[/] → truyền dọc từ mẹ → [b]GBS, E. coli, Listeria[/] → [g]Ampicillin + Gentamicin[/].",
   "[y]≥ 72 giờ[/] → [b]LOS[/] → truyền ngang NICU/catheter → [b]CoNS, S. aureus, Gram âm bệnh viện[/] → [g]Vancomycin (hoặc Oxacillin) + Aminoglycoside/Carbapenem[/].",
   "Ví dụ: trẻ [y]5 ngày[/] tuổi, sinh non, lưu catheter, chướng bụng, tăng ngừng thở, tiểu cầu giảm → là [b]LOS[/], [r]không dùng phác đồ EOS[/]."],
  "Chỉ cần nhìn tuổi giờ là chọn đúng nhóm vi khuẩn; Ampicillin không diệt được CoNS.",
  "PED-16 RELEASE v1, phần 1.1 và Checkpoint 1", algo=True)

# ============================ B2 SINH LÝ BỆNH ============================
B("PED16-B2-01", "B2", 1,
  "[y]4 tầng phòng thủ miễn dịch[/] non nớt của trẻ sơ sinh là gì và khiếm khuyết [y]số liệu[/] của từng tầng?",
  ["[b]Hàng rào da niêm mạc:[/] lớp sừng mỏng, biểu bì dễ bong, pH da kiềm, tính thấm niêm mạc ruột cao, thiếu dịch nhầy sIgA.",
   "[b]Miễn dịch bẩm sinh:[/] bổ thể (C3, C4, C5b-9) chỉ bằng [y]50%[/] người lớn; giảm opsonin hóa vi khuẩn có vỏ bọc.",
   "[b]Bạch cầu đa nhân:[/] kho dự trữ tủy chỉ bằng [y]20–30%[/] người lớn; hóa ứng động kém, cạn nhanh → [r]giảm bạch cầu hạt[/] khi nhiễm trùng.",
   "[b]Miễn dịch thể dịch:[/] không tự sản xuất IgG, phụ thuộc IgG mẹ qua nhau thai trong [y]3 tháng cuối[/]; trẻ [y]< 32 tuần[/] hầu như không có kháng thể mẹ."],
  "Mọi tầng đều khiếm khuyết nên vi khuẩn dễ xâm lấn và lan nhanh, đặc biệt ở trẻ đẻ non.",
  "PED-16 RELEASE v1, phần 2 (sơ đồ phòng thủ)")

B("PED16-B2-02", "B2", 2,
  "[b]Chuỗi 1 (GBS):[/] mô tả [y]3 tầng cơ chế[/] từ hít nước ối nhiễm khuẩn đến [r]PPHN[/]?",
  ["Sản phụ mang [b]GBS (Streptococcus agalactiae)[/] ở âm đạo không được IAP → xâm nhập ngược dòng gây viêm màng ối, thai hít nước ối chứa vi khuẩn vào phế nang.",
   "Độc tố [b]Hemolysin/Cytolysin[/] gắn tế bào biểu mô phế nang typ II → ly giải và [r]ngừng sản xuất Surfactant[/]; phospholipase vi khuẩn và protein huyết tương rỉ viêm [r]bất hoạt[/] Surfactant còn sót.",
   "Mất surfactant → sức căng bề mặt tăng, xẹp phế nang lan tỏa; toan hóa và thiếu oxy kích thích [b]Endothelin-1[/], [b]Thromboxane A2[/] → co thắt tiểu động mạch phổi → [r]PPHN[/]."],
  "Hai cơ chế cùng đánh vào phổi: xẹp phế nang (giống Bệnh màng trong) cộng co mạch phổi nên hạ oxy máu trơ.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 1")

B("PED16-B2-03", "B2", 2,
  "[b]Chuỗi 1 (GBS → PPHN):[/] [r]biểu hiện[/], [g]xử trí[/] và [r]hậu quả nếu nhầm với TTN[/]?",
  ["Áp lực tim phải vượt tim trái, máu đẩy ngược qua [b]PDA[/] và [b]PFO[/] tạo shunt [r]Phải - Trái[/]: suy hô hấp dữ dội, thở rên, tím tái [r]trơ với oxy thông thường[/].",
   "[g]Xử trí:[/] thông khí cơ học áp lực dương, thuốc giãn mạch phổi chọn lọc [g]khí Nitric Oxide hít (iNO)[/], kết hợp kháng sinh tĩnh mạch khẩn cấp.",
   "[r]Hậu quả nếu nhầm TTN và chỉ cho thở oxy gọng mũi:[/] co mạch phổi tiến triển thành suy tim phải cấp, hoại tử cơ tim thiếu máu, ngừng tuần hoàn không hồi sức được trong [y]6–12 giờ[/] đầu đời."],
  "Shunt phải-trái do tăng áp phổi khiến oxy đơn thuần không đủ; phải giãn mạch phổi và diệt khuẩn nguyên nhân.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 1 (tầng 4-5)")

B("PED16-B2-04", "B2", 2,
  "[b]Chuỗi 2 (E. coli K1):[/] [y]3 bước[/] vi khuẩn lẩn tránh miễn dịch và vượt [b]hàng rào máu não[/]?",
  ["[b]E. coli kháng nguyên vỏ K1[/] (polysialic acid) chiếm tới [y]80%[/] ca viêm màng não do E. coli ở sơ sinh, xâm nhập từ ruột hoặc hô hấp vào máu.",
   "Vỏ K1 giống chuỗi acid polysialic trên phân tử kết dính thần kinh [b]NCAM[/] của người (ngụy trang phân tử) → không bị bổ thể opsonin hóa, không bị đại thực bào nhận diện → [r]du khuẩn huyết nồng độ cao[/] ([y]> 1000 CFU/mL[/]) kéo dài.",
   "[b]OmpA[/] và fimbriae gắn thụ thể [b]gp96[/] trên nội mô mao mạch não → nhập bào qua trung gian thụ thể, vượt BBB vào khoang dưới nhện."],
  "Ngụy trang như mô người giúp vi khuẩn không bị nhận diện, tồn tại dai dẳng trong máu và có đủ thời gian xuyên màng não.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 2")

B("PED16-B2-05", "B2", 2,
  "[b]Chuỗi 2 (E. coli K1):[/] [r]biểu hiện[/], [g]xử trí bắt buộc[/] và [r]hậu quả nếu không chọc DNT[/]?",
  ["Dịch não tủy không có bổ thể và bạch cầu nên vi khuẩn nhân nhanh → viêm mủ khoang dưới nhện: [r]li bì, bỏ bú, thóp phồng, co giật[/].",
   "[g]Xử trí:[/] [g]chọc dịch não tủy (LP)[/] (tế bào, sinh hóa, nhuộm Gram) và nâng [g]Ampicillin lên liều màng não [y]200–300 mg/kg/ngày[/][/] kết hợp Aminoglycoside/Cefotaxime.",
   "[r]Nếu chỉ dùng liều nhiễm khuẩn huyết, không LP:[/] kháng sinh thấm màng não không đạt ngưỡng diệt khuẩn → mủ tắc [b]cống Sylvius[/], não úng thủy tắc nghẽn, nhuyễn hóa chất trắng quanh não thất, bại não vĩnh viễn."],
  "Kháng sinh vào dịch não tủy bị hạn chế nên phải LP để phát hiện viêm màng não và nâng liều cho đủ nồng độ.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 2 (tầng 4-5)")

B("PED16-B2-06", "B2", 2,
  "[b]Chuỗi 3 (catheter → CoNS → Biofilm → LOS):[/] [y]3 tầng cơ chế[/] từ catheter đến [r]viêm hệ thống mạn[/]?",
  ["Trẻ đẻ cực non có [b]UVC/PICC[/]; [b]CoNS (Staphylococcus epidermidis)[/] thường trú trên da xâm nhập qua vị trí chọc kim dọc thành ngoài hoặc trong ống thông.",
   "Vi khuẩn bám polymer catheter, tiết chất nền ngoại bào giàu polysaccharide gọi là [b]Biofilm[/]: kháng sinh không khuếch tán vào được và bạch cầu trung tính không thực bào được.",
   "Trong Biofilm vi khuẩn nhân lên, giải phóng ngắt quãng tế bào tự do (Planktonic) và độc tố [b]Peptidoglycan[/] → viêm hệ thống mạn với [b]IL-6[/], [b]TNF-alpha[/] tác động vùng dưới đồi và trung tâm hô hấp."],
  "Biofilm là pháo đài che chắn vi khuẩn; cytokin tác động trung tâm hô hấp giải thích vì sao tăng cơn ngừng thở là dấu hiệu sớm.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 3")

B("PED16-B2-07", "B2", 2,
  "[b]Chuỗi 3 (CoNS/Biofilm):[/] [r]biểu hiện[/], [g]xử trí[/] và [r]hậu quả nếu giữ catheter[/]?",
  ["[r]Biểu hiện kín đáo:[/] tăng tần số cơn ngừng thở, thân nhiệt dao động, tiêu hóa chậm, [y]tiểu cầu giảm dần dưới 100.000/mm³[/].",
   "[g]Xử trí:[/] cấy máu đồng thời qua catheter và máu ngoại vi để đo [b]DTP[/] (Differential Time to Positivity); kháng sinh diệt tụ cầu [g]Vancomycin[/]; [g]rút bỏ ngay catheter nhiễm khuẩn[/].",
   "[r]Hậu quả nếu giữ catheter và chỉ truyền kháng sinh:[/] vi khuẩn trong Biofilm không bị tiệt căn, nhiễm khuẩn huyết tái phát khi dừng thuốc, suy kiệt dinh dưỡng, viêm nội tâm mạc, xơ hóa tĩnh mạch trung tâm."],
  "Kháng sinh không thấm Biofilm nên chỉ rút ổ nhiễm (catheter) mới tiệt căn.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 3 (tầng 4-5)")

B("PED16-B2-08", "B2", 2,
  "[b]Chuỗi 4 (Gram âm → LPS):[/] cơ chế [y]3 tầng[/] từ [b]Endotoxin[/] đến [r]sốc nhiễm trùng[/]?",
  ["Gram âm ([b]Klebsiella pneumoniae, Pseudomonas aeruginosa, E. coli[/]) giải phóng [b]LPS (Endotoxin)[/] vào huyết tương.",
   "[b]Lipid A[/] gắn [b]LBP[/] → phức hợp [b]TLR4/MD-2/CD14[/] → hoạt hóa [b]NF-kappa B[/] → bão cytokin: [b]TNF-alpha, IL-1beta, IL-6, PAF[/].",
   "Cytokin kích hoạt [b]iNOS[/] → quá nhiều [b]NO[/] → giãn tiểu động mạch, sụp đổ [b]SVR[/]; nội mô co rút tăng tính thấm → thoát huyết tương; cơ tim sơ sinh dự trữ co bóp hạn chế bị [b]TNF-alpha[/] ức chế → cung lượng tim giảm."],
  "Tụt sức cản mạch, mất thể tích hiệu dụng và giảm co bóp cùng xảy ra nên sốc sơ sinh phức tạp hơn một cơ chế đơn lẻ.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 4")

B("PED16-B2-09", "B2", 2,
  "[b]Chuỗi 4 (sốc Gram âm):[/] [r]biểu hiện[/], [g]Gói hồi sức giờ đầu[/] và [r]hậu quả nếu truyền dịch quá mức[/]?",
  ["[r]Biểu hiện:[/] da tái xám nổi vân tím, mạch bẹn yếu, [y]CRT > 3 giây[/], huyết áp tụt, vô niệu ([y]< 1 mL/kg/h[/]), toan chuyển hóa tăng lactic.",
   "[g]Sepsis Bundle 1h:[/] thông khí hỗ trợ, bolus dịch tinh thể đẳng trương [y]10–20 mL/kg[/], vận mạch sớm ([g]Adrenaline/Dopamine[/]), kháng sinh diệt khuẩn phổ rộng.",
   "[r]Nếu trì hoãn vận mạch và truyền dịch quá mức[/] ([y]> 40–60 mL/kg[/]): cơ tim non nớt quá tải thể tích → phù phổi cấp, suy thận hoại tử ống thận cấp, tử vong do sốc kháng trị."],
  "Cơ tim sơ sinh chịu được ít dịch nên bolus chỉ 10–20 mL/kg rồi đánh giá lại và dùng vận mạch sớm.",
  "PED-16 RELEASE v1, phần 2 Chuỗi 4 (tầng 4-5)")

B("PED16-B2-10", "B2", 2,
  "Ghép [y]4 chuỗi bệnh sinh[/] với [g]hành động then chốt[/] tương ứng: GBS, E. coli K1, CoNS Biofilm, Gram âm LPS?",
  ["[b]GBS → PPHN:[/] [g]thở máy áp lực dương + iNO + kháng sinh TM khẩn[/].",
   "[b]E. coli K1 → viêm màng não:[/] [g]LP + Ampicillin 200–300 mg/kg/ngày[/] phối hợp Aminoglycoside/Cefotaxime.",
   "[b]CoNS Biofilm:[/] [g]Vancomycin + rút catheter[/], cấy máu catheter và ngoại vi (DTP).",
   "[b]Gram âm LPS → sốc:[/] [g]Sepsis Bundle 1h: bolus 10–20 mL/kg, vận mạch sớm, kháng sinh phổ rộng[/]."],
  "Mỗi chuỗi có một mắt xích mấu chốt: surfactant/PPHN, hàng rào máu não, Biofilm, bão cytokin; xử trí nhắm vào mắt xích đó.",
  "PED-16 RELEASE v1, phần 2 (4 chuỗi)")

# ============================ B3 CHẨN ĐOÁN ============================
B("PED16-B3-01", "B3", 1,
  "[y]3 công cụ chẩn đoán và phân tầng nguy cơ[/] chính trong bài là gì và dùng để làm gì?",
  ["[b]Bảng 6 nhóm triệu chứng tinh tế[/] (thân nhiệt, thần kinh, hô hấp, tuần hoàn-da, tiêu hóa, huyết học-chuyển hóa): phát hiện sớm khi trẻ không nói được.",
   "[b]Kaiser Sepsis Calculator:[/] phân tầng nguy cơ EOS cho trẻ [y]≥ 34 tuần[/] bằng 5 thông số tiền sản + lâm sàng.",
   "[b]NICE NG195:[/] nhị phân [r]Cờ đỏ[/] / yếu tố nguy cơ để quyết định ngay tại giường."],
  "Trẻ sơ sinh không có triệu chứng khu trú điển hình, nên cần quan sát toàn diện 6 hệ cơ quan và công cụ định lượng.",
  "PED-16 RELEASE v1, phần 3")

B("PED16-B3-02", "B3", 2,
  "Triệu chứng [y]sớm/tinh tế[/] và [r]muộn/nguy kịch[/] của [b]thân nhiệt[/], [b]thần kinh - hành vi[/] và [b]hô hấp[/] ở sơ sinh nhiễm khuẩn?",
  ["[b]Thân nhiệt:[/] sớm dao động, [y]hạ thân nhiệt < 36.5 °C[/] phải tăng nhiệt lồng ấp; muộn [r]sốt > 38.5 °C[/] hoặc [r]hạ thân nhiệt nặng < 35.5 °C[/] trơ với ủ ấm.",
   "[b]Thần kinh - hành vi:[/] sớm giảm vận động, quấy khóc rên rỉ yếu, trương lực hơi nhão, ngủ nhiều; muộn [r]li bì, hôn mê khó đánh thức, co giật, thóp phồng căng, người mềm nhão[/].",
   "[b]Hô hấp:[/] sớm thở nhanh nhẹ, thở không đều, cánh mũi phập phồng thoáng qua; muộn [r]thở rên liên tục, rút lõm ngực sâu, ngừng thở > 15–20 giây kèm nhịp tim chậm[/]."],
  "Dấu hiệu tinh tế xuất hiện trước và là cơ hội can thiệp sớm; dấu hiệu muộn tương đương Cờ đỏ.",
  "PED-16 RELEASE v1, phần 3.1 (hàng 1-3)")

B("PED16-B3-03", "B3", 2,
  "Triệu chứng [y]sớm[/] và [r]muộn[/] của [b]tuần hoàn - da[/], [b]tiêu hóa[/] và [b]huyết học - chuyển hóa[/] ở sơ sinh nhiễm khuẩn?",
  ["[b]Tuần hoàn - da:[/] sớm da xanh tái, tái nổi vân tím khi lạnh, [y]CRT 2.5–3 giây[/], nhịp tim nhanh [y]> 160 l/p[/]; muộn [r]CRT > 3–4 giây, đầu chi lạnh ngắt, mạch bẹn mất, tụt huyết áp, nhịp tim chậm < 100 l/p[/].",
   "[b]Tiêu hóa:[/] sớm bú kém (bú kéo dài gấp đôi), ứ đọng dịch dạ dày sau cữ bú [y]> 30%[/]; muộn [r]bỏ bú hoàn toàn, nôn dịch xanh/mật, chướng bụng căng bóng, quai ruột nổi[/].",
   "[b]Huyết học - chuyển hóa:[/] sớm vàng da trong [y]24h đầu[/], dao động đường huyết (hạ hoặc tăng); muộn [r]ban xuất huyết hoại tử da, chảy máu rỉ rả chân kim tiêm (DIC), toan lactic[/]."],
  "Những dấu hiệu như vàng da sớm hoặc đường huyết dao động tưởng vô hại nhưng có thể là biểu hiện đầu tiên của nhiễm khuẩn huyết.",
  "PED-16 RELEASE v1, phần 3.1 (hàng 4-6)")

B("PED16-B3-04", "B3", 2,
  "Vì sao trẻ sơ sinh nhiễm khuẩn huyết thường [r]hạ thân nhiệt[/] thay vì sốt? Nêu [y]3 lý do[/].",
  ["Tỷ lệ diện tích da/trọng lượng cao gấp gần [y]3 lần[/] người lớn, lớp mỡ cách nhiệt mỏng → mất nhiệt bức xạ và thoát hơi nước nhanh.",
   "Trung tâm điều nhiệt vùng dưới đồi chưa hoàn thiện đường dẫn truyền thần kinh giao cảm.",
   "Nguồn sinh nhiệt chính là [b]mô mỡ nâu[/] qua [b]UCP-1[/]; độc tố vi khuẩn và cytokin ức chế chuyển hóa mỡ nâu, cộng cạn glycogen → mất khả năng tạo cơn sốt."],
  "Vì vậy hạ thân nhiệt ở sơ sinh là dấu hiệu cảnh báo nhiễm khuẩn huyết tối nguy hiểm, không được chờ sốt.",
  "PED-16 RELEASE v1, phần 3.1 (hộp Vì sao)")

B("PED16-B3-05", "B3", 2,
  "[b]Kaiser Sepsis Calculator:[/] áp dụng cho [y]tuổi thai nào[/], cần nhập [y]5 thông số tiền sản[/] nào, và [g]xử trí[/] theo [y]3 nhóm lâm sàng[/] ra sao?",
  ["Áp dụng cho trẻ [y]≥ 34 tuần[/] tuổi thai.",
   "[y]5 thông số:[/] (1) tỷ lệ hiện mắc nền (thường chọn [y]0.5/1000[/] trẻ sống); (2) tuổi thai (tuần và ngày); (3) thân nhiệt cao nhất của mẹ trong chuyển dạ; (4) thời gian vỡ ối (giờ); (5) tình trạng GBS của mẹ và loại kháng sinh IAP.",
   "Máy tính nguy cơ nền trước sinh, rồi kết hợp lâm sàng: [g]Khỏe mạnh[/] (hồng hào, thở êm, bú tốt, trương lực tốt) → theo dõi lâm sàng, không dùng thuốc; [y]Nghi ngờ/lưỡng lự (Equivocal)[/] (1 dấu hiệu bất thường nhẹ kéo dài hoặc thoáng qua) → cấy máu + theo dõi, chưa dùng kháng sinh vội; [r]Bệnh lý (Clinically Ill)[/] (suy hô hấp rõ, thở rên, hạ thân nhiệt, sốc, li bì, co giật) → cấy máu + kháng sinh TM ngay."],
  "Nguy cơ nền trước sinh chỉ là nửa đầu; chính lâm sàng sau sinh quyết định có dùng kháng sinh hay không.",
  "PED-16 RELEASE v1, phần 3.2")

B("PED16-B3-06", "B3", 2,
  "[b]Kaiser Calculator[/] có [g]lợi ích[/] gì so với phương pháp truyền thống [b]CDC 2010[/]? Nêu [y]các con số[/].",
  ["CDC 2010 dựa vào yếu tố nguy cơ đơn lẻ (cứ vỡ ối [y]> 18h[/] là làm xét nghiệm và dùng kháng sinh) khiến [y]10–15%[/] trẻ sơ sinh khỏe bị chọc máu và tiêm kháng sinh oan.",
   "Calculator [g]giảm 40–50% tỷ lệ dùng kháng sinh không cần thiết[/] và [g]giảm 70–80% số lần lấy máu xét nghiệm[/], không làm tăng ca nhiễm khuẩn huyết bị bỏ sót."],
  "Phối hợp nhiều biến số cho nguy cơ cá thể chính xác hơn một yếu tố đơn lẻ, tránh điều trị oan.",
  "PED-16 RELEASE v1, phần 3.2")

B("PED16-B3-07", "B3", 2,
  "[b]NICE NG195 nhóm Cờ đỏ:[/] liệt kê [y]6 tiêu chí[/] và [g]hành động[/] trong bao lâu khi chỉ cần có 1 dấu hiệu?",
  ["Chỉ cần [y]1 dấu hiệu[/] → [g]cấy máu + kháng sinh TM trong vòng 60 phút[/].",
   "Sốc hoặc suy hô hấp cần hỗ trợ thở máy.",
   "[r]Thở rên[/], rút lõm ngực nặng, [y]SpO2 < 90%[/] khi thở khí phòng.",
   "[r]Co giật[/] hoặc li bì hôn mê.",
   "Nghi mẹ viêm màng ối: sốt chuyển dạ [y]≥ 38.0 °C[/] kèm nước ối hôi hoặc tim thai nhanh [y]> 160 l/p[/].",
   "Vỡ ối kéo dài [y]> 18 giờ[/] ở trẻ sinh non [y]< 37 tuần[/].",
   "Tiền sử sinh con lần trước bị nhiễm GBS xâm lấn."],
  "Đây là hệ nhị phân đơn giản: có Cờ đỏ thì không cân nhắc thêm mà điều trị ngay.",
  "PED-16 RELEASE v1, phần 3.3; NICE NG195")

B("PED16-B3-08", "B3", 2,
  "[b]NICE NG195 nhóm yếu tố nguy cơ (Non-Red Flags):[/] liệt kê [y]5 yếu tố[/] và [y]ngưỡng[/] để can thiệp?",
  ["Ngưỡng: [y]≥ 2 yếu tố[/], hoặc [y]1 yếu tố kèm triệu chứng lâm sàng nhẹ[/] mới can thiệp (cấy máu, kháng sinh).",
   "Vỡ ối [y]> 18 giờ[/] ở trẻ đủ tháng.",
   "Mẹ nhiễm [b]GBS[/] không được IAP đầy đủ.",
   "Sinh non tự nhiên [y]< 37 tuần[/].",
   "Nhịp thở nhanh nhẹ [y]> 60 lần/phút[/] sau 2 giờ đầu đời.",
   "Bú kém hoặc thân nhiệt dao động nhẹ."],
  "Một yếu tố đơn độc ở trẻ khỏe chưa đủ chỉ định kháng sinh; cộng dồn mới nâng nguy cơ, nhờ đó tránh lạm dụng.",
  "PED-16 RELEASE v1, phần 3.3; NICE NG195")

B("PED16-B3-09", "B3", 2,
  "Quyết định nhị phân [b]NICE[/]: trẻ có [r]Cờ đỏ[/] hay chỉ có [y]yếu tố nguy cơ[/] thì [g]làm gì[/]?",
  ["Có [r]≥ 1 Cờ đỏ[/] → [g]cấy máu + kháng sinh TM trong 60 phút[/], không chờ thêm.",
   "Chỉ có yếu tố nguy cơ, đủ [y]≥ 2[/] hoặc [y]1 kèm triệu chứng[/] → [g]cấy máu và kháng sinh[/].",
   "Chỉ 1 yếu tố nguy cơ đơn độc, trẻ khỏe → [b]không[/] đủ ngưỡng can thiệp theo nhóm này."],
  "Quy tắc dễ nhớ: Cờ đỏ đi một mình cũng đủ; yếu tố nguy cơ cần đi đôi hoặc đi kèm triệu chứng.",
  "PED-16 RELEASE v1, phần 3.3", algo=False)

B("PED16-B3-10", "B3", 2,
  "Ở ca sản phụ [y]sốt chuyển dạ 38.6 °C, ối vỡ 22 giờ có mùi hôi[/], trẻ [y]38 tuần[/] lúc 1 giờ tuổi hồng hào: tiêu chí nào làm đây là [r]Cờ đỏ[/]?",
  ["Mẹ sốt cao, ối vỡ kéo dài, ối hôi là [b]viêm màng ối lâm sàng (Clinical Chorioamnionitis)[/] → [r]Cờ đỏ tuyệt đối theo NICE[/] và nguy cơ rất cao theo Kaiser.",
   "[g]Xử trí:[/] cấy máu [y]≥ 1.0 mL[/], chuyển đơn vị sơ sinh, tiêm [g]Ampicillin + Gentamicin TM[/] ngay và theo dõi sát, dù trẻ đang trông khỏe."],
  "Trẻ khỏe ở 1 giờ tuổi không loại trừ nhiễm khuẩn; nguy cơ tiền sản đã đủ để xử trí.",
  "PED-16 RELEASE v1, Checkpoint 2")

# ============================ B4 XÉT NGHIỆM & THEO DÕI ============================
B("PED16-B4-01", "B4", 1,
  "[y]3 trụ cột xét nghiệm[/] trong nhiễm khuẩn sơ sinh và [g]điểm quyết định sống còn[/] của từng trụ cột?",
  ["[b]Cấy máu[/] (tiêu chuẩn vàng): [y]thể tích tối thiểu 1.0 mL[/].",
   "[b]Chỉ số viêm[/] ([b]CRP, Procalcitonin, I/T, ANC[/]): hiểu [y]động học theo giờ[/] để không quyết định sai.",
   "[b]Dịch não tủy (LP):[/] chỉ định và [y]giá trị bình thường riêng của sơ sinh[/]."],
  "Sai lầm kỹ thuật (thể tích máu, thời điểm CRT, ngưỡng PCT người lớn) dễ gây quyết định sai hơn là bản thân xét nghiệm.",
  "PED-16 RELEASE v1, phần 4")

B("PED16-B4-02", "B4", 2,
  "[b]Cấy máu sơ sinh:[/] [y]thể tích tối thiểu[/], vì sao, và [y]con số độ nhạy[/] theo thể tích?",
  ["Luôn lấy [g]tối thiểu 1.0 mL máu toàn phần[/] vào một chai cấy nhi khoa; cấy máu âm tính giả ở khoa sơ sinh lên tới [y]30–50%[/] do sai thể tích.",
   "Du khuẩn huyết nồng độ thấp ([y]≤ 4 CFU/mL[/]) chiếm [y]60%[/] ca nhiễm trùng thực sự.",
   "Lấy [y]0.5 mL[/]: độ nhạy chỉ [y]50–60%[/] (bỏ sót gần một nửa); lấy đủ [y]1.0 mL[/]: độ nhạy [y]> 90–95%[/]."],
  "Vì mật độ vi khuẩn rất thấp, máu càng ít thì càng dễ không có vi khuẩn trong mẫu.",
  "PED-16 RELEASE v1, phần 4.1; Schelonka 1996")

B("PED16-B4-03", "B4", 2,
  "[b]Kỹ thuật lấy máu cấy[/]: nên và không nên lấy từ đâu, sát khuẩn thế nào?",
  ["[r]Không[/] lấy máu cấy từ đường truyền tĩnh mạch đang lưu (trừ khi nghi nhiễm trùng đường truyền [b]CLABSI[/]).",
   "Sát khuẩn da [y]3 bước[/] bằng cồn [g]Chlorhexidine 2%[/] (hoặc cồn povidone iodine ở trẻ non tháng), đợi khô [y]60 giây[/].",
   "Chọc kim lấy [g]máu tĩnh mạch ngoại vi mới[/]."],
  "Đường truyền lưu dễ nhiễm vi khuẩn định cư nên mẫu máu không phản ánh nhiễm khuẩn huyết thật.",
  "PED-16 RELEASE v1, phần 4.1")

B("PED16-B4-04", "B4", 2,
  "[b]Động học CRP[/] trong nhiễm khuẩn sơ sinh: [y]khi nào tăng, khi nào đỉnh[/] và [r]độ nhạy lúc 0-2 giờ tuổi[/]?",
  ["CRP do gan sản xuất dưới kích thích [b]IL-6[/]; gan trẻ sơ sinh cần thời gian khởi động.",
   "Bắt đầu tăng sau [y]6–8 giờ[/], đạt đỉnh sau [y]24 đến 48 giờ[/].",
   "CRP lúc sinh (máu cuống rốn) hoặc [y]0–2 giờ[/] tuổi có độ nhạy [r]< 30%[/]: trẻ nhiễm GBS tối cấp lúc mới sinh vẫn có CRP bình thường."],
  "Gan cần thời gian tổng hợp nên CRP sớm gần như luôn bình thường dù nhiễm trùng nặng.",
  "PED-16 RELEASE v1, phần 4.2 (CRP)")

B("PED16-B4-05", "B4", 2,
  "[g]Giá trị thật sự[/] của CRP trong nhiễm khuẩn sơ sinh là gì, và [y]khi nào[/] có thể dừng kháng sinh dựa vào CRP?",
  ["Giá trị nằm ở [g]giá trị tiên đoán âm (NPV > 99%)[/] khi làm chuỗi động học.",
   "[y]Hai lần[/] CRP liên tiếp cách [y]24 giờ[/] (ví dụ 24h và 48h tuổi) đều [y]< 10 mg/L[/] → khẳng định trẻ không nhiễm khuẩn huyết, an toàn dừng kháng sinh."],
  "CRP không dùng để chẩn đoán lúc đầu mà để loại trừ và quyết định dừng thuốc.",
  "PED-16 RELEASE v1, phần 4.2 (CRP)")

B("PED16-B4-06", "B4", 2,
  "[b]Procalcitonin sơ sinh:[/] [y]khi nào tăng và đỉnh[/], [r]bẫy sinh lý[/] trong 48 giờ đầu và [g]nguyên tắc an toàn[/]?",
  ["PCT do tế bào biểu mô và nhu mô tiết dưới tác động nội độc tố; tăng sau [y]2–4 giờ[/], đỉnh sau [y]12–24 giờ[/].",
   "[r]Bẫy:[/] trẻ khỏe có đỉnh tăng vọt sinh lý [y]2–10 ng/mL[/] trong [y]24–36 giờ[/] đầu đời, giảm về [y]< 0.5 ng/mL[/] sau [y]48–72 giờ[/].",
   "[g]Không áp[/] ngưỡng người lớn [y]0.5 ng/mL[/] trong 48 giờ đầu; phải đối chiếu biểu đồ bách phân vị theo giờ tuổi của [b]Chiesa[/]."],
  "Đỉnh PCT sinh lý do thích nghi sau chuyển dạ nên áp ngưỡng người lớn gây chẩn đoán nhầm và dùng thuốc thừa.",
  "PED-16 RELEASE v1, phần 4.2 (PCT); Chiesa 1998")

B("PED16-B4-07", "B4", 2,
  "[b]Tỷ lệ I/T[/] tính thế nào, [y]ngưỡng[/] nào gợi ý nhiễm trùng và [b]ANC[/] cảnh báo ở mức nào?",
  ["I/T = bạch cầu non (đũa + tiền tủy bào + tủy bào) / tổng bạch cầu hạt trung tính (non + trưởng thành).",
   "[y]I/T ≥ 0.20[/] gợi ý nhiễm trùng huyết rất cao.",
   "[r]ANC < 1000/mm³[/] (giảm bạch cầu hạt) cảnh báo nhiễm trùng huyết nặng và nguy cơ tử vong cao hơn nhiều so với tăng bạch cầu."],
  "Giảm ANC phản ánh kho dự trữ tủy cạn kiệt nên tiên lượng xấu hơn tăng bạch cầu.",
  "PED-16 RELEASE v1, phần 4.2 (I/T, ANC)")

B("PED16-B4-08", "B4", 2,
  "[b]Chọc dịch não tủy (LP) sơ sinh:[/] [y]3 chỉ định bắt buộc[/] và tại sao cần LP dù cấy máu âm tính?",
  ["Viêm màng não mủ xuất hiện ở [y]10–15%[/] trẻ nhiễm khuẩn huyết, và [y]30%[/] trẻ viêm màng não mủ có cấy máu âm tính.",
   "Chỉ định: (1) [r]cấy máu dương tính[/] với vi khuẩn; (2) dấu hiệu thần kinh: [r]co giật, thóp phồng, li bì, giảm trương lực[/]; (3) lâm sàng xấu nhanh hoặc [r]không đáp ứng sau 48 giờ[/] kháng sinh thích hợp."],
  "Vì cấy máu có thể âm tính trong viêm màng não nên dấu hiệu thần kinh một mình đã đủ chỉ định LP.",
  "PED-16 RELEASE v1, phần 4.3")

B("PED16-B4-09", "B4", 2,
  "[b]Giá trị bình thường của dịch não tủy sơ sinh[/]: [y]số bạch cầu[/], [y]protein[/] và [y]tỷ lệ glucose DNT/máu[/]?",
  ["Bạch cầu DNT trẻ đủ tháng bình thường có thể [y]≤ 20–30 tế bào/mm³[/] (chủ yếu lympho hoặc mono); trẻ đẻ non có thể [y]30–40 tế bào/mm³[/].",
   "Protein DNT bình thường rất cao: [y]0.8 đến 1.5 g/L[/] do hàng rào máu não còn lỏng lẻo.",
   "Glucose DNT / glucose máu bình thường [y]≥ 0.6[/] (≥ 60%); trẻ đẻ non có thể [y]≥ 0.7–0.8[/]."],
  "Không áp giá trị trẻ lớn cho sơ sinh vì sẽ chẩn đoán nhầm viêm màng não.",
  "PED-16 RELEASE v1, phần 4.3")

B("PED16-B4-10", "B4", 2,
  "Bộ giải mã [y]ngưỡng biomarker sơ sinh[/]: CRP, PCT, I/T, ANC, thể tích máu cấy?",
  ["[b]CRP:[/] lúc 0-2h độ nhạy [r]< 30%[/]; đỉnh [y]24–48h[/]; 2 lần [y]< 10 mg/L[/] cách 24h → NPV [y]> 99%[/].",
   "[b]PCT:[/] đỉnh sinh lý [y]2–10 ng/mL[/] ở 24–36h, về [y]< 0.5[/] sau 48–72h; không dùng ngưỡng người lớn trong 48h đầu.",
   "[b]I/T:[/] [y]≥ 0.20[/] → nghi nhiễm trùng. [b]ANC:[/] [r]< 1000/mm³[/] → nặng, nguy cơ tử vong.",
   "[b]Cấy máu:[/] [g]≥ 1.0 mL[/] (0.5 mL chỉ nhạy 50–60%)."],
  "Mỗi chỉ số có một thời điểm vàng và một bẫy; nhớ cặp số và thời gian để không đọc sai kết quả.",
  "PED-16 RELEASE v1, phần 4.1-4.2", algo=True)

# ============================ B5 ĐIỀU TRỊ ============================
B("PED16-B5-01", "B5", 1,
  "Tóm tắt [g]chiến lược kháng sinh[/] sơ sinh: kinh nghiệm [b]EOS[/], kinh nghiệm [b]LOS[/] và [y]khi nào dừng[/]?",
  ["[b]EOS (< 72 giờ):[/] [g]Ampicillin + Gentamicin[/] (Gentamicin liều mở rộng khoảng cách).",
   "[b]LOS (≥ 72 giờ):[/] [g]Oxacillin/Nafcillin hoặc Vancomycin[/] + [g]Amikacin/Gentamicin hoặc Meropenem[/], ± kháng nấm ở trẻ cực non.",
   "[r]Cấm Ceftriaxone[/]; [r]tránh Cefotaxime[/] làm đầu tay.",
   "[y]Rule-out Sepsis 36–48 giờ[/]: cấy âm tính + khỏe + CRP bình thường → [g]ngừng kháng sinh ngay[/]."],
  "Chọn phác đồ theo tuổi giờ, tránh kháng sinh gây hại, và dừng sớm khi đủ điều kiện.",
  "PED-16 RELEASE v1, phần 5")

B("PED16-B5-02", "B5", 2,
  "[g]Ampicillin + Gentamicin[/] cho EOS: [y]phổ[/], [y]liều Ampicillin[/] thường và liều [r]viêm màng não[/], và [b]cơ chế hiệp đồng[/]?",
  ["[g]Ampicillin:[/] ức chế tổng hợp thành tế bào; bao phủ [b]GBS[/], [b]Listeria monocytogenes[/], [b]Enterococcus faecalis[/]; liều [y]100–150 mg/kg/ngày[/] chia 2 hoặc 3 lần TM chậm; viêm màng não xác định: [y]200–300 mg/kg/ngày[/].",
   "[g]Gentamicin:[/] diệt khuẩn phụ thuộc nồng độ qua ức chế ribosome [y]30S[/]; diệt mạnh trực khuẩn Gram âm đường ruột ([b]E. coli, Klebsiella[/]).",
   "[b]Hiệp đồng:[/] Ampicillin phá thành tế bào, mở đường cho Gentamicin thâm nhập ồ ạt vào nội bào diệt sạch vi khuẩn."],
  "Hai thuốc bổ sung phổ cho nhau: Ampicillin lo Gram dương và Listeria, Gentamicin lo Gram âm, đồng thời tăng hiệu quả diệt.",
  "PED-16 RELEASE v1, phần 5.1")

B("PED16-B5-03", "B5", 2,
  "[b]Gentamicin sơ sinh liều mở rộng khoảng cách:[/] [y]liều[/], [y]khoảng cách theo tuổi thai[/], [y]nồng độ đáy[/] và vì sao bỏ cách 2.5 mg/kg mỗi 12 giờ?",
  ["Liều [y]4.0 đến 5.0 mg/kg[/] truyền TM chậm trong [y]30 phút[/].",
   "Khoảng cách: đủ tháng [y]≥ 37 tuần[/] → mỗi [y]24 giờ[/]; non [y]30–36 tuần[/] → mỗi [y]36 giờ[/]; cực non [y]< 30 tuần[/] → mỗi [y]48 giờ[/].",
   "Nồng độ đáy lấy ngay trước cữ thứ hai phải [y]< 1.0–2.0 µg/mL[/] để bảo vệ ốc tai và cầu thận.",
   "Chia nhỏ [y]2.5 mg/kg mỗi 12 giờ[/] là lạc hậu và nguy hiểm vì sơ sinh có thể tích phân bố lớn ([y]0.45–0.55 L/kg[/]) nhưng GFR thấp, thải trừ chậm → tích lũy ở tai trong và thận."],
  "Liều đơn cao tận dụng diệt khuẩn phụ thuộc nồng độ và cho thận thời gian đào thải; trẻ càng non khoảng cách càng dài.",
  "PED-16 RELEASE v1, phần 5.1 (Gentamicin)")

B("PED16-B5-04", "B5", 2,
  "Vì sao [r]TUYỆT ĐỐI CẤM Ceftriaxone[/] ở trẻ sơ sinh? Nêu [y]2 cơ chế[/].",
  ["[r]Vàng da nhân não (Kernicterus):[/] Ceftriaxone gắn mạnh [b]Albumin[/], cạnh tranh và đẩy [b]Bilirubin gián tiếp[/] ra dạng tự do → ngấm qua hàng rào máu não, hoại tử nhân xám đáy não.",
   "[r]Kết tủa muối Canxi-Ceftriaxone:[/] tạo kết tủa với ion [b]Ca2+[/] trong máu → sỏi bùn mật, tắc mao mạch phổi, suy thận cấp, có thể tử vong."],
  "Cả hai cơ chế đều chết người và khó lường nên được xếp chống chỉ định tuyệt đối; thay bằng Ampicillin + Gentamicin.",
  "PED-16 RELEASE v1, phần 5.1 và Checkpoint 3")

B("PED16-B5-05", "B5", 2,
  "Vì sao [r]tránh Cefotaxime[/] làm kháng sinh kinh nghiệm đầu tay, và [y]2 trường hợp[/] mới được dùng?",
  ["Nghiên cứu [b]Clark RH[/] trên hơn [y]48.000[/] trẻ NICU: Ampicillin + Cefotaxime có [r]tử vong cao gấp 1.5 lần[/] ([y]RR = 1.5, 95% CI 1.1–2.0[/]) so với Ampicillin + Gentamicin.",
   "Làm bùng phát Gram âm tiết [b]ESBL[/] và tăng nguy cơ nhiễm [b]Candida[/] xâm lấn gấp [y]3 lần[/].",
   "[g]Chỉ dùng khi:[/] (1) nghi hoặc xác định [b]viêm màng não mủ do Gram âm[/] (Aminoglycoside thấm màng não kém); hoặc (2) [b]suy thận nặng[/] không dùng được Gentamicin."],
  "Cefotaxime chọn lọc vi khuẩn kháng thuốc, nên chỉ giữ cho các chỉ định đặc biệt.",
  "PED-16 RELEASE v1, phần 5.1; Clark 2006")

B("PED16-B5-06", "B5", 2,
  "[b]Kháng sinh kinh nghiệm cho LOS (≥ 72 giờ):[/] [y]3 nhóm thuốc[/] và [y]liều[/] từng thuốc?",
  ["[b]Gram dương:[/] [g]Oxacillin/Nafcillin[/] [y]100–150 mg/kg/ngày[/] chia mỗi 6–8 giờ (nếu tỷ lệ MRSA thấp); hoặc [g]Vancomycin[/] [y]10–15 mg/kg[/] mỗi 8–12–18 giờ, nồng độ đáy [y]10–15 µg/mL[/] (viêm màng não [y]15–20 µg/mL[/]); Vancomycin là đầu tay khi nghi CoNS hoặc MRSA ở trẻ lưu catheter trung tâm.",
   "[b]Gram âm:[/] [g]Amikacin[/] [y]15 mg/kg[/] mỗi 24h hoặc [g]Gentamicin[/] [y]4–5 mg/kg[/]; hoặc [g]Meropenem[/] [y]20–40 mg/kg[/] mỗi 8–12 giờ nếu sốc nặng hoặc nghi ESBL (Klebsiella, Pseudomonas).",
   "[b]Kháng nấm:[/] [g]Fluconazole[/] (tấn công [y]12 mg/kg[/], duy trì [y]6 mg/kg/ngày[/]) hoặc [g]Amphotericin B[/] nếu trẻ cực non [y]< 1000g[/] dùng kháng sinh phổ rộng kéo dài kèm giảm tiểu cầu dai dẳng."],
  "LOS là vi khuẩn bệnh viện qua catheter nên phải phủ CoNS/MRSA, Gram âm đa kháng, và nấm ở nhóm nguy cơ.",
  "PED-16 RELEASE v1, phần 5.2")

B("PED16-B5-07", "B5", 2,
  "Quy tắc [b]Rule-Out Sepsis[/] ở [y]36–48 giờ[/]: [y]3 tiêu chuẩn[/], [g]hành động[/] và [b]bằng chứng[/] hỗ trợ?",
  ["Nghiên cứu [b]SCOUT[/]: hơn [y]95%[/] mẫu cấy dương tính thật được máy phát hiện trong [y]24–36 giờ[/] đầu nuôi cấy.",
   "[y]3 tiêu chuẩn:[/] (1) cấy máu sơ bộ sau 36–48 giờ [g]âm tính[/]; (2) trẻ hoàn toàn khỏe, bú tốt, không suy hô hấp hay rối loạn thân nhiệt; (3) chỉ số viêm động học (CRP lần 2 ở 48h) bình thường.",
   "[g]NGỪNG KHÁNG SINH NGAY LẬP TỨC[/]; không 'tiêm nốt cho đủ 5 hoặc 7 ngày cho yên tâm'."],
  "Dừng sớm bảo tồn hệ vi sinh ruột và giảm tử vong muộn; tiêm bao vây không có lợi mà gây hại.",
  "PED-16 RELEASE v1, phần 5.3; SCOUT 2017")

B("PED16-B5-08", "B5", 2,
  "Bảng liều bỏ túi [g]kháng sinh sơ sinh[/]: Ampicillin, Gentamicin, Vancomycin, Amikacin, Meropenem, Fluconazole?",
  ["[g]Ampicillin EOS:[/] [y]100–150 mg/kg/ngày[/] chia 2–3 lần; viêm màng não [y]200–300 mg/kg/ngày[/].",
   "[g]Gentamicin:[/] [y]4–5 mg/kg[/] mỗi [y]24h[/] (≥ 37w) / [y]36h[/] (30–36w) / [y]48h[/] (< 30w); đáy [y]< 1–2 µg/mL[/].",
   "[g]Vancomycin:[/] [y]10–15 mg/kg[/] mỗi 8–12–18h; đáy [y]10–15 µg/mL[/].",
   "[g]Amikacin:[/] [y]15 mg/kg[/] mỗi 24h.",
   "[g]Meropenem:[/] [y]20–40 mg/kg[/] mỗi 8–12h.",
   "[g]Fluconazole:[/] tấn công [y]12 mg/kg[/], duy trì [y]6 mg/kg/ngày[/]."],
  "Gom các con số liều vào một bảng giúp tra nhanh tại giường; luôn đối chiếu tuổi thai và chức năng thận.",
  "PED-16 RELEASE v1, phần 5.1-5.2", algo=True)

B("PED16-B5-09", "B5", 2,
  "Checklist giường bệnh [y]3 KHÔNG & 3 NÊN[/] khi xử trí nhiễm khuẩn sơ sinh?",
  ["[r]KHÔNG[/] dùng [r]Ceftriaxone[/] cho trẻ sơ sinh (kernicterus, kết tủa Canxi).",
   "[r]KHÔNG[/] dùng [r]CRP cuống rốn[/] hoặc ngưỡng PCT người lớn [y]0.5 ng/mL[/] trong 48 giờ đầu để loại trừ/chẩn đoán.",
   "[r]KHÔNG[/] tiêm kháng sinh 'cho đủ 7 ngày' khi đã đủ tiêu chuẩn [b]Rule-out[/] ở 36–48 giờ.",
   "[g]NÊN[/] cấy máu [y]≥ 1.0 mL[/] trước liều kháng sinh đầu tiên.",
   "[g]NÊN[/] dùng [g]Ampicillin + Gentamicin[/] cho EOS, chỉnh khoảng cách Gentamicin theo tuổi thai.",
   "[g]NÊN[/] chọc DNT khi cấy máu dương tính hoặc có dấu hiệu thần kinh, và nâng Ampicillin lên [y]200–300 mg/kg/ngày[/] nếu viêm màng não."],
  "Sáu điều này là các lỗi và việc đúng thường gặp nhất, đều bắt nguồn từ cơ chế đã học.",
  "PED-16 RELEASE v1, phần 8 và 12", algo=True)

# ============================ B6 LƯU ĐỒ ============================
B("PED16-B6-01", "B6", 1,
  "Lưu đồ [b]EOS trong 24h đầu[/] cho trẻ [y]≥ 34 tuần[/] có yếu tố nguy cơ mẹ: [y]3 nhánh[/] chính và hành động của mỗi nhánh?",
  ["Yếu tố nguy cơ mẹ: sốt mẹ, vỡ ối [y]> 18h[/], GBS (+).",
   "[r]Bước 0, có dấu hiệu nguy cơ/bệnh lý[/] → cấp cứu hồi sức ngay.",
   "[g]Bước 1, trẻ hoàn toàn khỏe[/] (Kaiser hoặc NICE) với nguy cơ tính toán [y]< 1/1000[/] → theo dõi lâm sàng.",
   "[y]Bước 2, nguy cơ trung gian hoặc nghi ngờ (Equivocal)[/] → cấy máu chuẩn, I/T, hẹn CRP 24h, theo dõi sát, rồi đánh giá lại ở [y]36–48 giờ[/]."],
  "Lưu đồ đi từ cấp cứu đến theo dõi, đảm bảo trẻ bệnh được điều trị ngay trong khi trẻ khỏe không bị dùng kháng sinh oan.",
  "PED-16 RELEASE v1, phần 6")

B("PED16-B6-02", "B6", 2,
  "Nhánh [r]cấp cứu hồi sức[/] trong lưu đồ EOS: [y]dấu hiệu sàng lọc Bước 0[/] và [y]4 hành động[/]?",
  ["Sàng lọc: [r]thở rên? cơn ngừng thở? co giật? sốc, tưới máu kém? hạ thân nhiệt < 36.0 °C? li bì, giảm trương lực cơ?[/]",
   "[g]1.[/] Hỗ trợ hô hấp, thở oxy hoặc [g]CPAP[/].",
   "[g]2.[/] Cấy máu đủ thể tích [y]≥ 1.0 mL[/].",
   "[g]3.[/] Tiêm ngay [g]Ampicillin + Gentamicin[/].",
   "[g]4.[/] Chuyển đơn nguyên [b]NICU[/]."],
  "Thứ tự này đảm bảo cấy máu trước kháng sinh nhưng không để chậm thuốc.",
  "PED-16 RELEASE v1, phần 6 (Bước 0)")

B("PED16-B6-03", "B6", 2,
  "Nhánh [g]trẻ hoàn toàn khỏe, nguy cơ tính toán < 1/1000[/]: [y]4 việc nên/không làm[/]?",
  ["[g]Theo dõi lâm sàng[/], cho bú mẹ hoàn toàn.",
   "Theo dõi sinh hiệu [y]mỗi 4h[/] trong [y]24–48h[/].",
   "[r]TUYỆT ĐỐI KHÔNG dùng kháng sinh[/].",
   "[r]KHÔNG chọc máu xét nghiệm đại trà[/]."],
  "Nhiễm khuẩn ở trẻ khỏe có nguy cơ cực thấp; điều trị thừa gây hại nhiều hơn lợi.",
  "PED-16 RELEASE v1, phần 6 (Bước 1)")

B("PED16-B6-04", "B6", 2,
  "Nhánh [y]nguy cơ trung gian (Equivocal)[/]: [y]5 việc[/] cần làm và [y]2 kết quả[/] khi đánh giá lại ở 36–48 giờ?",
  ["Lấy máu cấy chuẩn [y]≥ 1.0 mL[/]; làm CTM tính [b]I/T[/]; hẹn [b]CRP[/] ở [y]24h[/] tuổi; theo dõi sát tại buồng; cân nhắc [y]tạm hoãn kháng sinh[/] nếu trẻ cải thiện nhanh sau [y]2 giờ[/] đầu.",
   "[g]Cấy máu âm tính + trẻ khỏe + CRP 2 lần < 10 mg/L:[/] [g]NGỪNG KHÁNG SINH[/], cho trẻ về với mẹ xuất viện.",
   "[r]Cấy máu dương tính hoặc lâm sàng nặng:[/] xác định vi khuẩn, [g]LP loại trừ viêm màng não[/], chỉnh kháng sinh theo kháng sinh đồ, điều trị đủ: nhiễm khuẩn huyết [y]7–10 ngày[/], viêm màng não mủ [y]14–21 ngày[/]."],
  "Nhánh trung gian là vùng cần đánh giá lại: thời điểm 36–48 giờ tách trẻ có thể dừng thuốc khỏi trẻ cần điều trị đủ liệu trình.",
  "PED-16 RELEASE v1, phần 6 (Bước 2)")

B("PED16-B6-05", "B6", 2,
  "Cây quyết định nhị phân [y]trẻ ≥ 34 tuần nguy cơ mẹ[/]: [r]có dấu hiệu bệnh lý không?[/] rồi [y]nguy cơ < 1/1000 không?[/]",
  ["[r]CÓ dấu hiệu nguy cơ/bệnh lý[/] → [g]hồi sức + cấy máu ≥ 1.0 mL + Ampicillin + Gentamicin + NICU[/].",
   "KHÔNG, trẻ khỏe và [y]nguy cơ tính toán < 1/1000[/] → [g]theo dõi lâm sàng[/], không kháng sinh, không chọc máu đại trà.",
   "KHÔNG, nhưng nguy cơ trung gian/Equivocal → [y]cấy máu, I/T, CRP 24h, theo dõi sát[/] → [y]đánh giá lại 36–48h[/]: âm tính + khỏe + CRP bình thường → [g]ngừng kháng sinh[/]; dương tính/nặng → [g]LP + điều trị đủ liệu trình[/]."],
  "Hai câu hỏi đầu tiên chia trẻ thành ba nhóm xử trí tương ứng ba mức nguy cơ.",
  "PED-16 RELEASE v1, phần 6", algo=True)

# ============================ B7 IAP & BIẾN CHỨNG ============================
B("PED16-B7-01", "B7", 1,
  "[b]IAP[/] giảm bao nhiêu EOS do GBS, và [y]3 nội dung[/] chính của protocol (chỉ định, phác đồ, hiệu lực)?",
  ["IAP là biện pháp y tế công cộng hiệu quả nhất, giảm hơn [y]80%[/] EOS do GBS.",
   "[b]Chỉ định:[/] 4 nhóm yếu tố.",
   "[g]Phác đồ:[/] Penicillin G (hàng đầu), Ampicillin (thay thế).",
   "[y]Hiệu lực:[/] ít nhất 1 liều trước sinh [y]≥ 4 giờ[/]."],
  "Ngăn GBS lây từ mẹ trước khi trẻ sinh ra là cách phòng bệnh hiệu quả nhất.",
  "PED-16 RELEASE v1, phần 7.1 (ACOG/CDC 2020)")

B("PED16-B7-02", "B7", 2,
  "[y]Chỉ định IAP[/] cho sản phụ khi có [y]bất kỳ một[/] trong những yếu tố nào?",
  ["Cấy ngoáy âm đạo - trực tràng tuần [y]36 0/7 – 37 6/7[/] có [b]GBS dương tính[/].",
   "Tiền sử sinh con lần trước nhiễm khuẩn huyết hoặc viêm màng não do GBS.",
   "Nhiễm khuẩn đường tiểu do GBS trong thai kỳ hiện tại.",
   "Chưa rõ tình trạng GBS nhưng có chuyển dạ sinh non [y]< 37 tuần[/], hoặc vỡ ối kéo dài [y]≥ 18 giờ[/], hoặc sốt chuyển dạ [y]≥ 38.0 °C[/]."],
  "Những yếu tố này đều làm tăng nguy cơ trẻ tiếp xúc GBS nên cần dự phòng ngay.",
  "PED-16 RELEASE v1, phần 7.1")

B("PED16-B7-03", "B7", 2,
  "[g]Phác đồ IAP chuẩn[/]: [y]thuốc hàng đầu, liều đầu, liều duy trì[/] của Penicillin G và thuốc thay thế Ampicillin?",
  ["[g]Penicillin G TM (hàng đầu):[/] liều đầu [y]5 triệu đơn vị[/], sau đó [y]2.5–3.0 triệu đơn vị[/] mỗi [y]4 giờ[/] đến khi sinh.",
   "[g]Ampicillin TM (thay thế):[/] liều đầu [y]2 g[/], sau đó [y]1 g[/] mỗi [y]4 giờ[/] đến khi sinh."],
  "Hai thuốc này đạt nồng độ diệt khuẩn trong nước ối nếu đủ thời gian trước sinh.",
  "PED-16 RELEASE v1, phần 7.1")

B("PED16-B7-04", "B7", 2,
  "Khi nào [y]IAP được coi là đầy đủ[/], và nếu tiêm [y]< 4 giờ[/] thì [r]hệ quả[/] và [g]xử trí[/] trẻ?",
  ["IAP đầy đủ khi sản phụ nhận ít nhất [y]1 liều kháng sinh chuẩn trước sinh ≥ 4 giờ[/].",
   "Nếu tiêm [y]< 4 giờ[/]: [r]IAP không đầy đủ (Inadequate IAP)[/], nồng độ kháng sinh trong nước ối chưa đạt ngưỡng diệt khuẩn.",
   "[g]Xử trí:[/] ghi nhận IAP < 4h là không đầy đủ và theo dõi sát lâm sàng trẻ trong [y]48 giờ[/]."],
  "Chỉ truyền 1–2 giờ trước sinh thì thuốc chưa kịp đạt nồng độ diệt khuẩn trong nước ối.",
  "PED-16 RELEASE v1, phần 7.1 và 8 (bẫy 8)")

B("PED16-B7-05", "B7", 2,
  "[y]3 biến chứng thần kinh dài hạn[/] của nhiễm khuẩn sơ sinh có viêm màng não mủ là gì và [g]xử trí/đặc điểm[/]?",
  ["[b]Viêm não thất mủ và tắc cống não:[/] mủ và mảnh vỡ tế bào bít cống Sylvius hoặc lỗ Luschka/Magendie → [b]não úng thủy tắc nghẽn sau viêm màng não[/], cần [g]phẫu thuật dẫn lưu não thất - ổ bụng (VP Shunt)[/].",
   "[b]Nhuyễn hóa chất trắng quanh não thất (PVL):[/] bão cytokin và thiếu máu cục bộ trong sốc phá hủy tế bào tiền thân thần kinh đệm ít nhánh → [r]bại não thể co cứng[/].",
   "[b]Mất thính lực tiếp nhận:[/] tổn thương ốc tai do độc tố vi khuẩn hoặc tích lũy liều [b]Aminoglycoside[/] nếu không giám sát nồng độ đáy."],
  "Biến chứng là tổn thương mô thần kinh không hồi phục; phòng bằng chẩn đoán sớm và giám sát nồng độ Gentamicin.",
  "PED-16 RELEASE v1, phần 7.2")

# ============================ B8 CẠM BẪY ============================
B("PED16-B8-01", "B8", 1,
  "Liệt kê [y]8 cạm bẫy lâm sàng chết người[/] trong nhiễm khuẩn sơ sinh?",
  ["Đợi [r]sốt cao[/] mới nghĩ đến nhiễm khuẩn huyết.",
   "Dùng [r]CRP máu cuống rốn[/] để quyết định điều trị.",
   "Áp [r]ngưỡng Procalcitonin người lớn[/] (0.5 ng/mL) trong 48h đầu.",
   "Lấy [r]thể tích máu cấy < 0.5 mL[/].",
   "Kê [r]Ceftriaxone[/] cho sơ sinh [y]< 28 ngày[/].",
   "Dùng [r]Cefotaxime[/] thay Gentamicin vì 'sợ độc thận'.",
   "Tiếp tục kháng sinh [y]7–10 ngày[/] khi cấy âm tính và trẻ khỏe.",
   "Cho rằng đã có IAP khi kháng sinh chỉ truyền [y]1–2h[/] trước sinh."],
  "Mỗi cạm bẫy đều xuất phát từ hiểu sai sinh lý hoặc dược lý sơ sinh, nên phải gắn mỗi bẫy với cơ chế của nó.",
  "PED-16 RELEASE v1, phần 8")

B("PED16-B8-02", "B8", 2,
  "Cạm bẫy [r]sốt, CRP cuống rốn, PCT người lớn[/]: [r]cơ chế sai[/] và [g]cách phòng[/]?",
  ["[b]Đợi sốt:[/] điều nhiệt kém, mỡ nâu bị ức chế → nhiễm khuẩn nặng thường [r]hạ thân nhiệt < 36.5 °C[/] hoặc dao động → [g]đo nhiệt hậu môn, coi hạ thân nhiệt là cờ đỏ tối khẩn[/].",
   "[b]CRP cuống rốn:[/] CRP cần [y]24–48h[/] mới đạt đỉnh → [g]không dùng CRP cuống rốn để loại trừ[/].",
   "[b]PCT người lớn:[/] đỉnh sinh lý [y]2–10 ng/mL[/] trong [y]24–36h[/] → chẩn đoán nhầm, thuốc thừa → [g]tra biểu đồ bách phân vị theo giờ tuổi (Chiesa)[/]."],
  "Ba bẫy này đều là sai thời điểm hoặc sai ngưỡng sinh lý.",
  "PED-16 RELEASE v1, phần 8 (bẫy 1-3)")

B("PED16-B8-03", "B8", 2,
  "Cạm bẫy [r]thể tích máu, Ceftriaxone, Cefotaxime[/]: [r]cơ chế sai[/] và [g]cách phòng[/]?",
  ["[b]Máu < 0.5 mL:[/] du khuẩn huyết thường ≤ [y]4 CFU/mL[/] → [r]âm tính giả 40–50%[/] → [g]bắt buộc ≥ 1.0 mL[/] vào chai nhi khoa.",
   "[b]Ceftriaxone < 28 ngày:[/] đẩy Bilirubin tự do gây kernicterus, kết tủa Canxi gây sỏi mật và suy thận cấp → [g]chống chỉ định tuyệt đối, dùng Ampicillin + Gentamicin[/].",
   "[b]Cefotaxime thay Gentamicin:[/] tử vong tăng [y]1.5 lần[/], kích hoạt ESBL → [g]dùng Gentamicin mở rộng khoảng cách 4–5 mg/kg mỗi 24–36–48h[/], an toàn cho thận."],
  "Tránh ba lỗi này bằng quy tắc: đủ máu, cấm Ceftriaxone, Gentamicin liều mở rộng khoảng cách.",
  "PED-16 RELEASE v1, phần 8 (bẫy 4-6)")

B("PED16-B8-04", "B8", 2,
  "Cạm bẫy [r]kéo dài kháng sinh 7-10 ngày[/] và [r]IAP chỉ 1–2 giờ[/]: [r]hậu quả[/] và [g]cách phòng[/]?",
  ["[b]Kéo dài kháng sinh khi cấy âm tính và trẻ khỏe:[/] loạn khuẩn ruột, [r]NEC[/], nấm xâm lấn, kháng thuốc → [g]Rule-out sepsis: ngừng kháng sinh ở 36–48 giờ[/].",
   "[b]IAP chỉ mới 1–2 giờ:[/] cần [y]≥ 4 giờ[/] để đạt nồng độ diệt khuẩn trong nước ối → [g]ghi nhận IAP < 4h là không đầy đủ và theo dõi sát trẻ 48 giờ[/]."],
  "Một bẫy là điều trị thừa, một bẫy là tin dự phòng chưa đủ; cả hai đều tránh được bằng mốc thời gian.",
  "PED-16 RELEASE v1, phần 8 (bẫy 7-8)")

# ============================ B9 CHECKPOINT & CA LÂM SÀNG ============================
B("PED16-B9-01", "B9", 1,
  "Tóm tắt [y]4 Checkpoint[/]: tình huống nào, [r]sai ở đâu[/] và [g]đáp án đúng[/]?",
  ["[b]CP1:[/] trẻ [y]5 ngày[/] NICU sinh non 28 tuần dùng Ampicillin + Gentamicin → [r]sai[/]: là LOS, cần [g]Vancomycin + Amikacin/Meropenem[/].",
   "[b]CP2:[/] CRP cuống rốn [y]1.2 mg/L[/] kết luận không nhiễm trùng → [r]cực kỳ nguy hiểm[/].",
   "[b]CP3:[/] Ceftriaxone [y]80 mg/kg/ngày[/] cho trẻ [y]10 ngày[/] vàng da → [r]chống chỉ định tuyệt đối[/].",
   "[b]CP4:[/] 48 giờ, cấy âm tính, CRP [y]3.5 mg/L[/] → [g]ngừng kháng sinh ngay[/]."],
  "Bốn tình huống tương ứng bốn lỗi kinh điển: nhầm EOS/LOS, tin CRP cuống rốn, Ceftriaxone, không dừng kháng sinh.",
  "PED-16 RELEASE v1, phần 9")

B("PED16-B9-02", "B9", 2,
  "[b]Checkpoint 1[/]: trẻ [y]5 ngày[/] NICU, sinh non [y]28 tuần[/], chướng bụng, tăng ngừng thở, tiểu cầu [y]220.000 → 60.000/mm³[/], đề xuất Ampicillin + Gentamicin. [r]Đúng hay sai[/], phác đồ đúng là gì?",
  ["[r]Không chuẩn xác.[/] Trẻ [y]≥ 72 giờ[/] là [b]LOS[/] với vi khuẩn hàng đầu [b]CoNS (~50%)[/], S. aureus, Gram âm bệnh viện đa kháng ([b]Klebsiella, Pseudomonas[/]).",
   "[g]Phác đồ đúng:[/] [g]Vancomycin[/] phối hợp [g]Amikacin[/] hoặc [g]Meropenem[/], tầm soát ổ nhiễm catheter và rút catheter nếu cần."],
  "Ampicillin vô hiệu với CoNS (kháng Penicillin do sinh Penicillinase và biến đổi PBP).",
  "PED-16 RELEASE v1, Checkpoint 1")

B("PED16-B9-03", "B9", 2,
  "[b]Checkpoint 2[/]: vì sao [r]kết luận 'CRP cuống rốn 1.2 mg/L nên không nhiễm trùng' là sai[/] và [g]cần làm gì[/]?",
  ["CRP do gan sản xuất, cần [y]24–48 giờ[/] mới đỉnh; lúc sinh gần như luôn bình thường (độ nhạy [y]< 30%[/]).",
   "Mẹ sốt, ối vỡ kéo dài, ối hôi là [b]viêm màng ối lâm sàng[/] → [r]Cờ đỏ tuyệt đối[/] theo NICE.",
   "[g]Cần làm:[/] cấy máu [y]≥ 1.0 mL[/], chuyển đơn vị sơ sinh, tiêm [g]Ampicillin + Gentamicin TM[/] ngay, theo dõi sát."],
  "Chậm tiêm kháng sinh vì tin CRP âm tính giả có thể gây tử vong tối cấp.",
  "PED-16 RELEASE v1, Checkpoint 2")

B("PED16-B9-04", "B9", 2,
  "[b]Checkpoint 3[/]: trẻ [y]10 ngày[/] vàng da, viêm phổi, được kê [r]Ceftriaxone 80 mg/kg/ngày[/]. [r]Sai ở đâu[/] và [g]sửa y lệnh[/] thế nào?",
  ["[r]Chống chỉ định tuyệt đối:[/] trẻ [y]< 28 ngày[/] đang vàng da; Ceftriaxone đẩy Bilirubin gián tiếp ra dạng tự do → [r]kernicterus[/]; kết tủa muối với Calci gây bùn mật và suy thận cấp.",
   "[g]Sửa:[/] [g]Ampicillin + Gentamicin[/], hoặc nếu nghi Gram âm kháng thuốc thì [g]Cefotaxime[/] [y]100 mg/kg/ngày chia 2 lần[/] (không đẩy Bilirubin, không kết tủa Calci)."],
  "Cefotaxime là cephalosporin thay thế vì không có hai cơ chế độc của Ceftriaxone.",
  "PED-16 RELEASE v1, Checkpoint 3")

B("PED16-B9-05", "B9", 2,
  "[b]Checkpoint 4[/]: trẻ [y]35 tuần[/], dùng Ampicillin + Gentamicin từ lúc sinh, [y]48 giờ[/] tuổi khỏe, bú tốt, nhịp thở [y]44 l/p[/], cấy âm tính, CRP [y]3.5 mg/L[/]. [g]Làm gì[/] và dựa trên [y]3 tiêu chuẩn[/] nào?",
  ["[g]NGỪNG KHÁNG SINH NGAY LẬP TỨC[/] (Antibiotic Stewardship).",
   "Đủ bộ 3 tiêu chuẩn Rule-out: (1) cấy máu âm tính sau 48h; (2) lâm sàng hoàn toàn khỏe; (3) biomarker (CRP lần 2) bình thường."],
  "Hơn 95% mầm bệnh mọc trong 36–48h đầu; tiếp tục 'cho đủ 7 ngày' không có lợi mà làm tổn thương hệ vi sinh ruột và chọn lọc kháng thuốc.",
  "PED-16 RELEASE v1, Checkpoint 4")

B("PED16-B9-06", "B9", 2,
  "[b]Ca 1[/]: bé trai [y]39 2/7 tuần[/], [y]3300 g[/], mẹ sốt [y]38.5 °C[/], vỡ ối [y]20h[/], không IAP; [y]6 giờ[/] tuổi thở rên, [y]35.8 °C[/], thở [y]68 l/p[/], CRT [y]3.5 s[/], SpO2 [y]88%[/]. [r]Cờ đỏ[/] và [g]xử trí Bundle 1h[/]?",
  ["[r]Cờ đỏ:[/] thở rên, SpO2 88%, hạ thân nhiệt 35.8 °C, CRT 3.5 s, li bì; nguy cơ tiền sản rất cao (sốt mẹ, vỡ ối 20h, không IAP) → [b]EOS thể hô hấp, theo dõi PPHN[/].",
   "[g]Hô hấp và nhiệt:[/] lồng ấp/giường sưởi (nhiệt độ da [y]36.5 °C[/]); [g]nCPAP[/] PEEP [y]5–6 cmH2O[/], FiO2 [y]40–50%[/], SpO2 ≥ [y]92–95%[/].",
   "[g]Xét nghiệm:[/] cấy máu [y]1.5 mL[/] (chlorhexidine 2%) trước kháng sinh; CTM, tiểu cầu, I/T, đường huyết, khí máu, X-quang phổi.",
   "[g]Kháng sinh:[/] Ampicillin [y]50 mg/kg/liều[/] = [y]165 mg[/] mỗi 12h; Gentamicin [y]5 mg/kg[/] = [y]16.5 mg[/] truyền 30 phút mỗi 24h.",
   "[g]Tuần hoàn:[/] bolus NaCl 0.9% [y]10 mL/kg[/] = [y]33 mL[/] trong 30 phút, đánh giá lại CRT và nhịp tim; theo dõi monitor, CRP ở 24h và 48h; GBS mọc → Ampicillin đủ [y]10 ngày[/]."],
  "Kaiser: nguy cơ nền > 15/1000, kết hợp lâm sàng Clinically Ill lên > 30/1000 nên bắt buộc cấy máu và kháng sinh ngay.",
  "PED-16 RELEASE v1, Ca lâm sàng 1")

B("PED16-B9-07", "B9", 2,
  "[b]Ca 2[/]: bé gái [y]27 4/7 tuần[/], [y]14 ngày[/], [y]1050 g[/], lưu [b]PICC[/], tăng ngừng thở, ứ dịch dạ dày, CRT [y]4 s[/], tiểu cầu [y]55.000/mm³[/], ANC [y]900/mm³[/]. [g]Xử trí đầy đủ[/]?",
  ["[b]Chẩn đoán:[/] LOS liên quan catheter trung tâm (CLABSI), sốc nhiễm khuẩn bù trừ; tác nhân hàng đầu [b]CoNS > 50%[/], rồi S. aureus (MRSA), Gram âm bệnh viện, [b]Candida albicans[/].",
   "[g]Hồi sức:[/] nâng CPAP lên [y]6–7 cmH2O[/] hoặc đặt lại nội khí quản; bolus NaCl 0.9% [y]10 mL/kg[/] ([y]10.5 mL[/]) trong [y]20–30 phút[/]; nếu CRT vẫn [y]> 3 giây[/] → [g]Adrenaline 0.05–0.1 mcg/kg/phút[/] hoặc Dopamine.",
   "[g]Cấy:[/] 1 mẫu [y]1.0 mL[/] qua PICC và 1 mẫu [y]1.0 mL[/] tĩnh mạch ngoại vi khác chi; [b]DTP[/]: mẫu PICC mọc trước ngoại vi [y]≥ 2 giờ[/] → khẳng định CLABSI; cấy nước tiểu, cân nhắc LP khi ổn định.",
   "[g]Kháng sinh:[/] [g]Vancomycin[/] [y]15 mg[/] truyền 60 phút mỗi 12h (đáy [y]10–15 µg/mL[/]) + [g]Amikacin[/] [y]15.5 mg[/] mỗi 24h; [g]rút bỏ ngay PICC[/] sau khi có đường truyền thay thế.",
   "[g]Theo dõi:[/] tiểu cầu mỗi 24h; nếu [y]< 30.000/mm³[/] sau Vancomycin 48h → thêm [g]Fluconazole[/] TM; NPO, nuôi dưỡng tĩnh mạch qua đường ngoại vi."],
  "Biofilm không tiệt căn nếu giữ catheter, và tiểu cầu tụt sâu dai dẳng gợi ý nấm xâm lấn.",
  "PED-16 RELEASE v1, Ca lâm sàng 2")

# ============================ B10 TIPS & TÓM TẮT ============================
B("PED16-B10-01", "B10", 1,
  "[y]7 mục[/] trong bảng kiểm an toàn tại buồng bệnh (Ward Round Checklist) cho nhiễm khuẩn sơ sinh?",
  ["[r]Hạ thân nhiệt < 36.5 °C[/] hoặc cơn ngừng thở trên monitor?",
   "Đã đánh giá nguy cơ tiền sản bằng [b]Kaiser Sepsis Calculator[/] hoặc [b]NICE Red Flags[/]?",
   "Máu cấy đã lấy đủ [y]≥ 1.0 mL[/] vào chai nhi khoa?",
   "Kháng sinh kinh nghiệm đúng [g]Ampicillin + Gentamicin[/] (tránh Ceftriaxone)?",
   "Khoảng cách liều Gentamicin đã chỉnh theo tuổi thai?",
   "Đã kiểm tra cấy máu ở [y]36–48 giờ[/] để quyết định Rule-out sepsis?",
   "Nếu nghi viêm màng não: đã chọc DNT và nâng Ampicillin lên [y]200–300 mg/kg[/]?"],
  "Bảng kiểm gom các nút then chốt: nhận diện sớm, cấy đúng, thuốc đúng, dừng đúng.",
  "PED-16 RELEASE v1, phần 12 (Ward Round Checklist)")

B("PED16-B10-02", "B10", 2,
  "Mẹo thực hành: [g]lấy đủ 1.0 mL máu ở trẻ non[/], [g]đo CRT[/] và [r]kiểm tra dịch dạ dày[/]?",
  ["[g]Lấy máu:[/] kim bướm [y]23–25G[/] chọc tĩnh mạch mu bàn tay hoặc tĩnh mạch hiển lớn cổ chân, để máu chảy tự do từng giọt vào xi-lanh vô khuẩn, không kéo pít-tông quá mạnh làm xẹp vỡ mạch.",
   "[g]Đo CRT:[/] dùng đồng hồ bấm giây, ấn lên xương ức đủ [y]5 giây[/] rồi buông và nhìn đồng hồ đếm; đếm nhẩm bằng miệng thường đếm quá nhanh và đánh giá thấp CRT thực.",
   "[r]Dịch dạ dày:[/] trước cữ bú nếu sữa cũ vón cục [y]> 30%[/] thể tích cữ trước hoặc dịch xanh rêu/vàng đậm → ruột giảm nhu động do nhiễm khuẩn huyết hoặc NEC sớm."],
  "Kỹ thuật tốt giúp có đủ máu cấy và phát hiện sớm giảm tưới máu và ruột giảm nhu động.",
  "PED-16 RELEASE v1, phần 11 (mẹo 3, 6, 7)")

B("PED16-B10-03", "B10", 2,
  "Các mẹo lâm sàng khác: [y]ánh sáng khám[/], [b]bàn tay và ống nghe[/], [r]cơn ngừng thở[/], [r]tăng đường huyết[/], đường truyền và tư vấn mẹ?",
  ["Khám dưới [g]ánh sáng tự nhiên hoặc đèn trắng[/], vì ánh sáng vàng che mottling, vàng da sớm, ban xuất huyết.",
   "[b]'Bàn tay vô trùng - Ống nghe sạch':[/] tay nhân viên và màng ống nghe là vật trung gian chính truyền [b]CoNS[/] và [b]Klebsiella[/] gây LOS; sát khuẩn tay bằng cồn, lau màng ống nghe trước khi chạm lồng ấp.",
   "Trẻ non đang ổn định bỗng [r]tăng cơn ngừng thở[/] → nghĩ [b]nhiễm khuẩn huyết[/] trước khi tăng áp lực máy thở.",
   "[r]Đường huyết tăng > 10–12 mmol/L[/] ở trẻ đang truyền dịch đường cố định → đề kháng insulin cấp do cytokin.",
   "Bảo tồn tĩnh mạch ngoại vi; nếu cần truyền kháng sinh kéo dài (Vancomycin gây viêm tĩnh mạch) → đặt [b]PICC[/] sớm trong vô khuẩn.",
   "Tư vấn mẹ: giải thích chiến lược [g]Rule-out sepsis[/]: bảo vệ bé bằng kháng sinh tạm thời [y]48 giờ[/] chờ kết quả, cấy âm tính sẽ dừng thuốc và bú mẹ hoàn toàn."],
  "Các mẹo này đều thực tế và gắn với cơ chế đã học (cytokin, vô khuẩn tay, Biofilm).",
  "PED-16 RELEASE v1, phần 11 (mẹo 1, 2, 4, 8, 9, 10)")

B("PED16-B10-04", "B10", 1,
  "[y]10 điều mang vào ca trực[/] về nhiễm khuẩn sơ sinh sớm và muộn?",
  ["Ranh giới [y]72 giờ[/]: EOS truyền dọc (GBS, E. coli), LOS truyền ngang NICU (CoNS, Gram âm).",
   "[r]Hạ thân nhiệt là cờ đỏ số 1[/] ([y]< 36.5 °C[/]), thân nhiệt dao động là cảnh báo sớm.",
   "Thể tích máu cấy tối thiểu [y]1.0 mL[/]; cấy [y]< 0.5 mL[/] âm tính giả [y]40–50%[/]; cấy máu trước liều kháng sinh đầu tiên.",
   "CRP cần [y]24–48h[/]; không dùng CRP cuống rốn; NPV [y]> 99%[/] khi 2 lần cách 24h đều âm tính.",
   "Cấm áp ngưỡng PCT người lớn [y]0.5 ng/mL[/]; đỉnh sinh lý [y]2–10 ng/mL[/] trong 24–36h.",
   "Kháng sinh EOS: [g]Ampicillin + Gentamicin[/] (hiệp đồng thành tế bào và ribosome).",
   "[r]Cấm Ceftriaxone[/] cho sơ sinh: kernicterus và kết tủa Calci.",
   "Gentamicin [y]4–5 mg/kg[/] mỗi [y]24h / 36h / 48h[/] theo tuổi thai; đáy [y]< 1–2 µg/mL[/].",
   "Rule-out ở [y]36–48 giờ[/]: cấy âm + khỏe + CRP bình thường → [g]ngừng kháng sinh ngay[/].",
   "IAP có hiệu lực khi Penicillin G hoặc Ampicillin TM cho mẹ [y]≥ 4 giờ[/] trước sinh."],
  "Đây là mười điểm lõi gom toàn bài; thuộc chúng là đủ để xử trí an toàn tại buồng bệnh.",
  "PED-16 RELEASE v1, phần 12")

# ============================ CLOZE (thẻ nhắc phụ, giữ lịch sử ôn) ============================
C("PED16-B1-C01", "B1", 1789472694572,
  "Nhiễm khuẩn sơ sinh khởi phát sớm (EOS - Early-Onset Sepsis) được định nghĩa là tình trạng nhiễm khuẩn huyết xuất hiện trong vòng {{c1::< 72 giờ đầu đời}}.",
  "Cơ chế chủ yếu là lây truyền dọc (Vertical transmission) từ mẹ sang con trước hoặc trong quá trình chuyển dạ.")
C("PED16-B1-C02", "B1", 1789472694574,
  "Nhiễm khuẩn sơ sinh khởi phát muộn (LOS - Late-Onset Sepsis) được định nghĩa là tình trạng nhiễm khuẩn huyết xuất hiện từ {{c1::≥ 72 giờ tuổi trở lên}}.",
  "Cơ chế chủ yếu là lây truyền ngang (Horizontal transmission) từ môi trường bệnh viện, bàn tay nhân viên y tế hoặc catheter xâm lấn.")
C("PED16-B0-C03", "B0", 1789472694580,
  "Tỷ lệ tế bào hạt non trên tổng số bạch cầu hạt trung tính (Tỷ lệ I/T) đạt ngưỡng {{c1::≥ 0.20}} là dấu hiệu gợi ý tủy xương đang bị kích thích mạnh giải phóng tế bào non do nhiễm trùng.",
  "I/T = (Bạch cầu đũa + Tiền tủy bào + Tủy bào) / Tổng bạch cầu hạt trung tính.")
C("PED16-B0-C04", "B0", 1789472694582,
  "Chiến lược 'Rule-Out Sepsis' cho phép bác sĩ ngừng kháng sinh an toàn ở thời điểm {{c1::36 đến 48 giờ sau sinh}} nếu cấy máu âm tính và trẻ hoàn toàn khỏe mạnh.",
  "Dừng kháng sinh sớm giúp bảo tồn hệ vi sinh đường ruột.")
C("PED16-B0-C05", "B0", 1789472694584,
  "Dấu hiệu thân nhiệt báo động đỏ cảnh báo nhiễm khuẩn huyết tối nguy hiểm ở trẻ sơ sinh là {{c1::Hạ thân nhiệt (< 36.0 °C)}} không đáp ứng với ủ ấm.",
  "Trẻ sơ sinh điều nhiệt kém và mô mỡ nâu bị ức chế bởi độc tố vi khuẩn.")
C("PED16-B0-C06", "B0", 1789472694586,
  "Cơn ngừng thở (Apnea) bệnh lý ở trẻ sơ sinh nghi ngờ nhiễm khuẩn huyết được định nghĩa khi thời gian ngừng thở kéo dài {{c1::> 15–20 giây}}, hoặc bất kỳ thời lượng nào có kèm theo tím tái hoặc nhịp tim chậm.",
  "Box đỏ cấp cứu sơ sinh.")
C("PED16-B0-C07", "B0", 1789472694588,
  "Thời gian đổ đầy mao mạch (CRT) ở xương ức kéo dài {{c1::> 3 giây}} là chỉ số lâm sàng chỉ điểm rối loạn tưới máu mô và sốc sơ sinh.",
  "Dùng đồng hồ bấm giây, ấn ngón tay lên xương ức đủ 5 giây rồi buông.")
C("PED16-B1-C08", "B1", 1789472694592,
  "Hơn {{c1::85%}} các ca Nhiễm khuẩn sơ sinh khởi phát sớm (EOS) xuất hiện triệu chứng lâm sàng ngay trong vòng 24 giờ đầu sau sinh.",
  "Thai nhi hít và nuốt nước ối nhiễm khuẩn.")
C("PED16-B1-C09", "B1", 1789472694594,
  "Hai tác nhân vi khuẩn hàng đầu gây Nhiễm khuẩn sơ sinh khởi phát sớm (EOS) là {{c1::Liên cầu nhóm B (GBS ~40%) và Escherichia coli (~30%)}}.",
  "Kế tiếp là Listeria monocytogenes.")
C("PED16-B1-C10", "B1", 1789472694596,
  "Tác nhân vi khuẩn hàng đầu gây Nhiễm khuẩn sơ sinh khởi phát muộn (LOS) tại NICU là {{c1::Tụ cầu âm tính Coagulase (CoNS)}} chiếm tới ~50% trường hợp.",
  "Vi khuẩn thường trú trên da, bám catheter và tạo màng Biofilm.")
C("PED16-B1-C11", "B1", 1789472694598,
  "Đường lây truyền Listeria monocytogenes từ mẹ sang thai nhi trong EOS là đường {{c1::qua máu qua bánh nhau}}.",
  "Truyền qua đường máu từ mẹ qua bánh nhau là con đường kinh điển của Listeria.")
C("PED16-B3-C12", "B3", 1789472694600,
  "Theo NICE NG195, khi trẻ sơ sinh có BẤT KỲ MỘT dấu hiệu 'Cờ đỏ' (Red Flag), bác sĩ bắt buộc phải lấy máu cấy và tiêm kháng sinh tĩnh mạch trong vòng {{c1::60 phút}}.",
  "Chỉ cần 1 Cờ đỏ là đủ chỉ định.")
C("PED16-B3-C13", "B3", 1789472694602,
  "Theo NICE NG195, nhóm yếu tố nguy cơ không phải cờ đỏ (Non-Red Flags) cần {{c1::từ 2 yếu tố trở lên, hoặc 1 yếu tố kèm triệu chứng lâm sàng}} mới can thiệp.",
  "Cấy máu và dùng kháng sinh khi đạt ngưỡng này.")
C("PED16-B2-C14", "B2", 1789472694604,
  "Nồng độ các thành phần Bổ thể (C3, C4, C5b-9) trong huyết thanh của trẻ sơ sinh chỉ bằng khoảng {{c1::50%}} so với người trưởng thành.",
  "Làm giảm opsonin hóa vi khuẩn có vỏ bọc.")
C("PED16-B2-C15", "B2", 1789472694606,
  "Kho dự trữ bạch cầu trung tính tại tủy xương (Neutrophil Storage Pool) của trẻ sơ sinh chỉ bằng {{c1::20–30%}} người lớn.",
  "Hóa ứng động kém, cạn nhanh dẫn đến giảm bạch cầu hạt khi nhiễm trùng.")
C("PED16-B2-C16", "B2", 1789472694608,
  "IgG bảo vệ trẻ sơ sinh phụ thuộc vào IgG mẹ truyền qua nhau thai trong {{c1::3 tháng cuối thai kỳ}}.",
  "Trẻ đẻ non < 32 tuần hầu như không có kháng thể mẹ.")
C("PED16-B2-C17", "B2", 1789472694610,
  "Độc tố Hemolysin/Cytolysin của GBS gắn vào biểu mô phế nang typ II làm ly giải tế bào và gây {{c1::ngừng sản xuất Surfactant}}.",
  "Phospholipase vi khuẩn và protein huyết tương rỉ viêm còn bất hoạt Surfactant nội sinh.")
C("PED16-B2-C18", "B2", 1789472694612,
  "Co thắt dữ dội tiểu động mạch phổi do GBS dẫn đến biến chứng {{c1::Tăng áp động mạch phổi tồn tại ở trẻ sơ sinh (PPHN)}}.",
  "Xẹp phế nang, toan hóa, thiếu oxy kích thích Endothelin-1; tạo shunt Phải - Trái qua PDA và PFO.")
C("PED16-B2-C19", "B2", 1789472694614,
  "Kháng nguyên vỏ K1 của E. coli có cấu trúc là {{c1::acid polysialic giống phân tử kết dính thần kinh NCAM của người}}.",
  "Ngụy trang phân tử giúp vi khuẩn không bị opsonin hóa và duy trì du khuẩn huyết.")
C("PED16-B2-C20", "B2", 1789472694616,
  "Protein OmpA của E. coli K1 gắn thụ thể gp96 trên nội mô mao mạch não, kích hoạt quá trình {{c1::nhập bào vượt qua hàng rào máu não}} vào khoang dưới nhện.",
  "Nhập bào qua trung gian thụ thể (Receptor-mediated endocytosis).")
C("PED16-B2-C21", "B2", 1789472694618,
  "CoNS bám catheter và tiết lớp chất nền ngoại bào dạng nhầy giàu polysaccharide gọi là {{c1::Biofilm}}.",
  "Biofilm ngăn kháng sinh khuếch tán và vô hiệu hóa thực bào của bạch cầu trung tính.")
C("PED16-B2-C22", "B2", 1789472694620,
  "Lipid A của LPS vi khuẩn Gram âm liên kết với phức hợp thụ thể {{c1::TLR4 / MD-2 / CD14}} trên đại thực bào để kích hoạt bão cytokin.",
  "Hoạt hóa NF-kappa B giải phóng TNF-alpha, IL-1beta, IL-6, PAF.")
C("PED16-B2-C23", "B2", 1789472694622,
  "Enzym iNOS được cytokin kích hoạt trong sốc nhiễm trùng sơ sinh sản sinh quá mức {{c1::Nitric Oxide (NO)}} gây giãn mạch toàn thân.",
  "Làm sụp đổ sức cản mạch máu hệ thống (SVR).")
C("PED16-B3-C24", "B3", 1789472694624,
  "Nguồn sinh nhiệt chính của trẻ sơ sinh là mô mỡ nâu thông qua protein không bắt cặp {{c1::UCP-1}}.",
  "Độc tố vi khuẩn và cytokin ức chế chuyển hóa mỡ nâu khiến trẻ không sốt được mà hạ thân nhiệt.")
C("PED16-B3-C25", "B3", 1789472694626,
  "Năm biến số tiền sản nhập vào Kaiser Sepsis Calculator gồm: {{c1::tỷ lệ hiện mắc nền, tuổi thai, thân nhiệt cao nhất của mẹ, thời gian vỡ ối, tình trạng GBS mẹ và loại kháng sinh IAP}}.",
  "Từ các biến này máy tính nguy cơ nền trước sinh.")
C("PED16-B10-C26", "B10", 1789472694630,
  "Ở trẻ sơ sinh nhiễm khuẩn huyết, ruột giảm nhu động thường biểu hiện sớm qua ứ đọng dịch sữa cũ trong dạ dày {{c1::> 30%}} thể tích cữ bú trước.",
  "Hoặc dịch dạ dày màu xanh rêu/vàng đậm.")
C("PED16-B10-C27", "B10", 1789472694632,
  "Tăng đường huyết (> 10–12 mmol/L) đột ngột ở trẻ đang truyền dịch ổn định là dấu hiệu của {{c1::đề kháng Insulin cấp tính do cytokin viêm}} trong nhiễm khuẩn huyết.",
  "Phóng thích cytokin viêm trong nhiễm khuẩn huyết.")
C("PED16-B4-C28", "B4", 1789472694634,
  "Thể tích máu cấy tối thiểu bắt buộc phải lấy ở trẻ sơ sinh để tránh âm tính giả là {{c1::1.0 mL máu toàn phần}}.",
  "Lấy 0.5 mL chỉ đạt độ nhạy 50–60%; du khuẩn huyết nồng độ thấp ≤ 4 CFU/mL.")
C("PED16-B4-C29", "B4", 1789472694636,
  "CRP bắt đầu tăng sau 6–8 giờ kể từ khi nhiễm trùng và đạt đỉnh sau {{c1::24 đến 48 giờ}}.",
  "Gan cần thời gian nhận tín hiệu IL-6 để tổng hợp CRP.")
C("PED16-B4-C30", "B4", 1789472694638,
  "CRP lấy từ máu cuống rốn hoặc lúc 0–2 giờ tuổi có độ nhạy {{c1::< 30%}}, không có giá trị loại trừ nhiễm khuẩn sơ sinh.",
  "Trẻ nhiễm GBS tối cấp lúc mới sinh vẫn có CRP bình thường.")
C("PED16-B4-C31", "B4", 1789472694642,
  "Ở trẻ sơ sinh khỏe, Procalcitonin có đỉnh tăng vọt sinh lý đạt {{c1::2 đến 10 ng/mL trong vòng 24–36 giờ đầu đời}}.",
  "Không áp ngưỡng người lớn 0.5 ng/mL trong 48 giờ đầu.")
C("PED16-B4-C32", "B4", 1789472694644,
  "ANC giảm xuống mức {{c1::< 1000 / mm³}} ở trẻ sơ sinh là dấu hiệu tiên lượng xấu, cảnh báo nguy cơ tử vong cao.",
  "Kho dự trữ bạch cầu tủy xương đã cạn kiệt.")
C("PED16-B4-C33", "B4", 1789472694646,
  "Số lượng bạch cầu DNT ở trẻ sơ sinh đủ tháng bình thường có thể lên tới {{c1::≤ 20–30 tế bào / mm³}}.",
  "Ở trẻ đẻ non có thể lên tới 30–40 tế bào/mm³.")
C("PED16-B4-C34", "B4", 1789472694648,
  "Protein trong DNT của trẻ sơ sinh bình thường dao động từ {{c1::0.8 đến 1.5 g/L}} do hàng rào máu não còn lỏng lẻo.",
  "Tính thấm hàng rào máu não sơ sinh cao.")
C("PED16-B5-C35", "B5", 1789472694652,
  "Phác đồ kháng sinh kinh nghiệm đầu tay cho EOS là phối hợp hiệp đồng {{c1::Ampicillin và Gentamicin}}.",
  "Ampicillin bao phủ GBS và Listeria; Gentamicin diệt E. coli và trực khuẩn Gram âm.")
C("PED16-B5-C36", "B5", 1789472694654,
  "Liều Gentamicin sơ sinh theo phác đồ mở rộng khoảng cách là {{c1::4.0 đến 5.0 mg/kg tiêm truyền tĩnh mạch chậm trong 30 phút}}.",
  "Liều duy nhất hàng ngày / mở rộng khoảng cách.")
C("PED16-B5-C37", "B5", 1789472694656,
  "Khoảng cách giữa các liều Gentamicin ở trẻ đủ tháng (≥ 37 tuần) là {{c1::mỗi 24 giờ}}.",
  "Trẻ 30–36 tuần mỗi 36 giờ; trẻ < 30 tuần mỗi 48 giờ.")
C("PED16-B5-C38", "B5", 1789472694658,
  "Nồng độ đáy của Gentamicin lấy ngay trước cữ tiêm thứ hai phải đạt {{c1::< 1.0 đến 2.0 µg/mL}}.",
  "Chống độc tính trên ốc tai và cầu thận.")
C("PED16-B5-C39", "B5", 1789472694660,
  "Ceftriaxone bị chống chỉ định tuyệt đối ở trẻ sơ sinh vì đẩy Bilirubin tự do gây {{c1::Vàng da nhân não (Kernicterus)}}.",
  "Còn tạo kết tủa muối Calci-Ceftriaxone gây suy thận cấp.")
C("PED16-B5-C40", "B5", 1789472694662,
  "Clark RH et al. cho thấy Ampicillin + Cefotaxime làm tăng nguy cơ {{c1::tử vong gấp 1.5 lần}} so với Ampicillin + Gentamicin.",
  "RR = 1.5, 95% CI 1.1–2.0; còn làm bùng phát ESBL và tăng nhiễm Candida xâm lấn.")
C("PED16-B5-C41", "B5", 1789472694664,
  "Khi chẩn đoán xác định Viêm màng não mủ sơ sinh, liều Ampicillin tĩnh mạch phải nâng lên {{c1::200 đến 300 mg/kg/ngày}}.",
  "Liều thông thường 100–150 mg/kg/ngày.")
C("PED16-B5-C42", "B5", 1789472694666,
  "Kháng sinh diệt tụ cầu Gram dương hàng đầu cho LOS nghi nhiễm trùng catheter do CoNS là {{c1::Vancomycin}}.",
  "Phối hợp Aminoglycoside (Amikacin) hoặc Carbapenem để bao phủ Gram âm bệnh viện.")
C("PED16-B6-C43", "B6", 1789472694668,
  "Thời gian điều trị kháng sinh cho nhiễm khuẩn huyết sơ sinh có cấy máu dương tính, không viêm màng não, là {{c1::7 đến 10 ngày}}.",
  "Viêm màng não mủ cần 14–21 ngày.")
C("PED16-B2-C44", "B2", 1789472694672,
  "Thể tích dịch tinh thể đẳng trương bolus ban đầu trong Sepsis Bundle 1h sơ sinh là {{c1::10 đến 20 mL/kg truyền tĩnh mạch trong 20–30 phút}}.",
  "Tránh truyền quá mức > 40–60 mL/kg vì cơ tim sơ sinh dễ quá tải thể tích.")
C("PED16-B2-C45", "B2", 1789472694674,
  "Nếu sau bolus 10–20 mL/kg mà CRT vẫn > 3 giây, thuốc vận mạch bắt đầu sớm là {{c1::Adrenaline (0.05–0.1 mcg/kg/phút) hoặc Dopamine}}.",
  "Ca lâm sàng 2: dùng Adrenaline liều thấp khi CRT vẫn > 3 giây sau bolus.")
C("PED16-B7-C46", "B7", 1789472694676,
  "Tầm soát GBS bằng ngoáy âm đạo - trực tràng theo ACOG/CDC ở tuổi thai {{c1::36 0/7 đến 37 6/7 tuần}}.",
  "Kết quả GBS dương tính là chỉ định IAP.")
C("PED16-B7-C47", "B7", 1789472694678,
  "IAP được coi là đầy đủ khi sản phụ nhận ít nhất 1 liều kháng sinh chuẩn trước sinh {{c1::≥ 4 giờ}}.",
  "Tiêm < 4 giờ: IAP không đầy đủ (Inadequate IAP).")
C("PED16-B7-C48", "B7", 1789472694682,
  "Biến chứng tắc nghẽn dịch não tủy sau viêm màng não mủ sơ sinh là {{c1::Não úng thủy tắc nghẽn (Post-meningitic Hydrocephalus)}}.",
  "Cần phẫu thuật dẫn lưu não thất - ổ bụng (VP Shunt).")
C("PED16-B7-C49", "B7", 1789472694684,
  "Tổn thương chất trắng quanh não thất do bão cytokin và thiếu máu trong sốc nhiễm trùng sơ sinh gọi là {{c1::Nhuyễn hóa chất trắng quanh não thất (PVL)}}.",
  "Để lại di chứng bại não thể co cứng.")
C("PED16-B9-C50", "B9", 1789472694710,
  "Ở trẻ 3.3 kg bị EOS, liều Ampicillin khởi đầu là {{c1::165 mg tiêm tĩnh mạch chậm mỗi 12 giờ (50 mg/kg/liều)}}.",
  "Ca lâm sàng 1; Gentamicin 16.5 mg (5 mg/kg) mỗi 24 giờ.")
C("PED16-B9-C51", "B9", 1789472694712,
  "Ở trẻ cực non 1050 g bị LOS do PICC, liều Vancomycin khởi đầu là {{c1::15 mg truyền tĩnh mạch chậm trong 60 phút mỗi 12 giờ}}.",
  "Ca lâm sàng 2; 1050 g × 15 mg/kg = 15 mg; đáy mục tiêu 10–15 µg/mL.")
C("PED16-B10-C52", "B10", 1789472694726,
  "Khi đo CRT ở trẻ sơ sinh, ấn ngón tay lên xương ức đủ {{c1::5 giây}} rồi buông ra và nhìn đồng hồ để đếm.",
  "Đếm nhẩm bằng miệng thường đếm quá nhanh và đánh giá thấp CRT.")
C("PED16-B4-C53", "B4", 1789472694756,
  "Mẫu máu qua catheter mọc khuẩn trước mẫu ngoại vi từ {{c1::≥ 2 giờ}} (DTP) khẳng định chẩn đoán nhiễm khuẩn liên quan catheter (CLABSI).",
  "Ca lâm sàng 2.")
C("PED16-B3-C54", "B3", 1789472694764,
  "Ban xuất huyết hoại tử da hoặc chảy máu rỉ rả chân kim tiêm ở trẻ nhiễm khuẩn huyết cảnh báo {{c1::Đông máu nội mạch rải rác (DIC)}}.",
  "Triệu chứng muộn/nguy kịch của hệ huyết học - chuyển hóa.")
