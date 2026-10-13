"""
send_exact_text_to_telegram.py
Gửi chính xác 100% nguyên văn bài giảng về RSV và Cúm A vừa viết ở trên vào Telegram bot.
Tự động chia thành các phần dưới 4000 ký tự theo đúng ranh giới phần để không bị lỗi giới hạn độ dài của Telegram.
"""
import os
import sys
import json
import urllib.request
import urllib.parse

CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", "6569183642"))
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()

# NỘI DUNG NGUYÊN VĂN CHÍNH XÁC TỪNG CHỮ CỦA BÀI TRẢ LỜI TRƯỚC
PART_1 = """Trong bức tranh giao ban của khoa bạn (với <b>21 ca RSV</b> và <b>11 ca Cúm A</b> chiếm gần một nửa tổng số bệnh nhi), đây chính là hai "thủ phạm" virus đường hô hấp nguy hiểm và phổ biến nhất ở trẻ em.

Dưới đây là bài giảng lâm sàng chuyên sâu, bóc tách toàn diện từ cơ chế phân tử, biểu hiện tại giường, bẫy tử vong đến phác đồ điều trị chuẩn EBM (AAP, CDC, WHO) cho từng tác nhân:

<code>                     HAI TÁC NHÂN VIRUS HÀNG ĐẦU TẠI KHOA NHI
  ┌──────────────────────────────────────┬──────────────────────────────────────┐
  │ 🫁 1. RSV (Virus Hợp Bào Hô Hấp)     │ 🌡️ 2. CÚM A (Influenza A Virus)      │
  │ • Đích tổn thương: Tiểu phế quản     │ • Đích tổn thương: Toàn bộ biểu mô   │
  │ • Nhóm tuổi: Nhũ nhi & Sơ sinh       │ • Nhóm tuổi: Mọi lứa tuổi, trẻ lớn   │
  │ • Hiểm họa: Tắc nút nhầy & Cơn ngưng │ • Hiểm họa: Bão cytokine, Co giật do │
  │   thở (Apnea) sơ sinh                │   sốt, Viêm phổi hoại tử sau cúm     │
  └──────────────────────────────────────┴──────────────────────────────────────┘</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>PHẦN 1: BỆNH HỌC NHIỄM RSV (RESPIRATORY SYNCYTIAL VIRUS)</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━

RSV thuộc họ Pneumoviridae, là nguyên nhân hàng đầu gây nhiễm trùng đường hô hấp dưới và nhập viện ở trẻ nhũ nhi trên toàn cầu.

<b>1. Sinh lý bệnh & Cơ chế tổn thương mô học</b>
RSV có ái tính đặc biệt với <b>biểu mô đường hô hấp nhỏ (tiểu phế quản &lt; 2 mm)</b>:
• <b>Hòa màng tạo hợp bào (Syncytia):</b> Glycoprotein F (Fusion) trên vỏ virus làm dung hợp màng các tế bào biểu mô lân cận thành các đại tế bào đa nhân khổng lồ (hợp bào).
• <b>Tam chứng tắc nghẽn lòng tiểu phế quản:</b>
  1) Tế bào biểu mô bị hoại tử, bong tróc vào lòng ống dẫn khí.
  2) Phù nề dữ dội thành tiểu phế quản và thâm nhiễm bạch cầu đơn nhân.
  3) Tuyến nhầy tăng tiết dịch nhầy quánh đặc.
  → Hỗn hợp xác tế bào + nhầy đặc tạo thành <b>nút nhầy (mucus plug)</b> bít tắc lòng tiểu phế quản.
• <b>Hậu quả cơ học:</b>
  - <b>Tắc van một chiều (Ball-valve effect):</b> Không khí hít vào được nhưng thở ra bị giữ lại → <b>Ứ khí phế nang (Hyperinflation)</b>.
  - <b>Tắc hoàn toàn lòng ống:</b> Không khí bị hấp thu hết → <b>Xẹp phổi (Atelectasis)</b>, vị trí kinh điển hay gặp nhất là <b>thùy trên phổi phải</b>.

<b>2. Hai kiểu hình lâm sàng kinh điển của RSV</b>

<code>                               HAI KIỂU HÌNH NHIỄM RSV
                                         │
           ┌─────────────────────────────┴─────────────────────────────┐
           ▼                                                           ▼
[KIỂU HÌNH 1: VIÊM TIỂU PHẾ QUẢN CẤP]                     [KIỂU HÌNH 2: CƠN NGỪNG THỞ (APNEA)]
(Trẻ 2 - 12 tháng tuổi)                                   (ĐẶC BIỆT TRẺ SƠ SINH & ĐẺ NON < 2 THÁNG)
• Ngày 1-3: Sổ mũi trong, nghẹt mũi, sốt nhẹ.              • Ngừng thở trung ương đột ngột > 20 giây
• Ngày 4-6 (Đỉnh điểm): Thở nhanh, co kéo rút lõm          • Nhịp tim chậm < 100 lần/phút, tím tái
  lồng ngực dữ dội, cánh mũi phập phồng, đầu gật gù.      • CÓ THỂ XUẤT HIỆN TRƯỚC KHI TRẺ KỊP HO
• Nghe phổi: Ran rít, ran ngáy, ran ẩm nhỏ hạt/ran nổ      HOẶC CO KÉO LỒNG NGỰC!
  mịn thì hít vào. Bú kém do mệt khi thở.                  • Cơ chế: RSV ức chế hành não & thần kinh phế vị.</code>

🚨 <b>BÀI HỌC VÀNG CHO 3 CA SƠ SINH TẠI BUỒNG CC-SS (21, 25, 28 NGÀY TUỔI):</b>
Ở trẻ sơ sinh và trẻ non tháng, trung tâm điều hòa hô hấp tại hành não chưa hoàn thiện. RSV xâm nhập kích thích các thụ thể cảm giác đường thở truyền tín hiệu ức chế qua dây thần kinh X, gây <b>ngừng thở phản xạ</b>. Trẻ có thể ngừng thở và tím tái đột ngột khi đang nằm yên mà chưa hề có tiếng khò khè hay co kéo! <b>Bắt buộc phải gắn monitor theo dõi SpO2 và nhịp tim liên tục.</b>

<b>3. Đối tượng nguy cơ cao diễn tiến nguy kịch do RSV</b>
1) Trẻ đẻ non (&lt; 35 tuần thai, đặc biệt &lt; 29 tuần).
2) Trẻ sơ sinh dưới 2 tháng tuổi.
3) Trẻ mắc <b>Bệnh phổi mạn tính ở trẻ sinh non (Loạn sản phế quản phổi - BPD)</b>.
4) Trẻ mắc <b>Bệnh tim bẩm sinh có luồng thông Trái - Phải lớn hoặc tăng áp phổi</b>.
5) Trẻ suy giảm miễn dịch nặng, bệnh thần kinh - cơ (bại não, teo cơ tủy).

<b>4. Cận lâm sàng & Hình ảnh học</b>
• <b>X-quang ngực:</b>
  - Dấu hiệu ứ khí phế nang 2 bên: Vòm hoành hạ thấp phẳng, lồng ngực hình thùng, các xương sườn nằm ngang, tăng sáng 2 phế trường.
  - Dày thành quanh phế quản (dày thành phế quản rốn phổi).
  - Xẹp phổi dạng dải hoặc xẹp phân thùy (thường gặp thùy trên phải — bẫy: rất dễ nhầm với viêm phổi thùy do phế cầu!).
• <b>Xét nghiệm vi sinh:</b> Test nhanh kháng nguyên RSV hoặc Real-time RT-PCR dịch tỵ hầu (độ nhạy &gt; 95%).

<b>5. Chiến lược điều trị RSV chuẩn EBM (AAP & NICE Guidelines)</b>
RSV là bệnh do virus tự giới hạn, <b>không có thuốc diệt virus đặc hiệu đường uống</b>. Mọi can thiệp điều trị tập trung vào <b>3 TRỤ CỘT HỖ TRỢ</b>:
1) <b>Hỗ trợ hô hấp:</b> Giữ SpO2 ≥ 90-92%, Thở Oxy gọng, HFNC dòng cao, CPAP áp lực dương giữ mở tiểu phế quản.
2) <b>Dinh dưỡng & nước:</b> Chia nhỏ cữ bú, Đặt sonde dạ dày nếu nhịp thở &gt; 60-70 lần/phút, Truyền dịch nếu ăn uống &lt; 50% nhu cầu.
3) <b>Thông thoáng mũi:</b> Nhỏ NaCl 0.9%, Hút sạch nhầy mũi họng trước khi ăn và trước khi ngủ.

<b>Những điều AAP và NICE khuyến cáo KHÔNG DÙNG THƯỜNG QUY:</b>
❌ <b>KHÔNG dùng Kháng sinh thường quy:</b> RSV là virus. Tỷ lệ bội nhiễm vi khuẩn ở đợt đầu &lt; 1-2%.
❌ <b>KHÔNG dùng Salbutamol (khí dung) thường quy:</b> Cơ chế tắc nghẽn của RSV là do phù nề và nút nhầy, không phải co thắt cơ trơn (trẻ &lt; 6 tháng cơ trơn chưa phát triển hoàn chỉnh). Khí dung Salbutamol chỉ làm tăng nhịp tim, run tay, kích thích quấy khóc. Chỉ thử khí dung 1 liều nếu có tiền sử gia đình dị ứng/hen, không đáp ứng sau 20 phút → dừng ngay!
❌ <b>KHÔNG dùng Corticoid toàn thân (Dexamethasone/Prednisolone):</b> Không rút ngắn thời gian thở oxy hay thời gian nằm viện."""

PART_2 = """━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>PHẦN 2: BỆNH HỌC NHIỄM CÚM A (INFLUENZA A)</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cúm A thuộc họ Orthomyxoviridae, có hệ gen gồm 8 đoạn RNA chuỗi đơn. Khác với RSV khu trú nhiều ở trẻ nhũ nhi, Cúm A tấn công <b>mọi lứa tuổi</b> và có khả năng bùng phát thành dịch lớn hàng năm.

<b>1. Cơ chế sinh bệnh & Hiện tượng "Bão Cytokine"</b>
• Kháng nguyên <b>Hemagglutinin (H)</b> gắn vào thụ thể Acid Sialic của tế bào biểu mô đường hô hấp để xâm nhập; kháng nguyên <b>Neuraminidase (N)</b> cắt đứt liên kết giúp virus mới nhân lên giải phóng ra ngoài.
• <b>Độc lực & Phản ứng viêm toàn thân:</b> Cúm A kích hoạt hệ thống miễn dịch bẩm sinh giải phóng ồ ạt các cytokine tiền viêm (IL-6, TNF-α, IFN-γ) → Gây nên triệu chứng sốt cao rét run, đau nhức cơ bắp dữ dội và vẻ mặt mệt lả nhiễm độc.
• <b>Phá hủy hàng rào niêm mạc:</b> Virus phá hủy lớp biểu mô có lông chuyển → Làm mất cơ chế làm sạch tự nhiên của phổi → <b>Mở đường cho bội nhiễm vi khuẩn cơ hội cực kỳ nguy hiểm (đặc biệt là Tụ cầu vàng CA-MRSA và Phế cầu)</b>.

<b>2. Biểu hiện lâm sàng của Cúm A ở trẻ em</b>
1) <b>Khởi phát đột ngột:</b> Trẻ đang chơi bình thường bỗng nhiên sốt vọt lên 39 - 40.5°C, sốt rét run, đáp ứng rất kém với thuốc hạ sốt thông thường.
2) <b>Hội chứng nhiễm độc - Đau nhức cơ (Myalgia):</b> Đau đầu dữ dội, mệt lả, li bì. Trẻ lớn thường than <b>đau bắp chân dữ dội (bắp chuối)</b>, từ chối đứng dậy hoặc đi lại.
3) <b>Triệu chứng hô hấp:</b> Rát bỏng họng, mắt đỏ, chảy nước mắt, ho khan rát buốt sau xương ức.
4) <b>Triệu chứng tiêu hóa (RẤT THƯỜNG GẶP Ở TRẺ EM):</b> Buồn nôn, nôn trớ, tiêu chảy phân lỏng, đau bụng quanh rốn (như chùm ca bệnh Cúm A kèm rối loạn tiêu hóa ở buồng 602, 605 khoa Nội Tổng hợp).

<b>3. Bốn biến chứng nguy hiểm tính mạng của Cúm A</b>

<code>                           CÁC BIẾN CHỨNG NGUY HIỂM CỦA CÚM A
                                           │
     ┌──────────────────────┬──────────────┴───────┬──────────────────────┐
     ▼                      ▼                      ▼                      ▼
[HÔ HẤP NẶNG]          [THẦN KINH]            [TIM MẠCH & CƠ]        [HỘI CHỨNG REYE]
• Croup (viêm thanh    • Sốt cao co giật      • Viêm cơ tim cấp      • Suy gan cấp + phù
  khí phế quản cấp)    • Viêm não hoại tử cấp   (rối loạn nhịp tim,    não tối cấp
• Viêm phổi bội nhiễm    (ANE - tử vong nhanh)  sốc tim, tụt HA)     • DO DÙNG ASPIRIN
  Tụ cầu hoại tử       • Hội chứng            • Viêm cơ tiêu vân cấp   HẠ SỐT KHI NHIỄM
• ARDS suy hô hấp cấp    Guillain-Barré         (tiểu màu xá xị)       VIRUS CÚM!</code>

<b>4. Thuốc kháng virus đặc hiệu: Oseltamivir (Tamiflu)</b>
Oseltamivir là chất ức chế chọn lọc men Neuraminidase, ngăn chặn sự giải phóng virus cúm khỏi tế bào nhiễm bệnh.

<b>Nguyên tắc sử dụng chuẩn EBM:</b>
• <b>Thời điểm vàng:</b> Hiệu quả tối đa khi được bắt đầu trong vòng <b>48 giờ đầu tiên</b> kể từ khi xuất hiện cơn sốt đầu tiên (giúp giảm trung bình 1–1.5 ngày bệnh, giảm đáng kể nguy cơ biến chứng viêm tai giữa và viêm phổi).
• <b>Sau 48 giờ có dùng không?</b> VẪN CHỈ ĐỊNH DÙNG cho: Trẻ bệnh nặng phải nhập viện, trẻ suy hô hấp tiến triển, hoặc trẻ thuộc nhóm nguy cơ cao (tim bẩm sinh, hen suyễn, suy giảm miễn dịch, trẻ &lt; 2 tuổi).

<b>Bảng liều dùng Oseltamivir đường uống (Liệu trình 5 ngày, uống ngày 2 lần):</b>
• <b>Trẻ nhũ nhi &lt; 1 tuổi:</b> 3.0 mg/kg/lần (Tổng liều: 6.0 mg/kg/ngày)
• <b>Trẻ ≤ 15 kg:</b> 30 mg/lần (Tổng liều: 60 mg/ngày)
• <b>Trẻ &gt; 15 - 23 kg:</b> 45 mg/lần (Tổng liều: 90 mg/ngày)
• <b>Trẻ &gt; 23 - 40 kg:</b> 60 mg/lần (Tổng liều: 120 mg/ngày)
• <b>Trẻ &gt; 40 kg & Trẻ lớn:</b> 75 mg/lần (Tổng liều: 150 mg/ngày)

<i>Tác dụng phụ hay gặp:</i> Buồn nôn, nôn trớ → Khắc phục bằng cách cho trẻ uống thuốc ngay sau bữa ăn hoặc cùng với sữa/thức ăn."""

PART_3 = """━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>PHẦN 3: BẢNG SO SÁNH ĐỐI ĐẦU TẠI GIƯỜNG: RSV vs CÚM A</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>1) Cơ quan đích ưu thế:</b>
• RSV: Đường hô hấp dưới nhỏ (Tiểu phế quản, phế nang).
• Cúm A: Đường hô hấp trên & toàn thân (khí phế quản, toàn thân).

<b>2) Lứa tuổi ưu thế:</b>
• RSV: Trẻ nhỏ &lt; 2 tuổi (đặc biệt &lt; 6 tháng và sơ sinh).
• Cúm A: Mọi lứa tuổi (đặc biệt trẻ mẫu giáo, học đường, người lớn).

<b>3) Kiểu hình sốt:</b>
• RSV: Sốt nhẹ hoặc sốt vừa (38 - 38.5°C), có thể không sốt.
• Cúm A: Sốt cao đột ngột 39 - 40.5°C, sốt rét run, khó hạ.

<b>4) Triệu chứng nổi bật:</b>
• RSV: Khò khè dữ dội, thở nhanh, co kéo rút lõm ngực.
• Cúm A: Đau mỏi cơ bắp, đau đầu, mệt lả, ho rát họng, nôn trớ.

<b>5) Ran nghe phổi:</b>
• RSV: Ran rít, ran ngáy, ran ẩm nhỏ hạt/ran nổ mịn 2 bên.
• Cúm A: Rì rào phế nang thô, giai đoạn đầu nghe phổi rất ít ran.

<b>6) X-quang ngực:</b>
• RSV: Ứ khí phế nang 2 bên, dày quanh phế quản, xẹp phổi thùy trên phải.
• Cúm A: Thường bình thường hoặc thâm nhiễm mô kẽ quanh rốn phổi.

<b>7) Biến chứng sợ nhất:</b>
• RSV: Cơn ngừng thở (Apnea) ở sơ sinh, suy hô hấp kiệt cơ.
• Cúm A: Viêm não hoại tử cấp (ANE), sốt co giật, viêm phổi tụ cầu hoại tử.

<b>8) Thuốc kháng virus:</b>
• RSV: Không có thuốc uống đặc hiệu (chủ yếu nâng đỡ, oxy, CPAP).
• Cúm A: Oseltamivir (Tamiflu) uống trong 48 giờ đầu.

<b>9) Dự phòng đặc hiệu:</b>
• RSV: Kháng thể đơn dòng (Palivizumab, Nirsevimab) cho trẻ nguy cơ.
• Cúm A: Vắc xin Cúm mùa hàng năm (tiêm từ 6 tháng tuổi).

━━━━━━━━━━━━━━━━━━━━━━━━━━━
<b>TỔNG KẾT BÀI HỌC THỰC TẾ KHI ĐI BUỒNG PHÒNG BỆNH</b>
━━━━━━━━━━━━━━━━━━━━━━━━━━━

<b>1. Với buồng RSV (Khoa Hô hấp & CC-SS):</b>
• Đừng tốn tiền của bệnh nhân vào kháng sinh hay thuốc ho thảo dược. Hãy tập trung vào: <b>Hút thông đờm mũi trước cữ bú</b>, <b>chia nhỏ cữ bú để tránh nôn trớ hít sặc</b>, và <b>chỉ định CPAP sớm</b> nếu trẻ co kéo ngực sâu hoặc SpO2 tụt.

<b>2. Với buồng Cúm A (Khoa Nội Tổng hợp):</b>
• Bắt Oseltamivir càng sớm càng tốt (trong 48h đầu).
• <b>Tuyệt đối không dùng Aspirin</b> để hạ sốt.
• Cảnh giác cơn co giật do sốt cao vọt và theo dõi sát tri giác: Nếu trẻ lơ mơ, mất định hướng, nôn liên tục → Phải hội chẩn loại trừ ngay biến chứng Viêm não do Cúm."""

def send_message_part(text, part_num):
    print(f"Đang gửi Phần {part_num}...")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = urllib.parse.urlencode({
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML',
        'disable_web_page_preview': True
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=payload)
    with urllib.request.urlopen(req, timeout=25) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"   -> Kết quả Phần {part_num}:", res.get('ok'))
        return res

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("Lỗi: Không tìm thấy TELEGRAM_BOT_TOKEN")
        sys.exit(1)
        
    send_message_part(PART_1, 1)
    send_message_part(PART_2, 2)
    send_message_part(PART_3, 3)
    print("ĐÃ GỬI XONG NGUYÊN VĂN 100%!")
