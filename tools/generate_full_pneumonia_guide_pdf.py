"""
generate_full_pneumonia_guide_pdf.py
Biên dịch CẨM NANG TOÀN DIỆN VIÊM PHỔI NHI KHOA CHUẨN ZERO-OMISSION (100% ĐẦY ĐỦ CHI TIẾT)
ra file PDF A4 (3 trang chuyên nghiệp) bằng Edge Headless và gửi qua Telegram Bot.
Không lược bỏ bất kỳ con số, cơ chế hay dấu hiệu lâm sàng nào.
"""
import os
import sys
import json
import subprocess
import urllib.request
from pathlib import Path
import shutil

# Paths
OUTPUT_DIR = Path(r"F:\DL\mavisresearch\Bai hoc y khoa\12_Nhi khoa\02_Ho_hap")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HTML_PATH = OUTPUT_DIR / "CAM_NANG_VIEM_PHOI_NHI_KHOA_ZERO_OMISSION.html"
PDF_PATH = OUTPUT_DIR / "CAM_NANG_VIEM_PHOI_NHI_KHOA_ZERO_OMISSION.pdf"
DESKTOP_PDF = Path(r"C:\Users\THANHANH\Desktop\Cam_Nang_Viem_Phoi_Nhi_Khoa_Toan_Dien_Zero_Omission.pdf")

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", "6569183642"))
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>CẨM NANG LÂM SÀNG TOÀN DIỆN: VIÊM PHỔI Ở TRẺ EM (ZERO-OMISSION)</title>
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
      font-size: 8.5pt;
      line-height: 1.4;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }
    
    /* Header bar */
    .header-box {
      border-bottom: 2.5px solid #0284c7;
      padding-bottom: 5px;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }
    .hospital-sub {
      font-size: 7.5pt;
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
      font-size: 13pt;
      font-weight: 800;
      color: #0f172a;
      text-transform: uppercase;
      margin: 3px 0 1px 0;
      letter-spacing: -0.01em;
    }
    .doc-subtitle {
      font-size: 8pt;
      font-weight: 500;
      color: #64748b;
      font-style: italic;
    }

    /* Section Styling */
    .section-title {
      font-size: 9pt;
      font-weight: 800;
      text-transform: uppercase;
      color: #0369a1;
      background: #f0f9ff;
      border-left: 3.5px solid #0284c7;
      padding: 3px 6px;
      margin: 8px 0 4px 0;
      display: flex;
      align-items: center;
      page-break-after: avoid;
    }

    /* Grid & Cards */
    .card-grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
      margin-bottom: 5px;
    }
    .card-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 5px;
      margin-bottom: 5px;
    }
    .panel {
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 5px 7px;
      page-break-inside: avoid;
    }
    .panel-header {
      font-weight: 800;
      font-size: 8.5pt;
      color: #0369a1;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 2px;
      margin-bottom: 3px;
      display: flex;
      justify-content: space-between;
    }
    .panel-header .badge {
      font-size: 6.5pt;
      background: #0284c7;
      color: #ffffff;
      padding: 1px 4px;
      border-radius: 3px;
      text-transform: uppercase;
    }
    
    .callout-box {
      background: #f8fafc;
      border-left: 3px solid #64748b;
      padding: 4px 7px;
      font-size: 8pt;
      margin: 4px 0;
      border-radius: 0 4px 4px 0;
      page-break-inside: avoid;
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
      font-size: 7.8pt;
      page-break-inside: avoid;
    }
    th, td {
      border: 1px solid #cbd5e1;
      padding: 3.5px 5.5px;
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
      margin: 2px 0 3px 12px;
      padding: 0;
    }
    li {
      margin-bottom: 1.5px;
    }

    .page-break {
      page-break-before: always;
    }

    .doc-footer {
      border-top: 1px solid #cbd5e1;
      padding-top: 3px;
      margin-top: 6px;
      font-size: 7.2pt;
      color: #94a3b8;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>

  <!-- ==================== TRANG 1 ==================== -->

  <!-- HEADER -->
  <div class="header-box">
    <div>
      <div class="hospital-sub">TÀI LIỆU HƯỚNG DẪN LÂM SÀNG & HUẤN LUYỆN Y KHOA • BỘ MÔN NHI KHOA</div>
      <div class="doc-title">CẨM NANG TOÀN DIỆN: VIÊM PHỔI Ở TRẺ EM</div>
      <div class="doc-subtitle">Bản chuẩn hóa Zero-Omission: Sinh lý bệnh • Quy trình 4 bước chẩn đoán • Phân độ WHO & Nhập viện • Cận lâm sàng chi tiết</div>
    </div>
    <div style="text-align: right;">
      <span class="doc-category">HÔ HẤP NHI LÂM SÀNG</span><br>
      <span style="font-size: 7pt; color: #64748b;">Trang 1/3 • Zero-Omission</span>
    </div>
  </div>

  <!-- PHẦN I: SINH LÝ BỆNH & CƠ CHẾ TỔN THƯƠNG -->
  <div class="section-title">I. SINH LÝ BỆNH & 2 CƠ CHẾ TRUNG TÂM DẪN ĐẾN SUY HÔ HẤP</div>
  <div class="card-grid-2">
    <div class="panel">
      <div class="panel-header">
        <span>1. RỐI LOẠN V/Q MISMATCH & SHUNT NỘI PHỔI</span>
        <span class="badge">TRAO ĐỔI KHÍ</span>
      </div>
      <ul>
        <li>Viêm cấp tính nhu mô phổi: Phế nang, phế quản tận và mô kẽ bị lấp đầy bởi dịch rỉ viêm, bạch cầu, fibrin và xác tế bào hoại tử.</li>
        <li><strong>Rối loạn tương xứng Thông khí / Tưới máu:</strong> Vùng phổi đông đặc mất hoàn toàn thông khí ($V = 0$) nhưng các mao mạch phổi xung quanh vẫn được tim bơm máu tưới ($Q > 0$).</li>
        <li><strong>Tạo dòng Shunt phải - trái nội phổi:</strong> Máu tĩnh mạch đi qua phế nang đông đặc không được trao đổi oxy $\rightarrow$ Đổ về nhĩ trái làm giảm nồng độ oxy máu hệ thống $\rightarrow$ <strong>Tụt $PaO_2$, tụt $SpO_2$</strong>.</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>2. GIẢM ĐỘ GIÃN NỞ (COMPLIANCE) & TĂNG CÔNG THỞ</span>
        <span class="badge">CƠ HỌC PHỔI</span>
      </div>
      <ul>
        <li>Nhu mô phổi đông đặc và ứ dịch trở nên "cứng" (giảm compliance), sức cản đường thở tăng cao.</li>
        <li>Trẻ phải tăng cường huy động các cơ hô hấp phụ (cơ liên sườn, cơ ức đòn chũm, cơ hoành) để kéo giãn lồng ngực $\rightarrow$ Xuất hiện các dấu hiệu cơ học: <strong>Rút lõm lồng ngực, phập phồng cánh mũi, đầu gật gù</strong>.</li>
        <li><strong>Kiệt cơ hô hấp (Exhaustion):</strong> Khi cơ liên sườn và cơ hoành kiệt sức, tiêu hao năng lượng tăng vọt $\rightarrow$ Nhịp thở có thể <strong>chậm lại bất thường</strong>, thở ngực bụng nghịch thường $\rightarrow$ Báo hiệu ngừng thở tối cấp!</li>
      </ul>
    </div>
  </div>

  <!-- PHẦN II: QUY TRÌNH 4 BƯỚC CHẨN ĐOÁN & PHÂN ĐỘ -->
  <div class="section-title">II. QUY TRÌNH 4 BƯỚC CHẨN ĐOÁN & PHÂN ĐỘ TẠI GIƯỜNG BỆNH</div>
  <div class="panel" style="margin-bottom: 5px;">
    <strong style="color: #0369a1;">BƯỚC 1: TRẺ CÓ BỊ VIÊM PHỔI KHÔNG?</strong> (Tiêu chuẩn WHO/IMCI: <strong>Có HO hoặc KHÓ THỞ + THỞ NHANH THEO LỨA TUỔI</strong>)
    <div style="font-size: 8pt; margin: 2px 0;">
      <em>Quy tắc đếm nhịp thở:</em> Đếm trọn vẹn trong <strong>60 giây</strong> khi trẻ nằm yên, không khóc, không sốt cao (phải hạ sốt trước khi đếm).
    </div>
    <table style="margin: 2px 0;">
      <thead>
        <tr>
          <th>Dưới 2 tháng tuổi</th>
          <th>Từ 2 đến 11 tháng tuổi</th>
          <th>Từ 12 tháng đến 5 tuổi</th>
          <th>Trên 5 tuổi (lâm sàng)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="color: #b91c1c; font-weight: 700;">$\ge 60$ lần/phút (Cảnh giác: bệnh rất nặng!)</td>
          <td style="font-weight: 700;">$\ge 50$ lần/phút</td>
          <td style="font-weight: 700;">$\ge 40$ lần/phút</td>
          <td style="font-weight: 700;">$\ge 30$ lần/phút</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="section-title">BẢNG PHÂN ĐỘ VIÊM PHỔI THEO WHO / IMCI (QUYẾT ĐỊNH TUYẾN ĐIỀU TRỊ)</div>
  <table>
    <thead>
      <tr>
        <th style="width: 20%;">Phân loại</th>
        <th style="width: 48%;">Tiêu chuẩn lâm sàng nhận diện</th>
        <th style="width: 32%;">Chiến lược điều trị & Tuyến xử trí</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Không viêm phổi</strong><br><small>(Ho hoặc cảm lạnh)</small></td>
        <td>• Có ho hoặc khó thở.<br>• <strong>Không</strong> thở nhanh theo lứa tuổi.<br>• <strong>Không</strong> rút lõm lồng ngực và không dấu hiệu nguy hiểm.</td>
        <td>• Chăm sóc, hạ sốt an toàn, vệ sinh mũi họng tại nhà.<br>• <strong>Không dùng kháng sinh</strong>.<br>• Dặn khám lại sau 2 ngày hoặc khi thở nhanh/nặng hơn.</td>
      </tr>
      <tr>
        <td><strong>2. Viêm phổi</strong><br><small>(Mức độ nhẹ - Ngoại trú)</small></td>
        <td>• Có ho hoặc khó thở + <strong>Có thở nhanh theo lứa tuổi</strong>.<br>• <strong>Không</strong> rút lõm lồng ngực.<br>• Không có dấu hiệu nguy hiểm toàn thân.</td>
        <td>• Điều trị ngoại trú với <strong>Amoxicillin uống liều cao: 80–90 mg/kg/ngày</strong> chia 2 lần x 5–7 ngày.<br>• Bắt buộc hẹn tái khám đánh giá sau 48 giờ.</td>
      </tr>
      <tr>
        <td><strong>3. Viêm phổi nặng</strong><br><small>(Bắt buộc nhập viện)</small></td>
        <td>• Thở nhanh + <strong>KÈM ÍT NHẤT 1 TRONG CÁC DẤU HIỆU:</strong><br>
           1) <strong>Rút lõm lồng ngực rõ</strong> (hạ sườn lõm vào ở thì hít vào).<br>
           2) <strong>Bất kỳ dấu hiệu nguy hiểm toàn thân nào</strong> (4 dấu hiệu bên dưới).<br>
           3) $SpO_2 < 90\%$ (hoặc $< 92\%$), tím tái trung ương.<br>
           4) Thở rên (grunting), phập phồng cánh mũi, đầu gật gù.</td>
        <td>• <strong>Nhập viện khẩn cấp / Khoa Cấp cứu</strong>.<br>
          • Thở oxy hỗ trợ nếu $SpO_2 < 92\%$ hoặc khó thở nặng.<br>
          • Kháng sinh tiêm tĩnh mạch: <strong>Ampicillin tiêm</strong> (150–200 mg/kg/ngày) hoặc <strong>Cefotaxime / Ceftriaxone</strong>.</td>
      </tr>
    </tbody>
  </table>

  <div class="callout-box callout-danger" style="margin-top: 3px;">
    🚨 <strong>4 Dấu hiệu nguy hiểm toàn thân (General Danger Signs):</strong> (1) Không uống được hoặc bỏ bú hoàn toàn; (2) Nôn tất cả mọi thứ uống/ăn vào; (3) Co giật trong đợt bệnh này hoặc đang co giật; (4) Li bì hoặc khó đánh thức (giảm tương tác nặng).
  </div>

  <!-- PHÂN ĐỘ NHẬP VIỆN CHUYÊN SÂU -->
  <div class="section-title">PHÂN ĐỘ LÂM SÀNG NHẬP VIỆN CHUYÊN SÂU (TẠI KHOA NỘI NHI / PICU)</div>
  <div class="card-grid-3">
    <div class="panel">
      <div class="panel-header">
        <span>VIÊM PHỔI NHẸ</span>
        <span class="badge">NGOẠI TRÚ / THEO DÕI</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li>Thở nhanh đơn thuần.</li>
        <li>Bú tốt, ăn uống được, tỉnh táo, tiếp xúc tốt.</li>
        <li>$SpO_2 \ge 95\%$ khí phòng, không co kéo cơ hô hấp phụ.</li>
      </ul>
    </div>
    <div class="panel">
      <div class="panel-header">
        <span>VIÊM PHỔI TRUNG BÌNH</span>
        <span class="badge">KHOA NỘI NHI</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li>Co kéo cơ liên sườn, rút lõm hõm ức mức độ vừa.</li>
        <li>Ăn/bú giảm (&lt; 50% bình thường), bứt rứt, quấy khóc.</li>
        <li>$SpO_2$ từ 92 – 94% khí phòng. Kháng sinh tiêm/uống có giám sát.</li>
      </ul>
    </div>
    <div class="panel">
      <div class="panel-header">
        <span>VIÊM PHỔI NẶNG / NGUY KỊCH</span>
        <span class="badge">CẤP CỨU / PICU</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li>Suy hô hấp nặng: Đầu gật gù, thở rên, thở nghịch thường.</li>
        <li>Li bì, da tái nổi vân tím, mạch nhanh yếu, $SpO_2 < 90–92\%$.</li>
        <li>Biến chứng: Tràn dịch/mủ màng phổi, tràn khí, áp xe phổi.</li>
      </ul>
    </div>
  </div>

  <!-- PHẦN CẬN LÂM SÀNG -->
  <div class="section-title">III. ĐẶC ĐIỂM CẬN LÂM SÀNG & GIÁ TRỊ THỰC TẾ</div>
  <div class="card-grid-3">
    <div class="panel">
      <div class="panel-header">
        <span>1. X-QUANG PHỔI THẲNG</span>
        <span class="badge">HÌNH ẢNH HỌC</span>
      </div>
      <ul style="font-size: 7.5pt;">
        <li><strong>Không chụp thường quy</strong> cho viêm phổi nhẹ ngoại trú.</li>
        <li><em>Chỉ định bắt buộc:</em> Viêm phổi nặng cần nhập viện, trẻ &lt; 2 tháng tuổi, nghi ngờ có biến chứng, hoặc thất bại sau 48–72h.</li>
        <li><strong>Đông đặc thùy (Lobar consolidation):</strong> Phế cầu, <em>Klebsiella</em> (hình ảnh phế quản khí).</li>
        <li><strong>Phế quản phế viêm:</strong> Ổ mờ rải rác 2 bên (Tụ cầu, Gr-).</li>
        <li><strong>Thâm nhiễm mô kẽ:</strong> Dày thành PQ, mạng lưới rốn phổi $\rightarrow$ Virus (RSV, Cúm) hoặc <em>Mycoplasma</em>.</li>
        <li><strong>Bóng khí (Pneumatocele) + Tràn mủ:</strong> Tụ cầu vàng.</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>2. HUYẾT HỌC & DẤU ẤN VIÊM</span>
        <span class="badge">XÉT NGHIỆM MÁU</span>
      </div>
      <ul style="font-size: 7.5pt;">
        <li><strong>Bạch cầu (WBC) & Neutrophil:</strong><br>
          • $\text{WBC} > 15.000/\mu\text{L}$ kèm $\text{Neu} > 70\%$: Nghiêng về vi khuẩn điển hình.<br>
          • $\text{WBC}$ bình thường/giảm, Lympho ưu thế: Hướng về virus.</li>
        <li><strong>CRP & Procalcitonin (PCT):</strong><br>
          • $\text{CRP} < 20\text{ mg/L}$: Thường do virus.<br>
          • $\text{CRP} > 40–60\text{ mg/L}$ hoặc $\text{PCT} > 0.5–2\text{ ng/mL}$: Khả năng cao do vi khuẩn, ủng hộ dùng kháng sinh và theo dõi đáp ứng.</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>3. TEST NHANH & PCR VIRUS</span>
        <span class="badge">VI SINH HỌC</span>
      </div>
      <ul style="font-size: 7.5pt;">
        <li><strong>Test nhanh RSV, Cúm A/B, Adenovirus:</strong><br>
          • Giúp cách ly tránh lây nhiễm chéo trong phòng bệnh.<br>
          • Hạn chế lạm dụng kháng sinh bao vây không cần thiết.<br>
          • Chỉ định sớm thuốc kháng virus đặc hiệu: <strong>Oseltamivir cho Cúm A</strong> trong vòng 48 giờ đầu khởi phát giúp giảm tỷ lệ tử vong và biến chứng phổi nặng.</li>
      </ul>
    </div>
  </div>

  <!-- FOOTER TRANG 1 -->
  <div class="doc-footer">
    <span>Bộ môn Nhi khoa • Cẩm nang Huấn luyện Kỹ năng Lâm sàng Y6</span>
    <span>Chuyên đề: Viêm phổi Trẻ em (Trang 1/3)</span>
    <span>Lưu hành học thuật</span>
  </div>

  <!-- ==================== TRANG 2 ==================== -->
  <div class="page-break"></div>

  <!-- HEADER TRANG 2 -->
  <div class="header-box">
    <div>
      <div class="hospital-sub">TÀI LIỆU HƯỚNG DẪN LÂM SÀNG & HUẤN LUYỆN Y KHOA • BỘ MÔN NHI KHOA</div>
      <div class="doc-title">CẨM NANG TOÀN DIỆN: VIÊM PHỔI Ở TRẺ EM (TIẾP THEO)</div>
      <div class="doc-subtitle">Phân định căn nguyên theo 3 trục • Tam giác chẩn đoán • Bảng đối chiếu 3 kiểu hình tại giường</div>
    </div>
    <div style="text-align: right;">
      <span class="doc-category">HÔ HẤP NHI LÂM SÀNG</span><br>
      <span style="font-size: 7pt; color: #64748b;">Trang 2/3 • Zero-Omission</span>
    </div>
  </div>

  <!-- PHẦN III: PHÂN ĐỊNH CĂN NGUYÊN THEO 3 TRỤC -->
  <div class="section-title">IV. PHÂN ĐỊNH CĂN NGUYÊN GÂY BỆNH THEO 3 TRỤC LÂM SÀNG THỰC CHIẾN</div>
  
  <!-- TRỤC 1: LỨA TUỔI -->
  <div style="margin-bottom: 3px; font-weight: 700; color: #0369a1; font-size: 8.3pt;">1. TRỤC THỨ NHẤT: PHÂN ĐỊNH THEO LỨA TUỔI (YẾU TỐ QUYẾT ĐỊNH HÀNG ĐẦU)</div>
  <table>
    <thead>
      <tr>
        <th style="width: 20%;">Nhóm tuổi</th>
        <th style="width: 38%;">Căn nguyên hàng đầu</th>
        <th style="width: 42%;">Đặc điểm lâm sàng & Cờ đỏ nhận diện</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Sơ sinh sớm<br><small>(&lt; 72 giờ tuổi)</small></strong></td>
        <td>• <strong>Liên cầu nhóm B (GBS)</strong> (<em>S. agalactiae</em>)<br>• <em>E. coli</em> và vi khuẩn Gram âm đường ruột<br>• <em>Listeria monocytogenes</em></td>
        <td>• Lây truyền chu sinh từ đường sinh dục mẹ (mẹ sốt, ối vỡ sớm &gt; 18h, viêm màng ối).<br>• Suy hô hấp xuất hiện ngay sau sinh, tiến triển nhanh thành sốc nhiễm khuẩn.</td>
      </tr>
      <tr>
        <td><strong>Sơ sinh muộn<br><small>(4 – 28 ngày tuổi)</small></strong></td>
        <td>• <strong>Tụ cầu vàng (<em>S. aureus</em>)</strong><br>• <em>Klebsiella pneumoniae</em>, <em>Pseudomonas</em><br>• GBS muộn, Virus (RSV, CMV, Enterovirus)</td>
        <td>• Nhiễm trùng từ môi trường bệnh viện/chăm sóc.<br>• Tổn thương hoại tử lan tỏa, dễ có bóng khí, tràn mủ màng phổi (nghĩ ngay đến Tụ cầu!).</td>
      </tr>
      <tr>
        <td><strong>1 – 3 tháng tuổi<br><small>(Giao thời)</small></strong></td>
        <td>• <strong>Virus hô hấp:</strong> RSV, Rhinovirus, Á cúm<br>• <strong>Vi khuẩn không sốt:</strong> <em>Chlamydia trachomatis</em><br>• <strong>Ho gà (<em>Bordetella pertussis</em>)</strong></td>
        <td>• <strong>Hội chứng viêm phổi không sốt:</strong> Trẻ ho ngắt quãng, thở nhanh nhưng không sốt, tiền sử mẹ viêm âm đạo/trẻ viêm kết mạc lúc 1–2 tuần tuổi $\rightarrow$ <em>Chlamydia</em>.<br>• Ho rũ rượi, đỏ mặt/tím tái, thở rít sau ho, bạch cầu Lympho tăng vọt $\rightarrow$ Ho gà.</td>
      </tr>
      <tr>
        <td><strong>3 tháng – 5 tuổi<br><small>(Tập trung nhiều nhất)</small></strong></td>
        <td>• <strong>Virus (chiếm 60–70%):</strong> RSV, Cúm A/B, Adeno, Parainfluenza, hMPV.<br>• <strong>Vi khuẩn điển hình:</strong> Phế cầu (<em>S. pneumoniae</em> - số 1), Hib, Tụ cầu vàng (kể cả CA-MRSA).</td>
        <td>• <strong>Virus:</strong> Khởi phát từ từ, viêm long hô hấp trên rầm rộ, ran rít/ngáy rải rác 2 bên, X-quang tổn thương mô kẽ, bạch cầu không tăng cao.<br>• <strong>Vi khuẩn:</strong> Sốt cao đột ngột, thở rên, vẻ mặt nhiễm độc, ran ẩm khu trú, đông đặc thùy.</td>
      </tr>
      <tr>
        <td><strong>Trên 5 tuổi<br><small>(Đi học & vị thành niên)</small></strong></td>
        <td>• <strong>Vi khuẩn không điển hình (30–50%):</strong> <em>Mycoplasma pneumoniae</em>, <em>C. pneumoniae</em>.<br>• Phế cầu (<em>S. pneumoniae</em>)<br>• Virus cúm, Adenovirus</td>
        <td>• <strong>Dấu hiệu "Phân ly lâm sàng - X quang":</strong> Trẻ sốt nhẹ/vừa, ho khan kịch phát dai dẳng, khám phổi ran rất ít nhưng X-quang tổn thương mô kẽ/đông đặc lan tỏa nặng nề.<br>• Có biểu hiện ngoài phổi: đau đầu, phát ban dát sẩn, đau cơ, thiếu máu tán huyết nhẹ.</td>
      </tr>
    </tbody>
  </table>

  <!-- TRỤC 2 & 3 -->
  <div class="card-grid-2" style="margin-top: 4px;">
    <div class="panel">
      <div class="panel-header">
        <span>2. TRỤC HOÀN CẢNH PHƠI NHIỄM</span>
        <span class="badge">DỊCH TỄ HỌC</span>
      </div>
      <ul style="font-size: 7.5pt;">
        <li><strong>Viêm phổi hít (Aspiration Pneumonia):</strong><br>
          • <em>Đối tượng:</em> Trẻ bại não, động kinh, GERD nặng, teo thực quản, sặc sữa/cháo, dị vật đường thở.<br>
          • <em>Căn nguyên:</em> Vi khuẩn kỵ khí vùng hầu họng (<em>Bacteroides, Peptostreptococcus, Fusobacterium</em>) + Gram âm đường ruột (<em>E. coli, Klebsiella</em>) + Axit dạ dày gây bỏng hóa học mô phổi.<br>
          • <em>X-quang:</em> Tổn thương ưu thế ở phân thùy đỉnh của thùy dưới hoặc phân thùy sau của thùy trên.</li>
        <li><strong>Viêm phổi bệnh viện (HAP/VAP):</strong><br>
          • Nằm viện / thở máy $\ge 48$ giờ mới xuất hiện tổn thương.<br>
          • Căn nguyên vi khuẩn đa kháng ESKAPE: <em>Pseudomonas aeruginosa</em>, <em>Acinetobacter baumannii</em>, <em>Klebsiella</em> sinh ESBL, MRSA bệnh viện, Nấm xâm lấn (<em>Candida</em>).</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>3. TRỤC CƠ ĐỊA ĐẶC BIỆT & SUY GIẢM MIỄN DỊCH</span>
        <span class="badge">MIỄN DỊCH HỌC</span>
      </div>
      <ul style="font-size: 7.5pt;">
        <li><strong>Suy dinh dưỡng cấp nặng (SAM - Marasmus/Kwashiorkor):</strong><br>
          • Tác nhân: Gr(-) đường ruột, Tụ cầu, Trực khuẩn Lao.<br>
          • ⚠️ <em>Bẫy:</em> Trẻ SAM bị viêm phổi nặng thường <strong>không sốt, không ho rõ</strong> do suy kiệt phản ứng viêm; chỉ lờ đờ, hạ thân nhiệt, thở nhanh kín đáo.</li>
        <li><strong>Tim bẩm sinh có luồng thông Trái - Phải (VSD, PDA lớn):</strong><br>
          • Ứ huyết phổi liên tục $\rightarrow$ phù nề biểu mô $\rightarrow$ vi khuẩn dễ bám dính. Hay gặp Phế cầu, Tụ cầu, RSV gây suy hô hấp tối cấp.</li>
        <li><strong>Suy giảm miễn dịch tế bào / HIV / Ghép tạng / Corticoid kéo dài:</strong><br>
          • <strong><em>Pneumocystis jirovecii</em> (PJP/PCP):</strong> Khó thở dữ dội, $SpO_2$ tụt sâu nhưng khám ít ran; X-quang kính mờ đối xứng cánh bướm.<br>
          • CMV, Nấm xâm lấn (<em>Aspergillus</em>), Lao và NTM.</li>
        <li><strong>Suy giảm miễn dịch dịch thể:</strong> Vi khuẩn có vỏ bọc (Phế cầu, Hib).</li>
      </ul>
    </div>
  </div>

  <!-- PHẦN BẢNG ĐỐI CHIẾU 3 KIỂU HÌNH -->
  <div class="section-title">V. BẢNG ĐỐI CHIẾU PHÂN BIỆT 3 KIỂU HÌNH CĂN NGUYÊN TẠI GIƯỜNG BỆNH</div>
  <table>
    <thead>
      <tr>
        <th style="width: 17%;">Tiêu chí lâm sàng</th>
        <th style="width: 28%;">Viêm phổi Điển hình (Vi khuẩn)</th>
        <th style="width: 27%;">Viêm phổi Không điển hình (<em>Mycoplasma</em>)</th>
        <th style="width: 28%;">Viêm phổi do Virus hô hấp</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Độ tuổi ưu thế</strong></td>
        <td>Mọi lứa tuổi (đặc biệt 1 – 5 tuổi).</td>
        <td>Trẻ &gt; 5 tuổi và thanh thiếu niên.</td>
        <td>Nhũ nhi & trẻ &lt; 2 tuổi.</td>
      </tr>
      <tr>
        <td><strong>Khởi phát & Sốt</strong></td>
        <td>Đột ngột, rầm rộ, sốt cao 39–40°C, vẻ mặt nhiễm độc.</td>
        <td>Bán cấp, từ từ, sốt nhẹ hoặc vừa, mệt mỏi, đau đầu.</td>
        <td>Từ từ, sau đợt cảm lạnh / viêm mũi họng, sốt vừa.</td>
      </tr>
      <tr>
        <td><strong>Tính chất ho</strong></td>
        <td>Ho có đờm đục (trẻ lớn) hoặc ho lọc xọc.</td>
        <td><strong>Ho khan kịch phát, rũ rượi, dai dẳng hàng tuần.</strong></td>
        <td>Ho kèm khò khè, thở rít, thở nông.</td>
      </tr>
      <tr>
        <td><strong>Khám phổi</strong></td>
        <td><strong>Ran ẩm to/nhỏ hạt khu trú 1 vùng</strong>, đông đặc rõ.</td>
        <td>Khám nghe ran rất ít dù bệnh nhân ho dữ dội.</td>
        <td><strong>Ran rít, ran ngáy, ran ẩm rải rác cả 2 phế trường.</strong></td>
      </tr>
      <tr>
        <td><strong>Dấu hiệu ngoài phổi</strong></td>
        <td>Ít gặp biểu hiện ngoài phổi.</td>
        <td>Đau đầu, đau cơ, nổi ban đỏ dát sẩn, đau khớp.</td>
        <td>Chảy mũi trong, đỏ kết mạc mắt, tiêu chảy nhẹ.</td>
      </tr>
      <tr>
        <td><strong>Bạch cầu & CRP</strong></td>
        <td>$\text{WBC} > 15.000/\mu\text{L}$ (Neutrophil ưu thế), $\text{CRP} > 40–60\text{ mg/L}$.</td>
        <td>$\text{WBC}$ bình thường/tăng nhẹ, $\text{CRP}$ tăng nhẹ ($10–40\text{ mg/L}$).</td>
        <td>$\text{WBC} < 15.000/\mu\text{L}$ (Lympho ưu thế), $\text{CRP} < 20\text{ mg/L}$.</td>
      </tr>
      <tr>
        <td><strong>Hình ảnh X-quang</strong></td>
        <td><strong>Đông đặc phân thùy/thùy</strong>, có phế quản khí.</td>
        <td>Thâm nhiễm mô kẽ quanh rốn phổi hoặc lưới nốt.</td>
        <td>Dày thành phế quản, ứ khí phế nang 2 bên.</td>
      </tr>
      <tr>
        <td><strong>Lựa chọn Kháng sinh</strong></td>
        <td><strong>Amoxicillin / Ampicillin / Cefotaxime</strong></td>
        <td><strong>Macrolide (Azithromycin / Clarithromycin)</strong></td>
        <td><strong>Không dùng kháng sinh</strong> (Cúm: Oseltamivir)</td>
      </tr>
    </tbody>
  </table>

  <!-- FOOTER TRANG 2 -->
  <div class="doc-footer">
    <span>Bộ môn Nhi khoa • Cẩm nang Huấn luyện Kỹ năng Lâm sàng Y6</span>
    <span>Chuyên đề: Viêm phổi Trẻ em (Trang 2/3)</span>
    <span>Lưu hành học thuật</span>
  </div>

  <!-- ==================== TRANG 3 ==================== -->
  <div class="page-break"></div>

  <!-- HEADER TRANG 3 -->
  <div class="header-box">
    <div>
      <div class="hospital-sub">TÀI LIỆU HƯỚNG DẪN LÂM SÀNG & HUẤN LUYỆN Y KHOA • BỘ MÔN NHI KHOA</div>
      <div class="doc-title">CẨM NANG TOÀN DIỆN: VIÊM PHỔI Ở TRẺ EM (TIẾP THEO)</div>
      <div class="doc-subtitle">Chiến lược kháng sinh phân cấp • Thuật toán 5 chữ C thất bại 48-72h • 4 Cờ đỏ tử vong & Bài học buồng bệnh</div>
    </div>
    <div style="text-align: right;">
      <span class="doc-category">HÔ HẤP NHI LÂM SÀNG</span><br>
      <span style="font-size: 7pt; color: #64748b;">Trang 3/3 • Zero-Omission</span>
    </div>
  </div>

  <!-- PHẦN CHIẾN LƯỢC KHÁNG SINH -->
  <div class="section-title">VI. CHIẾN LƯỢC ĐIỀU TRỊ KHÁNG SINH PHÂN CẤP THEO Y HỌC CHỨNG CỨ (EBM)</div>
  <div class="card-grid-2">
    <div class="panel">
      <div class="panel-header">
        <span>1. PHÁC ĐỒ KHÁNG SINH NGOẠI TRÚ & NỘI TRÚ</span>
        <span class="badge">PHÁC ĐỒ CHUẨN</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li><strong>NGOẠI TRÚ (VIÊM PHỔI NHẸ):</strong><br>
          • <em>Lựa chọn 1:</em> <strong>AMOXICILLIN LIỀU CAO: 80 – 90 mg/kg/ngày</strong> chia 2 lần uống x 5 – 7 ngày.<br>
          • <em>Nghi Mycoplasma (&gt; 5 tuổi):</em> <strong>AZITHROMYCIN</strong> 10 mg/kg ngày 1 (tối đa 500mg), sau đó 5 mg/kg/ngày từ ngày 2 đến 5 (tối đa 250mg).</li>
        <li><strong>NỘI TRÚ (VIÊM PHỔI NẶNG):</strong><br>
          • <em>Lựa chọn 1:</em> <strong>AMPICILLIN TIÊM TM</strong>: 150 – 200 mg/kg/ngày chia 4 lần.<br>
          • <em>Lựa chọn thay thế (chưa tiêm phòng Hib/Phế cầu hoặc nghi Gr-):</em> <strong>CEFOTAXIME</strong> (150 mg/kg/ngày chia 3 lần) hoặc <strong>CEFTRIAXONE</strong> (80 mg/kg/ngày tiêm 1 lần).</li>
        <li><strong>Trẻ sơ sinh (&lt; 2 tháng tuổi):</strong> Phổ vi khuẩn chu sinh $\rightarrow$ Phác đồ bắt buộc: <strong>AMPICILLIN + GENTAMICIN</strong> (hoặc Cefotaxime).</li>
        <li><strong>Nghi ngờ Tụ cầu (bóng khí, mụn mủ, tiến triển sét đánh):</strong> Bổ sung <strong>OXACILLIN / CLOXACILLIN</strong> (200 mg/kg/ngày) hoặc <strong>VANCOMYCIN / LINEZOLID</strong> (nếu nghi MRSA).</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>2. CƠ CHẾ DÙNG AMOXICILLIN LIỀU CAO (80–90 mg/kg/ngày)</span>
        <span class="badge">DƯỢC LÝ LÂM SÀNG</span>
      </div>
      <div style="font-size: 7.7pt; line-height: 1.45;">
        • <strong>Cơ chế đề kháng của Phế cầu (<em>S. pneumoniae</em>):</strong> Phế cầu kháng Penicillin/Amoxicillin bằng cách <strong>thay đổi cấu trúc protein gắn Penicillin (PBP)</strong>, chứ <strong>KHÔNG tiết men Beta-lactamase</strong>.<br><br>
        • <strong>Ý nghĩa nâng liều cao:</strong> Việc tăng liều Amoxicillin lên 80–90 mg/kg/ngày sẽ nâng nồng độ thuốc trong huyết tương và mô phổi vượt ngưỡng ức chế tối thiểu ($MIC$), giúp <strong>bão hòa và vượt qua được ái lực yếu của các thụ thể PBP đã biến đổi</strong>.<br><br>
        • <strong>Hệ quả thực hành:</strong> Tiêu diệt được hầu hết các chủng phế cầu kháng trung gian mà <strong>không cần vội vàng dùng Cephalosporin thế hệ 3 hoặc thêm Acid Clavulanic</strong> (giảm tác dụng phụ tiêu chảy và hạn chế chọn lọc vi khuẩn kháng thuốc).
      </div>
    </div>
  </div>

  <!-- PHẦN ĐÁNH GIÁ ĐÁP ỨNG & THUẬT TOÁN 48-72 GIỜ -->
  <div class="section-title">VII. ĐÁNH GIÁ ĐÁP ỨNG & THUẬT TOÁN XỬ TRÍ THẤT BẠI SAU 48–72 GIỜ (5 CHỮ C)</div>
  <table style="margin-bottom: 4px;">
    <thead>
      <tr>
        <th style="width: 20%;">Dấu hiệu theo dõi</th>
        <th style="width: 40%;">ĐÁP ỨNG TỐT (Tiếp tục phác đồ)</th>
        <th style="width: 40%;">THẤT BẠI ĐIỀU TRỊ (Báo động!)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Thân nhiệt</strong></td>
        <td>Cắt sốt hoặc nhiệt độ giảm dần, cơn sốt thưa ra.</td>
        <td>Vẫn sốt cao liên tục hoặc sốt vọt trở lại.</td>
      </tr>
      <tr>
        <td><strong>Nhịp thở & Công thở</strong></td>
        <td>Nhịp thở chậm lại (giảm $\ge 5$ nhịp/phút), rút lõm ngực đỡ dần.</td>
        <td>Thở nhanh hơn, co kéo tăng lên, xuất hiện thở rên.</td>
      </tr>
      <tr>
        <td><strong>Ăn uống & Tri giác</strong></td>
        <td>Bú khá hơn, đòi ăn, tương tác mắt tốt, chơi ngoan.</td>
        <td>Bỏ bú hoàn toàn, li bì, mệt lả, quấy khóc không dỗ được.</td>
      </tr>
      <tr>
        <td><strong>$SpO_2$</strong></td>
        <td>Duy trì $\ge 95\%$ khí phòng, giảm dần nhu cầu thở oxy.</td>
        <td>Tụt $SpO_2$, phụ thuộc oxy tăng dần.</td>
      </tr>
    </tbody>
  </table>

  <!-- THUẬT TOÁN 5 CHỮ C -->
  <div class="panel" style="margin-bottom: 5px;">
    <div class="panel-header">
      <span>THUẬT TOÁN 5 CHỮ C TÌM NGUYÊN NHÂN KHI ĐIỀU TRỊ THẤT BẠI SAU 48–72 GIỜ</span>
      <span class="badge">ALGORITHM</span>
    </div>
    <div style="font-size: 7.7pt; display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px;">
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 4px; border-radius: 3px;">
        <strong style="color: #0369a1;">1. Complications</strong><br>
        <strong>Biến chứng:</strong> Tràn mủ màng phổi, tràn khí, xẹp phổi, áp xe $\rightarrow$ Chụp lại X-quang hoặc Siêu âm màng phổi ngay!
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 4px; border-radius: 3px;">
        <strong style="color: #0369a1;">2. Coverage</strong><br>
        <strong>Chưa trùm đúng:</strong> Vi khuẩn kháng thuốc (MRSA), vi khuẩn không điển hình (cần Macrolide), hoặc thực tế là virus/nấm/lao.
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 4px; border-radius: 3px;">
        <strong style="color: #0369a1;">3. Compliance</strong><br>
        <strong>Tuân thủ & Liều:</strong> Liều có bị thiếu cân? Hấp thu đường uống kém (nôn)? Đường truyền tiêm có thông suốt?
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 4px; border-radius: 3px;">
        <strong style="color: #0369a1;">4. Co-morbidity</strong><br>
        <strong>Bệnh nền đi kèm:</strong> Dị tật tim bẩm sinh shunt lớn, GERD trào ngược sặc liên tục, suy giảm miễn dịch tiềm ẩn.
      </div>
      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 4px; border-radius: 3px;">
        <strong style="color: #0369a1;">5. Cause not pneumonia</strong><br>
        <strong>Chẩn đoán sai:</strong> Dị vật đường thở bỏ quên, cơn hen phế quản đầu tiên, suy tim ứ huyết, vòng nhẫn mạch máu.
      </div>
    </div>
  </div>

  <!-- PHẦN VIII: 4 CỜ ĐỎ LÂM SÀNG & BÀI HỌC BUỒNG BỆNH -->
  <div class="callout-box callout-danger" style="margin-top: 3px; padding: 5px 8px;">
    <strong style="font-size: 8.5pt;">VIII. 4 "CỜ ĐỎ" LÂM SÀNG TỬ VONG & BÀI HỌC XƯƠNG MÁU TẠI BUỒNG BỆNH:</strong>
    <ol style="margin: 2px 0 0 14px; font-size: 7.7pt;">
      <li><strong>1. Cảnh giác tối cao với trẻ Sơ sinh nhiễm RSV:</strong> RSV ở trẻ sơ sinh (&lt; 28 ngày) cơ chế nguy hiểm nhất là <strong>ức chế trung tâm hô hấp ở hành não $\rightarrow$ Cơn ngừng thở (Apnea)</strong>. Trẻ có thể ngừng thở đột ngột trong khi chưa kịp có biểu hiện thở co kéo rầm rộ! Bắt buộc gắn monitor theo dõi nhịp thở và nhịp tim liên tục.</li>
      <li><strong>2. Bẫy bỏ sót Viêm tai giữa mủ đi kèm:</strong> Tai giữa thông với vòm họng qua vòi Eustache (ở trẻ em ngắn, rộng và nằm ngang). Vi khuẩn viêm phổi rất dễ lan lên tai giữa. Trẻ viêm phổi dùng kháng sinh 3 ngày mà vẫn quấy khóc, bứt rứt, sốt âm ỉ: <strong>phải soi màng nhĩ ngay</strong>, không vội đổi kháng sinh phổ rộng toàn thân khi chưa kiểm soát ổ mủ tai giữa.</li>
      <li><strong>3. CẤM TUYỆT ĐỐI dùng thuốc ức chế ho (Codeine, Dextromethorphan):</strong> Ho là phản xạ sinh lý tống xuất đờm mủ bảo vệ đường thở. Dùng giảm ho làm ứ đọng đờm tắc nghẽn phế quản, nguy cơ suy hô hấp và xẹp phổi. Chăm sóc hút rửa thông mũi họng trước cữ bú quan trọng hơn nhiều so với việc chỉ chăm chăm dùng khí dung.</li>
      <li><strong>4. Nhận diện sớm tổn thương Tụ cầu & Viêm phổi hoại tử:</strong> X-quang có <strong>bóng khí (pneumatocele), tràn mủ màng phổi hoặc áp xe nhiều ổ</strong> $\rightarrow$ Nghĩ ngay đến Tụ cầu vàng $\rightarrow$ Dẫn lưu sớm và phối hợp Vancomycin/Linezolid. Cơn ho ngưng thở kèm bạch cầu tăng vọt (&gt; 30.000–50.000/µL, lympho &gt; 70%) cảnh giác Ho gà ác tính gây tăng áp phổi!</li>
    </ol>
  </div>

  <!-- FOOTER TRANG 3 -->
  <div class="doc-footer">
    <span>Bộ môn Nhi khoa • Lưu hành đào tạo lâm sàng Y6 & Bác sĩ thực hành</span>
    <span>Dựa trên Hướng dẫn Bộ Y tế, WHO và Nelson Textbook of Pediatrics (21st Edition)</span>
    <span>Trang 3/3</span>
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
    boundary = "----WebKitFormBoundaryPneumoniaZeroOmission2026"
    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    
    with open(pdf_file, "rb") as f:
        file_bytes = f.read()
        
    filename = "Cam_Nang_Viem_Phoi_Nhi_Khoa_Zero_Omission.pdf"
    
    caption = "🫁 CẨM NANG TOÀN DIỆN: VIÊM PHỔI Ở TRẺ EM (ZERO-OMISSION - 100% ĐẦY ĐỦ)\n\n" \
              "• Sinh lý bệnh: V/Q Mismatch, Shunt nội phổi, giảm độ giãn nở & Kiệt cơ hô hấp\n" \
              "• Quy trình 4 bước chẩn đoán & Phân độ WHO / IMCI + Phân độ nhập viện chuyên sâu\n" \
              "• Phân định căn nguyên 3 trục: Tuổi (Sơ sinh đến >5t), Hoàn cảnh (Hít/HAP), Cơ địa (SAM/Tim BS/PJP)\n" \
              "• Bảng đối chiếu 3 kiểu hình tại giường: Vi khuẩn điển hình vs Mycoplasma vs Virus\n" \
              "• Cận lâm sàng chi tiết: X-quang, WBC, CRP, PCT, Test nhanh & PCR virus hô hấp\n" \
              "• Chiến lược kháng sinh phân cấp & Cơ chế Amoxicillin liều cao (80-90 mg/kg/ngày)\n" \
              "• Thuật toán đánh giá đáp ứng sau 48-72h & 5 chữ C khi thất bại điều trị\n" \
              "• 4 Cờ đỏ lâm sàng tử vong & Bài học thực tế buồng bệnh."

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
