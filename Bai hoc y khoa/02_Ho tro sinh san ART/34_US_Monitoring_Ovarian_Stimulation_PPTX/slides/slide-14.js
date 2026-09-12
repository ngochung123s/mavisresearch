const { renderSlide } = require('./renderer');
const slideData = {
  "type": "matrix",
  "title": "Marker dự trữ buồng trứng: đọc đúng vai trò",
  "rows": [
    [
      "AFC",
      "Số nang có thể huy động",
      "Không dự đoán trực tiếp live birth",
      "Cần siêu âm tốt"
    ],
    [
      "AMH",
      "Oocyte yield",
      "Không thay tuổi để dự đoán chất lượng",
      "Ổn định trong chu kỳ"
    ],
    [
      "FSH",
      "Reserve giảm khi tăng rõ",
      "Không nhạy nếu đơn độc",
      "Hữu ích khi AMH/AFC thấp"
    ],
    [
      "Tuổi",
      "Chất lượng noãn, lệch bội",
      "Không đếm số nang trực tiếp",
      "Biến tiên lượng lớn"
    ],
    [
      "Cân nặng",
      "Nhu cầu gonadotropin",
      "Không phải marker reserve",
      "Giúp định liều"
    ],
    [
      "Tiền sử đáp ứng",
      "Response thực tế",
      "Không áp cho chu kỳ đầu",
      "Rất hữu ích nếu có"
    ]
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 13, 110);
}
module.exports = { createSlide };
