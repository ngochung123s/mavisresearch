# -*- coding: utf-8 -*-
import json
from pathlib import Path

ROOT = Path(__file__).parent
DATE = "2026-07-13"
STEM = "Semen_Analysis_Male_Infertility"
OUT = ROOT / f"{STEM}_slider3636_{DATE}.deck.json"
SRC = "Nguồn chính: WHO semen manual 6th ed 2021; AUA/ASRM Male Infertility Guideline amended 2024 PMID 39145501; EAU Sexual and Reproductive Health Guideline 2026."
slides = []


def note(action, why, risk="", src=SRC):
    text = f"Làm gì? {action}\nTại sao? {why}"
    if risk:
        text += f"\nNếu bỏ qua/làm sai? {risk}"
    if src:
        text += f"\n{src}"
    return text


def s(kind, **kw):
    d = {"type": kind}
    d.update(kw)
    slides.append(d)
    return d


def title(title, subtitle):
    s("title", variant="split_dark", title=title, subtitle=subtitle,
      author="Bác sĩ Ngọc Hưng", specialty="Hỗ trợ sinh sản / Nam khoa / Labo ART", date=DATE,
      note=note("Đặt thông điệp trung tâm ngay từ đầu.", "Người học cần hiểu tinh dịch đồ là snapshot chuẩn hóa, không phải xét nghiệm đậu/rớt fertility.", "Nếu mở bài bằng các cutoff, học viên dễ diễn giải như fertile/infertile."))


def outline(chapters):
    s("outline", variant="numbered", title="Bản đồ bài học", chapters=chapters,
      note=note("Dẫn người học đi từ mẫu xét nghiệm đến quyết định ART.", "Trình tự này buộc kiểm tra tiền phân tích trước khi đọc số và chọn can thiệp."))


def sec(num, part_title, sub=""):
    s("section", variant="number_block", part_number=str(num), part_title=part_title, part_subtitle=sub,
      note=note(f"Chuyển sang phần {num}: {part_title}.", "Section divider giúp người học reset câu hỏi lâm sàng trước phần mới."))


def c(title_, points, action="Trình bày ý chính.", why="Giúp biến kiến thức thành quyết định lâm sàng.", risk="", src=SRC):
    pts = list(points)
    if why and len(pts) < 6:
        pts.append(f"Ý nghĩa: {why}")
    if risk and len(pts) < 7:
        pts.append(f"Nếu sai, {risk}")
    s("content", variant="bullets", title=title_, points=pts, note=note(action, why, risk, src))


def tw(title_, lt, lp, rt, rp, action="So sánh hai vế.", why="So sánh giúp tránh quyết định theo một tiêu chí đơn độc.", risk="", src=SRC):
    s("two_column", variant="cards", title=title_, left_title=lt, left_points=lp,
      right_title=rt, right_points=rp + [f"Chốt: {why}"], note=note(action, why, risk, src))


def vs(title_, lt, lp, rt, rp, action="Đặt hai lựa chọn cạnh nhau.", why="Giúp chọn nhánh đúng.", risk="", src=SRC):
    s("two_column", variant="vs_compare", title=title_, left_title=lt, left_points=lp,
      right_title=rt, right_points=rp + [f"Chốt: {why}"], note=note(action, why, risk, src))


def flow(title_, steps, action="Đi theo thuật toán.", why="Thuật toán giảm bỏ sót khi ca phức tạp.", risk="", src=SRC):
    nodes = [{"text": t, "type": "start" if i == 0 else "end" if i == len(steps)-1 else "process"} for i, t in enumerate(steps)]
    s("algorithm", variant="linear_flow", title=title_, nodes=nodes, note=note(action, why, risk, src))


def mech(title_, pairs, action="Giải thích chuỗi cơ chế.", why="Hiểu cơ chế giúp đọc pattern đúng.", risk="", src=SRC):
    s("mechanism", variant="horizontal_steps", title=title_,
      steps=[{"title": a, "description": b} for a, b in pairs],
      outcome=f"Ý nghĩa lâm sàng: {why}", note=note(action, why, risk, src))


def checklist(title_, items, action="Dùng checklist tại phòng khám/labo.", why="Checklist giảm lỗi tiền phân tích và diễn giải quá mức.", risk="", src=SRC):
    interp = [{"range": "Cần làm", "label": action}, {"range": "Lý do", "label": why}]
    if risk:
        interp.append({"range": "Nếu bỏ sót", "label": risk})
    s("criteria", variant="score_points", title=title_,
      items=[{"text": i, "points": "✓"} for i in items], interpretation=interp,
      note=note(action, why, risk, src))


def summary(title_, points):
    s("summary", variant="takeaways", title=title_, points=points,
      note=note("Chốt các thông điệp hành động.", "Take-home ngắn giúp người học tự kiểm tra trước khi dùng kết quả SA cho ART."))


def refs(title_, items):
    s("references", variant="numbered", title=title_, refs=items,
      note=note("Ghi nguồn chính đã dùng trong bài.", "Nguồn giúp truy ngược các ngưỡng WHO và khuyến cáo AUA/ASRM, EAU."))


# 0 opening
title("Tinh dịch đồ trong vô sinh nam và ART", "Lấy mẫu đúng, đọc kết quả đúng, không biến reference values thành cutoff")
outline(["Vai trò và sinh lý", "Lấy mẫu - tiền phân tích - QC", "WHO 2021 và thuật ngữ", "Repeat testing và pattern", "ART decisions", "Advanced tests, report và cases"])
sec(0, "Thông điệp trung tâm", "Tinh dịch đồ là snapshot, không phải phép thử đậu/rớt fertility")
c("Một câu phải nhớ", ["Tinh dịch đồ mô tả một mẫu xuất tinh tại một thời điểm", "Không chứng minh người nam fertile hay infertile tuyệt đối", "Phải đọc cùng tiền phân tích, repeat và bối cảnh cặp đôi", "Nhiều thông số bất thường cùng lúc có ý nghĩa hơn một con số lẻ"], "Đặt định nghĩa vận hành cho bài học.", "Nếu hiểu sai vai trò, mọi con số phía sau sẽ bị dùng như cutoff chẩn đoán.", "Bệnh nhân có thể bị tư vấn ART quá mức hoặc trấn an quá mức.")
tw("Tinh dịch đồ đo gì và không đo gì", "Đo được", ["Volume, pH, hóa lỏng", "Concentration và total number", "Motility, vitality, morphology", "Round cells/WBC, agglutination", "Dấu gợi ý tắc/viêm"], "Không tự đo được", ["Fertile/infertile tuyệt đối", "Live birth chắc chắn", "DNA tinh trùng tuyệt đối bình thường", "Nguyên nhân giải phẫu chính xác", "IUI/IVF/ICSI chỉ bằng một chỉ số"], "Tách năng lực xét nghiệm khỏi diễn giải lâm sàng.", "SA là đầu vào của workup, không phải quyết định cuối.")

# 1 role and physiology
sec(1, "Vai trò và sinh lý nguồn gốc tinh dịch", "Biết dịch đến từ đâu để đọc pattern")
mech("Đường đi tinh trùng", [("Tinh hoàn", "sinh tinh"), ("Mào tinh", "trưởng thành và tăng vận động"), ("Ống dẫn tinh", "vận chuyển"), ("Túi tinh", "thể tích, fructose, pH kiềm"), ("Tiền liệt tuyến", "hóa lỏng và enzyme")], "Liên hệ giải phẫu với thông số báo cáo.", "Volume, pH và azoospermia chỉ có nghĩa khi hiểu tuyến phụ và đường dẫn tinh.")
tw("Pattern từ sinh lý", "Sản xuất kém", ["Tinh hoàn nhỏ", "FSH tăng", "Oligo/azoospermia", "Nghĩ NOA/suy sinh tinh"], "Tắc nghẽn", ["Tinh hoàn có thể bình thường", "FSH thường bình thường", "Mào tinh/ống dẫn tinh bất thường", "Nghĩ OA/CBAVD/EOD"], "Dùng pattern thay vì nhìn một con số.", "Cùng là azoospermia nhưng nhánh xử trí khác nhau hoàn toàn.", "Nhầm OA và NOA làm sai genetics, imaging và retrieval planning.")
c("Vì sao volume + pH quan trọng?", ["Low volume có thể do lấy mẫu thiếu hoặc xuất tinh ngược", "pH acid gợi ý thiếu đóng góp túi tinh", "Low-volume acidic azoospermia gợi ý CBAVD/EOD sau khi loại trừ lỗi mẫu", "Cần liên kết sang siêu âm bìu/TRUS ở bài 42 khi đúng chỉ định"], "Đọc đại thể trước khi nhảy sang ART.", "Một thông số đại thể có thể chỉ đường tới giải phẫu tắc nghẽn.", "Bỏ qua collection error có thể chẩn đoán tắc giả.")

# 2 preanalytics
sec(2, "Lấy mẫu và tiền phân tích", "Phần quan trọng nhất của bài")
checklist("Checklist trước khi nhận mẫu", ["Kiêng xuất tinh 2-7 ngày", "Lấy đủ toàn bộ mẫu, nhất là phần đầu", "Dụng cụ/lubricant không độc tinh trùng", "Ghi giờ lấy mẫu và giờ bắt đầu phân tích", "Vận chuyển nhanh, tránh lạnh/nóng", "Hỏi sốt, bệnh cấp, thuốc, testosterone/anabolic steroid"], "Kiểm tra mẫu trước khi đọc số.", "Tiền phân tích sai có thể tạo hypospermia, oligozoospermia hoặc asthenozoospermia giả.", "Kết luận bệnh lý từ mẫu lỗi sẽ kéo theo workup và ART sai.")
c("Kiêng xuất tinh: 2-7 ngày", ["WHO dùng 2-7 ngày để chuẩn hóa điều kiện so sánh", "Kiêng quá ngắn có thể thấp số lượng", "Kiêng quá dài có thể tăng tinh trùng già/kém di động", "Luôn ghi số ngày kiêng trên report"], "Ghi và diễn giải thời gian kiêng.", "Không có thông tin này thì khó so sánh mẫu giữa các lần.")
c("Lấy đủ mẫu: hỏi thẳng", ["Phần đầu mẫu thường giàu tinh trùng", "Mất phần đầu làm volume và count thấp giả", "Report phải ghi giới hạn mẫu", "Thường nên lặp lại đúng chuẩn trước khi chẩn đoán"], "Hỏi bệnh nhân có mất mẫu không.", "Câu hỏi đơn giản này tránh chẩn đoán hypospermia/oligozoospermia giả.")
c("Thời gian phân tích", ["WHO: bắt đầu phân tích lý tưởng trong 30 phút", "Muộn nhất trong 60 phút sau lấy mẫu", "Delay và nhiệt độ không phù hợp làm giảm motility giả", "Mẫu lấy tại nhà phải ghi giờ và điều kiện vận chuyển"], "Ghi delay và nhiệt độ vận chuyển.", "Motility là thông số rất nhạy với tiền phân tích.", "Có thể gắn nhãn asthenozoospermia sai.")
checklist("Khi nào report phải ghi giới hạn?", ["Báo mất một phần mẫu", "Mẫu đến muộn hoặc không rõ giờ lấy", "Dùng dụng cụ/lubricant không phù hợp", "Độ nhớt/hóa lỏng làm khó đếm", "Vừa sốt hoặc dùng thuốc ảnh hưởng sinh tinh", "Labo không đủ điều kiện đọc morphology/advanced test"], "Ghi limitation thay vì che lấp lỗi mẫu.", "Report trung thực giúp bác sĩ không xử trí quá mức.")

# 3 Basic and QC
sec(3, "Basic semen examination và QC", "Đọc đúng từng thông số")
tw("Concentration vs total sperm number", "Concentration", ["Triệu tinh trùng/mL", "Không tính volume", "Dễ bị nhìn đơn độc", "Ví dụ: 16 triệu/mL"], "Total sperm number", ["Tổng số tinh trùng/ejaculate", "Concentration x volume", "Phản ánh toàn mẫu hơn", "WHO 2021: 39 triệu/ejaculate"], "Dạy công thức trước khi đọc mức độ nặng.", "Hai bệnh nhân cùng concentration có thể có total count khác nhau.")
tw("Progressive vs total motility", "Progressive motility", ["Di chuyển tiến tới", "Liên quan thực hành IUI/ART hơn", "WHO 2021 lower 5th centile: 30%"], "Total motility", ["Progressive + non-progressive", "Có thể chỉ rung/động tại chỗ", "WHO 2021 lower 5th centile: 42%"], "Tách di động có ích khỏi chỉ có động đậy.", "Total motility cao nhưng progressive thấp vẫn có ý nghĩa lâm sàng.")
c("Khi motility thấp, cần vitality", ["Vitality phân biệt bất động còn sống với tinh trùng chết", "Motility thấp + vitality còn tốt: nghĩ vấn đề vận động/tiền phân tích", "Motility thấp + vitality thấp: nghĩ necrozoospermia hoặc tổn thương nặng", "WHO 2021 lower 5th centile vitality: 54%"], "Yêu cầu vitality khi motility thấp.", "Không phải mọi tinh trùng bất động đều đã chết.")
tw("Round cells vs leukocytospermia", "Round cells", ["Nhóm hình thái", "Có thể là bạch cầu", "Có thể là tế bào mầm non", "Chưa phải chẩn đoán nhiễm trùng"], "Leukocytospermia", ["Cần xác nhận là bạch cầu", "Đặt trong bối cảnh triệu chứng/nguy cơ", "Mới cân nhắc culture/điều trị", "Tránh overtreatment"], "Không gọi round cells là leukocytes khi chưa xác nhận.", "Giảm culture/kháng sinh không cần thiết.")
tw("Agglutination vs aggregation", "Agglutination", ["Tinh trùng dính với tinh trùng", "Có pattern đầu-đầu/đuôi-đuôi", "Có thể gợi ý ASA trong bối cảnh phù hợp"], "Aggregation", ["Tinh trùng kẹt với nhầy", "Dính mảnh vụn/tế bào khác", "Không thay thế thuật ngữ agglutination"], "Dùng đúng thuật ngữ labo.", "ASA testing không routine ban đầu chỉ vì một báo cáo mơ hồ.")
c("QC labo: bác sĩ cần biết gì?", ["Buồng đếm, pipette và timing phải chuẩn", "Đếm nên có duplicate/đánh giá sai số", "Morphology phụ thuộc nhuộm và người đọc", "CASA hữu ích nhưng không thay thế QC", "Advanced tests cần labo validate threshold"], "Hiểu nguồn sai số của kết quả.", "SA khác labo có thể khác vì phương pháp và QC, không chỉ vì bệnh nhân thay đổi.")

# 4 WHO values
sec(4, "WHO 2021 reference values", "Mốc tham chiếu, không phải cutoff fertile/infertile")
c("Bảng WHO 2021 lower 5th centile", ["Volume: 1.4 mL", "Concentration: 16 triệu/mL", "Total sperm number: 39 triệu/ejaculate", "Total motility: 42%; progressive motility: 30%", "Vitality: 54%; normal morphology: 4%"], "Dạy các mốc thường dùng.", "Cần thuộc số nhưng phải thuộc kèm ý nghĩa đúng.", "Học số mà quên provenance sẽ biến reference value thành cutoff.")
c("Câu cảnh báo bắt buộc", ["WHO 2021 lower fifth-centile reference values là mốc phân bố tham chiếu", "Không phải ranh giới fertile/infertile", "Dưới mốc: tăng xác suất male factor nhưng không vô sinh tuyệt đối", "Trên mốc: không bảo đảm có thai"], "Sửa cách gọi cutoff.", "Reference distribution không đo toàn bộ chức năng sinh sản của cặp đôi.", "Đây là critical miss lớn nhất của bài.")
vs("Dùng đúng vs dùng sai WHO values", "Dùng đúng", ["Chuẩn hóa báo cáo", "Ước lượng mức bất thường", "Quyết định repeat/workup", "Trao đổi với labo/cặp đôi"], "Dùng sai", ["Kết luận fertile/infertile", "Chọn ICSI chỉ bằng morphology", "Bỏ qua tiền phân tích", "Bỏ qua người nữ và cặp đôi"], "Đặt WHO values vào đúng vai trò.", "Mốc tham chiếu hỗ trợ tư duy, không thay thế tư duy.")
c("Morphology 4%: đừng overcall", ["Normal forms lower 5th centile là 4%", "Morphology biến thiên theo phương pháp và người đọc", "Không đại diện trực tiếp cho DNA hoặc khả năng thụ tinh tuyệt đối", "Isolated teratozoospermia không tự động là chỉ định ICSI"], "Giảm diễn giải quá mức morphology.", "Đây là lỗi thường gặp trong ART counseling.", "Bệnh nhân có thể bị chuyển sang ICSI không cần thiết.")

# 5 terminology and repeat
sec(5, "Thuật ngữ, độ biến thiên và repeat testing", "Không phân nhánh khi chẩn đoán chưa chắc")
checklist("Các cặp thuật ngữ dễ nhầm", ["Aspermia khác azoospermia", "Cryptozoospermia khác severe oligozoospermia", "Asthenozoospermia khác necrozoospermia", "Teratozoospermia không đồng nghĩa DNA xấu", "OAT là mô tả nhiều trục bất thường, không phải nguyên nhân"], "Chuẩn hóa từ vựng trước khi tư vấn.", "Dùng sai thuật ngữ làm sai workup và kỳ vọng bệnh nhân.")
c("Vì sao cần repeat?", ["Tinh dịch đồ dao động theo ngày kiêng, sốt, stress, thuốc, độc chất, giấc ngủ", "Một mẫu đơn độc có thể không đại diện baseline", "EAU 2026: ít nhất hai SA liên tiếp nếu baseline bất thường", "AUA/ASRM: đánh giá ban đầu bằng one or more semen analyses"], "Lặp lại mẫu bất thường khi phù hợp.", "Repeat phân biệt bất thường thật với dao động sinh học hoặc lỗi mẫu.")
flow("Azoospermia: xác nhận trước OA/NOA", ["Không thấy tinh trùng trên lam ban đầu", "Kiểm tra tiền phân tích và mẫu lấy đủ", "Ly tâm mẫu, tái huyền phù pellet, soi rare sperm", "Nếu vẫn không thấy: repeat SA", "Sau pellet + repeat mới phân nhánh OA/NOA"], "Không chẩn đoán azoospermia từ một lam ban đầu.", "Pellet/repeat tránh bỏ sót cryptozoospermia và mẫu lỗi.", "Sai ở bước này làm sai toàn bộ genetics, imaging và retrieval.")
c("EAU/AUA chi tiết cần nhớ", ["AUA/ASRM: repeat azoospermia sau ít nhất 1-2 tuần", "EAU: ly tâm khoảng 3.000g trong 15 phút và soi pellet", "EAU mô tả xác nhận bằng hai mẫu sau ly tâm", "Mục tiêu: phân biệt absolute azoospermia với cryptozoospermia"], "Ghi số liệu xác nhận azoospermia.", "Đây là chi tiết an toàn trước khi workup tắc hay suy sinh tinh.")
c("Khi nào không chờ quá lâu?", ["Azoospermia/cryptozoospermia sát chu kỳ ART", "Số lượng cực thấp có nguy cơ mẫu sau không còn tinh trùng", "Trước hóa trị/xạ trị hoặc điều trị độc sinh dục", "Sát ngày chọc hút noãn", "Cần chuẩn bị surgical sperm retrieval"], "Biết ngoại lệ của repeat chậm.", "Không trì hoãn khi kết quả sẽ ảnh hưởng chu kỳ ART hoặc bảo tồn sinh sản.")

# 6 patterns
sec(6, "Diễn giải theo pattern", "Đi từ lỗi mẫu đến nguyên nhân")
flow("Low volume pathway", ["Low volume", "Hỏi lấy đủ mẫu? mất phần đầu?", "Loại trừ xuất tinh ngược khi phù hợp", "Xem pH/fructose", "Low volume + pH acid + azoospermia: nghi CBAVD/EOD", "Khám ống dẫn tinh, CFTR nếu nghi CBAVD, TRUS/siêu âm theo bài 42"], "Đọc low volume theo thứ tự.", "Lỗi lấy mẫu thường gặp hơn tắc hiếm, nhưng pattern acid azoospermia rất quan trọng.", "Nhảy thẳng tới CBAVD/EOD có thể bỏ sót collection error.")
flow("Normal-volume azoospermia", ["Azoospermia đã pellet + repeat", "Volume và pH bình thường", "Khám tinh hoàn/ống dẫn tinh", "FSH/LH/testosterone", "Tinh hoàn nhỏ + FSH cao: nghi NOA", "Tinh hoàn bình thường + FSH bình thường + dấu tắc: nghi OA"], "Phân nhánh OA/NOA bằng pattern.", "Hormone và khám đặt SA vào sinh lý sản xuất hay tắc nghẽn.")
c("Severe oligozoospermia / cryptozoospermia", ["Repeat và loại trừ tiền phân tích", "Hỏi testosterone/anabolic steroid, sốt, thuốc, độc chất", "Đánh giá hormone khi nghi suy sinh tinh", "Nghĩ genetics theo ngưỡng guideline", "Cân nhắc trữ tinh trùng nếu chuẩn bị ART"], "Không xem số lượng rất thấp là ổn định.", "Mẫu sau có thể không còn tinh trùng để dùng ngày OPU.", "Có thể phải hủy chu kỳ hoặc retrieval khẩn cấp.")
c("Y-chromosome microdeletion testing", ["AUA/ASRM 2024: primary infertility kèm azoospermia", "Hoặc sperm concentration <=1 triệu/mL", "Khi có FSH tăng, teo tinh hoàn hoặc chẩn đoán impaired sperm production", "Kết quả ảnh hưởng tư vấn tiên lượng và di truyền"], "Dùng đúng ngưỡng xét nghiệm di truyền.", "Không phải mọi SA bất thường đều cần xét nghiệm Y microdeletion.")
c("Low motility pathway", ["Kiểm tra delay và nhiệt độ vận chuyển", "Hỏi lubricant/condom không phù hợp", "Xem hóa lỏng/độ nhớt", "Làm vitality khi motility thấp", "Chỉ sau đó mới quy asthenozoospermia thật"], "Tìm asthenozoospermia giả trước.", "Motility rất dễ bị preanalytics làm sai.")

# 7 ART decisions
sec(7, "Ý nghĩa đối với natural conception, IUI, IVF và ICSI", "Quyết định ở mức cặp đôi")
checklist("Ngoài SA, quyết định ART cần gì?", ["Tuổi và dự trữ buồng trứng của người nữ", "Thời gian vô sinh", "Vòi tử cung và tử cung", "Số lần thất bại trước", "Số thông số SA bất thường", "Khả năng repeat/trữ tinh trùng", "Năng lực labo và mong muốn cặp đôi"], "Luôn đưa người nữ và cặp đôi vào quyết định.", "Tinh dịch đồ không tồn tại trong chân không.", "Chọn IUI/IVF/ICSI bằng một chỉ số là critical miss.")
c("TMSC dùng để làm gì?", ["TMSC kết hợp volume, concentration và motility", "Gần với số tinh trùng di động có thể dùng hơn concentration đơn độc", "Hữu ích cho tư vấn IUI và lập kế hoạch labo", "Không dạy một cutoff cứng cho IUI/IVF/ICSI trong bài này"], "Dùng TMSC như công cụ tư vấn, không như luật.", "Ngưỡng phụ thuộc nghiên cứu, labo và toàn cảnh cặp đôi.")
vs("IUI/IVF/ICSI: cách nghĩ đúng", "Không làm", ["Không chọn bằng concentration đơn độc", "Không dùng morphology đơn độc để ICSI", "Không bỏ qua tuổi/noãn", "Không bỏ qua repeat và preanalytics"], "Nên làm", ["Xem toàn bộ SA và repeat", "Tính TMSC/post-wash nếu IUI", "Xem tiền sử fertilization failure", "Chuẩn bị backup sperm/retrieval nếu rất thấp"], "Dạy quyết định đa biến.", "ART là can thiệp của cả cặp đôi và labo.")
c("Khi nào chuẩn bị IVF/ICSI hoặc retrieval?", ["Azoospermia đã xác nhận", "Cryptozoospermia hoặc số lượng cực thấp", "OA: PESA/MESA/TESE + ICSI tùy vị trí và nguồn lực", "NOA: micro-TESE + ICSI sau nội tiết/di truyền và tư vấn", "Severe male factor: trữ tinh trùng backup nếu có mẫu"], "Lập kế hoạch ART sớm khi nguy cơ không có tinh trùng.", "Chuẩn bị labo và backup giảm nguy cơ hủy chu kỳ.")
c("Trữ tinh trùng ở số lượng rất thấp", ["Mẫu sau có thể không còn tinh trùng", "Ngày chọc hút noãn có thể không đủ tinh trùng", "Trữ mẫu có tinh trùng giảm nguy cơ hủy chu kỳ", "Không thay thế tìm nguyên nhân nhưng bảo vệ kế hoạch ART"], "Cân nhắc cryopreservation khi có tinh trùng hiếm.", "Đây là hành động ít xâm lấn có thể cứu chu kỳ.")

# 8 advanced tests
sec(8, "Extended / advanced tests", "Chỉ làm khi câu hỏi lâm sàng cụ thể")
tw("SDF: vai trò và giới hạn", "Có thể cân nhắc", ["RPL", "Thất bại ART", "Unexplained infertility chọn lọc", "Theo guideline/labo"], "Không dùng như", ["Screening routine ban đầu", "Cutoff chung cho mọi assay", "Thay thế SA/basic workup", "Quyết định ART đơn độc"], "Đặt sperm DNA fragmentation đúng vị trí.", "Threshold phụ thuộc assay và labo phải validate.")
c("ROS/oxidative stress", ["Đo stress oxy hóa hoặc proxy tùy assay", "Có thể quan tâm khi viêm, varicocele, độc chất hoặc nghiên cứu", "Deep-research chưa xác minh đủ để đưa vào thuật toán routine", "Không dạy như screening ban đầu"], "Không lạm dụng ROS trong bài này.", "Bằng chứng/chuẩn hóa chưa đủ cho routine pathway.")
c("ASA, culture, biochemistry", ["ASA: chọn lọc khi agglutination/bối cảnh phù hợp", "Culture: triệu chứng nhiễm trùng, leukocytes xác nhận, STI/viêm tuyến phụ", "Fructose/zinc/alpha-glucosidase: trả lời câu hỏi tuyến phụ/tắc nghẽn", "Không test nào thay thế khám, hormone, genetics, imaging khi cần"], "Chỉ định xét nghiệm nâng cao theo câu hỏi.", "Test thêm không làm kết quả tự rõ nếu câu hỏi ban đầu sai.")
checklist("Bốn câu trước advanced test", ["Test đo gì?", "Khi nào cân nhắc?", "Không trả lời được gì?", "Kết quả có đổi quản lý không?"], "Dùng bốn câu này trước khi order test.", "Nếu không đổi quản lý, test thường chỉ tăng chi phí và nhiễu.")

# 9 report and cases
sec(9, "Report chuẩn và mini-cases", "Biến kết quả thành hành động")
checklist("Report SA tối thiểu", ["Tiền phân tích: kiêng, giờ lấy, giờ phân tích, lấy đủ/mất mẫu", "Đại thể: volume, liquefaction, viscosity, appearance, pH", "Concentration và total sperm number", "Motility breakdown", "Vitality khi cần", "Morphology và phương pháp", "Round cells/leukocyte confirmation", "Comments: limitation, repeat, clinical correlation"], "Yêu cầu report đủ dữ liệu hành động.", "Thiếu tiền phân tích và comments khiến kết quả khó tin và khó dùng.")
c("Case 1: mất phần đầu mẫu", ["Volume 0,7 mL, concentration thấp", "Bệnh nhân báo phần đầu rơi ra ngoài", "Không kết luận hypospermia/oligozoospermia thật", "Ghi limitation và lặp mẫu đúng chuẩn"], "Xử trí mẫu mất phần đầu.", "Phần đầu giàu tinh trùng nên count/volume có thể thấp giả.")
c("Case 2: mẫu đến sau 2 giờ, trời lạnh", ["Motility thấp", "Nghĩ asthenozoospermia giả", "Cần repeat với vận chuyển đúng", "Không quy bệnh lý vận động từ mẫu delay/lạnh"], "Nhận diện lỗi vận chuyển.", "Delay/nhiệt độ là nguyên nhân giả thường gặp của motility thấp.")
c("Case 3: low-volume acidic azoospermia", ["Volume 0,6 mL, pH acid, mẫu lấy đủ", "Không bỏ qua pellet/repeat nếu chưa xác nhận", "Loại trừ xuất tinh ngược", "Khám ống dẫn tinh, CFTR nếu nghi CBAVD, TRUS/siêu âm theo bài 42"], "Đi theo pathway tắc đoạn xa.", "Pattern này gợi ý thiếu dịch túi tinh hoặc EOD/CBAVD.")
c("Case 4: normal-volume azoospermia + FSH cao", ["Azoospermia đã repeat/pellet", "Volume bình thường, tinh hoàn nhỏ, FSH cao", "Hướng NOA/suy sinh tinh", "Nội tiết, di truyền, tư vấn tiên lượng, cân nhắc micro-TESE + ICSI"], "Tư vấn nhánh NOA.", "Người bệnh cần biết khả năng không tìm được tinh trùng và lựa chọn thay thế.")
c("Case 5: cryptozoospermia", ["Pellet còn vài tinh trùng", "Không xem như 'không có gì để làm'", "Repeat và tìm nguyên nhân", "Trữ tinh trùng nếu có thể", "Chuẩn bị labo ART vì ngày OPU có thể không có tinh trùng"], "Bảo vệ chu kỳ ART khi tinh trùng dao động rất thấp.", "Không chuẩn bị backup có thể dẫn tới hủy chu kỳ hoặc retrieval khẩn cấp.")
c("Case 6: isolated teratozoospermia", ["Morphology thấp đơn độc", "Không tự động ICSI", "Xem repeat, method, TMSC, tiền sử fertilization failure", "Đặt trong tuổi/noãn và chính sách labo"], "Giảm over-treatment theo morphology.", "Morphology đơn độc là bẫy diễn giải rất thường gặp.")
c("Case 7: round cells tăng", ["Không gọi ngay leukocytospermia", "Xác định bạch cầu hay tế bào mầm non", "Culture/điều trị khi có triệu chứng hoặc bối cảnh phù hợp", "Tránh kháng sinh quá mức"], "Xử trí round cells có chọn lọc.", "Round cells là mô tả hình thái, không phải chẩn đoán nhiễm trùng.")
c("Case 8: varicocele + SA bất thường", ["OAT lặp lại và khám có varicocele sờ thấy", "Siêu âm bìu/Doppler hỗ trợ đánh giá theo bài 42", "Không mổ varicocele cận lâm sàng chỉ vì siêu âm giãn nhẹ", "Quyết định theo guideline, triệu chứng và mục tiêu cặp đôi"], "Liên kết SA bất thường với khám và siêu âm đúng chỉ định.", "Điều trị varicocele theo hình ảnh đơn độc có thể over-treatment.")

# 10 critical misses and close
sec(10, "Critical misses", "Sai ở đây thì phải ôn lại dù tổng điểm cao")
checklist("Critical miss checklist", ["Gọi WHO lower reference values là cutoff fertile/infertile", "Chẩn đoán azoospermia mà chưa pellet/repeat", "Bỏ qua lấy mẫu thiếu hoặc delay vận chuyển", "Dùng isolated morphology để chỉ định ICSI tự động", "Dùng SDF/ROS/ASA/culture như screening routine", "Quyết định ART bằng một chỉ số mà không xét toàn cặp đôi"], "Dùng checklist để tự chấm an toàn.", "Các lỗi này gây hại thực hành nhiều hơn quên một con số nhỏ.")
summary("Take-home messages", ["SA là snapshot chuẩn hóa, không phải xét nghiệm đậu/rớt fertility.", "Tiền phân tích đứng trước mọi con số: kiêng 2-7 ngày, lấy đủ mẫu, phân tích 30-60 phút.", "WHO 2021 lower fifth-centile values là mốc tham chiếu, không phải cutoff vô sinh.", "Azoospermia cần pellet + repeat trước OA/NOA.", "Quyết định IUI/IVF/ICSI là quyết định của cả cặp đôi, không phải của một chỉ số."])
refs("Tài liệu tham khảo chính", [
    "WHO laboratory manual for the examination and processing of human semen, 6th ed. 2021. ISBN 9789240030787.",
    "Boitrelle F et al. Sixth edition of the WHO manual: critical review and SWOT analysis. Andrology. 2021. PMID 33528873. DOI 10.1111/andr.12983.",
    "Paffoni A et al. Reference values for human semen analysis. Hum Reprod. 2022. PMID 35849333. DOI 10.1093/humrep/deac161.",
    "Brannigan RE et al. Updates to Male Infertility: AUA/ASRM Guideline (2024). J Urol. 2024. PMID 39145501. DOI 10.1097/JU.0000000000004180.",
    "AUA/ASRM. Diagnosis and Treatment of Infertility in Men: guideline, published 2020; amended 2024.",
    "EAU Guidelines on Sexual and Reproductive Health, chapter Male Infertility. 2026.",
    "Kohn TP et al. Genetic testing for men with NOA or severe oligozoospermia. Fertil Steril. 2019. PMID 31400948."
])

# concise drill slides for active recall and slide count
sec(11, "Drill nhanh", "Tập trả lời như khi đi lâm sàng")
for i, (t, pts, why, risk) in enumerate([
    ("WHO 16 triệu/mL là gì?", ["Lower 5th centile", "Không phải cutoff vô sinh", "Dưới mốc tăng xác suất male factor", "Trên mốc không bảo đảm có thai"], "Sửa critical miss về reference values.", "Dùng sai làm tư vấn fertile/infertile giả."),
    ("Một mẫu azoospermia ban đầu", ["Kiểm tra tiền phân tích", "Ly tâm và soi pellet", "Repeat SA", "Sau đó mới OA/NOA"], "Pellet/repeat tránh bỏ sót cryptozoospermia.", "Workup sai nhánh."),
    ("Motility thấp", ["Xem delay/nhiệt độ", "Xem lubricant/độ nhớt", "Làm vitality", "Repeat nếu mẫu lỗi"], "Motility dễ bị tiền phân tích làm sai.", "Chẩn đoán asthenozoospermia giả."),
    ("Volume thấp", ["Hỏi lấy đủ mẫu", "Hỏi mất phần đầu", "Loại trừ retrograde", "Xem pH/fructose nếu mẫu đáng tin"], "Low volume trước hết là câu hỏi collection.", "Gắn nhãn CBAVD/EOD quá sớm."),
    ("Severe oligo/crypto", ["Repeat", "Tìm thuốc/sốt/testosterone", "Hormone/genetics theo ngưỡng", "Trữ tinh trùng nếu chuẩn bị ART"], "Số lượng rất thấp có thể dao động tới zero.", "Không có tinh trùng ngày OPU."),
    ("Morphology thấp đơn độc", ["Không tự động ICSI", "Xem method/repeat", "Xem fertilization failure", "Xem tuổi/noãn/labo"], "Morphology có biến thiên cao.", "Over-treatment."),
    ("Round cells", ["Không mặc định bạch cầu", "Xác nhận loại tế bào", "Culture khi triệu chứng/leukocytes/nguy cơ", "Tránh kháng sinh quá mức"], "Round cells là mô tả hình thái.", "Overtesting/overtreatment."),
    ("TMSC", ["Volume x concentration x motility", "Hữu ích tư vấn IUI", "Không cutoff cứng trong bài", "Phụ thuộc labo/cặp đôi"], "TMSC tốt hơn concentration đơn độc nhưng không thay quyết định đa biến.", "Chọn ART máy móc."),
], 1):
    c(f"Drill {i}: {t}", pts, "Trả lời ca ngắn theo checklist.", why, risk)


deck = {
    "meta": {"title": "Tinh dịch đồ trong vô sinh nam và ART", "subtitle": "Bài giảng lâm sàng ART", "author": "Bác sĩ Ngọc Hưng", "specialty": "Hỗ trợ sinh sản / Nam khoa", "date": DATE},
    "slides": slides,
}
OUT.write_text(json.dumps(deck, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved {OUT} ({len(slides)} slides)")
