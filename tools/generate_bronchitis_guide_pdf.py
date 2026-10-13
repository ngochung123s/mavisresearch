"""
generate_bronchitis_guide_pdf.py
Biên dịch Cẩm nang Toàn diện Viêm phế quản Trẻ em (Định nghĩa, Giải phẫu, Căn nguyên, 
3 Giai đoạn, 4 Thể lâm sàng, Chẩn đoán phân biệt, EBM Điều trị & Cờ đỏ) ra PDF chuẩn A4 
bằng Microsoft Edge Headless, lưu tại Desktop và tự động gửi qua Telegram Bot.
Bảo toàn 100% dữ kiện, ZERO OMISSION, không lược bớt bất kỳ nội dung nào.
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

HTML_PATH = OUTPUT_DIR / "CAM_NANG_VIEM_PHE_QUAN_NHI_KHOA_TOAN_DIEN.html"
PDF_PATH = OUTPUT_DIR / "CAM_NANG_VIEM_PHE_QUAN_NHI_KHOA_TOAN_DIEN.pdf"
DESKTOP_PDF = Path(r"C:\Users\THANHANH\Desktop\Huong_Dan_Viem_Phe_Quan_Nhi_Khoa_Toan_Dien.pdf")

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID", "6569183642"))
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>CẨM NANG LÂM SÀNG TOÀN DIỆN: VIÊM PHẾ QUẢN Ở TRẺ EM</title>
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
      <div class="doc-title">CẨM NANG TOÀN DIỆN: VIÊM PHẾ QUẢN Ở TRẺ EM</div>
      <div class="doc-subtitle">Giải phẫu • Sinh lý bệnh • 3 Giai đoạn tiến triển • 4 Thể lâm sàng • Chẩn đoán phân biệt • Phác đồ EBM & Cờ đỏ</div>
    </div>
    <div style="text-align: right;">
      <span class="doc-category">HÔ HẤP NHI LÂM SÀNG</span><br>
      <span style="font-size: 7pt; color: #64748b;">Trang 1/2 • Y6 Clinical</span>
    </div>
  </div>

  <!-- PHẦN I: ĐỊNH NGHĨA & PHÂN BIỆT GIẢI PHẪU -->
  <div class="section-title">I. ĐỊNH NGHĨA & BẪY PHÂN BIỆT GIẢI PHẪU: VIÊM PHẾ QUẢN vs VIÊM TIỂU PHẾ QUẢN</div>
  <div style="margin-bottom: 4px; font-size: 8.2pt;">
    <strong>Định nghĩa:</strong> Viêm phế quản cấp là tình trạng viêm cấp tính của niêm mạc cây phế quản lớn và trung bình (từ phế quản gốc đến phế quản phân thùy — nơi thành phế quản <strong>vẫn còn sụn và tuyến tiết nhầy</strong>).
  </div>
  <table>
    <thead>
      <tr>
        <th style="width: 20%;">Tiêu chí so sánh</th>
        <th style="width: 40%;">Viêm phế quản (Bronchitis)</th>
        <th style="width: 40%;">Viêm tiểu phế quản (Bronchiolitis)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Vị trí tổn thương</strong></td>
        <td>Phế quản lớn & vừa (thành có sụn nâng đỡ, có tuyến tiết nhầy).</td>
        <td><strong>Tiểu phế quản tận & hô hấp</strong> (&lt; 2 mm, <strong>hoàn toàn không có sụn</strong>).</td>
      </tr>
      <tr>
        <td><strong>Lứa tuổi ưu thế</strong></td>
        <td>Trẻ lớn, trẻ mẫu giáo, học đường (&gt; 2 tuổi).</td>
        <td><strong>Trẻ nhũ nhi &lt; 2 tuổi</strong> (đặc biệt đỉnh điểm lứa tuổi &lt; 6 tháng).</td>
      </tr>
      <tr>
        <td><strong>Cơ chế tắc nghẽn</strong></td>
        <td>Phù nề niêm mạc + <strong>tăng tiết dịch nhầy trong lòng ống</strong>.</td>
        <td>Phù nề + hoại tử biểu mô $\rightarrow$ <strong>tắc nút nhầy sụp đổ tiểu phế quản</strong> (do không có sụn).</td>
      </tr>
      <tr>
        <td><strong>Dấu hiệu suy hô hấp</strong></td>
        <td><strong>Hiếm khi suy hô hấp</strong> (trừ thể co thắt nặng hoặc có bệnh nền).</td>
        <td><strong>Suy hô hấp rầm rộ</strong>, ứ khí phế nang, rút lõm ngực dữ dội, thở nhanh.</td>
      </tr>
      <tr>
        <td><strong>Ran nghe phổi</strong></td>
        <td><strong>Ran ngáy, ran rít, ran ẩm to hạt</strong> (thay đổi sau khi ho/vỗ rung).</td>
        <td><strong>Ran rít, ran ngáy, ran ẩm nhỏ hạt / ran nổ</strong> mịn cuối thì hít vào.</td>
      </tr>
    </tbody>
  </table>

  <!-- PHẦN II: CĂN NGUYÊN GÂY BỆNH -->
  <div class="section-title">II. CĂN NGUYÊN GÂY BỆNH: 85 – 90% LÀ VIRUS</div>
  <div class="card-grid-3">
    <div class="panel">
      <div class="panel-header">
        <span>1. VIRUS (ĐẠI ĐA SỐ 85–90%)</span>
        <span class="badge">CHÍNH</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li><strong>Rhinovirus</strong> (cảm lạnh lan xuống phế quản).</li>
        <li><strong>RSV</strong> (Virus hợp bào hô hấp).</li>
        <li><strong>Cúm A / B (Influenza)</strong>, Parainfluenza.</li>
        <li><strong>Adenovirus</strong>, Human Metapneumovirus (hMPV).</li>
        <li><em>Ý nghĩa:</em> Bệnh lý <strong>tự giới hạn (self-limiting)</strong>, kháng sinh không rút ngắn thời gian bệnh!</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>2. VI KHUẨN (HIẾM GẶP CẤP)</span>
        <span class="badge">ĐẶC BIỆT</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li><strong>Vi khuẩn không điển hình:</strong> <em>Mycoplasma pneumoniae</em>, <em>Chlamydophila pneumoniae</em> (ưu thế trẻ &gt; 5 tuổi, ho dai dẳng).</li>
        <li><strong>Ho gà (<em>Bordetella pertussis</em>):</strong> Cơn ho rũ rượi, tím tái, thở rít sau ho, nôn sau ho.</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>3. THỂ KÉO DÀI (PBB)</span>
        <span class="badge">BIOFILM</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li><strong>Viêm phế quản kéo dài vi khuẩn (PBB):</strong></li>
        <li><em>Haemophilus influenzae</em> không định type (NTHi).</li>
        <li><em>Streptococcus pneumoniae</em>, <em>M. catarrhalis</em>.</li>
        <li>Cơ chế tạo màng <strong>Biofilm</strong> dai dẳng trên niêm mạc.</li>
      </ul>
    </div>
  </div>

  <!-- PHẦN III: DIỄN TIẾN LÂM SÀNG QUA 3 GIAI ĐOẠN -->
  <div class="section-title">III. DIỄN TIẾN LÂM SÀNG QUA 3 GIAI ĐOẠN (10 – 14 NGÀY)</div>
  <div class="card-grid-3">
    <div class="panel">
      <div class="panel-header">
        <span>PHA 1: KHỞI PHÁT / VIÊM KHÔ</span>
        <span class="badge">NGÀY 1 - 3</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li>Viêm long hô hấp trên: Hắt hơi, sổ mũi trong, nghẹt mũi.</li>
        <li>Sốt nhẹ hoặc vừa ($37.5 - 38.5^\circ\text{C}$).</li>
        <li>Ho khan, rát cổ họng, cảm giác đau tức sau xương ức khi ho.</li>
        <li>Nghe phổi: Rì rào phế nang rõ, chưa có ran bệnh lý.</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>PHA 2: XUẤT TIẾT & Ứ ĐỌNG</span>
        <span class="badge">NGÀY 4 - 8</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li>Ho đờm, ho lọc xọc. Trẻ nhỏ nuốt đờm kích thích nôn trớ.</li>
        <li>Đờm đổi sang màu <strong>VÀNG / XANH</strong>.</li>
        <li>⚠️ <em>Bẫy:</em> Đờm vàng/xanh do men Myeloperoxidase của xác bạch cầu, <strong>KHÔNG PHẢI do vi khuẩn</strong>!</li>
        <li>Nghe phổi: <strong>Ran ngáy, ran rít, ran ẩm to hạt</strong> (thay đổi sau ho).</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>PHA 3: LUI BỆNH & HỒI PHỤC</span>
        <span class="badge">NGÀY 9 - 14</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li>Cắt sốt hoàn toàn, trẻ chơi ngoan, ăn uống bình thường trở lại.</li>
        <li>Đờm trong và loãng dần, giảm tần số cơn ho.</li>
        <li>Phản xạ tăng nhạy cảm đường thở (ho khan nhẹ) có thể còn kéo dài thêm 2–3 tuần.</li>
      </ul>
    </div>
  </div>

  <!-- PHẦN IV: BỐN THỂ LÂM SÀNG THƯỜNG GẶP -->
  <div class="section-title">IV. BỐN THỂ LÂM SÀNG THƯỜNG GẶP TRÊN THỰC TẾ</div>
  <table style="margin-bottom: 2px;">
    <thead>
      <tr>
        <th style="width: 25%;">Thể lâm sàng</th>
        <th style="width: 45%;">Đặc điểm bệnh cảnh & Tiêu chuẩn nhận diện</th>
        <th style="width: 30%;">Xử trí trọng tâm</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Viêm phế quản cấp đơn thuần</strong></td>
        <td>Diễn tiến đúng 3 pha tự giới hạn, trẻ tỉnh táo, không thở nhanh theo tuổi, không rút lõm lồng ngực.</td>
        <td>Chăm sóc hỗ trợ, bù dịch, vệ sinh mũi. <strong>Không dùng kháng sinh</strong>.</td>
      </tr>
      <tr>
        <td><strong>2. Viêm phế quản co thắt<br><small>(Wheezy Bronchitis)</small></strong></td>
        <td>Cơ địa dị ứng / tăng nhạy cảm sau virus. Ho kèm <strong>khò khè (wheezing)</strong>, thì thở ra kéo dài, ran rít ran ngáy rộ 2 phế trường.</td>
        <td><strong>Khí dung Salbutamol</strong> (đánh giá đáp ứng). Kháng Histamin hoặc Corticoid nếu nặng.</td>
      </tr>
      <tr>
        <td><strong>3. Viêm phế quản kéo dài do vi khuẩn (PBB)</strong></td>
        <td><strong>Ho đờm liên tục &gt; 4 tuần</strong>, không có cờ đỏ bệnh lý khác, không dấu hiệu suyễn. Do vi khuẩn tạo Biofilm (<em>H. influenzae, S. pneumoniae</em>).</td>
        <td><strong>Amoxicillin - Clavulanate (Augmentin)</strong> liều 80–90 mg/kg/ngày trong <strong>2 tuần liên tục</strong>.</td>
      </tr>
      <tr>
        <td><strong>4. Viêm phế quản phổi<br><small>(Bronchopneumonia)</small></strong></td>
        <td>Viêm lan từ phế quản vào tận nhu mô phế nang. Trẻ <strong>thở nhanh theo tuổi, rút lõm lồng ngực, sốt cao, ran ẩm nhỏ hạt khu trú</strong>.</td>
        <td>Thực chất là <strong>VIÊM PHỔI</strong>. Xử trí theo phác đồ Viêm phổi (nhập viện, kháng sinh).</td>
      </tr>
    </tbody>
  </table>

  <!-- FOOTER TRANG 1 -->
  <div class="doc-footer">
    <span>Bộ môn Nhi khoa • Cẩm nang Huấn luyện Kỹ năng Lâm sàng Y6</span>
    <span>Chuyên đề: Viêm phế quản Trẻ em (Trang 1/2)</span>
    <span>Lưu hành học thuật</span>
  </div>

  <!-- ==================== TRANG 2 ==================== -->
  <div class="page-break"></div>

  <!-- HEADER TRANG 2 -->
  <div class="header-box">
    <div>
      <div class="hospital-sub">TÀI LIỆU HƯỚNG DẪN LÂM SÀNG & HUẤN LUYỆN Y KHOA • BỘ MÔN NHI KHOA</div>
      <div class="doc-title">CẨM NANG TOÀN DIỆN: VIÊM PHẾ QUẢN Ở TRẺ EM (TIẾP THEO)</div>
      <div class="doc-subtitle">Chẩn đoán phân biệt • Cận lâm sàng • Chiến lược điều trị EBM • Bẫy thuốc & Cờ đỏ tái khám</div>
    </div>
    <div style="text-align: right;">
      <span class="doc-category">HÔ HẤP NHI LÂM SÀNG</span><br>
      <span style="font-size: 7pt; color: #64748b;">Trang 2/2 • Y6 Clinical</span>
    </div>
  </div>

  <!-- PHẦN V: CHẨN ĐOÁN PHÂN BIỆT -->
  <div class="section-title">V. BỐN CHẨN ĐOÁN PHÂN BIỆT TẠI GIƯỜNG (BẮT BUỘC KHI THI LÂM SÀNG)</div>
  <table>
    <thead>
      <tr>
        <th style="width: 20%;">Bệnh lý phân biệt</th>
        <th style="width: 45%;">Điểm nhận diện & Cờ đỏ đối soát</th>
        <th style="width: 35%;">Điểm khác biệt với Viêm phế quản</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Viêm phổi</strong></td>
        <td>• <strong>Thở nhanh theo lứa tuổi</strong>, rút lõm lồng ngực rõ.<br>• Nghe phổi có vùng giảm thông khí, <strong>ran ẩm nhỏ hạt khu trú</strong>.<br>• X-quang: Đám mờ thâm nhiễm hoặc đông đặc nhu mô.</td>
        <td>Viêm phế quản <strong>không thở nhanh</strong>, ran to hạt rải rác thay đổi sau ho, X-quang không có đông đặc nhu mô.</td>
      </tr>
      <tr>
        <td><strong>2. Hen phế quản (Suyễn)</strong></td>
        <td>• Tiền sử khò khè tái phát $\ge 3$ lần; tiền sử dị ứng bản thân/gia đình.<br>• Cơn khò khè xuất hiện ban đêm/gần sáng hoặc khi gặp dị nguyên.<br>• <strong>Đáp ứng cắt cơn nhanh và rõ rệt với Salbutamol xịt</strong>.</td>
        <td>Viêm phế quản thường xảy ra sau cảm cúm/viêm hô hấp trên, không có tính chất cơn chu kỳ lặp lại như hen.</td>
      </tr>
      <tr>
        <td><strong>3. Dị vật đường thở bỏ quên</strong></td>
        <td>• Có <strong>hội chứng xâm nhập</strong> (cơn ho sặc sụa, tím tái đột ngột khi ăn/chơi).<br>• Khò khè dai dẳng, nghe phổi rì rào phế nang <strong>giảm khu trú 1 bên</strong>.<br>• Điều trị kháng sinh và giãn phế quản hoàn toàn không cải thiện.</td>
        <td>Viêm phế quản ran nghe đều 2 bên, không có hội chứng xâm nhập đột ngột.</td>
      </tr>
      <tr>
        <td><strong>4. Trào ngược dạ dày thực quản (GERD)</strong></td>
        <td>• Ho nhiều sau bữa ăn, ợ trớ, ho khi nằm ngủ.<br>• Chậm tăng cân, khò khè tái diễn kéo dài.</td>
        <td>Không sốt, không có viêm long hô hấp trên rầm rộ ban đầu.</td>
      </tr>
    </tbody>
  </table>

  <!-- PHẦN VI: CẬN LÂM SÀNG -->
  <div class="card-grid-2">
    <div class="panel">
      <div class="panel-header">
        <span>VI. CẬN LÂM SÀNG: KHI NÀO CẦN LÀM?</span>
        <span class="badge">CHỈ ĐỊNH</span>
      </div>
      <ul>
        <li><strong>X-quang ngực thẳng:</strong><br>
          • <strong>KHÔNG CHỈ ĐỊNH THƯỜNG QUY</strong> cho viêm phế quản cấp đơn thuần.<br>
          • <em>Chỉ định khi:</em> Nghi ngờ biến chứng viêm phổi (sốt cao không dứt, thở nhanh), nghi dị vật đường thở, hoặc điều trị không cải thiện.<br>
          • <em>Hình ảnh nếu có:</em> Chỉ thấy <strong>dày thành phế quản</strong> (dấu hiệu "nòng súng" hoặc "đường ray xe lửa"), tăng đậm nhánh rốn phổi, phế trường 2 bên sáng đều.</li>
        <li><strong>Công thức máu & CRP:</strong> Thường bình thường hoặc tăng nhẹ. Chỉ làm khi trẻ sốt cao li bì để loại trừ nhiễm khuẩn huyết/viêm phổi nặng.</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>VII. CHIẾN LƯỢC EBM: NÊN LÀM & TRÁNH</span>
        <span class="badge">EBM PRINCIPLES</span>
      </div>
      <table style="margin: 2px 0;">
        <tr>
          <td style="color: #15803d; font-weight: 700; width: 50%;">NHỮNG ĐIỀU NÊN LÀM (DO)</td>
          <td style="color: #b91c1c; font-weight: 700; width: 50%;">TUYỆT ĐỐI TRÁNH (DON'T)</td>
        </tr>
        <tr>
          <td>• Uống nhiều nước ấm (làm loãng đờm tự nhiên tốt nhất).<br>• Vệ sinh mũi họng, hút thông thoáng trước ăn/ngủ.<br>• Khí dung Salbutamol nếu có co thắt.<br>• Kháng sinh CHỈ KHI có chỉ định rõ ràng.</td>
          <td>• KHÔNG dùng kháng sinh bừa bãi.<br>• <strong>CẤM THUỐC ỨC CHẾ HO</strong> (Codeine).<br>• Không lạm dụng Corticoid uống kéo dài.<br>• Không dùng thuốc long đờm cho trẻ &lt; 2 tuổi.</td>
        </tr>
      </table>
    </div>
  </div>

  <!-- PHẦN VII: QUY TẮC KHÁNG SINH & THUỐC ĐIỀU TRỊ -->
  <div class="section-title">VII. CHI TIẾT SỬ DỤNG THUỐC & QUY TẮC KHÁNG SINH CHUẨN</div>
  <div class="card-grid-2">
    <div class="panel">
      <div class="panel-header">
        <span>1. NGUYÊN TẮC DÙNG KHÁNG SINH (CÂU HỎI THI)</span>
        <span class="badge">ANTIBIOTICS</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li><strong>Viêm phế quản cấp đơn thuần: 100% KHÔNG DÙNG KHÁNG SINH.</strong> Bệnh cần 10–14 ngày để tự đào thải virus.</li>
        <li><strong>4 CHỈ ĐỊNH DÙNG KHÁNG SINH BẮT BUỘC:</strong><br>
          1) <strong>PBB (Viêm phế quản kéo dài vi khuẩn &gt; 4 tuần):</strong> <em>Amoxicillin - Clavulanate (Augmentin)</em> 80–90 mg/kg/ngày x 2 tuần liên tục.<br>
          2) <strong>Nghi <em>Mycoplasma pneumoniae</em> (&gt; 5 tuổi, ho dai dẳng):</strong> <em>Azithromycin</em> 10 mg/kg/ngày x 5 ngày.<br>
          3) <strong>Ho gà (<em>B. pertussis</em>):</strong> <em>Azithromycin</em> để giảm lây lan và mức độ nặng.<br>
          4) <strong>Có bằng chứng bội nhiễm vi khuẩn rõ:</strong> Viêm tai giữa mủ cấp, viêm phổi thùy xuất hiện sau đó.</li>
      </ul>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span>2. ĐIỀU TRỊ TRIỆU CHỨNG & THUỐC HỖ TRỢ</span>
        <span class="badge">SYMPTOMATIC</span>
      </div>
      <ul style="font-size: 7.6pt;">
        <li><strong>Bù nước:</strong> Nước là thuốc làm loãng đờm tự nhiên tốt nhất! Uống nước ấm, bú tăng cường giúp dịch phế quản lỏng ra.</li>
        <li><strong>Thuốc giãn phế quản (Salbutamol khí dung):</strong><br>
          • <em>Chỉ định:</em> CHỈ dùng khi có <strong>co thắt phế quản</strong> (khò khè, ran rít/ngáy, thở ra kéo dài).<br>
          • <em>Liều:</em> <strong>0.15 mg/kg/lần</strong> (min 1.25 mg, max 2.5–5 mg) pha NaCl 0.9% khí dung. Đánh giá lại sau 20 phút. Nếu không đỡ $\rightarrow$ Ngừng khí dung!</li>
        <li><strong>Thuốc giảm ho:</strong> <strong>CẤM TUYỆT ĐỐI thuốc ức chế ho (Codeine, Dextromethorphan)</strong> vì làm mất phản xạ ho gây ứ đờm, xẹp phổi. Trẻ &gt; 1 tuổi ho nhiều mất ngủ có thể dùng <strong>mật ong ấm</strong> (2.5–5 mL).</li>
        <li><strong>Thuốc long đờm (Acetylcysteine, Ambroxol):</strong> Thận trọng, không dùng cho trẻ &lt; 2 tuổi vì nguy cơ tràn ngập đờm đường thở.</li>
      </ul>
    </div>
  </div>

  <!-- PHẦN VIII: 6 CỜ ĐỎ DẶN PHỤ HUYNH TÁI KHÁM NGAY -->
  <div class="callout-box callout-danger" style="margin-top: 4px; padding: 4px 8px;">
    <strong>VIII. 6 "CỜ ĐỎ" BẮT BUỘC DẶN PHỤ HUYNH ĐƯA TRẺ ĐI CẤP CỨU / TÁI KHÁM NGAY:</strong>
    <ol style="margin: 2px 0 0 14px; font-size: 7.8pt;">
      <li><strong>Thở nhanh</strong> hoặc xuất hiện <strong>rút lõm lồng ngực</strong> (báo hiệu bệnh đã chuyển biến thành Viêm phổi!).</li>
      <li><strong>Khó thở, thở rên (grunting), tím tái</strong> môi/đầu chi, phập phồng cánh mũi.</li>
      <li>Trẻ <strong>bỏ bú, bú kém, nôn tất cả mọi thứ</strong> uống vào.</li>
      <li><strong>Li bì, lơ mơ</strong>, khó đánh thức hoặc xuất hiện <strong>co giật</strong>.</li>
      <li>Sốt cao liên tục $> 38.5 - 39^\circ\text{C}$ quá 3 ngày không hạ hoặc sốt vọt trở lại sau khi đã thuyên giảm.</li>
      <li>Ho đờm kéo dài liên tục quá 3–4 tuần không thuyên giảm (nghi ngờ PBB hoặc lao/dị vật).</li>
    </ol>
  </div>

  <!-- FOOTER TRANG 2 -->
  <div class="doc-footer">
    <span>Bộ môn Nhi khoa • Lưu hành đào tạo lâm sàng Y6 & Bác sĩ thực hành</span>
    <span>Dựa trên Hướng dẫn EBM: BTS Guidelines, AAP & Nelson Textbook of Pediatrics</span>
    <span>Trang 2/2</span>
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
    boundary = "----WebKitFormBoundaryBronchitisDoc2026"
    headers = {"Content-Type": f"multipart/form-data; boundary={boundary}"}
    
    with open(pdf_file, "rb") as f:
        file_bytes = f.read()
        
    filename = "Cam_Nang_Viem_Phe_Quan_Nhi_Khoa_Toan_Dien.pdf"
    
    caption = "🫁 CẨM NANG TOÀN DIỆN: VIÊM PHẾ QUẢN Ở TRẺ EM\n\n" \
              "• Định nghĩa & Phân biệt giải phẫu: Viêm phế quản vs Viêm tiểu phế quản\n" \
              "• Căn nguyên 85-90% virus & Diễn tiến 3 giai đoạn (bẫy đờm vàng/xanh do men Myeloperoxidase)\n" \
              "• 4 Thể lâm sàng: Cấp đơn thuần, Co thắt, Kéo dài vi khuẩn PBB (Biofilm), Viêm phế quản phổi\n" \
              "• 4 Chẩn đoán phân biệt tại giường: Viêm phổi, Hen (Suyễn), Dị vật đường thở, GERD\n" \
              "• Chiến lược EBM: 100% không dùng KS đơn thuần, 4 chỉ định KS bắt buộc & Cấm thuốc ức chế ho\n" \
              "• 6 Cờ đỏ dặn phụ huynh tái khám ngay."

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
