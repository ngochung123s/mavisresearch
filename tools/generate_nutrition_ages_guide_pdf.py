"""
generate_nutrition_ages_guide_pdf.py
Biên dịch Cẩm nang Hướng dẫn Khám & Đánh giá Dinh dưỡng Nhi khoa qua các Lứa tuổi ra PDF chuẩn A4 
bằng Microsoft Edge Headless, lưu tại Desktop và tự động gửi qua Telegram Bot.
Hoàn toàn phi cá nhân hóa (Zero-PHI), chuẩn hóa học thuật lâm sàng.
"""
import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
import shutil

# Paths
OUTPUT_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\04_Tieu_hoa_va_Dinh_duong")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HTML_PATH = OUTPUT_DIR / "HUONG_DAN_KHAM_DINH_DUONG_CAC_LUA_TUOI.html"
PDF_PATH = OUTPUT_DIR / "HUONG_DAN_KHAM_DINH_DUONG_CAC_LUA_TUOI.pdf"
DESKTOP_PDF = Path(r"C:\Users\THANHANH\Desktop\Huong_Dan_Kham_Dinh_Duong_Nhi_Khoa_Cac_Lua_Tuoi.pdf")

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", "6569183642"))
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>CẨM NANG KHÁM & ĐÁNH GIÁ DINH DƯỠNG NHI KHOA CÁC LỨA TUỔI</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 10mm 12mm 10mm 12mm;
    }
    *, *:before, *:after {
      box-sizing: border-box;
    }
    body {
      font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
      font-size: 9pt;
      line-height: 1.4;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }
    
    /* Header bar */
    .header-box {
      border-bottom: 2.5px solid #0284c7;
      padding-bottom: 6px;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }
    .hospital-sub {
      font-size: 8pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #0369a1;
    }
    .doc-category {
      font-size: 7.5pt;
      font-weight: 700;
      background: #e0f2fe;
      color: #0369a1;
      padding: 2px 7px;
      border-radius: 4px;
      display: inline-block;
    }
    .doc-title {
      font-size: 13.5pt;
      font-weight: 800;
      color: #0f172a;
      text-transform: uppercase;
      margin: 4px 0 2px 0;
      letter-spacing: -0.01em;
    }
    .doc-subtitle {
      font-size: 8.5pt;
      font-weight: 500;
      color: #64748b;
      font-style: italic;
    }

    /* Section Styling */
    .section-title {
      font-size: 9.5pt;
      font-weight: 800;
      text-transform: uppercase;
      color: #0369a1;
      background: #f0f9ff;
      border-left: 3.5px solid #0284c7;
      padding: 3px 6px;
      margin: 8px 0 5px 0;
      display: flex;
      align-items: center;
    }

    /* Grid & Cards */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
      margin-bottom: 6px;
    }
    .age-card {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 5px;
      padding: 6px 8px;
      page-break-inside: avoid;
    }
    .age-card-header {
      font-weight: 800;
      font-size: 9pt;
      color: #0369a1;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 3px;
      margin-bottom: 4px;
      display: flex;
      justify-content: space-between;
    }
    .age-card-header .badge {
      font-size: 7pt;
      background: #0284c7;
      color: #ffffff;
      padding: 1px 5px;
      border-radius: 3px;
      text-transform: uppercase;
    }
    
    .callout-box {
      background: #f8fafc;
      border-left: 3px solid #64748b;
      padding: 4px 8px;
      font-size: 8.5pt;
      margin: 4px 0;
      border-radius: 0 4px 4px 0;
    }
    .callout-alert {
      background: #fffbeb;
      border-left-color: #f59e0b;
      color: #92400e;
    }
    .callout-danger {
      background: #fef2f2;
      border-left-color: #ef4444;
      color: #991b1b;
    }

    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 4px 0 6px 0;
      font-size: 8pt;
    }
    th, td {
      border: 1px solid #cbd5e1;
      padding: 4px 6px;
      vertical-align: middle;
    }
    th {
      background-color: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
      text-align: left;
    }
    tr:nth-child(even) td {
      background-color: #f8fafc;
    }

    ul, ol {
      margin: 2px 0 4px 14px;
      padding: 0;
    }
    li {
      margin-bottom: 1px;
    }

    .doc-footer {
      border-top: 1px solid #cbd5e1;
      padding-top: 3px;
      margin-top: 8px;
      font-size: 7.5pt;
      color: #94a3b8;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <div class="header-box">
    <div>
      <div class="hospital-sub">TÀI LIỆU HƯỚNG DẪN LÂM SÀNG & HUẤN LUYỆN Y KHOA</div>
      <div class="doc-title">HƯỚNG DẪN KHÁM & ĐÁNH GIÁ DINH DƯỠNG NHI KHOA THEO CÁC LỨA TUỔI</div>
      <div class="doc-subtitle">Khung tiếp cận ABCD • Kỹ thuật nhân trắc học theo tuổi • Phân loại WHO Z-score • Nhận diện thiếu hụt vi chất</div>
    </div>
    <div style="text-align: right;">
      <span class="doc-category">DINH DƯỠNG LÂM SÀNG NHI</span><br>
      <span style="font-size: 7.5pt; color: #64748b;">Khổ in A4 • 2026.1</span>
    </div>
  </div>

  <!-- PHẦN 1: MÔ HÌNH ABCD -->
  <div class="section-title">1. KHUNG TIẾP CẬN ĐÁNH GIÁ DINH DƯỠNG TOÀN DIỆN (MÔ HÌNH ABCD)</div>
  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin-bottom: 6px;">
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px;">
      <strong style="color: #0369a1; font-size: 8.5pt;">A - Anthropometry</strong><br>
      <span style="font-size: 8pt; color: #475569;"><strong>Nhân trắc học:</strong> Cân nặng (W), Chiều cao/dài (H/L), Vòng đầu (HC), Vòng cánh tay (MUAC), Bề dày nếp gấp da (Triceps skinfold).</span>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px;">
      <strong style="color: #0369a1; font-size: 8.5pt;">B - Biochemical</strong><br>
      <span style="font-size: 8pt; color: #475569;"><strong>Cận lâm sàng:</strong> Albumin, Prealbumin (bán hủy 2 ngày), CTM (Hb, MCV), Ferritin, 25(OH)D, Canxi/Phospho/ALP, Kẽm huyết thanh.</span>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px;">
      <strong style="color: #0369a1; font-size: 8.5pt;">C - Clinical</strong><br>
      <span style="font-size: 8pt; color: #475569;"><strong>Khám lâm sàng:</strong> Toàn thân (teo cơ, mất lớp mỡ dưới da, phù dinh dưỡng), Tóc (thưa, dễ rụng), Mắt (khô mắt), Da niêm mạc, Hệ xương.</span>
    </div>
    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 5px;">
      <strong style="color: #0369a1; font-size: 8.5pt;">D - Dietary</strong><br>
      <span style="font-size: 8pt; color: #475569;"><strong>Khẩu phần ăn:</strong> Bú mẹ/Sữa công thức, thời điểm & cấu trúc ăn dặm, hỏi khẩu phần 24 giờ qua (24-h recall), dị ứng thức ăn, thói quen ăn vặt.</span>
    </div>
  </div>

  <!-- PHẦN 2: ĐẶC THÙ THEO TỪNG LỨA TUỔI -->
  <div class="section-title">2. QUY TRÌNH THĂM KHÁM & ĐẶC THÙ THEO TỪNG LỨA TUỔI</div>
  <div class="card-grid">

    <!-- TUỔI 1: SƠ SINH & DƯỚI 6 THÁNG -->
    <div class="age-card">
      <div class="age-card-header">
        <span>GIAI ĐOẠN 0 – 6 THÁNG TUỔI (BÚ MẸ HOÀN TOÀN)</span>
        <span class="badge">NHŨ NHI NHỎ</span>
      </div>
      <ul>
        <li><strong>Động lực tăng trưởng:</strong> Sụt cân sinh lý tối đa &lt; 10% trong 7–10 ngày đầu; lấy lại cân lúc 10–14 ngày. Tăng cân trung bình: 25–30 g/ngày (3 tháng đầu), 20 g/ngày (3 tháng sau).</li>
        <li><strong>Kỹ thuật đo:</strong> Cân máng điện tử (bỏ bỉm/quần áo); Đo chiều dài nằm bằng thước hộp đo nằm (Infantometer); Đo vòng đầu qua điểm nhô nhất ụ chẩm và cung mày.</li>
        <li><strong>Khám lâm sàng:</strong> Thóp trước (phẳng/trũng), lớp mỡ má (Bichat), độ đàn hồi da, trương lực cơ.</li>
        <li><strong>Khai thác nuôi dưỡng:</strong> Đánh giá cữ bú (8–12 lần/ngày), khớp ngậm đúng, số tã ướt (≥ 6 tã ướt/ngày chứng tỏ bú đủ sữa mẹ).</li>
      </ul>
      <div class="callout-box callout-alert" style="margin-top: 3px;">
        ⚠️ <em>Cảnh báo:</em> Sụt cân &gt; 10% sau sinh hoặc không lấy lại cân sau 2 tuần là cờ đỏ thiếu cung cấp sữa mẹ hoặc bệnh lý chuyển hóa/tim bẩm sinh.
      </div>
    </div>

    <!-- TUỔI 2: 6 – 24 THÁNG -->
    <div class="age-card">
      <div class="age-card-header">
        <span>GIAI ĐOẠN 6 – 24 THÁNG TUỔI (ĂN DẶM & TĂNG TRƯỞNG NHANH)</span>
        <span class="badge">ĂN DẶM</span>
      </div>
      <ul>
        <li><strong>Chỉ số then chốt:</strong> Vẫn đo chiều dài nằm (đến 24 tháng). Đo <strong>vòng cánh tay (MUAC)</strong> từ 6 tháng: đo điểm giữa mỏm cùng vai và mỏm khuỷu tay trái.
          <br>• MUAC &lt; 115 mm: Suy dinh dưỡng cấp nặng (SAM).
          <br>• MUAC 115 – 125 mm: Suy dinh dưỡng cấp vừa (MAM).</li>
        <li><strong>Khai thác ăn dặm:</strong> Số bữa/ngày, độ đặc, đủ 4 nhóm chất (đạm, bột, béo, rau/quả). Có kiêng dầu mỡ không?</li>
        <li><strong>Tầm soát thiếu vi chất:</strong> Thiếu máu thiếu sắt (xanh xao, mệt mỏi), Còi xương thiếu Vitamin D (chuỗi hạt sườn, vòng cổ tay, rụng tóc vành khăn, thóp chậm liền sau 18 tháng).</li>
      </ul>
      <div class="callout-box callout-danger" style="margin-top: 3px;">
        🚨 <em>Khám phù dinh dưỡng:</em> Dùng 2 ngón cái ấn nhẹ trên mu bàn chân 3 giây. Có vết lõm đối xứng hai bên = Phù Kwashiorkor (bắt buộc nhập viện!).
      </div>
    </div>

    <!-- TUỔI 3: 2 – 5 TUỔI -->
    <div class="age-card">
      <div class="age-card-header">
        <span>GIAI ĐOẠN 2 – 5 TUỔI (TIỀN HỌC ĐƯỜNG / MẪU GIÁO)</span>
        <span class="badge">TIỀN HỌC ĐƯỜNG</span>
      </div>
      <ul>
        <li><strong>Kỹ thuật đo:</strong> Chuyển sang <strong>đo chiều cao đứng</strong> bằng thước đứng (Stadiometer, 5 điểm chạm tường: gót chân, bắp chân, mông, bả vai, chẩm; mắt nhìn ngang theo mặt phẳng Frankfurt).</li>
        <li><strong>Chỉ số chính:</strong> Cân nặng theo chiều cao (WHZ) và BMI theo tuổi (BAZ).</li>
        <li><strong>Khám thực thể:</strong> Đánh giá teo cơ mông/đùi ("mông teo da bọc xương"), khám răng (sâu răng do bú bình đêm/ngậm đồ ngọt), viêm khóe mép, viêm loét miệng.</li>
        <li><strong>Tâm lý & hành vi ăn:</strong> Biếng ăn tâm lý, kén ăn (food neophobia), ăn vặt gần bữa chính, phụ thuộc màn hình điện thoại khi ăn.</li>
      </ul>
    </div>

    <!-- TUỔI 4: 6 – 18 TUỔI -->
    <div class="age-card">
      <div class="age-card-header">
        <span>GIAI ĐOẠN 6 – 18 TUỔI (HỌC ĐƯỜNG & VỊ THÀNH NIÊN)</span>
        <span class="badge">VỊ THÀNH NIÊN</span>
      </div>
      <ul>
        <li><strong>Gánh nặng kép dinh dưỡng:</strong> Đồng thời đối mặt Thừa cân/Béo phì và Thấp còi/Thiếu vi chất.</li>
        <li><strong>Chỉ số then chốt:</strong> BMI theo tuổi (BAZ) là chỉ số nhạy nhất. Đánh giá giai đoạn dậy thì theo <strong>thang điểm Tanner</strong> (ảnh hưởng trực tiếp đến đỉnh tăng trưởng chiều cao).</li>
        <li><strong>Dấu hiệu chuyển hóa & Béo phì:</strong> Dấu gai đen (Acanthosis nigricans) ở nếp gấp gáy/nách $\rightarrow$ Kháng insulin; Huyết áp cao; Rạn da (Striae); Vẹo cột sống hoặc biến dạng khớp gối vẹo trong (Genu valgum).</li>
        <li><strong>Hành vi lối sống:</strong> Thức uống có đường, trà sữa, thức ăn nhanh, ít vận động thể lực (&lt; 60 phút/ngày).</li>
      </ul>
    </div>

  </div>

  <!-- PHẦN 3: PHÂN LOẠI WHO Z-SCORE -->
  <div class="section-title">3. TIÊU CHUẨN PHÂN LOẠI TÌNH TRẠNG DINH DƯỠNG THEO WHO (Z-SCORE)</div>
  <table>
    <thead>
      <tr>
        <th style="width: 22%;">Chỉ số Nhân trắc</th>
        <th style="width: 22%;">&lt; -3 SD (Rất nặng)</th>
        <th style="width: 22%;">-3 SD đến &lt; -2 SD</th>
        <th style="width: 18%;">-2 SD đến +2 SD</th>
        <th style="width: 16%;">&gt; +2 SD / &gt; +3 SD</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>WAZ (Cân nặng / Tuổi)</strong><br><small>Chỉ áp dụng &lt; 10 tuổi</small></td>
        <td style="color: #b91c1c; font-weight: 700;">Nhẹ cân rất nặng</td>
        <td style="color: #d97706; font-weight: 600;">Nhẹ cân vừa</td>
        <td style="color: #15803d;">Bình thường</td>
        <td>Đánh giá qua BAZ</td>
      </tr>
      <tr>
        <td><strong>HAZ (Chiều cao / Tuổi)</strong><br><small>Đánh giá thấp còi mạn tính</small></td>
        <td style="color: #b91c1c; font-weight: 700;">Thấp còi rất nặng</td>
        <td style="color: #d97706; font-weight: 600;">Thấp còi vừa</td>
        <td style="color: #15803d;">Bình thường</td>
        <td>Rất cao (&gt; +3 SD: u tuyến yên?)</td>
      </tr>
      <tr>
        <td><strong>WHZ (Cân nặng / Cao)</strong><br><small>Áp dụng trẻ &lt; 5 tuổi</small></td>
        <td style="color: #b91c1c; font-weight: 700;">Gầy còm nặng (SAM)</td>
        <td style="color: #d97706; font-weight: 600;">Gầy còm vừa (MAM)</td>
        <td style="color: #15803d;">Bình thường</td>
        <td style="color: #d97706;">&gt; +2: Nguy cơ thừa cân<br>&gt; +3: Béo phì</td>
      </tr>
      <tr>
        <td><strong>BAZ (BMI / Tuổi)</strong><br><small>Chuẩn cho trẻ 5 – 19 tuổi</small></td>
        <td style="color: #b91c1c; font-weight: 700;">Gầy còm nặng</td>
        <td style="color: #d97706; font-weight: 600;">Gầy còm vừa</td>
        <td style="color: #15803d;">Bình thường</td>
        <td style="color: #b91c1c; font-weight: 700;">&gt; +1 SD: Thừa cân<br>&gt; +2 SD: Béo phì<br>&gt; +3 SD: Béo phì nặng</td>
      </tr>
    </tbody>
  </table>

  <!-- PHẦN 4: CHECKLIST DẤU HIỆU THIẾU VI CHẤT TỪ ĐẦU ĐẾN CHÂN -->
  <div class="section-title">4. CHECKLIST DẤU HIỆU THIẾU HỤT VI CHẤT TỪ ĐẦU ĐẾN CHÂN (HEAD-TO-TOE)</div>
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
    
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 5px;">
      <strong style="color: #0369a1; font-size: 8.5pt;">VÙNG ĐẦU – MẮT – TÓC</strong>
      <ul style="font-size: 7.5pt; margin-left: 12px;">
        <li><strong>Tóc thưa, dễ gãy rụng, đổi màu đỏ/vàng:</strong> Thiếu Protein, Kẽm, Đồng, Biotin.</li>
        <li><strong>Thóp rộng, chậm liền (&gt; 18 tháng):</strong> Còi xương thiếu Vitamin D.</li>
        <li><strong>Quáng gà, vệt Bitot, khô kết mạc:</strong> Thiếu Vitamin A.</li>
        <li><strong>Mặt "cụ già" (mất mỡ má):</strong> Suy dinh dưỡng thể Marasmus.</li>
      </ul>
    </div>

    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 5px;">
      <strong style="color: #0369a1; font-size: 8.5pt;">KHOANG MIỆNG – RĂNG – DA</strong>
      <ul style="font-size: 7.5pt; margin-left: 12px;">
        <li><strong>Viêm mép (Cheilosis), lưỡi đỏ tím (Glossitis):</strong> Thiếu Vitamin B2, B6, B12, Niacin.</li>
        <li><strong>Chảy máu lợi, chấm xuất huyết quanh nang lông:</strong> Thiếu Vitamin C.</li>
        <li><strong>Viêm da quanh các lỗ tự nhiên & đầu chi:</strong> Thiếu Kẽm (Acrodermatitis enteropathica).</li>
        <li><strong>Da khô ráp kiểu vảy cá (phrynoderma):</strong> Thiếu Vitamin A, Acid béo thiết yếu.</li>
      </ul>
    </div>

    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 5px;">
      <strong style="color: #0369a1; font-size: 8.5pt;">HỆ XƯƠNG – CƠ – MÓNG</strong>
      <ul style="font-size: 7.5pt; margin-left: 12px;">
        <li><strong>Chuỗi hạt sườn, vòng cổ tay/chân, chân chữ O/X:</strong> Còi xương thiếu Vitamin D / Canxi.</li>
        <li><strong>Móng tay thìa (Koilonychia), lòng bàn tay nhợt:</strong> Thiếu máu thiếu Sắt.</li>
        <li><strong>Teo khối cơ thái dương, mông, bắp chân:</strong> Thiếu năng lượng - đạm kéo dài.</li>
        <li><strong>Phù mu chân đối xứng, da tróc lở mảng ("sơn nứt"):</strong> Kwashiorkor (thiếu đạm nặng).</li>
      </ul>
    </div>

  </div>

  <!-- FOOTER -->
  <div class="doc-footer">
    <span>Bộ môn Nhi khoa • Tài liệu Huấn luyện Kỹ năng Tiền lâm sàng Y khoa</span>
    <span>Dinh dưỡng Trẻ em theo Khung chuẩn WHO & Viện Dinh Dưỡng Quốc Gia</span>
    <span>Trang 1/1</span>
  </div>

</body>
</html>
"""

def generate_pdf():
    print("1. Đang ghi file HTML template...")
    HTML_PATH.write_text(HTML_CONTENT, encoding="utf-8")
    print(f"   -> Đã ghi file HTML: {HTML_PATH}")

    print("2. Đang biên dịch PDF bằng Edge Headless...")
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        str(HTML_PATH)
    ]
    subprocess.run(cmd, check=True)
    pdf_size_kb = PDF_PATH.stat().st_size // 1024
    print(f"   -> Đã xuất file PDF thành công: {PDF_PATH} ({pdf_size_kb} KB)")

    # Sao chép ra Desktop
    shutil.copy2(PDF_PATH, DESKTOP_PDF)
    print(f"   -> Đã copy bản PDF ra Desktop: {DESKTOP_PDF}")
    return PDF_PATH

def send_to_telegram(pdf_file: Path):
    if not BOT_TOKEN:
        print("LỖI: Biến môi trường TELEGRAM_BOT_TOKEN không tồn tại!")
        return False
        
    print(f"3. Đang gửi file PDF qua Telegram Bot tới chat_id {CHAT_ID}...")
    boundary = "----WebKitFormBoundaryNutritionDoc2026"
    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    
    with open(pdf_file, "rb") as f:
        file_bytes = f.read()
        
    filename = "Huong_Dan_Kham_Dinh_Duong_Nhi_Khoa_Cac_Lua_Tuoi.pdf"
    
    caption = "📋 CẨM NANG LÂM SÀNG: KHÁM & ĐÁNH GIÁ DINH DƯỠNG NHI KHOA CÁC LỨA TUỔI\n\n" \
              "• Khung tiếp cận ABCD chuẩn hóa (Nhân trắc - Hóa sinh - Khám lâm sàng - Khẩu phần)\n" \
              "• Đặc thù 4 giai đoạn: 0-6 tháng, 6-24 tháng (MUAC/ăn dặm), 2-5 tuổi, 6-18 tuổi (Tanner/BAZ)\n" \
              "• Bảng đối chiếu phân loại Z-score chuẩn WHO (WAZ, HAZ, WHZ, BAZ)\n" \
              "• Checklist nhận diện thiếu hụt vi chất từ đầu đến chân (Head-to-Toe)."

    body = []
    body.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"chat_id\"\r\n\r\n{CHAT_ID}\r\n".encode("utf-8"))
    body.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"caption\"\r\n\r\n{caption}\r\n".encode("utf-8"))
    body.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"document\"; filename=\"{filename}\"\r\nContent-Type: application/pdf\r\n\r\n".encode("utf-8"))
    body.append(file_bytes)
    body.append(f"\r\n--{boundary}--\r\n".encode("utf-8"))
    
    payload = b"".join(body)
    req = urllib.request.Request(f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument", data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=40) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("   -> Kết quả gửi Telegram thành công:", res.get("ok"))
        return res

if __name__ == "__main__":
    pdf = generate_pdf()
    send_to_telegram(pdf)
    print("HOÀN TẤT 100%!")
