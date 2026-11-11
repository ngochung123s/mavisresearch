# -*- coding: utf-8 -*-
"""
Dữ liệu thẻ Anki chuẩn hóa cho bài SURG-22: Ung Thư Đại Tràng
Rebuild 100% từ barem: SURG-22_Ung_thu_dai_trang_BAREM.md
"""

def _c(hex_col: str, text: str) -> str:
    return f'<span style="color: {hex_col}; font-weight: bold;">{text}</span>'

def R(text: str) -> str:
    return _c("#ff6b6b", text)

def Y(text: str) -> str:
    return _c("#ffd43b", text)

def G(text: str) -> str:
    return _c("#51cf66", text)

def B(text: str) -> str:
    return _c("#74c0fc", text)

def clz(n: int, inner: str) -> str:
    return f"{{{{c{n}::{inner}}}}}"

def basic(cid, section, topic, tier, front, core, ai, barem, tags, red_flag=False, asks=None):
    b_tag = f"Ngoai::SURG-22::{section}"
    t_tag = f"Tier-{tier}"
    all_tags = [b_tag, t_tag] + [f"Ngoai::{t}" for t in tags]
    if red_flag:
        all_tags.append("Ngoai::Co-do")
    
    back = f"🎯 Trả lời cốt lõi:<br>{core}<br><br>💡 Giải thích của AI:<br>{ai}"
    
    res = {
        "id": cid,
        "type": "basic",
        "section": section,
        "topic": topic,
        "tier": tier,
        "front": front,
        "back": back,
        "extra": f"[{barem}]",
        "tags": all_tags,
    }
    if asks:
        res["asks"] = asks
    return res

def algo(cid, section, category, title, core, ai, barem, tags, asks=None):
    front = f"⚡ THUẬT TOÁN QUYẾT ĐỊNH — {G(category)}: {Y(title)}"
    return basic(
        cid, section, f"Thuật toán: {title}", 1,
        front, core, ai, barem, tags + ["Thuat-toan-Quyet-dinh"], asks=asks
    )

def trap(cid, section, topic, front, core, ai, barem, tags, red_flag=False, asks=None):
    prefix = f"🛑 {R('CỜ ĐỎ CẤP CỨU')} — " if red_flag else f"❌ {Y('BẪY LÂM SÀNG')} — "
    full_front = f"{prefix}{front}"
    return basic(
        cid, section, f"Bẫy: {topic}", 1,
        full_front, core, ai, barem, tags + (["Co-do"] if red_flag else ["Bay-lam-sang"]),
        red_flag=red_flag, asks=asks
    )

def redflag(cid, section, topic, front, core, ai, barem, tags, asks=None):
    return trap(cid, section, topic, front, core, ai, barem, tags, red_flag=True, asks=asks)

def cloze(cid, section, topic, text, barem, tags):
    b_tag = f"Ngoai::SURG-22::{section}"
    return {
        "id": cid,
        "type": "cloze",
        "section": section,
        "topic": topic,
        "tier": 1,
        "text": text,
        "extra": f"[{barem}]",
        "tags": [b_tag, "Tier-1"] + [f"Ngoai::{t}" for t in tags],
    }


cards_data = [
    # =========================================================================
    # B0: ĐẠI CƯƠNG & DỊCH TỄ HỌC
    # =========================================================================
    basic(
        "SURG22-B0-01", "B0", "Dịch tễ học toàn cầu 2018", 1,
        f"{B('[Dịch tễ học toàn cầu 2018]')} Số liệu mắc mới, tử vong, xếp hạng ung thư chung, tỷ lệ nam vs nữ và vùng địa lý mắc cao/thấp nhất?",
        f"1) <b>Gánh nặng toàn cầu:</b> Có khoảng {Y('1.096.601 ca mắc mới (6,1%)')}, đứng hàng thứ {Y('4')} (sau phổi, vú, tuyến tiền liệt); có {R('551.269 ca tử vong (5,8%)')}, đứng hàng thứ {R('5')} (sau phổi, dạ dày, gan, vú).<br>"
        f"2) <b>Phân bố theo giới tính:</b> Phổ biến thứ {Y('2 ở phụ nữ')} (614.000 ca, 9,2%) và phổ biến thứ {Y('3 ở nam giới')} (746.000 ca, 10,0%).<br>"
        f"3) <b>Phân bố địa lý:</b> Cao nhất ở {G('Úc, New Zealand')} (44,8 ở nam và 32,2 ở nữ trên 100.000 dân); thấp nhất ở {G('Tây Phi')} (4,5 ở nam và 3,8 ở nữ trên 100.000 dân).",
        "Ung thư đại trực tràng gắn liền với lối sống phương Tây hóa (nhiều thịt đỏ, mỡ, ít vận động, ít chất xơ).",
        "B0.01, B0.02, B0.03", ["Dich-te", "Toan-cau", "Ty-le-mac"],
    ),
    basic(
        "SURG22-B0-02", "B0", "Dịch tễ Việt Nam và Tiên lượng tiến triển", 1,
        f"{B('[Dịch tễ Việt Nam & Tiên lượng]')} Tần suất mắc bệnh tại Việt Nam theo Bệnh viện K Trung ương và tỷ lệ sống thêm 5 năm nếu mổ sớm?",
        f"1) <b>Tại Việt Nam (BV K Trung ương):</b> Đứng hàng thứ {Y('5')} các bệnh ung thư phổ biến (sau dạ dày, phổi, vú, vòm họng), tần suất mắc là {Y('11,2 / 100.000 dân')}.<br>"
        f"2) <b>Tốc độ tiến triển:</b> Ung thư đại tràng tiến triển {G('tương đối chậm và di căn muộn')} hơn nhiều loại ung thư đường tiêu hóa khác.<br>"
        f"3) <b>Khả năng sống thêm 5 năm:</b> Nếu phát hiện và mổ sớm khi ung thư {G('chưa đến lớp thanh mạc')} thì tỷ lệ sống trên 5 năm đạt tới {G('80% – 90%')}.",
        "Chẩn đoán sớm trước khi khối u vượt qua lớp thanh mạc là yếu tố then chốt quyết định tiên lượng sống còn.",
        "B0.04, B0.05", ["Dich-te-VN", "Tien-luong", "Song-5-nam"],
    ),

    # =========================================================================
    # B1: NGUYÊN NHÂN VÀ CÁC YẾU TỐ NGUY CƠ
    # =========================================================================
    basic(
        "SURG22-B1-01", "B1", "Vai trò của Polyp đại tràng trong sinh ung", 1,
        f"{B('[Yếu tố nguy cơ: Polyp đại tràng]')} Nhận định của Deinheka, Shinya - Wolf (1979) và Kozevnhikov về mối liên quan giữa số lượng polyp và tỷ lệ ung thư hóa?",
        f"1) <b>Nhận định Deinheka:</b> Trên {R('50%')} trường hợp ung thư đại tràng phát sinh trên nền polyp đại tràng. Số lượng polyp càng nhiều, tỷ lệ ung thư hóa càng cao.<br>"
        f"2) <b>Nghiên cứu Shinya và Wolf (1979 - 5.786 u tuyến):</b> Bệnh nhân có 1 polyp thì tỷ lệ ung thư hóa là {Y('31,3%')}; bệnh nhân có 3 polyp thì tỷ lệ ung thư hóa tăng vọt lên {R('45,6%')}.<br>"
        f"3) <b>Nghiên cứu A.I. Kozevnhikov (958 trường hợp):</b> Bệnh nhân có 1 polyp thì tỷ lệ ác tính là {Y('1/35')}; bệnh nhân có nhiều polyp thì tỷ lệ ác tính lên tới {R('1/3')}.",
        "Mọi polyp đại tràng phát hiện qua nội soi đều cần được sinh thiết hoặc cắt bỏ triệt để phòng ngừa tiến triển ác tính.",
        "B1.01, B1.02, B1.03", ["Polyp", "Shinya-Wolf", "Kozevnhikov", "Ty-le-ung-thu-hoa"],
    ),
    basic(
        "SURG22-B1-02", "B1", "Bệnh đại tràng mạn tính và Viêm loét đại tràng chảy máu", 1,
        f"{B('[Bệnh lý đại tràng mạn tính]')} Các bệnh nhiễm khuẩn mạn tính tiền đề, tỷ lệ ung thư hóa theo Saegesser - Waridel và {R('2 vị trí viêm loét')} hay gặp nhất?",
        f"1) <b>Các bệnh lý mạn tính:</b> Ung thư có thể phát sinh trên tổn thương của {Y('lỵ amíp, lao, giang mai, thương hàn')} và viêm đại tràng mạn tính.<br>"
        f"2) <b>Viêm loét đại tràng chảy máu:</b> Nghiên cứu của F. Saegesser và D. Waridel ghi nhận khoảng {R('3% – 4%')} bệnh nhân bị viêm loét đại tràng có biến chứng ung thư.<br>"
        f"3) <b>Hai vị trí hay bị tổn thương nhất:</b> {G('Manh tràng')} và {G('Đại tràng xích ma (sigmoid)')}. Lý do: Đây là các đoạn ruột {Y('gấp khúc gây cản trở sinh lý')}, phân bị ứ trệ lâu ngày gây viêm loét niêm mạc mạn tính.",
        "Hiện tượng ứ đọng phân kéo dài tại hai góc gấp khúc manh tràng và xích ma tạo điều kiện cho vi khuẩn và chất độc tiếp xúc niêm mạc lâu ngày.",
        "B1.04, B1.05, B1.06", ["Viem-loet-dai-trang", "Saegesser-Waridel", "Manh-trang", "Xich-ma"],
    ),
    basic(
        "SURG22-B1-03", "B1", "Cơ chế chế độ ăn và Các chất sinh ung thực nghiệm", 1,
        f"{B('[Cơ chế chế độ ăn & Hóa chất sinh ung]')} Cơ chế bệnh sinh do thức ăn theo Burkitt (1975), Wynder - Reddy (1977) và {R('3 chất phân hủy đạm')} theo Petrov?",
        f"1) <b>Chế độ ăn nguy cơ cao:</b> Ăn {R('ít chất bã (ít chất xơ)')}, {R('nhiều mỡ và đạm động vật')}.<br>"
        f"2) <b>Tác động vi khuẩn và acid mật:</b> Làm thay đổi {Y('hệ vi khuẩn yếm khí')} tại đại tràng, biến đổi {Y('axit mật và cholesterol')} thành các chất gây ung thư.<br>"
        f"3) <b>Hệ quả giảm khối lượng phân:</b> Thức ăn ít bã làm giảm thể tích phân, gây {Y('táo bón')}, khiến chất gây ung thư tiếp xúc với niêm mạc ruột {R('lâu hơn và nồng độ cô đặc hơn')}.<br>"
        f"4) <b>Ba chất thoái biến của đạm gây ung thư thực nghiệm (Petrov):</b> Gồm {R('Indol')}, {R('Scatol')} và {R('Piridin')}.",
        "Petrov đã chứng minh trên thực nghiệm động vật rằng Indol, Scatol và Piridin là các chất sinh ung trực tiếp đối với niêm mạc ruột.",
        "B1.07, B1.08", ["Che-do-an", "Burkitt", "Petrov", "Indol", "Scatol", "Piridin"],
    ),
    basic(
        "SURG22-B1-04", "B1", "Hội chứng di truyền: Đa polyp FAP và Hội chứng Lynch", 1,
        f"{B('[Yếu tố di truyền]')} Đặc điểm đột biến gen, tỷ lệ ung thư hóa và chiến lược phẫu thuật của {Y('FAP')} và {Y('Hội chứng Lynch (HNPCC)')}?",
        f"1) <b>Bệnh đa polyp đại tràng gia đình (FAP):</b> Liên quan đến đột biến {R('gen APC')}. Chiếm {Y('< 1%')} ung thư đại trực tràng. Đặc điểm: {R('100% hóa ác')} nếu không phẫu thuật {G('cắt toàn bộ đại tràng trước 40 tuổi')}.<br>"
        f"2) <b>Hội chứng Lynch (HNPCC):</b> Chiếm khoảng {Y('5%')} ung thư đại trực tràng, di truyền trội NST thường do đột biến các gen sửa chữa ghép cặp sai DNA ({G('MLH1, MSH2')}), phối hợp biến đổi gen {G('p53, RAS và DCC')}.",
        "Bệnh nhân FAP cần được nội soi tầm soát từ tuổi dậy thì và chủ động cắt toàn bộ đại tràng dự phòng trước năm 40 tuổi.",
        "B1.09, B1.10", ["FAP", "Lynch", "APC", "MLH1", "MSH2"],
    ),

    # =========================================================================
    # B2: GIẢI PHẪU BỆNH LÝ & ĐẠI THỂ
    # =========================================================================
    basic(
        "SURG22-B2-01", "B2", "Phân bố vị trí ung thư theo các tác giả kinh điển", 2,
        f"{B('[Giải phẫu bệnh: Phân bố vị trí]')} Tỷ lệ phân bố ung thư đại tràng (Phải vs Ngang vs Trái) theo 4 tác giả: Morcaux, M. Galante, A. Deinheka và Nguyễn Văn Vân?",
        f"1) <b>Morcaux (480 BN):</b> ĐT phải {Y('26,7%')}, ĐT ngang {Y('6,8%')}, ĐT trái chiếm đa số {R('66,1%')}.<br>"
        f"2) <b>M. Galante (975 BN):</b> ĐT phải {Y('28,0%')}, ĐT ngang {Y('14,0%')}, ĐT trái chiếm đa số {R('57,9%')}.<br>"
        f"3) <b>A. Deinheka:</b> ĐT phải {Y('49,3%')}, ĐT ngang {Y('8,0%')}, ĐT trái {Y('42,7%')}.<br>"
        f"4) <b>Nguyễn Văn Vân (157 BN tại Việt Nam):</b> ĐT phải chiếm ưu thế {R('52,2%')}, ĐT ngang {Y('7,6%')}, ĐT trái {Y('40,1%')}.",
        "Các tác giả Âu Mỹ ghi nhận ưu thế đại tràng trái, trong khi số liệu Việt Nam (Nguyễn Văn Vân) ghi nhận đại tràng phải chiếm trên 50%.",
        "B2.01", ["Phan-bo-vi-tri", "Morcaux", "Galante", "Deinheka", "Nguyen-Van-Van"],
    ),
    basic(
        "SURG22-B2-02", "B2", "Hai vị trí hay gặp nhất và Tỷ lệ ung thư đồng thì", 1,
        f"{B('[Vị trí hay gặp & Ung thư đồng thì]')} Hai vị trí chiếm tỷ lệ cao nhất trên khung đại tràng và tỷ lệ xuất hiện ung thư đồng thì (nhiều nơi cùng lúc)?",
        f"1) <b>Hai vị trí thường gặp nhất:</b> {G('Đại tràng xích ma')} và {G('Manh tràng')}, mỗi nơi chiếm khoảng {Y('25% – 30%')}, sau đó mới tới các vị trí khác.<br>"
        f"2) <b>Ung thư đồng thì (nhiều ổ cùng lúc):</b> Thường ở một vị trí, nhưng có khoảng {R('5%')} trường hợp xuất hiện ở nhiều nơi đồng thời trên khung đại tràng.<br>"
        f"3) <b>Thái độ lâm sàng bắt buộc:</b> Phải thăm dò hoặc nội soi kiểm tra {R('toàn bộ khung đại tràng')} để tránh bỏ sót khối u thứ hai.",
        "5% tổn thương đồng thì là lý do mọi bệnh nhân K đại tràng đều phải soi toàn bộ khung ruột hoặc chụp CT đối quang kỹ lưỡng trước mổ.",
        "B2.02, B2.03", ["Xich-ma", "Manh-trang", "Dong-thi", "Bo-sot-u"],
    ),
    basic(
        "SURG22-B2-03", "B2", "Ba thể tổn thương đại thể của Ung thư đại tràng", 1,
        f"{B('[Giải phẫu bệnh: Thể đại thể]')} Vị trí ưu thế, đặc điểm hình thái và nguy cơ biến chứng của {G('Thể sùi')}, {Y('Thể loét')} và {R('Thể thắt nhẫn')}?",
        f"1) <b>Thể sùi (u sùi):</b> Hay gặp ở {G('đại tràng phải (manh tràng)')}; phát triển lồi vào lòng ruột hình súp lơ, tổ chức mềm mủn dễ chảy máu, lòng ruột rộng nên {Y('ít khi gây tắc ruột')}.<br>"
        f"2) <b>Thể loét:</b> Bờ nham nhở gồ ghề, ăn sâu qua các lớp thành ruột, dễ gây biến chứng {R('thủng thành ruột')} gây viêm phúc mạc hoặc chảy máu rỉ rả.<br>"
        f"3) <b>Thể thắt nhẫn (thâm nhiễm co thắt):</b> Hay gặp ở {R('đại tràng trái (đại tràng xuống và xích ma)')}; tế bào u thâm nhiễm vòng tròn xơ chai siết hẹp lòng ruột như chiếc nhẫn, rất dễ gây biến chứng {R('tắc ruột cơ học')}.",
        "Thể sùi to xốp nhưng ít tắc ở ĐT phải; thể thắt nhẫn xơ chai nhỏ nhưng gây tắc ruột sớm và dữ dội ở ĐT trái.",
        "B2.04, B2.05, B2.06", ["The-sui", "The-loet", "The-that-nhan", "Tac-ruot"],
    ),

    # =========================================================================
    # B3: TRIỆU CHỨNG LÂM SÀNG (ĐỐI CHIẾU ĐẠI TRÀNG PHẢI VÀ TRÁI)
    # =========================================================================
    basic(
        "SURG22-B3-01", "B3", "Đối chiếu triệu chứng Đau bụng Đại tràng Phải và Trái", 1,
        f"{B('[Lâm sàng: Đau bụng (70–80%)]')} Phân biệt tính chất đau bụng, vị trí khu trú và chẩn đoán phân biệt giữa {G('Đại tràng phải')} và {Y('Đại tràng trái')}?",
        f"1) <b>Đại tràng phải:</b> Đau {Y('âm ỉ mơ hồ không thành cơn')} ở hố chậu phải hoặc hạ sườn phải. Dễ chẩn đoán nhầm với {R('viêm ruột thừa mạn tính')} hoặc {R('viêm túi mật / sỏi mật')}.<br>"
        f"2) <b>Đại tràng trái:</b> Đau {R('quặn từng cơn dọc theo khung đại tràng')}, kèm theo sôi bụng, bụng trướng; khi {G('trung tiện hoặc đại tiện được thì đỡ đau rõ rệt')} ({Y('hội chứng Koenig')}).",
        "Hội chứng Koenig (đau quặn bụng + sôi bụng + trung tiện đỡ đau) là dấu hiệu bán tắc ruột kinh điển của đại tràng trái.",
        "B3.01", ["Dau-bung", "Koenig", "Ruot-thua-man", "Dai-trang-phai", "Dai-trang-trai"],
    ),
    basic(
        "SURG22-B3-02", "B3", "Đối chiếu Rối loạn lưu thông tiêu hóa", 1,
        f"{B('[Lâm sàng: Rối loạn lưu thông tiêu hóa]')} Cơ chế và biểu hiện rối loạn đại tiện phân biệt giữa {G('Đại tràng phải')} và {Y('Đại tràng trái')}?",
        f"1) <b>Đại tràng phải:</b> Biểu hiện {Y('tiêu chảy hoặc phân lỏng xen kẽ táo bón')}. Cơ chế do {R('hiện tượng ứ đọng, lên men thối rữa và tăng tiết dịch nhầy')}. Dễ nhầm với hội chứng lỵ hoặc viêm đại tràng co thắt.<br>"
        f"2) <b>Đại tràng trái:</b> Biểu hiện chủ yếu là {R('táo bón tăng dần')}. Cơ chế do phân tại đây {Y('đã thành khuôn đặc')}, lòng ruột nhỏ và khối u {Y('thể thắt nhẫn')} gây chít hẹp cơ học.",
        "Đại tràng phải phân lỏng + lên men -> Tiêu chảy; Đại tràng trái phân đặc + lòng hẹp siết nhẫn -> Táo bón tiến triển.",
        "B3.02", ["Roi-loan-tieu-hoa", "Tao-bon", "Tieu-chay", "Len-men"],
    ),
    basic(
        "SURG22-B3-03", "B3", "Đối chiếu Tính chất Phân lẫn máu & Xuất huyết", 1,
        f"{B('[Lâm sàng: Phân lẫn máu]')} Phân biệt màu sắc phân, cách hòa lẫn máu và hậu quả toàn thân giữa {G('Đại tràng phải')} và {Y('Đại tràng trái')}?",
        f"1) <b>Đại tràng phải:</b> Máu {Y('lẫn sâu trong phân')}, phân có màu {R('đỏ sẫm hoặc màu bã cà phê')}. Chảy máu rỉ rả vi thể kéo dài dẫn đến {R('hội chứng thiếu máu nhược sắc trầm trọng')} mà không nhìn thấy máu tươi rõ rệt.<br>"
        f"2) <b>Đại tràng trái:</b> Khối u cọ xát phân khuôn cứng, máu {Y('bọc bên ngoài khuôn phân')} thành vệt {R('máu đỏ tươi hoặc đỏ bầm')} kèm chất nhầy mủ.",
        "Phân lẫn máu bã cà phê + thiếu máu nặng = Đại tràng phải; Phân bọc vệt máu tươi bên ngoài = Đại tràng trái/trực tràng.",
        "B3.03", ["Phan-lan-mau", "Ba-ca-phe", "Mau-tuoi", "Thieu-mau-nhuoc-sac"],
    ),
    basic(
        "SURG22-B3-04", "B3", "Đối chiếu Khả năng sờ thấy khối u bụng (60%)", 1,
        f"{B('[Lâm sàng: Khám sờ u bụng (60%)]')} Tại sao khối u ung thư {G('Đại tràng phải')} rất dễ sờ thấy trên lâm sàng, trong khi {Y('Đại tràng trái')} lại rất khó sờ thấy?",
        f"1) <b>Đại tràng phải (rất dễ sờ thấy u):</b> Do vị trí manh tràng nằm {G('nông sát thành bụng trước')} (hố chậu phải hoặc mạng sườn phải) và khối u thường thuộc {Y('thể sùi kích thước lớn')}.<br>"
        f"2) <b>Đại tràng trái (rất khó sờ thấy u):</b> Do khối u thường nhỏ thuộc {R('thể thắt nhẫn thâm nhiễm')}, nằm sâu ở khoang {Y('sau phúc mạc')} hoặc bị che lấp bởi {Y('bờ hạ sườn và mào chậu')}.",
        "Sờ thấy khối chắc không đau vùng hố chậu phải ở người già luôn phải nghĩ tới ung thư manh tràng trước tiên.",
        "B3.04", ["So-thay-u", "Manh-trang", "Sau-phuc-mac", "Kham-bung"],
    ),
    basic(
        "SURG22-B3-05", "B3", "Triệu chứng toàn thân và Dấu hiệu Sốt theo Peltekallio", 1,
        f"{B('[Triệu chứng toàn thân & Dấu hiệu sốt]')} Dấu hiệu nổi bật của ung thư đại tràng phải và tỷ lệ sốt đơn thuần theo Peltekallio (1965)?",
        f"1) <b>Hội chứng thiếu máu:</b> Là dấu hiệu đặc trưng nổi bật của {G('ung thư đại tràng phải')}. Bệnh nhân đến khám vì {Y('da xanh xao, hoa mắt chóng mặt, mệt mỏi')} dù chưa rõ triệu chứng tiêu hóa, kèm {Y('sút cân nhanh')}.<br>"
        f"2) <b>Sốt đơn thuần theo Peltekallio (1965):</b> Khoảng {R('16% – 18%')} bệnh nhân có sốt đơn thuần. Cơ chế do {R('hoại tử khối u')} hoặc {R('nhiễm trùng thứ phát quanh u')}.<br>"
        f"3) <b>Bệnh cảnh dễ nhầm lẫn:</b> Dễ chẩn đoán nhầm với {Y('sốt thương hàn')} hoặc các ổ nhiễm trùng sâu trong ổ bụng.",
        "Sốt kéo dài kèm thiếu máu ở người trung niên - cao tuổi là cờ đỏ cảnh báo ung thư đại tràng hoại tử.",
        "B3.05, B3.06", ["Toan-than", "Thieu-mau", "Sot", "Peltekallio", "Hoai-tu-u"],
    ),

    # =========================================================================
    # B4: PHÂN LOẠI GIAI ĐOẠN (ASTLER - COLLER & DUKES)
    # =========================================================================
    basic(
        "SURG22-B4-01", "B4", "Phân loại giai đoạn Astler - Coller A, B1 và B2", 1,
        f"{B('[Phân loại Astler - Coller]')} Tiêu chuẩn giải phẫu bệnh chi tiết của 3 giai đoạn {G('Giai đoạn A')}, {Y('Giai đoạn B1')} và {R('Giai đoạn B2')}?",
        f"1) <b>Giai đoạn A:</b> Khối u khu trú ở {G('lớp niêm mạc và dưới niêm mạc')}, {Y('chưa xâm lấn vào lớp cơ')}, chưa có di căn hạch.<br>"
        f"2) <b>Giai đoạn B1:</b> Khối u đã {Y('xâm lấn vào lớp cơ')} nhưng {Y('chưa vượt qua lớp cơ')} (chưa tới thanh mạc), chưa có di căn hạch.<br>"
        f"3) <b>Giai đoạn B2:</b> Khối u {R('xâm lấn xuyên thủng toàn bộ lớp cơ')} tới thanh mạc hoặc ra mô mỡ quanh đại tràng, {Y('chưa có di căn hạch')}.",
        "Giai đoạn B phân định bởi độ sâu lớp cơ: B1 chưa qua cơ, B2 đã xuyên qua cơ tới thanh mạc / mô mỡ quanh ruột (tất cả hạch đều âm tính).",
        "B4.01, B4.02, B4.03", ["Astler-Coller", "Giai-doan-A", "Giai-doan-B1", "Giai-doan-B2"],
    ),
    basic(
        "SURG22-B4-02", "B4", "Phân loại giai đoạn Astler - Coller C1, C2 và D", 1,
        f"{B('[Phân loại Astler - Coller]')} Tiêu chuẩn giải phẫu bệnh chi tiết của 3 giai đoạn {Y('Giai đoạn C1')}, {R('Giai đoạn C2')} và {R('Giai đoạn D')}?",
        f"1) <b>Giai đoạn C1:</b> Khối u {Y('chưa vượt quá lớp cơ')} (tương ứng độ sâu B1) nhưng {R('ĐÃ CÓ di căn hạch vùng')}.<br>"
        f"2) <b>Giai đoạn C2:</b> Khối u {R('đã xâm lấn xuyên qua lớp cơ tới thanh mạc / mô quanh đại tràng')} (tương ứng độ sâu B2) và {R('ĐÃ CÓ di căn hạch vùng')}.<br>"
        f"3) <b>Giai đoạn D:</b> Khối u ở bất kỳ mức độ xâm lấn nào nhưng {R('ĐÃ CÓ di căn xa')} (gan, phổi, phúc mạc, buồng trứng...).",
        "Chỉ cần có di căn hạch bạch huyết (N+) là xếp nhóm C (C1 nếu chưa qua cơ, C2 nếu đã qua cơ). Có di căn xa chuyển ngay thành nhóm D.",
        "B4.04, B4.05, B4.06", ["Astler-Coller", "Giai-doan-C1", "Giai-doan-C2", "Giai-doan-D", "Di-can-hach"],
    ),
    basic(
        "SURG22-B4-03", "B4", "Bản chất đối chiếu phân loại Astler - Coller với Dukes", 2,
        f"{B('[Phân loại Astler - Coller vs Dukes]')} Điểm cải tiến mang tính bước ngoặt của hệ thống Astler - Coller so với phân loại Dukes nguyên bản là gì?",
        f"1) <b>Điểm cải tiến nhóm B:</b> Dukes chỉ có giai đoạn B chung (u vượt quá thành ruột); Astler - Coller chia tách thành {Y('B1 (u vào lớp cơ nhưng chưa qua cơ)')} và {R('B2 (u đã xuyên qua lớp cơ tới thanh mạc)')}.<br>"
        f"2) <b>Điểm cải tiến nhóm C:</b> Dukes chỉ có giai đoạn C chung (có di căn hạch); Astler - Coller phân định thành {Y('C1 (hạch dương tính nhưng u chưa qua cơ)')} và {R('C2 (hạch dương tính và u đã xuyên qua cơ)')}.<br>"
        f"3) <b>Ý nghĩa tiên lượng:</b> Độ sâu xâm lấn thành ruột kết hợp tình trạng di căn hạch phản ánh chính xác nguy cơ tái phát và tỷ lệ sống thêm sau phẫu thuật.",
        "Sự phân định B1/B2 và C1/C2 của Astler - Coller là tiền đề đặt nền móng trực tiếp cho hệ thống phân loại TNM hiện đại.",
        "B4.01, B4.02, B4.03, B4.04, B4.05, B4.06", ["Astler-Coller", "Dukes", "Cai-tien", "Do-sau-xam-lan"],
    ),

    # =========================================================================
    # B5: TIẾN TRIỂN VÀ BIẾN CHỨNG CẤP CỨU
    # =========================================================================
    basic(
        "SURG22-B5-01", "B5", "Biến chứng Tắc ruột ung thư đại tràng", 1,
        f"{B('[Biến chứng: Tắc ruột (~30%)]')} So sánh tỷ lệ tắc ruột giữa 3 vị trí (Trái vs Ngang vs Phải) và giải thích nguyên nhân?",
        f"1) <b>Tần suất theo phân đoạn:</b> Gặp ở {R('Đại tràng trái (46% – 48%)')} cao vượt trội so với {Y('Đại tràng ngang (33%)')} và {G('Đại tràng phải (18%)')}.<br>"
        f"2) <b>Lý do đại tràng trái hay bị tắc ruột nhất:</b> Do khối u thường thuộc {R('thể thắt nhẫn')} gây chít hẹp lòng ruột, thành đại tràng trái dày nhỏ và {Y('phân đã tạo khuôn rắn')}.",
        "Gần 1/2 bệnh nhân K đại tràng trái nhập viện trong bệnh cảnh tắc ruột cấp cứu.",
        "B5.01", ["Tac-ruot", "Ty-le", "Dai-trang-trai", "The-that-nhan"],
    ),
    basic(
        "SURG22-B5-02", "B5", "Xử trí cấp cứu Tắc ruột Đại tràng Phải", 1,
        f"{B('[Cấp cứu: Tắc ruột Đại tràng Phải]')} Chiến lược phẫu thuật cấp cứu trong 2 tình huống: Toàn trạng cho phép vs Bệnh nhân quá yếu / Viêm phúc mạc?",
        f"1) <b>Toàn trạng cho phép, bụng tương đối sạch:</b> Tiến hành {G('Cắt nửa đại tràng phải')} và {G('nối hồi – đại tràng ngang ngay thì đầu')} (nối tận – bên hoặc bên – bên theo kỹ thuật Quénu).<br>"
        f"2) <b>Bệnh nhân quá yếu hoặc viêm phúc mạc nặng:</b> {R('Cắt u đưa 2 đầu ruột ra ngoài làm hậu môn nhân tạo')}, hồi sức ổn định và {Y('nối lại ở thì 2')}.",
        "Đại tràng phải có ưu thế lòng sạch hơn và cấp máu dồi dào từ động mạch hồi - đại tràng nên cho phép cắt u nối ngay nếu toàn trạng ổn.",
        "B5.02", ["Cap-cuu", "Tac-ruot-phai", "Quenu", "Cat-noi-ngay"],
    ),
    basic(
        "SURG22-B5-03", "B5", "Xử trí cấp cứu Tắc ruột Đại tràng Trái: Hartmann vs Schloffer", 1,
        f"{B('[Cấp cứu: Tắc ruột Đại tràng Trái]')} Tại sao cấm nối ngay thì đầu và kỹ thuật tiến hành {R('Phẫu thuật Hartmann')} so với {Y('Phẫu thuật Schloffer 3 thì')}?",
        f"1) <b>Lý do cấm nối ngay thì đầu:</b> Thành ruột trái giãn mỏng, ứ đọng khối lượng lớn phân thối bẩn và vi khuẩn yếm khí, nguy cơ {R('bục miệng nối gây viêm phúc mạc tử vong cực cao')}.<br>"
        f"2) <b>Phẫu thuật Hartmann (2 thì):</b> Cắt đoạn đại tràng mang khối u → {G('Đưa đầu trên ra ngoài làm hậu môn nhân tạo')} → {Y('Khâu đóng kín mỏm dưới (mỏm trực tràng)')}. Đóng hậu môn nhân tạo và nối lại ở thì sau.<br>"
        f"3) <b>Phẫu thuật Schloffer (3 thì):</b> Thì 1: {Y('Làm hậu môn nhân tạo trên u (ĐT ngang)')} giải áp → Thì 2: {G('Cắt u và khâu nối lưu thông')} → Thì 3: {G('Đóng hậu môn nhân tạo')}.",
        "Phẫu thuật Hartmann hiện nay là lựa chọn kinh điển và phổ biến nhất trong tắc ruột cấp cứu do u đại tràng trái/xích ma.",
        "B5.03", ["Hartmann", "Schloffer", "Tac-ruot-trai", "Chong-chi-dinh-noi-ngay"],
    ),
    basic(
        "SURG22-B5-04", "B5", "Biến chứng Thủng u, Chảy máu dữ dội và Rò tiêu hóa", 1,
        f"{B('[Biến chứng ngoại khoa khác]')} Đặc điểm lâm sàng của biến chứng {R('Thủng u')}, {R('Chảy máu dữ dội')} và {Y('Rò đại tràng vào các tạng')}?",
        f"1) <b>Thủng khối u gây viêm phúc mạc:</b> Đau bụng dữ dội đột ngột, khám bụng có hội chứng {R('viêm phúc mạc toàn thể')} hoặc tạo ổ áp xe khu trú quanh khối u.<br>"
        f"2) <b>Chảy máu dữ dội:</b> Chảy máu ồ ạt qua đường tiêu hóa dưới do khối u hoại tử làm rách các nhánh mạch máu lớn.<br>"
        f"3) <b>Rò đại tràng vào bàng quang:</b> Biểu hiện kinh điển {Y('tiểu ra hơi (pneumaturia)')}, {Y('tiểu ra cặn phân (fecaluria)')} và nhiễm trùng tiết niệu tái phát dai dẳng.<br>"
        f"4) <b>Rò vào các cơ quan khác:</b> Rò vào {Y('âm đạo')} (phân chảy qua âm đạo) hoặc rò ra {Y('thành bụng')}.",
        "Tiểu ra hơi và phân là dấu hiệu chỉ điểm 100% của rò đại tràng - bàng quang, thường gặp ở K xích ma xâm lấn đáy bàng quang.",
        "B5.04, B5.05", ["Thung-u", "Chay-mau", "Ro-bang-quang", "Pneumaturia", "Fecaluria"],
    ),

    # =========================================================================
    # B6: CHUẨN BỊ TRƯỚC MỔ PHIÊN & RỬA RUỘT TRONG MỔ
    # =========================================================================
    basic(
        "SURG22-B6-01", "B6", "Chuẩn bị bệnh nhân trước mổ phiên và Thuốc tẩy Fortrans", 1,
        f"{B('[Chuẩn bị trước mổ: Làm sạch ruột]')} Phác đồ chế độ ăn, kháng sinh dự phòng, thành phần & quy cách dùng {G('Fortrans')} so với {R('Manitol 10%')}?",
        f"1) <b>Chế độ ăn & Kháng sinh:</b> Chế độ ăn {Y('không bã 2–3 ngày')} trước mổ; dùng kháng sinh đường ruột dự phòng {G('Neomycin phối hợp Metronidazol')}.<br>"
        f"2) <b>Quy cách dùng Fortrans:</b> Hộp chứa các gói Polyethyleneglycol 4000 (64g) cùng các muối điện giải. Pha mỗi gói trong {Y('1 lít nước')}, uống {Y('2 – 3 gói trong 2 – 3 giờ')} vào buổi chiều trước ngày mổ.<br>"
        f"3) <b>Ưu điểm vượt trội của Fortrans:</b> {G('Không gây rối loạn nước - điện giải')} và {G('không làm phù nề niêm mạc ruột')} (khắc phục hoàn toàn 2 nguy cơ nguy hiểm của Manitol 10%).",
        "Manitol 10% từng bị đào thải vì gây mất nước điện giải nặng và lên men sinh khí nổ khi dùng dao điện trong mổ.",
        "B6.01, B6.02", ["Chuan-bi-mo", "Fortrans", "Manitol", "Neomycin", "Metronidazol"],
    ),
    basic(
        "SURG22-B6-02", "B6", "Kỹ thuật Rửa đại tràng trong mổ (On-table lavage)", 1,
        f"{B('[Rửa đại tràng trong mổ: On-table lavage]')} Kỹ thuật tiến hành theo Dudley - Radilipffe và tình huống lâm sàng áp dụng?",
        f"1) <b>Tình huống áp dụng:</b> Mổ cấp cứu {Y('tắc ruột hoặc bán tắc ruột')} nhưng phẫu thuật viên quyết định {G('cắt u và lập lại lưu thông (nối ngay thì đầu)')}.<br>"
        f"2) <b>Kỹ thuật Dudley - Radilipffe:</b> Đặt ống thông qua {Y('manh tràng hoặc gốc ruột thừa')}, bơm rửa toàn bộ khung đại tràng bằng {G('dung dịch muối đẳng trương')} cho tới khi nước rửa chảy ra qua đầu dưới hoàn toàn trong và sạch trước khi tiến hành khâu nối.",
        "Kỹ thuật Dudley - Radilipffe giúp biến đại tràng tắc bẩn thành đại tràng sạch ngay trên bàn mổ để bảo vệ miệng nối thì đầu.",
        "B6.03", ["On-table-lavage", "Dudley-Radilipffe", "Rua-ruot", "Cap-cuu"],
    ),

    # =========================================================================
    # B7: ĐIỀU TRỊ NGOẠI KHOA, TAI BIẾN & ĐIỀU TRỊ BỔ TRỢ
    # =========================================================================
    basic(
        "SURG22-B7-01", "B7", "Phẫu thuật Cắt nửa đại tràng phải (Right Hemicolectomy)", 1,
        f"{B('[Ngoại khoa: Cắt nửa đại tràng phải]')} Chỉ định vị trí u, phạm vi cắt bỏ ruột non/ruột già, các mạch máu/chuỗi hạch cần nạo vét và kiểu miệng nối?",
        f"1) <b>Vị trí tổn thương phù hợp:</b> Khối u ở {Y('manh tràng, đại tràng lên, góc gan và 1/3 phải đại tràng ngang')}.<br>"
        f"2) <b>Phạm vi cắt bỏ:</b> Cắt {R('20 – 30 cm đoạn cuối hồi tràng')}, toàn bộ {R('manh tràng, đại tràng lên, góc gan và 1/2 phải đại tràng ngang')}.<br>"
        f"3) <b>Nạo vét mạch máu &amp; hạch:</b> Vét hạch dọc {G('động mạch hồi – đại tràng')}, {G('động mạch đại tràng phải')} và {G('nhánh phải động mạch đại tràng giữa')}.<br>"
        f"4) <b>Phục hồi lưu thông:</b> Làm miệng nối {Y('hồi tràng – đại tràng ngang')} (kiểu tận – tận, tận – bên hoặc bên – bên).",
        "Đoạn 20-30 cm cuối hồi tràng phải cắt bỏ vì chung cuống mạch máu nuôi với manh tràng qua ĐM hồi - đại tràng.",
        "B7.01", ["Right-hemicolectomy", "Cat-nua-phai", "Pham-vi-cat", "Hoi-dai-trang-ngang"],
    ),
    basic(
        "SURG22-B7-02", "B7", "Phẫu thuật Cắt nửa đại tràng trái (Left Hemicolectomy)", 1,
        f"{B('[Ngoại khoa: Cắt nửa đại tràng trái]')} Chỉ định vị trí u, phạm vi cắt bỏ ruột non/ruột già, xử trí mạch máu/hạch và kiểu miệng nối?",
        f"1) <b>Vị trí tổn thương phù hợp:</b> Khối u ở {Y('góc lách, đại tràng xuống và đại tràng xích ma cao')}.<br>"
        f"2) <b>Phạm vi cắt bỏ:</b> Cắt từ {R('1/3 ngoài đại tràng ngang')} đến {R('hết đại tràng xích ma')}.<br>"
        f"3) <b>Thắt cuống mạch &amp; nạo hạch:</b> {G('Thắt sát gốc động mạch mạc treo tràng dưới')}, nạo vét toàn bộ chuỗi hạch bạch huyết tương ứng.<br>"
        f"4) <b>Phục hồi lưu thông:</b> Làm miệng nối giữa {Y('đại tràng ngang với trực tràng')}.",
        "Thắt sát gốc ĐM mạc treo tràng dưới là nguyên tắc ung thư học bắt buộc để nạo vét sạch hạch nhóm trung tâm.",
        "B7.02", ["Left-hemicolectomy", "Cat-nua-trai", "Mac-treo-trang-duoi", "Dai-trang-ngang-truc-trang"],
    ),
    basic(
        "SURG22-B7-03", "B7", "Cắt đoạn đại tràng xích ma và Cắt toàn bộ đại tràng", 1,
        f"{B('[Ngoại khoa: Cắt xích ma & Cắt toàn bộ]')} Bờ an toàn phẫu thuật cắt đại tràng xích ma; Chỉ định và các phương án phục hồi lưu thông khi {R('Cắt toàn bộ đại tràng')}?",
        f"1) <b>Cắt đoạn đại tràng xích ma:</b> Cắt đoạn ruột cách bờ u {G('tối thiểu > 5 cm')}, nạo vét hạch cuống mạch mạc treo tràng dưới, nối đại tràng xuống với trực tràng.<br>"
        f"2) <b>Tình huống cắt toàn bộ đại tràng:</b> {R('Bệnh đa polyp gia đình (FAP)')}, {R('hội chứng Lynch đa u đồng thì')}, {R('viêm loét đại tràng toàn bộ ung thư hóa')}.<br>"
        f"3) <b>Phương án phục hồi lưu thông:</b><br>"
        f"   • Nối {G('hồi tràng – trực tràng')}.<br>"
        f"   • Hoặc cắt bỏ toàn bộ đại trực tràng và tạo hình {G('túi chứa hồi tràng hình chữ J nối ống hậu môn (IPAA)')}.<br>"
        f"   • Hoặc mở thông hồi tràng kiểu Brooke / túi Kock.",
        "IPAA (Ileal Pouch-Anal Anastomosis) là phẫu thuật tiêu chuẩn vàng bảo tồn tự chủ đại tiện sau cắt toàn bộ đại trực tràng.",
        "B7.03, B7.04", ["Cat-xich-ma", "Cat-toan-bo", "IPAA", "Brooke", "FAP"],
    ),
    basic(
        "SURG22-B7-04", "B7", "Tai biến phẫu thuật: Nguy cơ tổn thương tạng lân cận", 1,
        f"{B('[Tai biến trong mổ]')} Hai cấu trúc giải phẫu dễ bị tổn thương nhất trong {G('Cắt nửa đại tràng phải')} và hai cấu trúc trong {Y('Cắt nửa đại tràng trái')}?",
        f"1) <b>Cắt nửa đại tràng phải:</b> Rất dễ làm tổn thương {R('Niệu quản phải')} và {R('Tá tràng đoạn D2')} nằm ngay phía sau mạc Toldt phải. Bắt buộc phải {G('bộc lộ rõ niệu quản phải trước khi giải phóng mạc Toldt')}.<br>"
        f"2) <b>Cắt nửa đại tràng trái:</b> Rất dễ làm tổn thương {R('Niệu quản trái')} và nguy cơ {R('rách vỡ nhu mô lách')} khi thực hiện thao tác co kéo hạ góc lách.",
        "Bộc lộ rõ niệu quản hai bên trước khi thắt mạch mạc treo hoặc giải phóng mạc dính là nguyên tắc an toàn hàng đầu của phẫu thuật viên tiêu hóa.",
        "B7.05", ["Tai-bien-mo", "Nieu-quan-phai", "Ta-trang-D2", "Nieu-quan-trai", "Rach-lach"],
    ),
    basic(
        "SURG22-B7-05", "B7", "Tỷ lệ bục miệng nối và 3 nguyên tắc sống còn khi làm miệng nối", 1,
        f"{B('[Bục miệng nối đại tràng]')} So sánh tỷ lệ bục miệng nối (Phải vs Trái) và {R('3 nguyên tắc sống còn')} bắt buộc tuân thủ khi làm miệng nối ruột?",
        f"1) <b>Tần suất bục rò theo vị trí:</b> Cắt nửa đại tràng phải là {Y('5,8% – 14,6%')}; cắt nửa đại tràng trái là {Y('4,6% – 11,6%')}.<br>"
        f"2) <b>Nguyên tắc 1 — Cung cấp máu tốt:</b> Mép diện cắt phải hồng hào, máu động mạch {G('phun thành tia')}, tuyệt đối {R('không bóc tách thanh mạc quá xa mép nối (> 1 cm)')}.<br>"
        f"3) <b>Nguyên tắc 2 — Không bị căng:</b> Giải phóng đại tràng rộng rãi, miệng nối nằm hoàn toàn tự nhiên {G('không chịu lực co kéo')}.<br>"
        f"4) <b>Nguyên tắc 3 — Không nhiễm trùng:</b> Lòng ruột phải {G('chuẩn bị thật sạch phân')}, đảm bảo {G('vô trùng tuyệt đối')} trong mổ và đặt dẫn lưu ổ bụng đúng quy cách.",
        "Bóc tách trơ thanh mạc quá 1 cm làm thiếu máu nuôi mép cắt - nguyên nhân hàng đầu gây hoại tử bục rò miệng nối sau mổ.",
        "B7.06", ["Buc-mieng-noi", "3-nguyen-tac", "Tuoi-mau", "Khong-cang", "Vo-trung"],
    ),
    basic(
        "SURG22-B7-06", "B7", "Điều trị Hóa chất bổ trợ và Thuốc đích", 1,
        f"{B('[Điều trị bổ trợ]')} Phác đồ hóa chất bổ trợ tiêu chuẩn (giai đoạn áp dụng) và vai trò của hai nhóm thuốc sinh học điều trị đích {G('Bevacizumab')} và {Y('Cetuximab')}?",
        f"1) <b>Hóa chất bổ trợ sau mổ:</b> Phác đồ chứa {G('5-FU / Leucovorin')} kết hợp {G('Oxaliplatin')} ({Y('FOLFOX4')} hoặc {Y('CAPOX')}). Chỉ định cho {R('Giai đoạn III (có di căn hạch)')} hoặc {Y('Giai đoạn II có nguy cơ cao')}.<br>"
        f"2) <b>Thuốc kháng VEGF (Bevacizumab):</b> Dùng {G('Bevacizumab')} ức chế tăng sinh mạch máu nuôi khối u.<br>"
        f"3) <b>Thuốc kháng EGFR (Cetuximab):</b> Dùng {G('Cetuximab')}, đặc biệt hiệu quả và chỉ định cho các bệnh nhân mang {Y('gen KRAS / NRAS tự nhiên / hoang dại (wild-type)')}.",
        "Cetuximab mất hoàn toàn tác dụng nếu bệnh nhân có đột biến gen KRAS hoặc NRAS.",
        "B7.07", ["Hoa-tri", "FOLFOX4", "CAPOX", "Bevacizumab", "Cetuximab", "KRAS"],
    ),

    # =========================================================================
    # BẪY THI & CỜ ĐỎ LÂM SÀNG (TRAPS & RED FLAGS)
    # =========================================================================
    trap(
        "SURG22-TRAP-01", "B3", "Bẫy chẩn đoán Thiếu máu nhược sắc người cao tuổi",
        f"Bệnh nhân nam 65 tuổi đến khám vì hoa mắt, da xanh xao, xét nghiệm thấy {R('thiếu máu nhược sắc nặng')} nhưng phân đại tiện bình thường. Sai lầm nguy hiểm nhất là gì?",
        f"1) <b>Sai lầm thường gặp:</b> Chỉ chẩn đoán thiếu máu thiếu sắt đơn thuần và kê đơn thuốc sắt ngoại trú mà không tìm nguyên nhân mất máu.<br>"
        f"2) <b>Thực tế bệnh học:</b> Đây là triệu chứng chỉ điểm hàng đầu của {R('Ung thư đại tràng phải (manh tràng)')}. Khối u thể sùi chảy máu rỉ rả vi thể làm máu lẫn sâu trong phân không nhìn thấy được bằng mắt thường.<br>"
        f"3) <b>Hành động bắt buộc:</b> Phải chỉ định {G('Nội soi toàn bộ khung đại tràng')} ngay lập tức để tìm khối u manh tràng / đại tràng lên.",
        "Ở người cao tuổi, mọi trường hợp thiếu máu nhược sắc không rõ nguyên nhân đều phải coi là ung thư đại tràng phải cho đến khi có bằng chứng ngược lại.",
        "B3.03, B3.05", ["Bay-thieu-mau", "Dai-trang-phai", "Noi-soi", "Manh-trang"],
    ),
    trap(
        "SURG22-TRAP-02", "B5", "Bẫy xử trí Tắc ruột đại tràng trái cấp cứu",
        f"Tại sao phẫu thuật viên trẻ tuyệt đối {R('KHÔNG ĐƯỢC')} cắt đoạn u đại tràng xích ma và khâu nối ngay thì đầu trong mổ cấp cứu tắc ruột?",
        f"1) <b>Tình trạng đại tràng trái khi tắc ruột:</b> Thành ruột giãn mỏng tối đa, ứ đọng hàng lít phân thối bẩn với mật độ vi khuẩn cực cao, áp lực lòng ruột tăng vọt.<br>"
        f"2) <b>Hiểm họa nếu nối ngay:</b> Nguy cơ {R('bục rò miệng nối rất cao')}, gây viêm phúc mạc phân toàn thể dẫn đến nhiễm khuẩn nặng tử vong.<br>"
        f"3) <b>Quyết định chuẩn mực:</b> Phải thực hiện {G('Phẫu thuật Hartmann')} (cắt u, đưa đầu trên làm HMNT, đóng mỏm trực tràng) hoặc {G('phẫu thuật Schloffer 3 thì')} để bảo đảm an toàn tính mạng cho bệnh nhân.",
        "Không được đánh đổi an toàn tính mạng bệnh nhân để lấy một miệng nối thì đầu trong điều kiện ruột bẩn và thành ruột thiếu máu.",
        "B5.03", ["Bay-tac-ruot-trai", "Hartmann", "Cam-noi-ngay", "Buc-mieng-noi"],
    ),
    redflag(
        "SURG22-TRAP-03", "B5", "Cờ đỏ cấp cứu: Thủng u đại tràng gây Viêm phúc mạc",
        f"Dấu hiệu lâm sàng cảnh báo khối u ung thư đại tràng đã {R('biến chứng thủng')} và hướng xử trí ngoại khoa?",
        f"1) <b>Cơ năng:</b> Bệnh nhân đau bụng {R('đột ngột dữ dội')}, lan ra toàn ổ bụng.<br>"
        f"2) <b>Thực thể:</b> {R('Viêm phúc mạc toàn thể')} (bụng co cứng, cảm ứng phúc mạc lan tỏa) hoặc tạo ổ {Y('áp xe quanh khối u')}.<br>"
        f"3) <b>Phẫu thuật mở bụng khẩn cấp:</b> Hồi sức chống sốc, kháng sinh và {G('mổ cấp cứu xử trí biến chứng')}.",
        "Thủng u trên nền đại tràng tắc nghẽn là một cấp cứu ngoại khoa tối khẩn cấp với tỷ lệ tử vong rất cao do viêm phúc mạc phân.",
        "B5.04", ["Thung-u", "Liem-hoi", "Co-cung-bung", "Viem-phuc-mac"],
    ),
    redflag(
        "SURG22-TRAP-04", "B5", "Cờ đỏ lâm sàng: Rò đại tràng vào bàng quang",
        f"Hai dấu hiệu lâm sàng kinh điển khẳng định chắc chắn có {R('đường rò')} giữa đại tràng xích ma và bàng quang?",
        f"1) <b>Hiện tượng Pneumaturia:</b> {R('Tiểu ra bọt khí / tiểu ra hơi')} (khi đi tiểu thấy nước tiểu sủi bọt hoặc có tiếng xì hơi qua niệu đạo).<br>"
        f"2) <b>Hiện tượng Fecaluria:</b> {R('Tiểu ra cặn phân')} (nước tiểu đục, có cặn vàng nâu mùi phân).<br>"
        f"3) <b>Bệnh cảnh kèm theo:</b> Bệnh nhân bị {Y('nhiễm trùng đường tiết niệu tái phát dai dẳng')}.",
        "Pneumaturia và Fecaluria là cặp triệu chứng bệnh học đặc trưng khẳng định 100% rò bàng quang - tiêu hóa.",
        "B5.05", ["Ro-bang-quang", "Pneumaturia", "Fecaluria", "Tieu-ra-hoi"],
    ),
    trap(
        "SURG22-TRAP-05", "B7", "Bẫy phẫu thuật: Bảo vệ niệu quản phải và D2 tá tràng",
        f"Mốc giải phẫu nguy hiểm và nguyên tắc bộc lộ để tránh cắt nhầm vào {R('Niệu quản phải')} và {R('Tá tràng D2')}?",
        f"1) <b>Vị trí nguy hiểm:</b> Cả {R('Niệu quản phải')} và {R('Đoạn D2 tá tràng')} đều nằm ngay sau mạc dính đại tràng phải ({Y('mạc Toldt phải')}).<br>"
        f"2) <b>Nguy cơ tai biến:</b> Khi phẫu thuật viên cắt giải phóng mạc Toldt quá sâu vào khoang sau phúc mạc sẽ cắt đứt niệu quản phải hoặc làm rách thành sau D2 tá tràng (rò tá tràng tử vong).<br>"
        f"3) <b>Nguyên tắc bảo vệ:</b> Luôn phải {G('phẫu tích nhận diện rõ niệu quản phải')} (có nhu động giun bò) và đẩy tá tràng D2 ra sau trước khi cặp cắt các nhánh mạch mạc treo.",
        "Cắt đứt niệu quản và thủng D2 tá tràng là hai tai biến phẫu thuật kinh hoàng nhất trong phẫu thuật cắt nửa đại tràng phải.",
        "B7.05", ["Bay-mo", "Nieu-quan-phai", "Ta-trang-D2", "Mac-Toldt"],
    ),
    trap(
        "SURG22-TRAP-06", "B7", "Bẫy phẫu thuật: Hạ góc lách cắt đại tràng trái",
        f"Hai nguy cơ tai biến lớn nhất khi thao tác {R('hạ góc lách đại tràng')} và cách phòng tránh?",
        f"1) <b>Tai biến 1 — Rách nhu mô lách:</b> Dây chằng hoành - đại tràng và lách - đại tràng dính sát cực dưới của lách. Kéo giật mạnh đại tràng sẽ làm {R('rách bao lách hoặc đứt cuống lách')} gây chảy máu dữ dội, bắt buộc phải cắt lách.<br>"
        f"2) <b>Tai biến 2 — Tổn thương niệu quản trái:</b> Niệu quản trái bắt chéo phía sau mạc Toldt trái, rất dễ bị cặp cắt nhầm nếu không phẫu tích bộc lộ.<br>"
        f"3) <b>Kỹ thuật phẫu tích an toàn:</b> Cắt dây chằng thận trọng {G('áp sát thành đại tràng, tránh co kéo cực dưới của lách')}; nhận diện rõ niệu quản trái trước khi thắt gốc ĐM mạc treo tràng dưới.",
        "Hạ góc lách là thì mổ khó khăn và đòi hỏi sự tinh tế nhất trong phẫu thuật cắt đại tràng trái.",
        "B7.05", ["Ha-goc-lach", "Rach-lach", "Nieu-quan-trai", "Mac-treo-trang-duoi"],
    ),
    trap(
        "SURG22-TRAP-07", "B1", "Bẫy di truyền: Hội chứng Đa polyp gia đình (FAP)",
        f"Một bệnh nhân 25 tuổi nội soi đại tràng phát hiện {Y('hơn 200 polyp')} khắp khung ruột, kết quả sinh thiết đều là u tuyến lành tính. Sai lầm nguy hiểm nhất là gì?",
        f"1) <b>Sai lầm chết người:</b> Yên tâm vì kết quả sinh thiết là lành tính và chỉ hẹn nội soi theo dõi định kỳ.<br>"
        f"2) <b>Bản chất bệnh lý:</b> Đây là bệnh đa polyp đại tràng gia đình (FAP) do đột biến gen APC. Bệnh chắc chắn {R('100% sẽ tiến triển thành ung thư')} nếu để nguyên.<br>"
        f"3) <b>Phương án can thiệp bắt buộc:</b> Phải chủ động {G('phẫu thuật cắt toàn bộ đại tràng trước năm 40 tuổi')} để cứu sống bệnh nhân và xét nghiệm gen tầm soát cho toàn bộ người thân trực hệ.",
        "FAP là bệnh lý tiền ung thư tuyệt đối: 100% chuyển thành ung thư đại trực tràng nếu không cắt toàn bộ đại tràng trước 40 tuổi.",
        "B1.09", ["Bay-FAP", "Dot-bien-APC", "Cat-toan-bo-dai-trang", "Truoc-40-tuoi"],
    ),

    # =========================================================================
    # THUẬT TOÁN QUYẾT ĐỊNH (ALGORITHM CARDS)
    # =========================================================================
    algo(
        "SURG22-ALGO-01", "B3", "Đối chiếu Lâm sàng", "Phân định Đại tràng Phải vs Trái",
        f"1) <b>Tiêu chí 1 — Đau bụng:</b><br>"
        f"   • ĐT Phải: Đau {Y('âm ỉ mơ hồ ở hố chậu phải / hạ sườn phải')}.<br>"
        f"   • ĐT Trái: Đau {R('quặn từng cơn, sôi bụng, trung tiện đỡ đau (HC Koenig)')}.<br>"
        f"2) <b>Tiêu chí 2 — Rối loạn tiêu hóa:</b><br>"
        f"   • ĐT Phải: {Y('Tiêu chảy hoặc phân lỏng xen kẽ táo bón')} (ứ đọng lên men thối rữa).<br>"
        f"   • ĐT Trái: {R('Táo bón tăng dần')} (lòng ruột hẹp, phân thành khuôn).<br>"
        f"3) <b>Tiêu chí 3 — Tính chất phân lẫn máu:</b><br>"
        f"   • ĐT Phải: Máu {Y('lẫn sâu trong phân, màu đỏ sẫm/bã cà phê')}, rỉ rả gây thiếu máu nặng.<br>"
        f"   • ĐT Trái: Phân {R('bọc vệt máu tươi bên ngoài hoặc máu đỏ bầm')} kèm nhầy mủ.<br>"
        f"4) <b>Tiêu chí 4 — Khám sờ u bụng:</b><br>"
        f"   • ĐT Phải: {G('Rất dễ sờ thấy')} (manh tràng nông, u thể sùi lớn).<br>"
        f"   • ĐT Trái: {Y('Rất khó sờ thấy')} (u nhỏ thắt nhẫn, nằm sâu sau phúc mạc).<br>"
        f"5) <b>Tiêu chí 5 — Triệu chứng toàn thân &amp; Biến chứng:</b><br>"
        f"   • ĐT Phải: {R('Thiếu máu nhược sắc nổi bật')}, ít khi tắc ruột.<br>"
        f"   • ĐT Trái: {R('Tắc ruột cơ học chiếm gần 50%')}, ít thiếu máu nặng.",
        "Bảng thuật toán đối chiếu kinh điển giúp định hướng chính xác vị trí khối u ngay từ khi hỏi bệnh và thăm khám lâm sàng.",
        "B3.01, B3.02, B3.03, B3.04, B3.05, B5.01", ["Thuat-toan", "Doi-chieu-phai-trai", "Koenig", "Thieu-mau"],
    ),
    algo(
        "SURG22-ALGO-02", "B5", "Cấp cứu Ngoại khoa", "Xử trí Tắc ruột do Ung thư đại tràng",
        f"1) <b>Nhánh 1 — Tắc ruột do ung thư Đại tràng Phải:</b><br>"
        f"   • Toàn trạng bệnh nhân tốt, bụng sạch → {G('Phẫu thuật cắt nửa đại tràng phải và khâu nối hồi – đại tràng ngang ngay thì đầu')} (nối tận – bên hoặc bên – bên kiểu Quénu).<br>"
        f"   • Bệnh nhân quá yếu, suy kiệt nặng hoặc viêm phúc mạc → {R('Cắt u đưa 2 đầu ruột làm hậu môn nhân tạo')}, nối lại ở thì 2.<br>"
        f"2) <b>Nhánh 2 — Tắc ruột do ung thư Đại tràng Trái (KHÔNG ĐƯỢC nối ngay):</b><br>"
        f"   • Lựa chọn ưu tiên: {G('Phẫu thuật Hartmann (2 thì)')} → Cắt đoạn u đại tràng → Đưa đầu trên ra làm hậu môn nhân tạo → Khâu đóng kín mỏm dưới. Nối lại ở thì sau.<br>"
        f"   • Lựa chọn thứ hai: {Y('Phẫu thuật Schloffer (3 thì)')} → Thì 1 mở thông giải áp trên u → Thì 2 cắt u và nối → Thì 3 đóng hậu môn nhân tạo.<br>"
        f"   • Ngoại lệ duy nhất nếu muốn nối ngay: Bắt buộc phải thực hiện {G('Rửa đại tràng trong mổ (On-table lavage theo Dudley - Radilipffe)')}.",
        "Thuật toán xử trí tắc ruột cấp cứu nhấn mạnh nguyên tắc an toàn: Không bao giờ nối đại tràng trái thì đầu khi ruột chưa được làm sạch.",
        "B5.02, B5.03, B6.03", ["Thuat-toan", "Cap-cuu-tac-ruot", "Hartmann", "Quenu", "Schloffer"],
    ),
    algo(
        "SURG22-ALGO-03", "B7", "Phẫu thuật Triệt căn", "Lựa chọn phương pháp theo vị trí giải phẫu",
        f"1) <b>Nhánh 1 — U manh tràng, ĐT lên, góc gan, 1/3 phải ĐT ngang:</b><br>"
        f"   → {G('Cắt nửa đại tràng phải')}: Cắt 20–30 cm cuối hồi tràng đến nửa phải ĐT ngang; nạo vét 3 cuống mạch; làm miệng nối hồi tràng – ĐT ngang.<br>"
        f"2) <b>Nhánh 2 — U góc lách, ĐT xuống, xích ma cao:</b><br>"
        f"   → {G('Cắt nửa đại tràng trái')}: Cắt từ 1/3 ngoài ĐT ngang đến hết xích ma; thắt gốc ĐM mạc treo tràng dưới; nối ĐT ngang – trực tràng.<br>"
        f"3) <b>Nhánh 3 — U đại tràng xích ma:</b><br>"
        f"   → {Y('Cắt đoạn đại tràng xích ma')}: Cắt cách bờ u > 5 cm, nạo hạch cuống mạch MTTD, nối ĐT xuống với trực tràng.<br>"
        f"4) <b>Nhánh 4 — Đa polyp FAP, Lynch đa u, viêm loét toàn bộ ung thư hóa:</b><br>"
        f"   → {R('Cắt toàn bộ đại tràng')}: Nối hồi – trực tràng hoặc cắt toàn bộ đại trực tràng tạo hình {G('túi chứa hồi tràng hình chữ J (IPAA)')}.",
        "Mỗi vị trí giải phẫu có một phác đồ cắt bỏ ruột và nạo vét chuỗi mạch máu tương ứng theo nguyên tắc phẫu tích ung thư học chuẩn mực.",
        "B7.01, B7.02, B7.03, B7.04", ["Thuat-toan", "Phau-thuat-triet-can", "Right-hemicolectomy", "Left-hemicolectomy", "IPAA"],
    ),

    # =========================================================================
    # THẺ CLOZE (HIGH YIELD NUMBERS & BAREM GỐC)
    # =========================================================================
    cloze(
        "SURG22-B1-05", "B1", "Tỷ lệ ung thư hóa theo số lượng polyp",
        f"Theo Shinya và Wolf (1979 - 5786 u tuyến): 1 polyp có tỷ lệ ung thư hóa là {clz(1, Y('31,3%'))}, 3 polyp có tỷ lệ ung thư hóa là {clz(2, R('45,6%'))}. Theo Kozevnhikov (958 ca): 1 polyp có tỷ lệ ác tính {clz(3, Y('1/35'))}, nhiều polyp là {clz(4, R('1/3'))}.",
        "B1.02, B1.03", ["Polyp", "Shinya-Wolf", "Kozevnhikov", "Ty-le-ung-thu-hoa"],
    ),
    cloze(
        "SURG22-B6-03", "B6", "Quy cách và liều dùng thuốc tẩy ruột Fortrans",
        f"Chuẩn bị đại tràng bằng Fortrans: Thành phần chính gồm {clz(1, G('Polyethyleneglycol 4000 (64g)'))} cùng các muối điện giải. Mỗi gói pha trong {clz(2, Y('1 lít nước'))}, cho bệnh nhân uống {clz(3, Y('2 – 3 gói'))} trong thời gian {clz(4, Y('2 – 3 giờ'))} vào buổi chiều trước ngày mổ.",
        "B6.02", ["Fortrans", "PEG-4000", "Lieu-dung", "Chuan-bi-mo"],
    ),
    cloze(
        "SURG22-B7-07", "B7", "Tỷ lệ bục miệng nối đại tràng phải và trái",
        f"Thống kê ngoại khoa về tỷ lệ bục miệng nối: Phẫu thuật cắt nửa đại tràng phải có tỷ lệ bục là {clz(1, Y('5,8% – 14,6%'))}, phẫu thuật cắt nửa đại tràng trái có tỷ lệ bục là {clz(2, Y('4,6% – 11,6%'))}.",
        "B7.06", ["Buc-mieng-noi", "Ty-le", "Cat-nua-phai", "Cat-nua-trai"],
    ),
]
