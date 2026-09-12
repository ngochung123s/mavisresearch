const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "Ovarian reserve vs ovarian response",
  "columns": [
    {
      "title": "Ovarian reserve",
      "points": [
        "Số lượng noãn còn lại theo nghĩa tiềm năng",
        "Ước lượng bằng AFC, AMH, FSH, tuổi",
        "Không đồng nghĩa chất lượng noãn"
      ]
    },
    {
      "title": "Ovarian response",
      "points": [
        "Số nang/noãn thực tế sau kích thích",
        "Bị ảnh hưởng bởi liều, protocol, tiền sử, kỹ thuật theo dõi",
        "Có thể khác với dự đoán ban đầu"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 10, 110);
}
module.exports = { createSlide };
