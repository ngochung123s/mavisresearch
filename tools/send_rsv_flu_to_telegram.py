"""
send_rsv_flu_to_telegram.py
Gửi toàn bộ bài học chuyên sâu về nhiễm RSV và Cúm A ở trẻ em lên Telegram Bot
dưới 2 định dạng hiển thị đẹp mắt nhất trên Telegram:
1. Ảnh Infographic / Poster độ phân giải cao (hiển thị trực tiếp trong khung chat).
2. Bài viết Telegra.ph chuẩn Instant View (Xem nhanh trực tiếp trong Telegram, dàn trang đẹp mắt).
"""
import os
import sys
import json
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path
import re

# Paths
OUTPUT_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\02_Ho_hap")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HTML_PATH = OUTPUT_DIR / "INFOGRAPHIC_RSV_VA_CUM_A.html"
PNG_PATH = OUTPUT_DIR / "INFOGRAPHIC_RSV_VA_CUM_A.png"

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", "6569183642"))
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()

# -------------------------------------------------------------
# 1. HTML NỘI DUNG TRÌNH BÀY CHUẨN UI HIỆN ĐẠI (ĐỂ CHỤP ẢNH POSTER)
# -------------------------------------------------------------
HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>BỆNH HỌC CHUYÊN SÂU: NHIỄM RSV VÀ CÚM A Ở TRẺ EM</title>
  <style>
    *, *:before, *:after { box-sizing: border-box; }
    body {
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
      font-size: 13.5px;
      line-height: 1.5;
      color: #1e293b;
      background: #f8fafc;
      margin: 0;
      padding: 24px;
      width: 1200px;
    }
    .container {
      background: #ffffff;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.06);
      padding: 28px 32px;
      border: 1px solid #e2e8f0;
    }
    /* Header */
    .header-box {
      border-bottom: 3px solid #0284c7;
      padding-bottom: 14px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }
    .header-left .sub {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #0369a1;
    }
    .header-left h1 {
      font-size: 24px;
      font-weight: 900;
      color: #0f172a;
      margin: 4px 0;
      text-transform: uppercase;
      letter-spacing: -0.02em;
    }
    .header-left .desc {
      font-size: 13px;
      color: #64748b;
      font-style: italic;
    }
    .badge-y6 {
      background: #e0f2fe;
      color: #0369a1;
      font-weight: 800;
      font-size: 11px;
      padding: 5px 12px;
      border-radius: 6px;
      text-transform: uppercase;
    }

    /* Section Titles */
    .section-title {
      font-size: 15px;
      font-weight: 800;
      text-transform: uppercase;
      color: #0369a1;
      background: #f0f9ff;
      border-left: 4px solid #0284c7;
      padding: 6px 12px;
      margin: 20px 0 10px 0;
      border-radius: 0 6px 6px 0;
    }

    /* Grids */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 14px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-bottom: 14px;
    }
    .card {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 12px 14px;
    }
    .card-header {
      font-weight: 800;
      font-size: 13px;
      color: #0f172a;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 6px;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .card-badge {
      font-size: 10px;
      padding: 2px 7px;
      border-radius: 4px;
      font-weight: 700;
      text-transform: uppercase;
    }
    .badge-rsv { background: #e0f2fe; color: #0369a1; }
    .badge-flu { background: #fef3c7; color: #b45309; }
    .badge-red { background: #fee2e2; color: #b91c1c; }

    /* Callouts */
    .callout {
      border-radius: 6px;
      padding: 10px 14px;
      margin: 10px 0;
      font-size: 12.5px;
      line-height: 1.5;
    }
    .callout-danger {
      background: #fef2f2;
      border-left: 4px solid #ef4444;
      color: #991b1b;
    }
    .callout-alert {
      background: #fffbeb;
      border-left: 4px solid #f59e0b;
      color: #92400e;
    }
    .callout-info {
      background: #f0fdf4;
      border-left: 4px solid #22c55e;
      color: #166534;
    }

    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0 16px 0;
      font-size: 12px;
    }
    th, td {
      border: 1px solid #cbd5e1;
      padding: 7px 10px;
      vertical-align: middle;
    }
    th {
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
    }
    tr:nth-child(even) td { background-color: #f8fafc; }

    ul, ol { margin: 4px 0 6px 18px; padding: 0; }
    li { margin-bottom: 3px; }

    .footer {
      border-top: 1px solid #e2e8f0;
      padding-top: 10px;
      margin-top: 20px;
      font-size: 11px;
      color: #94a3b8;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>
  <div class="container">
    
    <!-- HEADER -->
    <div class="header-box">
      <div class="header-left">
        <div class="sub">TÀI LIỆU LÂM SÀNG BỘ MÔN NHI KHOA • Y6 CLINICAL HANDBOOK</div>
        <h1>BỆNH HỌC CHUYÊN SÂU: NHIỄM RSV VÀ CÚM A Ở TRẺ EM</h1>
        <div class="desc">Bản đồ so sánh đối đầu • Sinh lý bệnh phân tử • Phác đồ EBM & Nhận diện cờ đỏ tử vong tại buồng bệnh</div>
      </div>
      <div>
        <span class="badge-y6">Y6 PEDIATRICS</span>
      </div>
    </div>

    <!-- KHUNG ĐỐI CHIẾU NHANH -->
    <div class="grid-2">
      <!-- RSV CARD -->
      <div class="card" style="border-top: 4px solid #0284c7;">
        <div class="card-header">
          <span style="color: #0369a1; font-size: 14px;">🫁 1. VIRUS HỢP BÀO HÔ HẤP (RSV)</span>
          <span class="card-badge badge-rsv">Pneumoviridae</span>
        </div>
        <ul>
          <li><strong>Đích tổn thương:</strong> Biểu mô tiểu phế quản (&lt; 2 mm).</li>
          <li><strong>Cơ chế:</strong> Glycoprotein F hòa màng tạo <strong>hợp bào khổng lồ</strong> $\rightarrow$ Tế bào hoại tử + phù nề + nhầy đặc $\rightarrow$ <strong>Tắc nút nhầy (Mucus plug)</strong>.</li>
          <li><strong>Hậu quả:</strong> Ứ khí phế nang (van 1 chiều) và <strong>Xẹp phổi (thường gặp thùy trên phải)</strong>.</li>
          <li><strong>Hai kiểu hình:</strong>
            <br>• <em>Trẻ 2–12 tháng:</em> Viêm tiểu phế quản cấp (khò khè, co kéo, ran rít/ngáy, ran nổ mịn).
            <br>• <em>Sơ sinh & đẻ non:</em> <strong>Cơn ngừng thở (Apnea) & nhịp tim chậm</strong> (do ức chế hành não & dây X).</li>
          <li><strong>3 Trụ cột điều trị (AAP):</strong> Hỗ trợ hô hấp (Oxy/HFNC/CPAP), Dinh dưỡng/bù nước (chia nhỏ cữ bú/sonde), Hút thông thoáng mũi họng.</li>
          <li><strong>Khuyến cáo KHÔNG:</strong> Không dùng KS thường quy; Không dùng Salbutamol thường quy; Không dùng Corticoid toàn thân.</li>
        </ul>
      </div>

      <!-- CÚM A CARD -->
      <div class="card" style="border-top: 4px solid #d97706;">
        <div class="card-header">
          <span style="color: #b45309; font-size: 14px;">🌡️ 2. VIRUS CÚM A (INFLUENZA A)</span>
          <span class="card-badge badge-flu">Orthomyxoviridae</span>
        </div>
        <ul>
          <li><strong>Cấu trúc:</strong> Kháng nguyên H (Hemagglutinin - bám dính) & N (Neuraminidase - phóng thích).</li>
          <li><strong>Cơ chế:</strong> Phá hủy hàng rào lông chuyển + Kích hoạt <strong>Bão Cytokine</strong> toàn thân (IL-6, TNF-$\alpha$).</li>
          <li><strong>Lâm sàng:</strong> Sốt cao đột ngột 39–40.5°C rét run, đau nhức cơ bắp dữ dội (đau bắp chân từ chối đi lại), rát bỏng họng, đỏ mắt, <strong>rối loạn tiêu hóa (nôn trớ, tiêu chảy)</strong>.</li>
          <li><strong>4 Biến chứng nguy hiểm:</strong>
            <br>1) <em>Hô hấp:</em> Croup, Viêm phổi hoại tử do Tụ cầu vàng CA-MRSA, ARDS.
            <br>2) <em>Thần kinh:</em> Sốt cao co giật, <strong>Viêm não hoại tử cấp (ANE)</strong>.
            <br>3) <em>Tim & cơ:</em> Viêm cơ tim cấp, Tiêu cơ vân cấp.
            <br>4) <em>Hội chứng Reye:</em> Suy gan cấp + phù não tối cấp <strong>DO DÙNG ASPIRIN</strong>!</li>
          <li><strong>Thuốc đặc hiệu:</strong> <strong>Oseltamivir (Tamiflu)</strong> uống trong <strong>48 giờ đầu</strong> (liều: &lt;1t: 3mg/kg; $\le$15kg: 30mg; 15-23kg: 45mg; 23-40kg: 60mg; &gt;40kg: 75mg x 2 lần/ngày x 5 ngày).</li>
        </ul>
      </div>
    </div>

    <!-- BẢNG SO SÁNH ĐỐI ĐẦU TOÀN DIỆN -->
    <div class="section-title">BẢNG ĐỐI CHIẾU SO SÁNH LÂM SÀNG TẠI GIƯỜNG: RSV vs CÚM A</div>
    <table>
      <thead>
        <tr>
          <th style="width: 18%;">Tiêu chí lâm sàng</th>
          <th style="width: 41%;">Nhiễm RSV (Virus Hợp Bào Hô Hấp)</th>
          <th style="width: 41%;">Nhiễm Cúm A (Influenza A)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Cơ quan đích ưu thế</strong></td>
          <td><strong>Đường hô hấp dưới nhỏ</strong> (Tiểu phế quản, phế nang).</td>
          <td><strong>Đường hô hấp trên & toàn thân</strong> (khí phế quản, toàn thân).</td>
        </tr>
        <tr>
          <td><strong>Lứa tuổi ưu thế</strong></td>
          <td><strong>Trẻ nhỏ &lt; 2 tuổi</strong> (đặc biệt &lt; 6 tháng và trẻ sơ sinh).</td>
          <td><strong>Mọi lứa tuổi</strong> (mẫu giáo, học đường, vị thành niên, người lớn).</td>
        </tr>
        <tr>
          <td><strong>Kiểu hình sốt</strong></td>
          <td>Sốt nhẹ hoặc vừa (38 – 38.5°C), một số trường hợp không sốt.</td>
          <td><strong>Sốt cao đột ngột 39 – 40.5°C</strong>, rét run, đáp ứng kém với hạ sốt.</td>
        </tr>
        <tr>
          <td><strong>Triệu chứng nổi bật</strong></td>
          <td><strong>Khò khè dữ dội, thở nhanh, co kéo rút lõm ngực, bú kém.</strong></td>
          <td><strong>Đau mỏi cơ bắp (bắp chân), đau đầu, ho rát cổ, nôn trớ, tiêu chảy.</strong></td>
        </tr>
        <tr>
          <td><strong>Ran nghe phổi</strong></td>
          <td><strong>Ran rít, ran ngáy, ran ẩm nhỏ hạt/ran nổ mịn 2 bên phế trường.</strong></td>
          <td>Rì rào phế nang thô, giai đoạn đầu nghe phổi rất ít hoặc không có ran.</td>
        </tr>
        <tr>
          <td><strong>X-quang ngực thẳng</strong></td>
          <td><strong>Ứ khí phế nang 2 bên</strong>, dày quanh phế quản, <strong>xẹp thùy trên phải</strong>.</td>
          <td>Thường bình thường hoặc thâm nhiễm mô kẽ nhẹ quanh rốn phổi.</td>
        </tr>
        <tr>
          <td><strong>Biến chứng sợ nhất</strong></td>
          <td><strong>Cơn ngừng thở (Apnea) ở sơ sinh</strong>, suy hô hấp kiệt cơ.</td>
          <td><strong>Viêm não hoại tử cấp (ANE)</strong>, co giật, <strong>viêm phổi tụ cầu hoại tử</strong>.</td>
        </tr>
        <tr>
          <td><strong>Thuốc điều trị đặc hiệu</strong></td>
          <td><strong>Không có thuốc uống đặc hiệu</strong> (chủ yếu oxy, CPAP, dịch).</td>
          <td><strong>Oseltamivir (Tamiflu)</strong> uống trong 48 giờ đầu tiên.</td>
        </tr>
        <tr>
          <td><strong>Dự phòng đặc hiệu</strong></td>
          <td>Kháng thể đơn dòng (<em>Palivizumab, Nirsevimab</em>) cho nhóm nguy cơ.</td>
          <td><strong>Vắc xin Cúm mùa hàng năm</strong> (tiêm cho trẻ từ 6 tháng tuổi).</td>
        </tr>
      </tbody>
    </table>

    <!-- BÀI HỌC VÀNG TẠI BUỒNG BỆNH -->
    <div class="grid-2">
      <div class="callout callout-danger">
        🚨 <strong>CẢNH BÁO CHO 3 CA SƠ SINH TẠI BUỒNG CC-SS:</strong>
        <br>Trẻ sơ sinh (&lt; 28 ngày) nhiễm RSV có nguy cơ cao bị <strong>cơn ngừng thở đột ngột (&gt; 20 giây kèm nhịp tim chậm)</strong> do virus ức chế trung tâm hô hấp ở hành não. Trẻ có thể tím tái ngừng thở mà chưa kịp có tiếng khò khè hay co kéo lồng ngực. <strong>Bắt buộc gắn monitor theo dõi $SpO_2$ và nhịp tim liên tục!</strong>
      </div>
      <div class="callout callout-alert">
        ⚡ <strong>LƯU Ý THỰC CHIẾN TẠI BUỒNG CÚM A (NỘI TỔNG HỢP):</strong>
        <br>• Khởi động Oseltamivir càng sớm càng tốt (trong 48h đầu).
        <br>• <strong>CẤM TUYỆT ĐỐI DÙNG ASPIRIN</strong> để hạ sốt $\rightarrow$ Nguy cơ Hội chứng Reye tử vong.
        <br>• Cảnh giác co giật do sốt cao và biến chứng viêm tai giữa mủ kèm theo.
      </div>
    </div>

    <!-- FOOTER -->
    <div class="footer">
      <span>Bộ môn Nhi khoa • Lưu hành học thuật Y6 & Bác sĩ thực hành</span>
      <span>Nguồn: AAP Guidelines, CDC Influenza Treatment & Nelson Textbook of Pediatrics</span>
    </div>

  </div>
</body>
</html>
"""

def generate_image_poster():
    print("1. Đang ghi file HTML template...")
    HTML_PATH.write_text(HTML_CONTENT, encoding="utf-8")
    print(f"   -> Đã ghi HTML: {HTML_PATH}")

    print("2. Đang render ảnh Infographic Poster bằng Edge Headless...")
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--window-size=1240,1650",
        f"--screenshot={PNG_PATH}",
        str(HTML_PATH)
    ]
    subprocess.run(cmd, check=True)
    img_size_kb = PNG_PATH.stat().st_size // 1024
    print(f"   -> Đã xuất ảnh Poster thành công: {PNG_PATH} ({img_size_kb} KB)")
    return PNG_PATH

def create_telegraph_page():
    print("3. Đang tạo bài viết Telegra.ph chuẩn Instant View...")
    acc_url = 'https://api.telegra.ph/createAccount?short_name=Y6Pediatrics&author_name=BacSiNhiKhoa'
    with urllib.request.urlopen(acc_url) as resp:
        acc = json.loads(resp.read().decode())['result']
    token = acc['access_token']

    # Cấu trúc nội dung Telegra.ph
    nodes = [
        {"tag": "p", "children": ["Tài liệu học tập & hướng dẫn lâm sàng chuyên sâu Nhi khoa Y6: Phân tích cơ chế bệnh sinh, triệu chứng tại giường, biến chứng và phác đồ điều trị chuẩn EBM."]},
        {"tag": "h3", "children": ["🫁 PHẦN 1: BỆNH HỌC NHIỄM RSV (RESPIRATORY SYNCYTIAL VIRUS)"]},
        {"tag": "p", "children": ["• Đích tổn thương: Biểu mô đường hô hấp nhỏ (tiểu phế quản < 2 mm)."]},
        {"tag": "p", "children": ["• Cơ chế phân tử: Glycoprotein F làm hòa màng tế bào tạo hợp bào khổng lồ (Syncytia) -> tế bào hoại tử, bong tróc + phù nề + nhầy đặc tạo nút nhầy (Mucus plug) bít tắc đường thở."]},
        {"tag": "p", "children": ["• Hậu quả: Hiệu ứng van một chiều gây ứ khí phế nang hai bên; tắc hoàn toàn gây xẹp phổi (điển hình xẹp thùy trên phổi phải)."]},
        {"tag": "blockquote", "children": ["🚨 CỜ ĐỎ SƠ SINH: Trẻ sơ sinh (< 28 ngày) và đẻ non nhiễm RSV có thể bị CƠN NGỪNG THỞ ĐỘT NGỘT (Apnea > 20s kèm nhịp tim chậm) do virus ức chế hành não & dây X. Cơn ngưng thở có thể xuất hiện TRƯỚC KHI TRẺ KỊP HO HAY CO KÉO!"]},
        {"tag": "p", "children": ["• 3 Trụ cột điều trị (AAP & NICE): (1) Hỗ trợ hô hấp (giữ SpO2 ≥ 90-92%, Oxy/HFNC/CPAP); (2) Dinh dưỡng & nước (chia nhỏ cữ bú, đặt sonde nếu thở nhanh > 60-70l/p); (3) Hút thông thoáng mũi họng."]},
        {"tag": "p", "children": ["• Khuyến cáo KHÔNG: Không dùng kháng sinh thường quy; Không dùng Salbutamol thường quy; Không dùng Corticoid toàn thân."]},
        
        {"tag": "h3", "children": ["🌡️ PHẦN 2: BỆNH HỌC NHIỄM CÚM A (INFLUENZA A VIRUS)"]},
        {"tag": "p", "children": ["• Cơ chế: Kháng nguyên H bám dính, N phóng thích virus. Phá hủy biểu mô lông chuyển + kích hoạt BÃO CYTOKINE toàn thân (IL-6, TNF-alpha)."]},
        {"tag": "p", "children": ["• Biểu hiện lâm sàng: Sốt cao đột ngột 39-40.5°C rét run khó hạ, đau nhức cơ bắp dữ dội (trẻ lớn than đau bắp chuối, từ chối đi lại), rát họng, ho khan, nôn trớ, tiêu chảy phân lỏng."]},
        {"tag": "p", "children": ["• 4 Biến chứng nguy hiểm: (1) Croup, Viêm phổi bội nhiễm Tụ cầu vàng CA-MRSA, ARDS; (2) Sốt cao co giật, Viêm não hoại tử cấp (ANE); (3) Viêm cơ tim cấp, Tiêu cơ vân cấp; (4) Hội chứng Reye (suy gan não cấp) DO DÙNG ASPIRIN!"]},
        {"tag": "p", "children": ["• Thuốc kháng virus đặc hiệu Oseltamivir (Tamiflu): Uống trong 48 giờ đầu. Liều: <1 tuổi: 3 mg/kg x 2; ≤15 kg: 30 mg x 2; 15-23 kg: 45 mg x 2; 23-40 kg: 60 mg x 2; >40 kg: 75 mg x 2 (liệu trình 5 ngày)."]},
        
        {"tag": "h3", "children": ["⚖️ PHẦN 3: SO SÁNH ĐỐI ĐẦU TẠI GIƯỜNG: RSV vs CÚM A"]},
        {"tag": "p", "children": ["1) Cơ quan đích: RSV khu trú tiểu phế quản dưới | Cúm A tấn công khí phế quản trên & toàn thân."]},
        {"tag": "p", "children": ["2) Lứa tuổi: RSV chủ yếu trẻ < 2 tuổi (đặc biệt < 6 tháng) | Cúm A gặp mọi lứa tuổi."]},
        {"tag": "p", "children": ["3) Kiểu sốt: RSV sốt nhẹ/vừa (38-38.5°C) | Cúm A sốt cao đột ngột 39-40.5°C rét run."]},
        {"tag": "p", "children": ["4) Triệu chứng: RSV khò khè, thở nhanh, co kéo rút lõm ngực | Cúm A đau cơ bắp, mệt lả, nôn trớ, tiêu chảy."]},
        {"tag": "p", "children": ["5) Nghe phổi: RSV rộ ran rít, ngáy, ran ẩm nhỏ hạt/nổ mịn | Cúm A rì rào phế nang thô, ít ran ban đầu."]},
        {"tag": "p", "children": ["6) X-quang: RSV ứ khí phế nang 2 bên, xẹp thùy trên phải | Cúm A bình thường hoặc mô kẽ nhẹ."]},
        {"tag": "p", "children": ["7) Điều trị: RSV không có thuốc uống đặc hiệu (chủ yếu oxy, CPAP) | Cúm A dùng Oseltamivir trong 48h."]}
    ]

    page_data = {
        'access_token': token,
        'title': 'Bệnh Học Chuyên Sâu: Nhiễm RSV và Cúm A Ở Trẻ Em',
        'author_name': 'Bộ Môn Nhi Khoa - Y6',
        'content': json.dumps(nodes),
        'return_content': False
    }

    req = urllib.request.Request('https://api.telegra.ph/createPage', data=urllib.parse.urlencode(page_data).encode('utf-8'))
    with urllib.request.urlopen(req, timeout=15) as resp:
        res = json.loads(resp.read().decode())
        page_url = res.get('result', {}).get('url', '')
        print(f"   -> Đã tạo trang Telegra.ph: {page_url}")
        return page_url

def send_to_telegram(photo_path: Path, telegraph_url: str):
    print("4. Đang gửi ảnh Poster và Tin nhắn Instant View tới Telegram...")
    boundary = "----WebKitFormBoundaryTelegramMultiFormat2026"
    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    
    with open(photo_path, "rb") as f:
        photo_bytes = f.read()

    caption = "📊 INFOGRAPHIC LÂM SÀNG: NHIỄM RSV VÀ CÚM A Ở TRẺ EM\n\n" \
              "• Bản đồ so sánh đối đầu toàn diện RSV vs Cúm A\n" \
              "• Sinh lý bệnh hòa màng hợp bào & bão cytokine\n" \
              "• 3 Trụ cột điều trị RSV & Liều Oseltamivir chuẩn Cúm A\n" \
              "• Cảnh báo cơn ngừng thở sơ sinh & biến chứng thần kinh."

    # Gửi ảnh photo
    body = []
    body.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"chat_id\"\r\n\r\n{CHAT_ID}\r\n".encode("utf-8"))
    body.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"caption\"\r\n\r\n{caption}\r\n".encode("utf-8"))
    body.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"photo\"; filename=\"rsv_flu_infographic.png\"\r\nContent-Type: image/png\r\n\r\n".encode("utf-8"))
    body.append(photo_bytes)
    body.append(f"\r\n--{boundary}--\r\n".encode("utf-8"))
    
    payload = b"".join(body)
    req = urllib.request.Request(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=40) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("   -> Đã gửi ảnh thành công:", res.get("ok"))

    # Gửi tin nhắn kèm Instant View link
    msg_text = f"📖 <b>BÀI GIẢNG ĐẦY ĐỦ: NHIỄM RSV & CÚM A (XEM NHANH)</b>\n\n" \
               f"Để đọc định dạng bài viết đẹp mắt, đầy đủ từng mục ngay trong Telegram (không cần tải file), mời bạn bấm vào nút <b>Instant View / Xem nhanh</b> bên dưới:\n\n" \
               f"🔗 {telegraph_url}\n\n" \
               f"<i>(Đã tích hợp đầy đủ cơ chế, liều thuốc Oseltamivir và bảng đối chiếu lâm sàng)</i>"

    send_msg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    msg_payload = urllib.parse.urlencode({
        'chat_id': CHAT_ID,
        'text': msg_text,
        'parse_mode': 'HTML',
        'disable_web_page_preview': False
    }).encode('utf-8')
    
    req2 = urllib.request.Request(send_msg_url, data=msg_payload)
    with urllib.request.urlopen(req2, timeout=20) as resp2:
        res2 = json.loads(resp2.read().decode("utf-8"))
        print("   -> Đã gửi tin nhắn Instant View thành công:", res2.get("ok"))

if __name__ == "__main__":
    img = generate_image_poster()
    url = create_telegraph_page()
    send_to_telegram(img, url)
    print("HOÀN TẤT 100%!")
