"""
Build 2 Anki decks for YHCT Phan loai thuoc:
- Deck 1: Phan loai thuoc YHCT (v2 - cau chuyen ngan) — 14 groups + 28 subgroups + 20 cloze memory stories
- Deck 2: Tra cuu vị thuốc (Front=ten thuoc, Back=nhom)
"""

import json

# ============================================================
# DECK 1: Rewrite với mẹo nhớ ngắn gọn (1-2 dòng/vị)
# Style: câu chuyện mini, tên vị thuốc = tên nhân vật/hình ảnh Việt
# ============================================================

deck1_cards = []

# --- NHÓM 1: GIẢI BIỂU (19 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm GIẢI BIỂU (thuốc chữa cảm mạo) gồm những phân nhóm nào?",
    "back": "2 phân nhóm, 19 vị:<br>• <b>Tân ôn giải biểu</b> (cảm phong hàn): Ma hoàng, Quế chi, Tế tân, Bạch chỉ, Sinh khương, Tía tô, Hương nhu, Khương hoạt, Phòng phong, Tân giao<br>• <b>Tân lương giải biểu</b> (cảm phong nhiệt): Bạc hà, Cúc hoa, Tang diệp, Mạn kinh tử, Ngưu bàng tử, Cát cánh, Sài hồ, Thăng ma, Phù bình",
    "extra": "Gặp bệnh nhân cảm mạo → nghĩ ngay nhóm GIẢI BIỂU. Phân biệt hàn (Tân ôn - lạnh, sợ lạnh, không mồ hôi) vs nhiệt (Tân lương - sốt, đau họng, khát)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Phân nhóm Tân ôn giải biểu — mẹo nhớ 10 vị:<br><br>Một đêm đông giá rét, <b>{{c1::anh Mã}}</b> (Ma hoàng — phát hãn mạnh nhất, trị cảm không ra mồ hôi + hen) đi đường bị cảm. <b>{{c1::Vợ anh — chị Quế}}</b> (Quế chi — phát hãn nhẹ, ấm kinh, trị cảm biểu hư) đun nồi nước <b>{{c1::gừng tươi}}</b> (Sinh khương — ấm vị, chống nôn, dẫn thuốc) cho anh uống. <b>{{c1::Bà hàng xóm chị Bạch}}</b> (Bạch chỉ — chuyên trị đau đầu vùng trán, viêm xoang) mang sang lọ tinh dầu xoa. <b>{{c1::Ông nội ông Tế}}</b> (Tế tân — ấm sâu, trị đau răng + đau đầu do hàn) bà nội bà <b>{{c1::Tân}}</b> (Tân giao — phong thấp, đau nhức xương khớp) đội mũ đi mua thuốc. Em vợ <b>{{c1::Khương hoạt}}</b> (đau đầu đỉnh, phong thấp tay chân) chạy trước, <b>{{c1::Phòng phong}}</b> (phong thấp, tay chân tê, đau đầu) chạy sau. Bà ngoại <b>{{c1::Hương nhu}}</b> (trị cảm nắng + cảm hàn mùa hè) gửi nồi lá xông. Cô hàng xóm <b>{{c1::Tía tô}}</b> (cảm + nôn, an toàn cho bà bầu, giải cua cá độc) mang đĩa rau xào sang.",
    "extra": "Câu vần khóa: <b>\"Mã-Quế-Sinh-Bạch-Tế-Tân-Khương-Phòng-Hương-Tía\"</b>. Tân ôn = ấm, dùng cho cảm HÀN. Tân lương = mát, dùng cho cảm NHIỆT (họng đau, sốt, khát)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Phân nhóm Tân lương giải biểu — mẹo nhớ 9 vị:<br><br>Chàng trai <b>{{c1::Bạc}}</b> (Bạc hà — sốt nhẹ, đau họng, nhức đầu vùng thái dương) đi chợ mua hoa. Trước cổng chợ có <b>{{c1::bà Cúc}}</b> (Cúc hoa — đau đầu, chóng mặt, mắt đỏ) bán hoa cúc vàng. Vào trong, <b>{{c1::cô Tàng}}</b> (Tang diệp — ho khan, sốt nhẹ, mắt đỏ) bán lá dâu. Bên cạnh có <b>{{c1::bà Mạn}}</b> (Mạn kinh tử — đau đầu, mắt đỏ, phong nhiệt) bán quả kinh giới. Chàng ghé <b>{{c1::quán ông Ngưu}}</b> (Ngưu bàng tử — sốt, họng sưng đau, phát ban) ăn bát phở. Chạy sang <b>{{c1::hiệu thuốc chị Cát}}</b> (Cát cánh — trị họng, dẫn thuốc lên phế) mua thêm. <b>{{c1::Ông Sài}}</b> (Sài hồ — sốt cao, sốt rét, kinh nguyệt không đều) gọi thêm. <b>{{c1::Cô Thăng}}</b> (Thăng ma — sốt, họng đau, sa giáng) thêm 1 gói. Chàng ra về, thấy <b>{{c1::mấy quả {{c1::Phù bình}}</b> (Phù bình — phong nhiệt, sốt, khó thở) nổi trên mặt ao — chàng nhớ ra mẹo Phù bình trị sốt cao.",
    "extra": "Câu vần khóa: <b>\"Bạc-Cúc-Tang-Mạn-Ngưu-Cát-Sài-Thăng-Phù\"</b>. Dùng cho cảm NHIỆT (sốt, đau họng, khát nước)."
})

# --- NHÓM 2: THANH NHIỆT (34 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm THANH NHIỆT (thuốc trị nhiệt, lửa, độc) gồm những phân nhóm nào?",
    "back": "5 phân nhóm, 34 vị:<br>• <b>Thanh nhiệt tả hỏa</b> (nhiệt sốt cao): Thạch cao, Tri mẫu, Chi tử, Hạ khô thảo, Thảo quyết minh, Trúc diệp, Lô căn, Tây qua, Lá sen<br>• <b>Thanh nhiệt lương huyết</b> (nhiệt vào huyết): Huyền sâm, Sinh địa, Xích thược, Mẫu đơn bì, Địa cốt bì<br>• <b>Thanh nhiệt giải độc</b> (mụn nhọt, viêm): Kim ngân, Liên kiều, Bồ công anh, Sài đất, Xa can, Hoàng cầm, Hoàng liên, Hoàng bá, Khổ sâm<br>• <b>Thanh nhiệt trừ thấp</b> (thấp nhiệt tiết niệu): Hoàng bá, Hoàng cầm, Hoàng liên, Khổ sâm<br>• <b>Thanh nhiệt giải thử</b> (trúng nắng): Thạch cao, Hương nhu, Hoắc hương, Bạch biển đậu, Tây qua, Lá sen, Sinh địa",
    "extra": "5 phân nhóm chia theo MỨC ĐỘ sâu của nhiệt: tả hỏa (khí phận) → lương huyết (huyết phận) → giải độc (nhiệt độc) → trừ thấp (thấp nhiệt) → giải thử (trúng thử)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh nhiệt tả hỏa — mẹo nhớ 9 vị:<br><br>Bệnh nhân sốt cao 40°C nhập viện. Bác sĩ dùng <b>{{c1::Thạch cao}}</b> (viên đá trắng, hạ sốt cực mạnh, sốt cao khát nước) đập vụn. Thêm <b>{{c1::Tri mẫu}}</b> (mẹ Tri — hỗ trợ Thạch cao, trị sốt + táo bón) sắc cùng. Pha <b>{{c1::Chi tử}}</b> (sơn chi — quả dành dành, sốt bứt rứt, nước tiểu vàng) vào nước. <b>{{c1::Hạ khô thảo}}</b> (cỏ khô đầu hạ — sốt, mắt đỏ, huyết áp cao) và <b>{{c1::Thảo quyết minh}}</b> (hạt cây quyết minh — mắt đỏ, táo bón, hạ mỡ) thêm vào. <b>{{c1::Trúc diệp}}</b> (lá tre trúc — sốt khát, tâm phiền), <b>{{c1::Lô căn}}</b> (rễ sậy — sốt khát, nôn) sắc lên. Bệnh nhân uống nước <b>{{c1::dưa hấu Tây qua}}</b> (thanh nhiệt, giải khát) và <b>{{c1::nước lá sen}}</b> (thanh tâm hỏa, an thần).",
    "extra": "Câu vần: <b>\"Thạch-Tri-Chi-Hạ-Thảo-Trúc-Lô-Tây-Sen\"</b>. Thạch cao + Tri mẫu là cặp kinh điển (Bạch hổ thang)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh nhiệt lương huyết — mẹo nhớ 5 vị:<br><br>Bệnh nhân sốt cao vài ngày, nhiệt vào huyết → xuất huyết, ban đỏ. Bác sĩ kê đơn 5 vị, đặt tên là <b>\"nhóm 5 HUYỀN SINH\"</b>: <b>{{c1::Huyền sâm}}</b> (rễ huyền sâm — thanh nhiệt huyết phận, dưỡng âm, trị họng viêm, lao), <b>{{c1::Sinh địa}}</b> (địa hoàng tươi — dưỡng âm, mát huyết, sốt âm hư), <b>{{c1::Xích thược}}</b> (thược dược đỏ — mát huyết, hoạt huyết, trị ban đỏ), <b>{{c1::Mẫu đơn bì}}</b> (vỏ rễ mẫu đơn — mát huyết, hoạt huyết, kinh nguyệt), <b>{{c1::Địa cốt bì}}</b> (vỏ rễ cây địa cốt — sốt âm hư, ho lao).",
    "extra": "Câu vần: <b>\"Huyền-Sinh-Xích-Đơn-Địa\"</b>. Đây là 5 vị cốt lõi của Thanh nhiệt lương huyết — tất cả đều MÁT HUYẾT, trị sốt cao gây xuất huyết, ban xuất huyết."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh nhiệt giải độc — mẹo nhớ 9 vị:<br><br>Bệnh nhân bị mụn nhọt, viêm nhiễm. Bác sĩ kê: <b>{{c1::Kim ngân}}</b> (hoa kim ngân — sốt, mụn nhọt, viêm họng) + <b>{{c1::Liên kiều}}</b> (quả liên kiều — sốt, mụn nhọt, viêm) — đây là cặp kinh điển. Thêm <b>{{c1::Bồ công anh}}</b> (cây bồ công anh — mụn nhọt, viêm vú, viêm mắt), <b>{{c1::Sài đất}}</b> (cây sài đất — mụn nhọt trẻ em, viêm da), <b>{{c1::Xa can}}</b> (rễ xạ can — họng sưng đau, viêm phổi). Thêm 3 vị <b>\"3 anh em Hoàng nghèo nuôi mèo\"</b>: <b>{{c1::Hoàng cầm}}</b> (thân rễ — sốt, viêm phổi, vàng da), <b>{{c1::Hoàng liên}}</b> (rễ — viêm dạ dày, lỵ, mụn), <b>{{c1::Hoàng bá}}</b> (vỏ — thấp nhiệt hạ tiêu, viêm tiết niệu), <b>{{c1::Khổ sâm}}</b> (cây khổ sâm — mụn nhọt, lỵ, viêm da).",
    "extra": "Câu vần: <b>\"Kim-Liên-Bồ-Sài-Xa-Hoàng-Hoàng-Hoàng-Khổ\"</b>. Kim ngân + Liên kiều = cặp \"giải độc đệ nhất\"."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh nhiệt trừ thấp — mẹo nhớ 4 vị:<br><br>Bệnh nhân tiểu buốt, tiểu rắt, viêm đường tiết niệu. Bác sĩ kê <b>\"3 anh em Hoàng nghèo nuôi mèo trên núi ẩm\"</b>:<br>• <b>{{c1::Hoàng bá}}</b> (vỏ cây — thấp nhiệt hạ tiêu, tiểu buốt rắt, viêm tiết niệu, mồ hôi trộm)<br>• <b>{{c1::Hoàng cầm}}</b> (thân rễ — thấp nhiệt, vàng da, viêm phổi, lỵ)<br>• <b>{{c1::Hoàng liên}}</b> (rễ củ — thấp nhiệt tỳ vị, viêm dạ dày, lỵ, mụn)<br>• <b>{{c1::Khổ sâm}}</b> (cây khổ sâm — thấp chẩn, mụn nhọt, lỵ, viêm da)",
    "extra": "Câu vần: <b>\"Bá-Cầm-Liên-Khổ\"</b> = <b>\"Ba Cầm Liền Khổ\"</b> (cầm cứ khổ). Nhớ 3 vị Hoàng cùng họ 'thanh nhiệt táo thấp', Khổ sâm chuyên về da liễu."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh nhiệt giải thử — mẹo nhớ 7 vị:<br><br>Mùa hè nắng nóng, bệnh nhân trúng nắng, nôn, mất nước. Bác sĩ kê:<br>• <b>{{c1::Thạch cao}}</b> (hạ sốt, giải khát)<br>• <b>{{c1::Hương nhu}}</b> (cảm nắng mùa hè, ra mồ hôi)<br>• <b>{{c1::Hoắc hương}}</b> (nôn, tiêu chảy do thử thấp)<br>• <b>{{c1::Bạch biển đậu}}</b> (đậu ván trắng — tỳ vị, trúng thử, tiêu chảy)<br>• <b>{{c1::Tây qua}}</b> (vỏ dưa hấu — giải khát, giải thử)<br>• <b>{{c1::Lá sen}}</b> (thanh tâm, giải thử, an thần)<br>• <b>{{c1::Sinh địa}}</b> (mát huyết, bổ âm, giải thử)",
    "extra": "Câu vần: <b>\"Thạch-Hương-Hoắc-Đậu-Tây-Sen-Sinh\"</b>. Thử = nắng nóng. Tây qua + Lá sen là cặp giải khát quen thuộc mùa hè."
})

# --- NHÓM 3: BỔ (39 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm BỔ (thuốc bồi bổ cơ thể) gồm những phân nhóm nào?",
    "back": "4 phân nhóm, 39 vị:<br>• <b>Bổ khí</b> (mệt mỏi, hụt hơi, ăn kém): Nhân sâm, Đẳng sâm, Hoàng kỳ, Cam thảo, Đại táo, Hoài sơn, Bạch truật<br>• <b>Bổ huyết</b> (thiếu máu, da xanh): Đương quy, Thục địa, Bạch thược, A giao, Tử hà xa, Tang thầm, Ưng nhận, Nữ trinh tử, Hà thủ ô, Kỳ hồ<br>• <b>Bổ âm</b> (khô háo, sốt về chiều, mồ hôi trộm): Sa sâm, Thiên môn, Mạch môn, Cẩu kỷ tử, Quy bản, Miết giáp, Thạch hộc, Ngọc trúc, Hà thủ ô, Bách hợp<br>• <b>Bổ dương</b> (lạnh, mỏi gối, liệt dương, tiểu đêm): Lộc nhung, Nhục thung dung, Cốt toái bổ, Thủ ty tử, Đỗ trọng, Tục đoạn, Ba kích, Tiên mao, Cốc tinh, Ích trí nhân, Tang phiêu tiêu, Sơn thù du",
    "extra": "Bốn loại hư: Khí-Huyết-Âm-Dương. Mệt mỏi → khí hư. Xanh xao → huyết hư. Khô háo, sốt về chiều → âm hư. Sợ lạnh, mỏi gối → dương hư."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Bổ khí — mẹo nhớ 7 vị:<br><br>Bệnh nhân mệt mỏi, hụt hơi, ăn kém → Bổ khí. Bác sĩ kê đơn <b>\"Tứ quân tử thang\"</b> biến thể:<br>• <b>{{c1::Nhân sâm}}</b> (sâm chính — đại bổ nguyên khí, người suy kiệt)<br>• <b>{{c1::Đẳng sâm}}</b> (sâm rẻ tiền thay Nhân sâm, bổ khí)<br>• <b>{{c1::Hoàng kỳ}}</b> (bổ khí + thăng dương, ra mồ hôi tự ra, phù)<br>• <b>{{c1::Cam thảo}}</b> (cam thảo — kiện tỳ, điều hòa các vị)<br>• <b>{{c1::Đại táo}}</b> (táo đỏ — bổ tỳ, dưỡng huyết, an thần)<br>• <b>{{c1::Hoài sơn}}</b> (củ mài — bổ tỳ vị, phế, thận)<br>• <b>{{c1::Bạch truật}}</b> (kiện tỳ, táo thấp, an thai)",
    "extra": "Câu vần: <b>\"Sâm-Sâm-Kỳ-Cam-Táo-Sơn-Truật\"</b>. Tứ quân = Sâm-Truật-Phục-Linh-Cam thảo."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Bổ huyết — mẹo nhớ 10 vị:<br><br>Bệnh nhân da xanh xao, chóng mặt, kinh nguyệt ít → Bổ huyết. Bác sĩ kê <b>\"Tứ vật thang\"</b> biến thể:<br>• <b>{{c1::Thục địa}}</b> (địa hoàng chín — đại bổ huyết, chữa cốt)<br>• <b>{{c1::Bạch thược}}</b> (thược dược trắng — dưỡng huyết, liễm âm)<br>• <b>{{c1::Đương quy}}</b> (đầu bổ huyết, đuôi hoạt huyết, thân cả hai — \"vừa bổ vừa chạy\")<br>• <b>{{c1::Xuyên khung}}</b> (hành khí hoạt huyết — đầu vị Tứ vật)<br>• <b>{{c1::A giao}}</b> (keo da lừa — bổ huyết, chỉ huyết)<br>• <b>{{c1::Tử hà xa}}</b> (nhau thai — bổ huyết, ích tinh)<br>• <b>{{c1::Tang thầm}}</b> (quả dâu — bổ huyết, sinh tân dịch, tóc bạc sớm)<br>• <b>{{c1::Ưng nhận}}</b> (rễ cỏ tranh — cùng Tang thầm trị tóc bạc sớm)<br>• <b>{{c1::Nữ trinh tử}}</b> (trinh nữ — bổ can thận, sáng mắt, tóc bạc)<br>• <b>{{c1::Hà thủ ô}}</b> (đầu đen — bổ can thận, tóc đen trở lại, táo bón)<br>• <b>{{c1::Kỳ hồ}}</b> (kê huyết đằng — bổ huyết, hoạt huyết)",
    "extra": "Câu vần: <b>\"Thục-Thược-Đương-Khung-A-Giao-Xa-Tang-Ưng-Nữ-Hà-Kỳ\"</b>. Tứ vật = Thục-Thược-Đương-Khung."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Bổ âm — mẹo nhớ 10 vị:<br><br>Bệnh nhân khô miệng, háo khát, sốt về chiều, mồ hôi trộm → Bổ âm. Bác sĩ kê <b>\"Lục vị địa hoàng\"</b> biến thể:<br>• <b>{{c1::Sa sâm}}</b> (sâm cát — dưỡng âm, thanh phế)<br>• <b>{{c1::Thiên môn}}</b> (thiên môn đông — dưỡng âm, thanh nhiệt)<br>• <b>{{c1::Mạch môn}}</b> (mạch môn đông — dưỡng vị âm, phế âm)<br>• <b>{{c1::Cẩu kỷ tử</b> (kỷ tử — bổ can thận, sáng mắt)<br>• <b>{{c1::Quy bản}}</b> (mai rùa — bổ thận âm, tư âm tiềm dương)<br>• <b>{{c1::Miết giáp}}</b> (mai ba ba — bổ thận âm, tiềm dương, mềm cứng)<br>• <b>{{c1::Thạch hộc}}</b> (hoàng thảo — bổ thận, dưỡng vị âm)<br>• <b>{{c1::Ngọc trúc}}</b> (ngọc trúc — dưỡng âm, nhuận táo)<br>• <b>{{c1::Hà thủ ô}}</b> (bổ can thận âm)<br>• <b>{{c1::Bách hợp}}</b> (hoa bách hợp — dưỡng phế âm, an thần, trị ho)",
    "extra": "Câu vần: <b>\"Sa-Thiên-Mạch-Kỷ-Quy-Miết-Thạch-Ngọc-Hà-Bách\"</b>. Quy bản + Miết giáp = cặp tư âm tiềm dương kinh điển."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Bổ dương — mẹo nhớ 12 vị:<br><br>Bệnh nhân sợ lạnh, đau lưng mỏi gối, liệt dương, tiểu đêm → Bổ dương. Bác sĩ kê:<br>• <b>{{c1::Lộc nhung}}</b> (sừng hươu non — đại bổ thận dương, ích tinh huyết, số 1 bổ dương)<br>• <b>{{c1::Nhục thung dung}}</b> (tẩm tía — bổ thận dương, nhuận tràng)<br>• <b>{{c1::Cốt toái bổ}}</b> (tắc kè đá — bổ thận, lành xương, đau lưng)<br>• <b>{{c1::Thủ ty tử}}</b> (hạt tơ — bổ thận, dưỡng gan, sáng mắt, an thai)<br>• <b>{{c1::Đỗ trọng}}</b> (vỏ cây — bổ thận, an thai, hạ áp)<br>• <b>{{c1::Tục đoạn}}</b> (rễ — bổ thận, an thai, nối gân xương)<br>• <b>{{c1::Ba kích}}</b> (rễ — bổ thận dương, mạnh gân cốt)<br>• <b>{{c1::Tiên mao}}</b> (củ — bổ thận dương, trừ hàn thấp)<br>• <b>{{c1::Cốc tinh}}</b> (hạt — bổ thận, sáng mắt)<br>• <b>{{c1::Ích trí nhân}}</b> (quả ích trí — ôn thận, cố tinh, cầm tiểu)<br>• <b>{{c1::Tang phiêu tiêu}}</b> (tổ bọ ngựa trên cây dâu — cố tinh, sáp niệu)<br>• <b>{{c1::Sơn thù du}}</b> (quả sơn thù — bổ can thận, cố tinh)",
    "extra": "Câu vần: <b>\"Lộc-Nhục-Cốt-Thủ-Đỗ-Tục-Ba-Tiên-Cốc-Ích-Tang-Sơn\"</b>. Lộc nhung = vua bổ dương, đắt nhất."
})

# --- NHÓM 4: TẢ HẠ (11 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm TẢ HẠ (thuốc thông đại tiện, trị táo bón) gồm những phân nhóm nào?",
    "back": "3 phân nhóm, 11 vị:<br>• <b>Hàn hạ</b> (táo bón do thực nhiệt, sốt cao): Đại hoàng, Mang tiêu, Lô hội, Phan tả diệp<br>• <b>Nhiệt hạ</b> (táo bón do hàn ngưng, lạnh bụng): Ba đậu, Lưu hoàng<br>• <b>Nhuận hạ</b> (táo bón do âm hư, tân dịch hao): Ma nhân, Mật ong, Chút chít, Muồng trâu, Vỏ cây đại",
    "extra": "Hàn hạ = hạ hàn (tả nhiệt bằng lạnh). Nhiệt hạ = hạ nhiệt (tả hàn bằng nóng). Nhuận hạ = bôi trơn."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Hàn hạ — mẹo nhớ 4 vị:<br><br>Bệnh nhân sốt cao, táo bón, bụng đau. Bác sĩ dùng <b>{{c1::Đại hoàng}}</b> (vua tả hạ — tả nhiệt thông tiện, thanh lửa, hoạt huyết) — quân dược. Thêm <b>{{c1::Mang tiêu}}</b> (natri sunfat — hạ mạnh, phá kết tích). Thêm <b>{{c1::Lô hội}}</b> (nha đam — tả nhiệt, thanh can, mụn nhọt). <b>{{c1::Phan tả diệp}}</b> (lá — nhuận tả, dùng trong X-quang ruột).",
    "extra": "Câu vần: <b>\"Đại-Mang-Lô-Phan\"</b>. Đại hoàng + Mang tiêu = cặp Đại Thừa Khí Thang."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Nhiệt hạ — mẹo nhớ 2 vị:<br><br>Bệnh nhân bụng lạnh, táo bón, nôn. Bác sĩ dùng <b>{{c1::Ba đậu}}</b> (hạt — hạ hàn tích, trừ thủy thũng, RẤT ĐỘC, phải bỏ vỏ ép bã) và <b>{{c1::Lưu hoàng}}</b> (lưu huỳnh — ôn thông tiện, trị ghẻ, ngoài da).",
    "extra": "Cả 2 đều có độc tính, dùng cẩn thận. Ba đậu chống chỉ định với phụ nữ có thai."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Nhuận hạ — mẹo nhớ 5 vị:<br><br>Bệnh nhân già yếu, âm hư, táo bón lâu ngày → Nhuận hạ (bôi trơn, không tả mạnh). Bác sĩ dùng: <b>{{c1::Ma nhân}}</b> (hạt gai dầu — nhuận tràng, dưỡng huyết, bổ), <b>{{c1::Mật ong}}</b> (nhuận tràng, dưỡng vị, an thần), <b>{{c1::Chút chít}}</b> (lá — nhuận tả), <b>{{c1::Vỏ cây đại}}</b> (nhuận tả, lợi tiểu), <b>{{c1::Muồng trâu}}</b> (lá — nhuận tả, hạ áp nhẹ).",
    "extra": "Câu vần: <b>\"Ma-Mật-Chút-Đại-Muồng\"</b>. Dùng cho người già, sản phụ, người suy yếu — không gây đau bụng."
})

# --- NHÓM 5: LỢI NIỆU (16 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm LỢI NIỆU (thuốc thông tiểu, trừ thấp) gồm những phân nhóm nào?",
    "back": "2 phân nhóm, 16 vị:<br>• <b>Lợi thủy thấm thấp</b> (phù, tiểu ít, thấp): Trạch tả, Xa tiền tử, Mộc thông, Ý dĩ, Hoạt thạch, Tỳ giải, Kim tiền thảo, Phục linh, Trư linh, Phong kỳ, Đậu đỏ, Thông thảo<br>• <b>Thực thủy</b> (phù nặng, cổ trướng): Cam toại, Nguyên hoa, Đại kích, Bạt kế",
    "extra": "Lợi thủy thấm thấp = thông tiểu nhẹ, bổ. Thực thủy = tả nước mạnh, RẤT MẠNH, dùng cẩn thận."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Lợi thủy thấm thấp — mẹo nhớ 12 vị:<br><br>Bệnh nhân phù nhẹ, tiểu ít. Bác sĩ kê:<br>• <b>{{c1::Phục linh}}</b> (nấm — lợi thấm, kiện tỳ, an thần, quân dược)<br>• <b>{{c1::Trư linh}}</b> (nấm — lợi thủy mạnh hơn Phục linh)<br>• <b>{{c1::Trạch tả}}</b> (củ — lợi thấm, thanh nhiệt)<br>• <b>{{c1::Ý dĩ}}</b> (hạt bo bo — lợi thấm, kiện tỳ, trừ mủ)<br>• <b>{{c1::Xa tiền tử}}</b> (hạt mã đề — lợi thủy, trị tiểu buốt rắt, sỏi)<br>• <b>{{c1::Mộc thông}}</b> (thân — lợi thủy, thông kinh, thanh tâm)<br>• <b>{{c1::Hoạt thạch}}</b> (bột talc — lợi thủy, thanh nhiệt, trị tiểu buốt)<br>• <b>{{c1::Tỳ giải}}</b> (củ — lợi thấp, phân thanh trọc)<br>• <b>{{c1::Kim tiền thảo}}</b> (cỏ — trị sỏi tiết niệu, mật)<br>• <b>{{c1::Phong kỳ}}</b> (kỳ — lợi thủy, trừ phong thấp)<br>• <b>{{c1::Đậu đỏ}}</b> (hạt — lợi thủy, tiêu thũng)<br>• <b>{{c1::Thông thảo}}</b> (lõi thông — lợi thủy, thông sữa)",
    "extra": "Câu vần: <b>\"Phục-Trư-Trạch-Ý-Xa-Mộc-Hoạt-Tỳ-Kim-Phong-Đậu-Thông\"</b>. Phục linh + Trư linh = cặp Ngũ Lâm Tán."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thực thủy — mẹo nhớ 4 vị:<br><br>Bệnh nhân cổ trướng, phù nặng cần tả nước mạnh. Bác sĩ dùng 4 vị <b>\"bốn sát thủ\"</b>: <b>{{c1::Cam toại}}</b> (củ — tả thủy thũng, độc), <b>{{c1::Nguyên hoa}}</b> (hoa — tả thủy, trục đờm, độc), <b>{{c1::Đại kích}}</b> (rễ — tả thủy, phá kết, độc), <b>{{c1::Bạt kế}}</b> (rễ — tả thủy, tiêu mủ, độc).",
    "extra": "Câu vần: <b>\"Cam-Nguyên-Đại-Bạt\"</b>. Tất cả đều có ĐỘC, dùng cẩn thận, chống chỉ định với phụ nữ có thai."
})

# --- NHÓM 6: AN THẦN (10 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm AN THẦN (thuốc trị mất ngủ, lo âu) gồm những phân nhóm nào?",
    "back": "2 phân nhóm, 10 vị:<br>• <b>Dưỡng tâm an thần</b> (mất ngủ, hay quên, hồi hộp): Toan táo nhân, Vông nem, Bá tử nhân, Viễn chí, Long nhãn, Lạc tiên<br>• <b>Bình can tiềm dương</b> (mất ngủ do can hỏa vượng, đau đầu, bốc hỏa): Chân sa, Mẫu lệ, Trân châu mẫu, Hổ phách",
    "extra": "Dưỡng tâm an thần dùng cho mất ngủ do TÂM HUYẾT HƯ (tim đập nhanh, hay quên). Bình can tiềm dương dùng cho mất ngủ do CAN DƯƠNG VỌNG (đau đầu, bốc hỏa)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Dưỡng tâm an thần — mẹo nhớ 6 vị:<br><br>Bệnh nhân mất ngủ, hồi hộp, hay quên → Tâm huyết hư. Bác sĩ kê <b>\"6 vị an thần dưỡng tâm\"</b>:<br>• <b>{{c1::Toan táo nhân}}</b> (hạt táo chua — dưỡng tâm an thần, số 1 trị mất ngủ)<br>• <b>{{c1::Bá tử nhân}}</b> (hạt trắc bách — dưỡng tâm, nhuận tràng)<br>• <b>{{c1::Vông nem}}</b> (lá — an thần, trị mất ngủ)<br>• <b>{{c1::Viễn chí}}</b> (rễ — an thần, ích trí, trừ đờm)<br>• <b>{{c1::Long nhãn}}</b> (cùi nhãn — bổ huyết, an thần)<br>• <b>{{c1::Lạc tiên}}</b> (dây — an thần dân gian, trị mất ngủ)",
    "extra": "Câu vần: <b>\"Táo-Bá-Vông-Viễn-Long-Lạc\"</b>. Toan táo nhân + Bá tử nhân = cặp dưỡng tâm an thần kinh điển (Thiên Vương Bổ Tâm Đan)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Bình can tiềm dương — mẹo nhớ 4 vị:<br><br>Bệnh nhân mất ngủ do can dương vượng, đau đầu, bốc hỏa. Bác sĩ dùng 4 vị <b>\"khoáng vật nặng trấn\"</b>:<br>• <b>{{c1::Chân sa}}</b> (thuỷ ngân — trấn tâm an thần, thanh nhiệt, độc, ít dùng)<br>• <b>{{c1::Mẫu lệ}}</b> (vỏ hàu — tiềm dương, liễm hãn, cố tinh)<br>• <b>{{c1::Trân châu mẫu}}</b> (mẹ ngọc trai — bình can, an thần, sáng mắt)<br>• <b>{{c1::Hổ phách}}</b> (hổ phách — trấn tâm, lợi tiểu, hoạt huyết)",
    "extra": "Câu vần: <b>\"Chân-Mẫu-Trân-Hổ\"</b>. Tất cả đều là khoáng vật/đá → nặng → trấn, tiềm. Chân sa có độc (thuỷ ngân) → hạn chế dùng."
})

# --- NHÓM 7: CHỈ HUYẾT (10 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm CHỈ HUYẾT (thuốc cầm máu) gồm những phân nhóm nào?",
    "back": "3 phân nhóm, 10 vị:<br>• <b>Chỉ ứ chỉ huyết</b> (chảy máu do huyết ứ): Tam thất, Bạch cập, Huyết dư thán, Ngẫu tiết<br>• <b>Thanh nhiệt chỉ huyết</b> (chảy máu do nhiệt): Trắc bá diệp, Hoa hòe, Hạ liên thảo, Bạch mao căn<br>• <b>Kiện tỳ chỉ huyết</b> (chảy máu do tỳ hư): Ô tặc cốt, Ngẫu bì",
    "extra": "Cầm máu không phải lúc nào cũng dùng thuốc cầm máu. Phải tìm nguyên nhân: huyết ứ → hoạt huyết cầm máu, nhiệt → thanh nhiệt cầm máu, tỳ hư → kiện tỳ cầm máu."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Chỉ ứ chỉ huyết — mẹo nhớ 4 vị:<br><br>Bệnh nhân chảy máu do huyết ứ (chấn thương, sau sinh). Bác sĩ dùng 4 vị <b>\"vừa cầm máu vừa hoạt huyết\"</b>:<br>• <b>{{c1::Tam thất}}</b> (củ — số 1 cầm máu do ứ, tiêu sưng, bổ huyết)<br>• <b>{{c1::Bạch cập}}</b> (củ lan — cầm máu, sinh cơ, dùng ngoài da trị bỏng, lở)<br>• <b>{{c1::Huyết dư thán}}</b> (tóc đốt — cầm máu, lợi tiểu)<br>• <b>{{c1::Ngẫu tiết}}</b> (đốt ngẫu — cầm máu, trị băng huyết)",
    "extra": "Câu vần: <b>\"Tam-Bạch-Huyết-Ngẫu\"</b>. Tam thất = quân dược, dùng cho cả chảy máu nội + ngoại."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh nhiệt chỉ huyết — mẹo nhớ 4 vị:<br><br>Bệnh nhân chảy máu cam, ho ra máu, kinh nguyệt cường do hỏa. Bác sĩ dùng 4 vị <b>\"mát huyết cầm máu\"</b>:<br>• <b>{{c1::Trắc bá diệp}}</b> (lá trắc bá — cầm máu, mát huyết, trị ho ra máu, kiết lỵ)<br>• <b>{{c1::Hoa hòe}}</b> (hoa — cầm máu, hạ huyết áp, trị trĩ)<br>• <b>{{c1::Hạ liên thảo}}</b> (cỏ cứt lợn — cầm máu, giải độc)<br>• <b>{{c1::Bạch mao căn}}</b> (rễ cỏ tranh — cầm máu, lợi tiểu, thanh nhiệt)",
    "extra": "Câu vần: <b>\"Trắc-Hòe-Liên-Mao\"</b>. Hoa hòe + Trắc bá diệp = cặp thanh nhiệt chỉ huyết kinh điển (Trắc Hòe Hợp Tể)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Kiện tỳ chỉ huyết — mẹo nhớ 2 vị:<br><br>Bệnh nhân chảy máu mạn do tỳ hư (đại tiện ra máu, kinh nguyệt rỉ rả). Bác sĩ dùng: <b>{{c1::Ô tặc cốt}}</b> (mai mực — cầm máu, cố toan, chữa loét dạ dày) và <b>{{c1::Ngẫu bì}}</b> (vỏ củ ấu — cầm máu, thu liễm).",
    "extra": "Câu vần: <b>\"Ô-Ngẫu\"</b>. Ô tặc cốt vừa cầm máu, vừa trung hòa acid dạ dày → trị loét dạ dày tá tràng."
})

# --- NHÓM 8: CỐ SÁP (11 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm CỐ SÁP (thuốc thu liễm, cầm) gồm những phân nhóm nào?",
    "back": "3 phân nhóm, 11 vị:<br>• <b>Liễm hãn</b> (mồ hôi trộm, ra mồ hôi nhiều): Tiểu mạch, Ngũ vị tử, Mẫu lệ<br>• <b>Cố tinh - Sáp niệu</b> (di tinh, tiểu đêm, tiểu nhiều): Kim anh tử, Tang phiêu tiêu, Khiếm thực, Liên nhục, Sơn thù<br>• <b>Sáp trường chỉ tả</b> (tiêu chảy mạn): Ô mai, Thạch lựu bì, Kha tử",
    "extra": "Cố sáp = thu liễm, cố giữ chất bị thoát ra: mồ hôi, tinh dịch, nước tiểu, phân. Bản chất là 'đóng cửa' — phải chẩn đoán đúng nguyên nhân hư."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Liễm hãn — mẹo nhớ 3 vị:<br><br>Bệnh nhân ra mồ hôi trộm, tự ra mồ hôi. Bác sĩ dùng 3 vị <b>\"cầm mồ hôi\"</b>: <b>{{c1::Tiểu mạch}}</b> (lúa mì non — liễm hãn, dưỡng tâm, thanh nhiệt), <b>{{c1::Ngũ vị tử}}</b> (5 vị — liễm hãn, sinh tân, bổ thận, an thần), <b>{{c1::Mẫu lệ}}</b> (vỏ hàu — liễm hãn, tiềm dương, cố tinh, trung hòa acid).",
    "extra": "Câu vần: <b>\"Mạch-Ngũ-Mẫu\"</b>. Ngũ vị tử = vị thuốc bổ thận duy nhất có thể liễm hãn + cố tinh + an thần."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Cố tinh - Sáp niệu — mẹo nhớ 5 vị:<br><br>Bệnh nhân di tinh, tiểu đêm, tiểu nhiều. Bác sĩ dùng 5 vị <b>\"giữ tinh, cầm tiểu\"</b>: <b>{{c1::Kim anh tử}}</b> (quả tầm xuân — sáp trường, cố tinh), <b>{{c1::Tang phiêu tiêu}}</b> (tổ bọ ngựa trên cây dâu — cố tinh, sáp niệu), <b>{{c1::Khiếm thực}}</b> (hạt súng — cố tinh, kiện tỳ, trừ thấp), <b>{{c1::Liên nhục}}</b> (hạt sen — cố tinh, kiện tỳ, an thần), <b>{{c1::Sơn thù du}}</b> (quả — bổ can thận, cố tinh, cầm mồ hôi).",
    "extra": "Câu vần: <b>\"Kim-Tang-Khiếm-Liên-Sơn\"</b>. Khiếm thực + Liên nhục = cặp Thủy Lục Nhị Tinh (Kim Quỳ Yếu Lược)."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Sáp trường chỉ tả — mẹo nhớ 3 vị:<br><br>Bệnh nhân tiêu chảy mạn tính. Bác sĩ dùng 3 vị <b>\"cầm tiêu chảy\"</b>: <b>{{c1::Ô mai}}</b> (mận đen muối — sáp trường, chỉ tả, sinh tân, trị giun), <b>{{c1::Thạch lựu bì}}</b> (vỏ lựu — sáp trường, chỉ huyết, trị sán dây), <b>{{c1::Kha tử}}</b> (quả kha tử — sáp trường, liễm phế, trị ho, khàn tiếng).",
    "extra": "Câu vần: <b>\"Ô-Lựu-Kha\"</b>. Ô mai = vua trị tiêu chảy + giun (Ô mai Hoàn)."
})

# --- NHÓM 9: TRỪ TÀM (8 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm TRỪ TÀM (thuốc trị giun, sán, ký sinh trùng) gồm những phân nhóm nào?",
    "back": "2 phân nhóm, 8 vị:<br>• <b>Thanh hóa nhiệt tàm</b>: Thược nhệ, Qua lâu thực, Bối mẫu<br>• <b>Ôn hóa hàn tàm</b>: Bạch hạ chỉ, Thiên nam tinh, Bạch giới tử, Tạo giác, Bạch phụ tử",
    "extra": "Nhiệt tàm = trong người có nhiệt + giun → dùng thuốc hàn. Hàn tàm = trong người có hàn + giun → dùng thuốc ôn."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh hóa nhiệt tàm — mẹo nhớ 3 vị:<br><br>Bệnh nhân có giun kèm miệng đắng, sốt, bụng nóng. Bác sĩ dùng: <b>{{c1::Thược nhệ}}</b> (hạt — sát giun, nhuận tràng), <b>{{c1::Qua lâu thực}}</b> (hạt gấc — sát giun, thu liễm), <b>{{c1::Bối mẫu}}</b> (xuyên bối mẫu — thanh nhiệt, trừ đờm, giảm đau).",
    "extra": "Câu vần: <b>\"Thược-Qua-Bối\"</b>. Thược nhệ + Qua lâu thực = thuốc trị giun kinh điển, vừa sát giun vừa nhuận để tống giun ra."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Ôn hóa hàn tàm — mẹo nhớ 5 vị:<br><br>Bệnh nhân có giun kèm bụng lạnh, đau quặn, nôn. Bác sĩ dùng 5 vị: <b>{{c1::Bạch hạ chỉ}}</b> (rễ — trị đau đầu, sát trùng), <b>{{c1::Thiên nam tinh}}</b> (củ — ôn hóa hàn tàm, trị đờm, phong), <b>{{c1::Bạch giới tử}}</b> (hạt — ôn hóa hàn đờm, tán kết), <b>{{c1::Tạo giác}}</b> (quả bồ kết — sát trùng, khử đờm, thông khiếu), <b>{{c1::Bạch phụ tử}}</b> (củ — ôn trung, tán hàn, trị đau đầu).",
    "extra": "Câu vần: <b>\"Bạch-Thiên-Bạch-Tạo-Bạch\"</b>. Tạo giác (bồ kết) vừa sát trùng, vừa tẩy uế, dùng cả nội + ngoại."
})

# --- NHÓM 10: CHỈ KHÁI (11 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm CHỈ KHÁI (thuốc trị ho, hen suyễn) gồm những phân nhóm nào?",
    "back": "2 phân nhóm, 11 vị:<br>• <b>Thanh phế chỉ khái</b> (ho do nhiệt, đờm vàng): Tang bạch bì, Tỳ bà diệp, Bạch tiền, Tiền hồ<br>• <b>Ôn phế chỉ khái</b> (ho do hàn, đờm trắng loãng): Bách bộ, Cát cánh, Hạnh nhân, La bặc tử, Tử uyển, Bạch quả, Khoản đông hoa",
    "extra": "Ho nhiệt (đờm vàng, khát) dùng Thanh phế. Ho hàn (đờm trắng, sợ lạnh) dùng Ôn phế. Tây y thường phân biệt ho có đờm/không, YHCT phân biệt hàn/nhiệt."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Thanh phế chỉ khái — mẹo nhớ 4 vị:<br><br>Bệnh nhân ho đờm vàng, sốt, khát → Thanh phế. Bác sĩ dùng 4 vị: <b>{{c1::Tang bạch bì}}</b> (vỏ rễ dâu — thanh phế, hạ khí, lợi tiểu), <b>{{c1::Tỳ bà diệp}}</b> (lá — thanh phế, hóa đờm, chỉ ẩu), <b>{{c1::Bạch tiền}}</b> (rễ — hạ khí, hóa đờm, chỉ khái), <b>{{c1::Tiền hồ}}</b> (rễ — giáng khí, hóa đờm, trị ho ngoại cảm).",
    "extra": "Câu vần: <b>\"Tang-Tỳ-Bạch-Tiền\"</b>. Tỳ bà diệp = lá chống nôn, vừa trị ho vừa chống nôn."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Ôn phế chỉ khái — mẹo nhớ 7 vị:<br><br>Bệnh nhân ho đờm trắng loãng, sợ lạnh → Ôn phế. Bác sĩ dùng 7 vị: <b>{{c1::Bách bộ}}</b> (rễ — số 1 trị ho mọi loại, sát trùng), <b>{{c1::Cát cánh}}</b> (rễ — dẫn thuốc lên phế, trị họng, hóa đờm), <b>{{c1::Hạnh nhân}}</b> (hạt mơ — hạ khí, chỉ khái, nhuận tràng), <b>{{c1::La bặc tử}}</b> (hạt cải trắng — ôn phế, hóa đờm, tiêu kết), <b>{{c1::Tử uyển}}</b> (rễ — ôn phế, hóa đờm, chỉ khái), <b>{{c1::Bạch quả}}</b> (hạt — liễm phế, trị hen, RẤT ĐỘC, liều nhỏ), <b>{{c1::Khoản đông hoa}}</b> (hoa — ôn phế, hóa đờm, chỉ khái, độc nhẹ).",
    "extra": "Câu vần: <b>\"Bách-Cát-Hạnh-La-Tử-Bạch-Khoản\"</b>. Bách bộ + Cát cánh = cặp chỉ khái kinh điển (Tô Hợp Hương Tố). Bạch quả dùng cẩn thận, có thể gây co giật."
})

# --- NHÓM 11: TIÊU THỰC (5 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm TIÊU THỰC (thuốc giúp tiêu hóa, ăn ngon) gồm những phân nhóm nào?",
    "back": "1 phân nhóm, 5 vị:<br>• <b>Tiêu thực đạo trệ</b>: Sơn tra, Mạch nha, Cốc nha, Kê nội kim, Thần khúc",
    "extra": "Hay dùng cho trẻ em biếng ăn, người ăn uống không tiêu. 5 vị đều là vị dân gian, an toàn."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Tiêu thực đạo trệ — mẹo nhớ 5 vị:<br><br>Bệnh nhân ăn không tiêu, đầy bụng, biếng ăn. Bác sĩ dùng 5 vị <b>\"tiêu hóa cổ điển\"</b>: <b>{{c1::Sơn tra}}</b> (quả táo mèo — tiêu thịt, dạ dày), <b>{{c1::Mạch nha}}</b> (mầm lúa mạch — tiêu tinh bột, kiện tỳ, bổ sữa), <b>{{c1::Cốc nha}}</b> (mầm gạo — tiêu tinh bột, kiện tỳ), <b>{{c1::Kê nội kim}}</b> (màng mề gà — tiêu đạo, trị cam tích trẻ em), <b>{{c1::Thần khúc}}</b> (men rượu — tiêu đạo, kiện tỳ, tổng hợp).",
    "extra": "Câu vần: <b>\"Sơn-Mạch-Cốc-Kê-Thần\"</b>. Sơn tra chuyên tiêu thịt, Mạch nha chuyên tiêu tinh bột, Kê nội kim chuyên cho trẻ em cam tích."
})

# --- NHÓM 12: TỨC HÃN (7 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm TỨC HÃN (thuốc chống ra mồ hôi) gồm những phân nhóm nào?",
    "back": "2 phân nhóm, 7 vị:<br>• <b>Ôn lý tức hãn</b> (mồ hôi do dương hư, lạnh): Can khương, Thảo quả, Ngô thù du, Cao lương khương, Lệ chi hạch<br>• <b>Hỗ trợ dương vận nghịch</b> (mồ hôi do dương thoát): Phụ tử chế, Nhục quế",
    "extra": "LƯU Ý: TỨC HÃN = cầm mồ hôi do dương hư/dương thoát (trong YHCT gọi là tự hãn - ra mồ hôi tự nhiên, hoặc đạo hãn - mồ hôi trộm do dương hư). Phân biệt với LIỄM HÃN (nhóm Cố sáp) — cả 2 đều cầm mồ hôi nhưng Tức hãn dùng thuốc ôn để hồi dương, Liễm hãn dùng thuốc thu liễm."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Ôn lý tức hãn — mẹo nhớ 5 vị:<br><br>Bệnh nhân dương hư, sợ lạnh, ra mồ hôi lạnh. Bác sĩ dùng 5 vị <b>\"ôn trung cầm mồ hôi\"</b>: <b>{{c1::Can khương}}</b> (gừng khô — ôn trung, hồi dương, trị mồ hôi lạnh, đau bụng lạnh), <b>{{c1::Thảo quả}}</b> (quả thảo quả — ôn trung, táo thấp, trị sốt rét, đờm), <b>{{c1::Ngô thù du}}</b> (quả ngô thù — ôn trung, tán hàn, chỉ ẩu, đau đầu), <b>{{c1::Cao lương khương}}</b> (riềng — ôn vị, tán hàn, chỉ thống), <b>{{c1::Lệ chi hạch}}</b> (hạt vải — ôn trung, lý khí, thống kinh).",
    "extra": "Câu vần: <b>\"Can-Thảo-Ngô-Cao-Lệ\"</b>. Can khương = vua ôn trung tán hàn, cầm mồ hôi lạnh."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Hỗ trợ dương vận nghịch — mẹo nhớ 2 vị:<br><br>Bệnh nhân dương thoát nặng, mồ hôi đầm đìa, chân tay lạnh, mạch vi. Bác sĩ dùng 2 vị <b>\"hồi dương cứu nghịch\"</b>: <b>{{c1::Phụ tử chế}}</b> (con ô đầu chế — hồi dương cứu nghịch, RẤT ĐỘC nếu dùng sống, liều 1.5-4.5g) và <b>{{c1::Nhục quế}}</b> (vỏ quế — bổ hỏa, trợ dương, tán hàn, thông kinh).",
    "extra": "Câu vần: <b>\"Phụ-Quế\"</b>. Phụ tử chế + Nhục quế = cặp kinh điển (Sâm Phụ Thang, Tứ Nghịch Thang)."
})

# --- NHÓM 13: BÌNH CAN TỨC PHONG (8 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm BÌNH CAN TỨC PHONG (thuốc trị chóng mặt, co giật, run) gồm những phân nhóm nào?",
    "back": "1 phân nhóm, 8 vị:<br>• <b>Bình can tức phong nội phong</b>: Câu đằng, Thiên ma, Bạch tật lê, Tang ký sinh, Ngô công, Toàn yết, Cương tàm, Thuyền thoái",
    "extra": "Nội phong = phong do can thận âm hư sinh ra (co giật, run, liệt nửa người). Bình can = hạ can dương, tức phong = dừng phong co giật."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Bình can tức phong — mẹo nhớ 8 vị:<br><br>Bệnh nhân chóng mặt, run tay, co giật. Bác sĩ dùng 8 vị <b>\"4 thực vật + 4 động vật\"</b>:<br><i>Thực vật:</i><br>• <b>{{c1::Câu đằng}}</b> (dây câu đằng — thanh can, tức phong, hạ áp)<br>• <b>{{c1::Thiên ma}}</b> (củ — bình can, tức phong, trị chóng mặt, đau đầu)<br>• <b>{{c1::Bạch tật lê}}</b> (quả — bình can, sáng mắt, trị đau đầu)<br>• <b>{{c1::Tang ký sinh}}</b> (tầm gửi dâu — bổ can thận, an thai, trừ phong thấp)<br><i>Động vật:</i><br>• <b>{{c1::Ngô công}}</b> (con rết — tức phong, giải độc, trị co giật, độc)<br>• <b>{{c1::Toàn yết}}</b> (con bọ cạp — tức phong, thống kinh, độc)<br>• <b>{{c1::Cương tàm}}</b> (con tằm — tức phong, hóa đờm, tán kết)<br>• <b>{{c1::Thuyền thoái}}</b> (xác ve sầu — tức phong, thanh nhiệt, phát ban)",
    "extra": "Câu vần: <b>\"Câu-Thiên-Tật-Tang-Ngô-Toàn-Cương-Thuyền\"</b>. Thiên ma + Câu đằng = cặp bình can tức phong kinh điển (Thiên Ma Câu Đằng Ẩm)."
})

# --- NHÓM 14: HÀNH KHÍ (13 vị) ---
deck1_cards.append({
    "type": "basic",
    "front": "Nhóm HÀNH KHÍ (thuốc làm thông khí, giải uất) gồm những phân nhóm nào?",
    "back": "2 phân nhóm, 13 vị:<br>• <b>Hành khí giải uất</b> (khí trệ, đau ngực, bụng chướng): Hậu phác, Thanh bì, Trần bì, Mộc hương, Hương phụ, Sa nhân, Ô dược, Chỉ xác<br>• <b>Phá khí giáng nghịch</b> (khí nghịch lên, nôn, ợ): Chỉ thực, Chỉ xác, Đại phúc bì, Trầm hương, Thị đế",
    "extra": "Hành khí = thông khí, giải uất. Phá khí = phá khí mạnh, kéo khí nghịch xuống. Chỉ xác thuộc cả 2 phân nhóm."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Hành khí giải uất — mẹo nhớ 8 vị:<br><br>Bệnh nhân khí trệ: đau ngực, bụng chướng, stress. Bác sĩ dùng 8 vị <b>\"hành khí kinh điển\"</b>: <b>{{c1::Hậu phác}}</b> (vỏ — hạ khí, táo thấp, tiêu đờm), <b>{{c1::Thanh bì}}</b> (vỏ quả xanh — sơ can, phá khí, tiêu đờm), <b>{{c1::Trần bì}}</b> (vỏ quýt — lý khí, kiện tỳ, hóa đờm), <b>{{c1::Mộc hương'''</b> (rễ — hành khí, chỉ thống, tỳ vị), <b>{{c1::Hương phụ}}</b> (củ — sơ can, điều kinh, quân dược khí), <b>{{c1::Sa nhân}}</b> (quả — hành khí, ôn trung, trị tỳ vị), <b>{{c1::Ô dược}}</b> (rễ — hành khí, chỉ thống, ôn thận), <b>{{c1::Chỉ xác}}</b> (quả trấp non — phá khí, tiêu tích, thông trường).",
    "extra": "Câu vần: <b>\"Hậu-Thanh-Trần-Mộc-Hương-Sa-Ô-Chỉ\"</b>. Hương phụ = quân dược khí, chuyên sơ can điều kinh."
})

deck1_cards.append({
    "type": "cloze",
    "text": "Phá khí giáng nghịch — mẹo nhớ 5 vị:<br><br>Bệnh nhân khí nghịch: nôn, ợ, đầy bụng trên. Bác sĩ dùng 5 vị <b>\"phá khí, giáng nghịch\"</b>: <b>{{c1::Chỉ thực}}</b> (quả trấp non — phá khí, tiêu tích, mạnh hơn Chỉ xác), <b>{{c1::Chỉ xác}}</b> (vỏ quả trấp — hành khí, tiêu tích, tiêu đờm), <b>{{c1::Đại phúc bì}}</b> (vỏ dừa — hành khí, lợi thủy, tiêu phù), <b>{{c1::Trầm hương}}</b> (gỗ trầm — hành khí, giáng nghịch, ôn thận, đắt), <b>{{c1::Thị đế}}</b> (mỏ — giáng khí, chỉ ẩu, chống nôn).",
    "extra": "Câu vần: <b>\"Chỉ-Chỉ-Đại-Trầm-Thị\"</b>. Chỉ thực + Chỉ xác = cặp Chỉ Thực Thang. Thị đế = chống nôn, vị dân gian."
})

# ============================================================
# DECK 2: Tra cứu ngược - Front=tên thuốc, Back=nhóm
# ============================================================
deck2_cards = []
HERB_TO_GROUP = {
    # GIẢI BIỂU
    "Ma hoàng": "GIẢI BIỂU → Tân ôn giải biểu (cảm phong hàn, sợ lạnh, không mồ hôi)",
    "Quế chi": "GIẢI BIỂU → Tân ôn giải biểu (cảm phong hàn, biểu hư, có mồ hôi)",
    "Tế tân": "GIẢI BIỂU → Tân ôn giải biểu (đau răng, đau đầu do hàn)",
    "Bạch chỉ": "GIẢI BIỂU → Tân ôn giải biểu (đau đầu vùng trán, viêm xoang)",
    "Sinh khương": "GIẢI BIỂU → Tân ôn giải biểu (gừng tươi — ấm vị, chống nôn)",
    "Tía tô": "GIẢI BIỂU → Tân ôn giải biểu (cảm + nôn, an toàn cho bà bầu)",
    "Hương nhu": "GIẢI BIỂU → Tân ôn giải biểu (cảm nắng mùa hè)",
    "Khương hoạt": "GIẢI BIỂU → Tân ôn giải biểu (phong thấp, đau đầu đỉnh)",
    "Phòng phong": "GIẢI BIỂU → Tân ôn giải biểu (phong thấp, tay chân tê, đau đầu)",
    "Tân giao": "GIẢI BIỂU → Tân ôn giải biểu (phong thấp đau nhức xương khớp)",
    "Bạc hà": "GIẢI BIỂU → Tân lương giải biểu (sốt nhẹ, đau họng, nhức đầu thái dương)",
    "Cúc hoa": "GIẢI BIỂU → Tân lương giải biểu (đau đầu, chóng mặt, mắt đỏ)",
    "Tang diệp": "GIẢI BIỂU → Tân lương giải biểu (ho khan, sốt nhẹ, mắt đỏ)",
    "Mạn kinh tử": "GIẢI BIỂU → Tân lương giải biểu (đau đầu, mắt đỏ, phong nhiệt)",
    "Ngưu bàng tử": "GIẢI BIỂU → Tân lương giải biểu (sốt, họng sưng, phát ban)",
    "Cát cánh": "GIẢI BIỂU → Tân lương giải biểu (trị họng, dẫn thuốc lên phế)",
    "Sài hồ": "GIẢI BIỂU → Tân lương giải biểu (sốt cao, sốt rét, kinh nguyệt không đều)",
    "Thăng ma": "GIẢI BIỂU → Tân lương giải biểu (sốt, họng đau, sa giáng)",
    "Phù bình": "GIẢI BIỂU → Tân lương giải biểu (phong nhiệt, sốt, khó thở)",
    # THANH NHIỆT
    "Thạch cao": "THANH NHIỆT → Thanh nhiệt tả hỏa (sốt cao, khát nước) HOẶC Thanh nhiệt giải thử (trúng nắng)",
    "Tri mẫu": "THANH NHIỆT → Thanh nhiệt tả hỏa (hỗ trợ Thạch cao, sốt + táo)",
    "Chi tử": "THANH NHIỆT → Thanh nhiệt tả hỏa (sốt bứt rứt, nước tiểu vàng)",
    "Hạ khô thảo": "THANH NHIỆT → Thanh nhiệt tả hỏa (sốt, mắt đỏ, huyết áp cao)",
    "Thảo quyết minh": "THANH NHIỆT → Thanh nhiệt tả hỏa (mắt đỏ, táo bón, hạ mỡ)",
    "Trúc diệp": "THANH NHIỆT → Thanh nhiệt tả hỏa (sốt khát, tâm phiền, lá tre trúc)",
    "Lô căn": "THANH NHIỆT → Thanh nhiệt tả hỏa (sốt khát, nôn — rễ sậy)",
    "Tây qua": "THANH NHIỆT → Thanh nhiệt tả hỏa / giải thử (giải khát, vỏ dưa hấu)",
    "Lá sen": "THANH NHIỆT → Thanh nhiệt tả hỏa / giải thử (thanh tâm hỏa, an thần)",
    "Huyền sâm": "THANH NHIỆT → Thanh nhiệt lương huyết (thanh nhiệt huyết, dưỡng âm, trị họng)",
    "Sinh địa": "THANH NHIỆT → Thanh nhiệt lương huyết / giải thử (dưỡng âm, mát huyết)",
    "Xích thược": "THANH NHIỆT → Thanh nhiệt lương huyết (mát huyết, hoạt huyết, ban đỏ)",
    "Mẫu đơn bì": "THANH NHIỆT → Thanh nhiệt lương huyết (mát huyết, hoạt huyết, kinh nguyệt)",
    "Địa cốt bì": "THANH NHIỆT → Thanh nhiệt lương huyết (sốt âm hư, ho lao)",
    "Kim ngân": "THANH NHIỆT → Thanh nhiệt giải độc (hoa kim ngân — sốt, mụn nhọt, viêm họng)",
    "Liên kiều": "THANH NHIỆT → Thanh nhiệt giải độc (sốt, mụn nhọt, viêm)",
    "Bồ công anh": "THANH NHIỆT → Thanh nhiệt giải độc (mụn nhọt, viêm vú, viêm mắt)",
    "Sài đất": "THANH NHIỆT → Thanh nhiệt giải độc (mụn nhọt trẻ em, viêm da)",
    "Xa can": "THANH NHIỆT → Thanh nhiệt giải độc (họng sưng đau, viêm phổi)",
    "Hoàng bá": "THANH NHIỆT → Thanh nhiệt giải độc / trừ thấp (thấp nhiệt hạ tiêu, tiểu buốt rắt, mồ hôi trộm)",
    "Hoàng cầm": "THANH NHIỆT → Thanh nhiệt giải độc / trừ thấp (sốt, viêm phổi, vàng da, lỵ)",
    "Hoàng liên": "THANH NHIỆT → Thanh nhiệt giải độc / trừ thấp (viêm dạ dày, lỵ, mụn)",
    "Khổ sâm": "THANH NHIỆT → Thanh nhiệt giải độc / trừ thấp (mụn nhọt, lỵ, viêm da, thấp chẩn)",
    "Hương nhu-tt": "THANH NHIỆT → Thanh nhiệt giải thử (cảm nắng mùa hè, ra mồ hôi)",
    "Hoắc hương": "THANH NHIỆT → Thanh nhiệt giải thử (nôn, tiêu chảy do thử thấp)",
    "Bạch biển đậu": "THANH NHIỆT → Thanh nhiệt giải thử (tỳ vị, trúng thử, tiêu chảy — đậu ván trắng)",
    # BỔ
    "Nhân sâm": "BỔ → Bổ khí (đại bổ nguyên khí, sâm chính)",
    "Đẳng sâm": "BỔ → Bổ khí (sâm rẻ tiền thay Nhân sâm, bổ khí)",
    "Hoàng kỳ": "BỔ → Bổ khí (bổ khí + thăng dương, ra mồ hôi tự ra, phù)",
    "Cam thảo": "BỔ → Bổ khí (kiện tỳ, điều hòa các vị)",
    "Đại táo": "BỔ → Bổ khí (bổ tỳ, dưỡng huyết, an thần — táo đỏ)",
    "Hoài sơn": "BỔ → Bổ khí (củ mài — bổ tỳ vị, phế, thận)",
    "Bạch truật": "BỔ → Bổ khí (kiện tỳ, táo thấp, an thai)",
    "Đương quy": "BỔ → Bổ huyết (đầu bổ huyết, đuôi hoạt huyết)",
    "Thục địa": "BỔ → Bổ huyết (đại bổ huyết, chữa cốt, địa hoàng chín)",
    "Bạch thược": "BỔ → Bổ huyết (dưỡng huyết, liễm âm, thược dược trắng)",
    "A giao": "BỔ → Bổ huyết (keo da lừa — bổ huyết, chỉ huyết)",
    "Tử hà xa": "BỔ → Bổ huyết (nhau thai — bổ huyết, ích tinh)",
    "Tang thầm": "BỔ → Bổ huyết (quả dâu — bổ huyết, sinh tân dịch, tóc bạc sớm)",
    "Ưng nhận": "BỔ → Bổ huyết (rễ cỏ tranh — cùng Tang thầm trị tóc bạc sớm)",
    "Nữ trinh tử": "BỔ → Bổ huyết (bổ can thận, sáng mắt, tóc bạc)",
    "Hà thủ ô": "BỔ → Bổ huyết / Bổ âm (bổ can thận, tóc đen, táo bón)",
    "Kỳ hồ": "BỔ → Bổ huyết (kê huyết đằng — bổ huyết, hoạt huyết)",
    "Sa sâm": "BỔ → Bổ âm (dưỡng âm, thanh phế, sâm cát)",
    "Thiên môn": "BỔ → Bổ âm (dưỡng âm, thanh nhiệt, thiên môn đông)",
    "Mạch môn": "BỔ → Bổ âm (dưỡng vị âm, phế âm, mạch môn đông)",
    "Cẩu kỷ tử": "BỔ → Bổ âm (bổ can thận, sáng mắt, kỷ tử)",
    "Quy bản": "BỔ → Bổ âm (mai rùa — bổ thận âm, tư âm tiềm dương)",
    "Miết giáp": "BỔ → Bổ âm (mai ba ba — bổ thận âm, tiềm dương, mềm cứng)",
    "Thạch hộc": "BỔ → Bổ âm (hoàng thảo — bổ thận, dưỡng vị âm)",
    "Ngọc trúc": "BỔ → Bổ âm (dưỡng âm, nhuận táo)",
    "Bách hợp": "BỔ → Bổ âm (hoa bách hợp — dưỡng phế âm, an thần, trị ho)",
    "Lộc nhung": "BỔ → Bổ dương (sừng hươu non — số 1 bổ dương, ích tinh huyết)",
    "Nhục thung dung": "BỔ → Bổ dương (bổ thận dương, nhuận tràng, tẩm tía)",
    "Cốt toái bổ": "BỔ → Bổ dương (tắc kè đá — bổ thận, lành xương, đau lưng)",
    "Thủ ty tử": "BỔ → Bổ dương (hạt tơ — bổ thận, dưỡng gan, sáng mắt, an thai)",
    "Đỗ trọng": "BỔ → Bổ dương (vỏ cây — bổ thận, an thai, hạ áp)",
    "Tục đoạn": "BỔ → Bổ dương (rễ — bổ thận, an thai, nối gân xương)",
    "Ba kích": "BỔ → Bổ dương (rễ — bổ thận dương, mạnh gân cốt)",
    "Tiên mao": "BỔ → Bổ dương (củ — bổ thận dương, trừ hàn thấp)",
    "Cốc tinh": "BỔ → Bổ dương (hạt — bổ thận, sáng mắt)",
    "Ích trí nhân": "BỔ → Bổ dương (quả ích trí — ôn thận, cố tinh, cầm tiểu)",
    "Tang phiêu tiêu": "BỔ → Bổ dương / Cố sáp sáp niệu (tổ bọ ngựa trên cây dâu — cố tinh, sáp niệu)",
    "Sơn thù du": "BỔ → Bổ dương / Cố sáp sáp niệu (bổ can thận, cố tinh, cầm mồ hôi)",
    # TẢ HẠ
    "Đại hoàng": "TẢ HẠ → Hàn hạ (vua tả hạ — tả nhiệt thông tiện, hoạt huyết)",
    "Mang tiêu": "TẢ HẠ → Hàn hạ (natri sunfat — hạ mạnh, phá kết tích)",
    "Lô hội": "TẢ HẠ → Hàn hạ (nha đam — tả nhiệt, thanh can, mụn nhọt)",
    "Phan tả diệp": "TẢ HẠ → Hàn hạ (lá — nhuận tả, dùng trong X-quang ruột)",
    "Ba đậu": "TẢ HẠ → Nhiệt hạ (hạt — hạ hàn tích, RẤT ĐỘC, chống chỉ định có thai)",
    "Lưu hoàng": "TẢ HẠ → Nhiệt hạ (lưu huỳnh — ôn thông tiện, trị ghẻ)",
    "Ma nhân": "TẢ HẠ → Nhuận hạ (hạt gai dầu — nhuận tràng, dưỡng huyết, bổ)",
    "Mật ong": "TẢ HẠ → Nhuận hạ (nhuận tràng, dưỡng vị, an thần)",
    "Chút chít": "TẢ HẠ → Nhuận hạ (lá — nhuận tả)",
    "Muồng trâu": "TẢ HẠ → Nhuận hạ (lá — nhuận tả, hạ áp nhẹ)",
    "Vỏ cây đại": "TẢ HẠ → Nhuận hạ (nhuận tả, lợi tiểu)",
    # LỢI NIỆU
    "Phục linh": "LỢI NIỆU → Lợi thủy thấm thấp (nấm — lợi thấm, kiện tỳ, an thần, quân dược)",
    "Trư linh": "LỢI NIỆU → Lợi thủy thấm thấp (nấm — lợi thủy mạnh hơn Phục linh)",
    "Trạch tả": "LỢI NIỆU → Lợi thủy thấm thấp (củ — lợi thấm, thanh nhiệt)",
    "Ý dĩ": "LỢI NIỆU → Lợi thủy thấm thấp (hạt bo bo — lợi thấm, kiện tỳ, trừ mủ)",
    "Xa tiền tử": "LỢI NIỆU → Lợi thủy thấm thấp (hạt mã đề — lợi thủy, trị tiểu buốt rắt, sỏi)",
    "Mộc thông": "LỢI NIỆU → Lợi thủy thấm thấp (thân — lợi thủy, thông kinh, thanh tâm)",
    "Hoạt thạch": "LỢI NIỆU → Lợi thủy thấm thấp (bột talc — lợi thủy, thanh nhiệt)",
    "Tỳ giải": "LỢI NIỆU → Lợi thủy thấm thấp (củ — lợi thấp, phân thanh trọc)",
    "Kim tiền thảo": "LỢI NIỆU → Lợi thủy thấm thấp (cỏ — trị sỏi tiết niệu, mật)",
    "Phong kỳ": "LỢI NIỆU → Lợi thủy thấm thấp (lợi thủy, trừ phong thấp)",
    "Đậu đỏ": "LỢI NIỆU → Lợi thủy thấm thấp (hạt — lợi thủy, tiêu thũng)",
    "Thông thảo": "LỢI NIỆU → Lợi thủy thấm thấp (lõi thông — lợi thủy, thông sữa)",
    "Cam toại": "LỢI NIỆU → Thực thủy (củ — tả thủy thũng, độc)",
    "Nguyên hoa": "LỢI NIỆU → Thực thủy (hoa — tả thủy, trục đờm, độc)",
    "Đại kích": "LỢI NIỆU → Thực thủy (rễ — tả thủy, phá kết, độc)",
    "Bạt kế": "LỢI NIỆU → Thực thủy (rễ — tả thủy, tiêu mủ, độc)",
    # AN THẦN
    "Toan táo nhân": "AN THẦN → Dưỡng tâm an thần (hạt táo chua — số 1 trị mất ngủ, dưỡng tâm)",
    "Bá tử nhân": "AN THẦN → Dưỡng tâm an thần (hạt trắc bách — dưỡng tâm, nhuận tràng)",
    "Vông nem": "AN THẦN → Dưỡng tâm an thần (lá — an thần, trị mất ngủ)",
    "Viễn chí": "AN THẦN → Dưỡng tâm an thần (rễ — an thần, ích trí, trừ đờm)",
    "Long nhãn": "AN THẦN → Dưỡng tâm an thần (cùi nhãn — bổ huyết, an thần)",
    "Lạc tiên": "AN THẦN → Dưỡng tâm an thần (dây — an thần dân gian, trị mất ngủ)",
    "Chân sa": "AN THẦN → Bình can tiềm dương (thuỷ ngân — trấn tâm an thần, độc, ít dùng)",
    "Mẫu lệ": "AN THẦN / Cố sáp liễm hãn → Bình can tiềm dương / Liễm hãn (vỏ hàu — tiềm dương, liễm hãn, cố tinh)",
    "Trân châu mẫu": "AN THẦN → Bình can tiềm dương (mẹ ngọc trai — bình can, an thần, sáng mắt)",
    "Hổ phách": "AN THẦN → Bình can tiềm dương (hổ phách — trấn tâm, lợi tiểu, hoạt huyết)",
    # CHỈ HUYẾT
    "Tam thất": "CHỈ HUYẾT → Chỉ ứ chỉ huyết (củ — số 1 cầm máu do ứ, tiêu sưng, bổ huyết)",
    "Bạch cập": "CHỈ HUYẾT → Chỉ ứ chỉ huyết (củ lan — cầm máu, sinh cơ, bỏng, lở)",
    "Huyết dư thán": "CHỈ HUYẾT → Chỉ ứ chỉ huyết (tóc đốt — cầm máu, lợi tiểu)",
    "Ngẫu tiết": "CHỈ HUYẾT → Chỉ ứ chỉ huyết (đốt ngẫu — cầm máu, băng huyết)",
    "Trắc bá diệp": "CHỈ HUYẾT → Thanh nhiệt chỉ huyết (lá — cầm máu, mát huyết, ho ra máu, kiết lỵ)",
    "Hoa hòe": "CHỈ HUYẾT → Thanh nhiệt chỉ huyết (hoa — cầm máu, hạ áp, trị trĩ)",
    "Hạ liên thảo": "CHỈ HUYẾT → Thanh nhiệt chỉ huyết (cỏ cứt lợn — cầm máu, giải độc)",
    "Bạch mao căn": "CHỈ HUYẾT → Thanh nhiệt chỉ huyết (rễ cỏ tranh — cầm máu, lợi tiểu, thanh nhiệt)",
    "Ô tặc cốt": "CHỈ HUYẾT → Kiện tỳ chỉ huyết (mai mực — cầm máu, cố toan, loét dạ dày)",
    "Ngẫu bì": "CHỈ HUYẾT → Kiện tỳ chỉ huyết (vỏ củ ấu — cầm máu, thu liễm)",
    # CỐ SÁP
    "Tiểu mạch": "CỐ SÁP → Liễm hãn (lúa mì non — liễm hãn, dưỡng tâm, thanh nhiệt)",
    "Ngũ vị tử": "CỐ SÁP → Liễm hãn (5 vị — liễm hãn, sinh tân, bổ thận, an thần)",
    "Kim anh tử": "CỐ SÁP → Cố tinh sáp niệu (quả tầm xuân — sáp trường, cố tinh)",
    "Khiếm thực": "CỐ SÁP → Cố tinh sáp niệu (hạt súng — cố tinh, kiện tỳ, trừ thấp)",
    "Liên nhục": "CỐ SÁP → Cố tinh sáp niệu (hạt sen — cố tinh, kiện tỳ, an thần)",
    "Ô mai": "CỐ SÁP → Sáp trường chỉ tả (mận đen muối — sáp trường, chỉ tả, sinh tân, trị giun)",
    "Thạch lựu bì": "CỐ SÁP → Sáp trường chỉ tả (vỏ lựu — sáp trường, chỉ huyết, trị sán dây)",
    "Kha tử": "CỐ SÁP → Sáp trường chỉ tả (quả kha tử — sáp trường, liễm phế, trị ho, khàn tiếng)",
    # TRỪ TÀM
    "Thược nhệ": "TRỪ TÀM → Thanh hóa nhiệt tàm (hạt — sát giun, nhuận tràng)",
    "Qua lâu thực": "TRỪ TÀM → Thanh hóa nhiệt tàm (hạt gấc — sát giun, thu liễm)",
    "Bối mẫu": "TRỪ TÀM → Thanh hóa nhiệt tàm (xuyên bối mẫu — thanh nhiệt, trừ đờm, giảm đau)",
    "Bạch hạ chỉ": "TRỪ TÀM → Ôn hóa hàn tàm (rễ — trị đau đầu, sát trùng)",
    "Thiên nam tinh": "TRỪ TÀM → Ôn hóa hàn tàm (củ — ôn hóa hàn tàm, trị đờm, phong)",
    "Bạch giới tử": "TRỪ TÀM → Ôn hóa hàn tàm (hạt — ôn hóa hàn đờm, tán kết)",
    "Tạo giác": "TRỪ TÀM → Ôn hóa hàn tàm (quả bồ kết — sát trùng, khử đờm, thông khiếu)",
    "Bạch phụ tử": "TRỪ TÀM → Ôn hóa hàn tàm (củ — ôn trung, tán hàn, trị đau đầu)",
    # CHỈ KHÁI
    "Tang bạch bì": "CHỈ KHÁI → Thanh phế chỉ khái (vỏ rễ dâu — thanh phế, hạ khí, lợi tiểu)",
    "Tỳ bà diệp": "CHỈ KHÁI → Thanh phế chỉ khái (lá — thanh phế, hóa đờm, chỉ ẩu, chống nôn)",
    "Bạch tiền": "CHỈ KHÁI → Thanh phế chỉ khái (rễ — hạ khí, hóa đờm, chỉ khái)",
    "Tiền hồ": "CHỈ KHÁI → Thanh phế chỉ khái (rễ — giáng khí, hóa đờm, trị ho ngoại cảm)",
    "Bách bộ": "CHỈ KHÁI → Ôn phế chỉ khái (rễ — số 1 trị ho mọi loại, sát trùng)",
    "Hạnh nhân": "CHỈ KHÁI → Ôn phế chỉ khái (hạt mơ — hạ khí, chỉ khái, nhuận tràng)",
    "La bặc tử": "CHỈ KHÁI → Ôn phế chỉ khái (hạt cải trắng — ôn phế, hóa đờm, tiêu kết)",
    "Tử uyển": "CHỈ KHÁI → Ôn phế chỉ khái (rễ — ôn phế, hóa đờm, chỉ khái)",
    "Bạch quả": "CHỈ KHÁI → Ôn phế chỉ khái (hạt — liễm phế, trị hen, RẤT ĐỘC, liều nhỏ)",
    "Khoản đông hoa": "CHỈ KHÁI → Ôn phế chỉ khái (hoa — ôn phế, hóa đờm, chỉ khái, độc nhẹ)",
    # TIÊU THỰC
    "Sơn tra": "TIÊU THỰC → Tiêu thực đạo trệ (quả táo mèo — tiêu thịt, dạ dày)",
    "Mạch nha": "TIÊU THỰC → Tiêu thực đạo trệ (mầm lúa mạch — tiêu tinh bột, kiện tỳ, bổ sữa)",
    "Cốc nha": "TIÊU THỰC → Tiêu thực đạo trệ (mầm gạo — tiêu tinh bột, kiện tỳ)",
    "Kê nội kim": "TIÊU THỰC → Tiêu thực đạo trệ (màng mề gà — tiêu đạo, trị cam tích trẻ em)",
    "Thần khúc": "TIÊU THỰC → Tiêu thực đạo trệ (men rượu — tiêu đạo, kiện tỳ, tổng hợp)",
    # TỨC HÃN
    "Can khương": "TỨC HÃN → Ôn lý tức hãn (gừng khô — ôn trung, hồi dương, trị mồ hôi lạnh, đau bụng lạnh)",
    "Thảo quả": "TỨC HÃN → Ôn lý tức hãn (quả thảo quả — ôn trung, táo thấp, trị sốt rét, đờm)",
    "Ngô thù du": "TỨC HÃN → Ôn lý tức hãn (quả ngô thù — ôn trung, tán hàn, chỉ ẩu, đau đầu)",
    "Cao lương khương": "TỨC HÃN → Ôn lý tức hãn (riềng — ôn vị, tán hàn, chỉ thống)",
    "Lệ chi hạch": "TỨC HÃN → Ôn lý tức hãn (hạt vải — ôn trung, lý khí, thống kinh)",
    "Phụ tử chế": "TỨC HÃN → Hỗ trợ dương vận nghịch (con ô đầu chế — hồi dương cứu nghịch, RẤT ĐỘC nếu sống)",
    "Nhục quế": "TỨC HÃN → Hỗ trợ dương vận nghịch (vỏ quế — bổ hỏa, trợ dương, tán hàn, thông kinh)",
    # BÌNH CAN TỨC PHONG
    "Câu đằng": "BÌNH CAN TỨC PHONG (dây câu đằng — thanh can, tức phong, hạ áp)",
    "Thiên ma": "BÌNH CAN TỨC PHONG (củ — bình can, tức phong, chóng mặt, đau đầu)",
    "Bạch tật lê": "BÌNH CAN TỨC PHONG (quả — bình can, sáng mắt, đau đầu)",
    "Tang ký sinh": "BÌNH CAN TỨC PHONG (tầm gửi dâu — bổ can thận, an thai, trừ phong thấp)",
    "Ngô công": "BÌNH CAN TỨC PHONG (con rết — tức phong, giải độc, co giật, độc)",
    "Toàn yết": "BÌNH CAN TỨC PHONG (con bọ cạp — tức phong, thống kinh, độc)",
    "Cương tàm": "BÌNH CAN TỨC PHONG (con tằm — tức phong, hóa đờm, tán kết)",
    "Thuyền thoái": "BÌNH CAN TỨC PHONG (xác ve sầu — tức phong, thanh nhiệt, phát ban)",
    # HÀNH KHÍ
    "Hậu phác": "HÀNH KHÍ → Hành khí giải uất (vỏ — hạ khí, táo thấp, tiêu đờm)",
    "Thanh bì": "HÀNH KHÍ → Hành khí giải uất (vỏ quả xanh — sơ can, phá khí, tiêu đờm)",
    "Trần bì": "HÀNH KHÍ → Hành khí giải uất (vỏ quýt — lý khí, kiện tỳ, hóa đờm)",
    "Mộc hương": "HÀNH KHÍ → Hành khí giải uất (rễ — hành khí, chỉ thống, tỳ vị)",
    "Hương phụ": "HÀNH KHÍ → Hành khí giải uất (củ — sơ can, điều kinh, quân dược khí)",
    "Sa nhân": "HÀNH KHÍ → Hành khí giải uất (quả — hành khí, ôn trung, trị tỳ vị)",
    "Ô dược": "HÀNH KHÍ → Hành khí giải uất (rễ — hành khí, chỉ thống, ôn thận)",
    "Chỉ xác": "HÀNH KHÍ → Hành khí giải uất / Phá khí giáng nghịch (vỏ quả trấp — hành khí, tiêu tích)",
    "Chỉ thực": "HÀNH KHÍ → Phá khí giáng nghịch (quả trấp non — phá khí, tiêu tích, mạnh hơn Chỉ xác)",
    "Đại phúc bì": "HÀNH KHÍ → Phá khí giáng nghịch (vỏ dừa — hành khí, lợi thủy, tiêu phù)",
    "Trầm hương": "HÀNH KHÍ → Phá khí giáng nghịch (gỗ trầm — hành khí, giáng nghịch, ôn thận, đắt)",
    "Thị đế": "HÀNH KHÍ → Phá khí giáng nghịch (mỏ — giáng khí, chỉ ẩu, chống nôn)",
    "Cát cánh-2": "GIẢI BIỂU + CHỈ KHÁI (rễ — dẫn thuốc lên phế, trị họng, hóa đờm, kiêm 2 nhóm)",
}

# Build deck 2
for name, info in HERB_TO_GROUP.items():
    # Skip suffix variants in key but use base name for front
    base = name.split("-")[0]
    front = base
    back = info
    extra = "Tra cứu ngược: tên thuốc → nhóm. Dùng để test recall khi đi lâm sàng gặp tên thuốc lạ."
    deck2_cards.append({
        "type": "basic",
        "front": front,
        "back": back,
        "extra": extra
    })

# Save both JSON
with open(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\cards_yhct_v2_short.json", "w", encoding="utf-8") as f:
    json.dump(deck1_cards, f, ensure_ascii=False, indent=2)
print(f"Deck 1 (cau chuyen ngan): {len(deck1_cards)} cards")

with open(r"F:\DL\mavisresearch\Bai hoc y khoa\10_Script Python\cards_yhct_reverse.json", "w", encoding="utf-8") as f:
    json.dump(deck2_cards, f, ensure_ascii=False, indent=2)
print(f"Deck 2 (tra cuu nguoc): {len(deck2_cards)} cards")
