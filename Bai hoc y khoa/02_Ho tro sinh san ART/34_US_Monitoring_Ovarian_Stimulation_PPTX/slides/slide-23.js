const { renderSlide } = require('./renderer');
const slideData = {
  "type": "matrix",
  "title": "Bảng so sánh marker: số lượng vs chất lượng",
  "rows": [
    [
      "AFC",
      "Rất tốt",
      "Chất lượng noãn",
      "Phụ thuộc người siêu âm"
    ],
    [
      "AMH",
      "Rất tốt",
      "Live birth độc lập với tuổi",
      "Không cần ngày cố định"
    ],
    [
      "FSH",
      "Trung bình khi tăng rõ",
      "Dự đoán tốt nếu bình thường",
      "Dễ dao động"
    ],
    [
      "Tuổi",
      "Không trực tiếp",
      "Rất tốt",
      "Luôn cần trong tư vấn"
    ],
    [
      "BMI",
      "Nhu cầu thuốc",
      "Chất lượng noãn",
      "Yếu tố định liều"
    ],
    [
      "Tiền sử",
      "Response chu kỳ sau",
      "Không có ở chu kỳ đầu",
      "Giá trị thực chiến"
    ]
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 22, 110);
}
module.exports = { createSlide };
