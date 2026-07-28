#!/usr/bin/env python3
"""
build_pink_apkg_full.py — Build APKG tone hồng tự động vét toàn bộ kiến thức từ 6 Part của IBS.
"""
import sys
import re
import hashlib
import warnings
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

warnings.filterwarnings('ignore', category=UserWarning, module='genanki')

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

import genanki

PINK_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700&display=swap');

.card {
  font-family: 'Be Vietnam Pro', 'Segoe UI', 'Noto Sans', Arial, sans-serif;
  font-size: 17px;
  line-height: 1.8;
  text-align: left;
  color: #4a2c3a;
  background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
  padding: 24px;
  border-radius: 12px;
}
.card.nightMode {
  background: linear-gradient(135deg, #4a2c3a 0%, #5c3a4a 100%);
  color: #ffe4e1;
}
#front, #back {
  background-color: rgba(255, 255, 255, 0.85);
  padding: 18px 22px;
  border-radius: 10px;
  border: 1px solid #ffb6c1;
  box-shadow: 0 2px 6px rgba(255,182,193,0.2);
  margin-bottom: 14px;
}
.card.nightMode #front, .card.nightMode #back {
  background-color: rgba(255, 255, 255, 0.1);
  border-color: rgba(255,182,193,0.2);
  color: #fff0f5;
}
#front p, #back p { margin: 6px 0; }
#front ul, #back ul, #front ol, #back ol { margin: 6px 0; padding-left: 22px; }
#front li, #back li { margin: 4px 0; line-height: 1.7; }
#front b, #back b, #front strong, #back strong {
  color: #d1495b;
  font-weight: 600;
}
.card.nightMode #front b, .card.nightMode #back b,
.card.nightMode #front strong, .card.nightMode #back strong {
  color: #ffb6c1;
}
.tag {
  display: inline-block;
  background-color: #ffb6c1;
  color: #d1495b;
  padding: 2px 10px;
  border-radius: 12px;
  font-size: 12px;
  margin-right: 6px;
  font-weight: 500;
}
hr#answer {
  margin: 12px 0;
  border: 0;
  border-top: 1px dashed #ffb6c1;
}
"""

def stable_id(seed_str):
    h = hashlib.md5(seed_str.encode()).hexdigest()[:12]
    return int(h, 16) % 9000000000000 + 1000000000000

def build_ibs_pink_apkg():
    cards = []
    
    # ---------------------------------------------------------
    # PART 1: TỔNG QUAN & TRỤC NÃO RUỘT (Cơ chế sinh lý bệnh)
    # ---------------------------------------------------------
    cards.extend([
        {
            'front': 'Hội chứng ruột kích thích (IBS) được định nghĩa theo Rome IV là gì?',
            'back': 'IBS là một <b>Rối loạn Tương tác Não - Ruột (DGBIs - Disorders of Gut-Brain Interaction)</b>. Nó không phải là rối loạn chức năng đơn thuần mà là sự sai lệch trong giao tiếp hai chiều giữa hệ thần kinh trung ương và hệ thần kinh ruột.',
            'tag': 'Part1-TongQuan'
        },
        {
            'front': 'Hệ thần kinh ruột (ENS - Enteric Nervous System) bao gồm 2 đám rối thần kinh chính nào và chức năng của chúng?',
            'back': '1. <b>Đám rối Auerbach (Myenteric plexus):</b> Nằm giữa lớp cơ dọc và cơ vòng, điều hòa <b>nhu động co bóp</b>.<br>2. <b>Đám rối Meissner (Submucosal plexus):</b> Nằm ở lớp dưới niêm mạc, điều hòa <b>tiết dịch và hấp thu</b>.',
            'tag': 'Part1-GiaiPhau'
        },
        {
            'front': 'Cơ chế bệnh sinh cốt lõi của IBS (Trục Não - Ruột) bao gồm 3 yếu tố chính nào?',
            'back': '1. <b>Tăng nhạy cảm tạng (Visceral Hypersensitivity):</b> Ruột cảm nhận đau với những kích thích bình thường (như khí, phân).<br>2. <b>Rối loạn nhu động ruột (Altered Motility):</b> Co thắt quá mức gây tiêu chảy, hoặc lười co bóp gây táo bón.<br>3. <b>Rối loạn hệ vi sinh và viêm vi thể (Dysbiosis & Low-grade inflammation):</b> Thường gặp sau nhiễm trùng tiêu hóa (PI-IBS).',
            'tag': 'Part1-CoChe'
        },
        {
            'front': 'Serotonin (5-HT) đóng vai trò gì trong cơ chế bệnh sinh của IBS?',
            'back': 'Khoảng <b>95% Serotonin cơ thể nằm ở ruột</b>. Nó là chất dẫn truyền thần kinh chính điều hòa nhu động và cảm giác đau.<br>- Thừa Serotonin (hoặc tăng nhạy cảm thụ thể) → Tăng nhu động → <b>IBS-D (Tiêu chảy)</b>.<br>- Thiếu Serotonin → Giảm nhu động → <b>IBS-C (Táo bón)</b>.',
            'tag': 'Part1-CoChe'
        },
        {
            'front': 'Tại sao stress, lo âu lại làm trầm trọng thêm triệu chứng của IBS?',
            'back': 'Stress kích hoạt trục HPA (Hạ đồi - Tuyến yên - Thượng thận), giải phóng Cortisol và CRH. Các chất này tác động trực tiếp lên hệ thần kinh ruột, làm <b>tăng co thắt đại tràng và tăng tính thấm niêm mạc ruột</b>, gây bùng phát cơn đau và tiêu chảy.',
            'tag': 'Part1-CoChe'
        },
        {
            'front': 'Tăng nhạy cảm tạng (Visceral Hypersensitivity) trong IBS liên quan đến thụ thể cảm giác nào?',
            'back': 'Liên quan đến sự nhạy cảm hóa thụ thể <b>TRPV1 (Transient Receptor Potential Vanilloid 1)</b> trên đầu tận thần kinh cảm giác ruột. Ngưỡng kích hoạt bị hạ thấp khiến một lượng khí hay phân bình thường cũng gây đau quặn dữ dội.',
            'tag': 'Part1-CoChe'
        },
        {
            'front': 'IBS sau nhiễm trùng (PI-IBS) liên quan đến sự gia tăng của loại tế bào miễn dịch nào tại niêm mạc ruột?',
            'back': 'Liên quan đến sự gia tăng <b>tế bào Mast (Mast cells)</b>. Tế bào Mast liên tục giải phóng Histamine và Tryptase làm tổn thương sợi thần kinh ruột, duy trì tình trạng viêm vi thể (Low-grade inflammation).',
            'tag': 'Part1-CoChe'
        }
    ])

    # ---------------------------------------------------------
    # PART 2: TIÊU CHUẨN ROME IV & PHÂN THỂ
    # ---------------------------------------------------------
    cards.extend([
        {
            'front': 'Tiêu chuẩn chẩn đoán Rome IV cho IBS yêu cầu triệu chứng đau bụng với tần suất và thời gian như thế nào?',
            'back': 'Đau bụng tái phát trung bình <b>ít nhất 1 ngày/tuần trong 3 tháng gần đây</b>, kèm theo khởi phát triệu chứng <b>ít nhất 6 tháng trước khi chẩn đoán</b>.',
            'tag': 'Part2-RomeIV'
        },
        {
            'front': 'Theo Rome IV, triệu chứng đau bụng trong IBS phải thỏa mãn ít nhất 2 trong 3 tiêu chí nào?',
            'back': '1. Liên quan đến việc đi tiêu (tăng hoặc giảm đau sau khi đi tiêu).<br>2. Liên quan đến sự thay đổi <b>tần suất</b> đi tiêu.<br>3. Liên quan đến sự thay đổi <b>hình dạng (độ cứng/lỏng)</b> của phân.',
            'tag': 'Part2-RomeIV'
        },
        {
            'front': 'Kể tên 8 Dấu hiệu Báo động (Red Flags) cần loại trừ trước khi chẩn đoán IBS.',
            'back': '1. Tuổi khởi phát ≥ 50 tuổi.<br>2. Đi ngoài ra máu tươi hoặc phân đen.<br>3. Tiêu chảy kéo dài liên tục vào đêm.<br>4. Sụt cân bất thường không rõ nguyên nhân (>5%).<br>5. Sốt kéo dài không rõ nguyên nhân.<br>6. Thiếu máu thiếu sắt.<br>7. Tiền sử gia đình có ung thư đại trực tràng, Celiac hoặc IBD.<br>8. Khám thấy khối u bất thường ở bụng.',
            'tag': 'Part2-RedFlags'
        },
        {
            'front': 'Thang điểm Bristol (Bristol Stool Form Scale) chia phân thành mấy type và type nào tương ứng với IBS-C, IBS-D?',
            'back': 'Chia làm 7 type:<br>- <b>Type 1, 2 (Cứng, lổn nhổn):</b> Đặc trưng cho Táo bón (IBS-C).<br>- <b>Type 3, 4, 5:</b> Bình thường.<br>- <b>Type 6, 7 (Lỏng, nước):</b> Đặc trưng cho Tiêu chảy (IBS-D).',
            'tag': 'Part2-PhanThe'
        },
        {
            'front': 'Tiêu chuẩn phân loại 4 thể IBS (IBS-C, IBS-D, IBS-M, IBS-U) dựa trên tỷ lệ phần trăm các loại phân Bristol như thế nào?',
            'back': '- <b>IBS-C (Táo bón):</b> >25% phân Type 1/2 và <25% phân Type 6/7.<br>- <b>IBS-D (Tiêu chảy):</b> >25% phân Type 6/7 và <25% phân Type 1/2.<br>- <b>IBS-M (Hỗn hợp):</b> >25% phân Type 1/2 VÀ >25% phân Type 6/7.<br>- <b>IBS-U (Không phân loại):</b> Không đủ tiêu chuẩn của 3 thể trên.',
            'tag': 'Part2-PhanThe'
        },
        {
            'front': 'Theo ACG 2021, nếu bệnh nhân nghi ngờ IBS-D không có Red Flags, 2 xét nghiệm chuyên sâu nào được khuyến cáo để loại trừ bệnh lý thực thể?',
            'back': '1. <b>Xét nghiệm tTG-IgA:</b> Loại trừ bệnh Celiac.<br>2. <b>Xét nghiệm Fecal Calprotectin (hoặc CRP):</b> Loại trừ Bệnh Viêm Ruột Mạn (IBD). Calprotectin < 50 μg/g giúp loại trừ IBD an toàn.',
            'tag': 'Part2-XetNghiem'
        }
    ])

    # ---------------------------------------------------------
    # PART 3: DINH DƯỠNG LOW-FODMAP
    # ---------------------------------------------------------
    cards.extend([
        {
            'front': 'FODMAP là viết tắt của những nhóm chất nào và tại sao chúng gây triệu chứng IBS?',
            'back': 'FODMAP = Fermentable Oligosaccharides, Disaccharides, Monosaccharides, And Polyols.<br>Đây là các carbohydrate chuỗi ngắn <b>hấp thu kém ở ruột non</b>. Khi xuống đại tràng, chúng kéo nước vào lòng ruột (gây tiêu chảy) và bị vi khuẩn lên men sinh ra lượng lớn khí (gây trướng bụng, đau quặn).',
            'tag': 'Part3-DinhDuong'
        },
        {
            'front': 'Chế độ ăn Low-FODMAP trong điều trị IBS gồm 3 pha (giai đoạn) nào?',
            'back': '1. <b>Pha Loại trừ (Elimination):</b> Kéo dài 2-6 tuần, loại bỏ hoàn toàn thực phẩm High-FODMAP.<br>2. <b>Pha Thử nghiệm lại (Re-introduction):</b> Kéo dài 6-8 tuần, đưa từng nhóm FODMAP trở lại để tìm thủ phạm.<br>3. <b>Pha Cá nhân hóa (Personalization):</b> Duy trì chế độ ăn đa dạng nhất có thể, chỉ tránh nhóm gây triệu chứng.',
            'tag': 'Part3-DinhDuong'
        },
        {
            'front': 'Kể tên một số thực phẩm High-FODMAP phổ biến cần tránh trong Pha 1.',
            'back': '- <b>Oligo:</b> Lúa mì, hành tây, tỏi, các loại đậu.<br>- <b>Di:</b> Sữa bò, sữa chua, kem (chứa Lactose).<br>- <b>Mono:</b> Táo, lê, dưa hấu, mật ong (chứa Fructose).<br>- <b>Polyols:</b> Kẹo cao su không đường, mận, súp lơ (chứa Sorbitol, Mannitol).',
            'tag': 'Part3-DinhDuong'
        },
        {
            'front': 'Tại sao trong IBS lại ưu tiên dùng Chất xơ hòa tan (Psyllium) và cấm dùng Chất xơ không hòa tan (Cám lúa mì)?',
            'back': '<b>Chất xơ hòa tan (Psyllium)</b> tạo gel mềm, không bị vi khuẩn lên men sinh khí, giúp điều hòa cả tiêu chảy và táo bón.<br><b>Chất xơ không hòa tan (Cám, rau thô)</b> gây cọ xát cơ học lên niêm mạc ruột nhạy cảm và bị lên men mạnh tạo ra nhiều khí, làm tăng đau quặn và trướng bụng.',
            'tag': 'Part3-DinhDuong'
        },
        {
            'front': 'Dầu bạc hà (Peppermint oil) có cơ chế tác dụng gì trong điều trị IBS?',
            'back': 'Thành phần L-menthol trong dầu bạc hà giúp <b>chẹn kênh Canxi (Calcium channel blocker) ở cơ trơn ruột</b>, làm giãn cơ trơn, giảm co thắt và giảm đau quặn bụng hiệu quả.',
            'tag': 'Part3-KhongThuoc'
        }
    ])

    # ---------------------------------------------------------
    # PART 4: DƯỢC LÝ TRÚNG ĐÍCH
    # ---------------------------------------------------------
    cards.extend([
        {
            'front': 'Cơ chế tác dụng của Rifaximin trong điều trị IBS-D là gì và liều dùng chuẩn?',
            'back': 'Rifaximin là kháng sinh phổ rộng, <b>không hấp thu vào máu (<0.4%)</b>, chỉ tác dụng tại lòng ruột. Nó giúp điều hòa hệ vi sinh (eubiotic effect) và giảm vi khuẩn sinh khí.<br><b>Liều chuẩn:</b> 550 mg x 3 lần/ngày, uống trong 14 ngày.',
            'tag': 'Part4-DuocLy'
        },
        {
            'front': 'Phác đồ thuốc điều trị trúng đích cho IBS thể Tiêu chảy (IBS-D) bao gồm 3 trụ cột nào?',
            'back': '1. <b>Kháng sinh lòng ruột:</b> Rifaximin 550mg x 3 lần/ngày (14 ngày).<br>2. <b>Chống co thắt:</b> Mebeverine (135mg x 3) hoặc Alverine.<br>3. <b>Neuromodulator:</b> Amitriptyline (TCA) liều thấp buổi tối.',
            'tag': 'Part4-DuocLy'
        },
        {
            'front': 'Phác đồ thuốc điều trị trúng đích cho IBS thể Táo bón (IBS-C) từ cơ bản đến nâng cao là gì?',
            'back': '<b>Bước 1:</b> Chất xơ hòa tan (Psyllium) + Nhuận tràng thẩm thấu (PEG 3350 / Forlax).<br><b>Bước 2 (nếu thất bại):</b> Thuốc kích hoạt bài tiết dịch ruột (Linaclotide 290mcg hoặc Lubiprostone).<br><b>Neuromodulator:</b> Ưu tiên SSRI (Sertraline) vì có tác dụng phụ gây tiêu chảy nhẹ.',
            'tag': 'Part4-DuocLy'
        },
        {
            'front': 'Trong điều trị IBS, nhóm thuốc Neuromodulators (TCA và SSRI) được chọn lọc cho từng thể (IBS-D và IBS-C) như thế nào?',
            'back': '- <b>IBS-D (Tiêu chảy):</b> Dùng <b>TCA (Amitriptyline 10-25mg)</b> vì tác dụng phụ kháng cholinergic làm chậm nhu động ruột và giảm tiết dịch.<br>- <b>IBS-C (Táo bón):</b> Dùng <b>SSRI (Sertraline 25-50mg)</b> vì tác dụng phụ kích thích thụ thể 5-HT làm tăng nhu động ruột.',
            'tag': 'Part4-DuocLy'
        },
        {
            'front': 'Tại sao Loperamide không được khuyến cáo dùng hàng ngày kéo dài cho IBS-D?',
            'back': 'Loperamide chỉ là thuốc liệt nhu động làm rắn phân cấp thời, <b>không giải quyết được bản chất Tăng nhạy cảm tạng</b>. Dùng kéo dài làm ứ trệ hơi và chất thải, gây căng trướng đại tràng và làm tăng cảm giác đau quặn.',
            'tag': 'Part4-DuocLy'
        },
        {
            'front': 'Cơ chế hoạt động của Linaclotide trong điều trị IBS-C là gì?',
            'back': 'Linaclotide là chất chủ vận thụ thể <b>Guanylate Cyclase-C (GC-C)</b> trên biểu mô ruột. Nó kích thích bài tiết Cl- và HCO3- vào lòng ruột, kéo theo nước làm mềm phân và tăng nhu động ruột.',
            'tag': 'Part4-DuocLy'
        }
    ])

    # ---------------------------------------------------------
    # PART 5: THỰC CHIẾN VIỆT NAM
    # ---------------------------------------------------------
    cards.extend([
        {
            'front': 'Khi tiếp cận bệnh nhân nghi ngờ IBS tại Việt Nam (tuyến cơ sở), 3 xét nghiệm/cận lâm sàng cơ bản nhất (Plan B) cần làm để loại trừ bệnh lý thực thể là gì?',
            'back': '1. <b>Công thức máu (CBC):</b> Loại trừ thiếu máu, nhiễm trùng.<br>2. <b>CRP máu:</b> Loại trừ tình trạng viêm hệ thống (như IBD).<br>3. <b>Soi phân 3 mẫu:</b> Tìm ký sinh trùng/amip (rất phổ biến ở VN gây triệu chứng giống IBS).',
            'tag': 'Part5-ThucChien'
        },
        {
            'front': 'Tại sao việc giải thích cơ chế "Trục Não - Ruột" cho bệnh nhân IBS lại được coi là một phương pháp điều trị?',
            'back': 'Vì IBS là bệnh lý có yếu tố tâm lý làm khuếch đại tín hiệu đau. Việc giải thích rõ ràng giúp bệnh nhân hiểu <b>"bệnh là có thật nhưng không nguy hiểm đến tính mạng"</b>, từ đó cắt đứt vòng luẩn quẩn: Đau ruột → Lo âu → Não kích thích ruột co thắt → Càng đau hơn.',
            'tag': 'Part5-ThucChien'
        },
        {
            'front': 'Lỗi sai phổ biến nhất của bác sĩ tuyến cơ sở ở Việt Nam khi chẩn đoán IBS là gì?',
            'back': 'Chẩn đoán bừa là <b>"Viêm đại tràng mạn"</b> và kê đơn kháng sinh toàn thân (Metronidazole, Ciprofloxacin) bừa bãi. Việc này phá hủy hoàn toàn hệ vi sinh đường ruột, làm IBS nặng thêm và gây kháng kháng sinh.',
            'tag': 'Part5-ThucChien'
        }
    ])

    # ---------------------------------------------------------
    # PART 6: MASTER CLINICAL CASES
    # ---------------------------------------------------------
    cards.extend([
        {
            'front': '<b>CA LÂM SÀNG 1:</b> Bệnh nhân nam 29 tuổi, lập trình viên, tiêu chảy 4-6 lần/ngày kéo dài 8 tháng, tăng nặng khi stress. Đã tự uống Loperamide 3 tháng, phân bớt lỏng nhưng bụng đau quặn và trướng nhiều hơn. Nội soi bình thường.<br><b>Chẩn đoán và Hướng xử trí?</b>',
            'back': '<b>Chẩn đoán:</b> IBS-D.<br><b>Xử trí:</b><br>1. Ngưng Loperamide dùng hàng ngày.<br>2. Rifaximin 550mg x 3/ngày (14 ngày).<br>3. Amitriptyline 10mg tối.<br>4. Mebeverine 135mg x 3/ngày.<br>5. Chế độ ăn Low-FODMAP Pha 1.',
            'tag': 'Part6-CaseStudy'
        },
        {
            'front': '<b>CA LÂM SÀNG 2:</b> Bệnh nhân nữ 45 tuổi, táo bón 4-5 ngày/lần, phân cứng (Bristol 1). Nghe lời khuyên trên mạng ăn nhiều rau sống và cám lúa mì 2 tháng nay → Bụng trướng căng, trung tiện nhiều, đau quặn dữ dội hơn.<br><b>Chẩn đoán và Hướng xử trí?</b>',
            'back': '<b>Chẩn đoán:</b> IBS-C.<br><b>Xử trí:</b><br>1. Ngưng cám lúa mì và rau thô cứng (Insoluble fiber).<br>2. Chuyển sang Psyllium (Soluble fiber) 5g/ngày.<br>3. Nhuận tràng thẩm thấu: Macrogol 4000 (Forlax) 1-2 gói/ngày.<br>4. Giảm đau trướng: Alverine/Simethicone.',
            'tag': 'Part6-CaseStudy'
        },
        {
            'front': '<b>CA LÂM SÀNG 3:</b> Bệnh nhân nữ 32 tuổi, khởi phát tiêu chảy và đau quặn bụng kéo dài 4 tháng nay, ngay sau một đợt ngộ độc thực phẩm nặng phải nằm viện truyền dịch. Hiện tại cấy phân âm tính.<br><b>Chẩn đoán là gì?</b>',
            'back': '<b>Chẩn đoán:</b> Hội chứng ruột kích thích sau nhiễm trùng (Post-Infectious IBS / PI-IBS).',
            'tag': 'Part6-CaseStudy'
        }
    ])

    # Build Deck
    deck_name = "IBS-AI tự tạo"
    model_id = stable_id(deck_name + "model")
    deck_id = stable_id(deck_name + "deck")
    
    model = genanki.Model(
        model_id,
        f"Pink Basic Model - {deck_name}",
        fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'Tags'}],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div id="front">{{Question}}</div>',
                'afmt': '<div id="front">{{Question}}</div><hr id="answer"><div id="back">{{Answer}}</div><br>{{Tags}}',
            }
        ],
        css=PINK_CSS
    )
    deck = genanki.Deck(deck_id, deck_name, description="Bộ thẻ ôn tập Hội chứng ruột kích thích (IBS) - Tone Hồng (Bao phủ toàn diện 6 Part)")

    for i, card in enumerate(cards):
        note = genanki.Note(
            model=model,
            fields=[card['front'], card['back'], f'<span class="tag">IBS</span> <span class="tag">{card["tag"]}</span>'],
            guid=stable_id(f"IBS_card_full_v3_{i}")
        )
        deck.add_note(note)

    out_path = PROJECT_ROOT / '11_Noi khoa' / 'IM-IBS_Hoi_chung_ruot_kich_thich' / f'Anki - {deck_name}.apkg'
    genanki.Package(deck).write_to_file(str(out_path))
    print(f"✅ Đã tạo thành công bộ flashcard tone hồng: {out_path}")
    print(f"Tổng số thẻ: {len(cards)}")

if __name__ == "__main__":
    build_ibs_pink_apkg()
