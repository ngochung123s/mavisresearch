const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "Siêu âm là trục chính, hormone là công cụ bổ sung",
  "columns": [
    {
      "title": "Siêu âm",
      "points": [
        "Đếm và đo nang",
        "Đọc phân bố kích thước",
        "Đánh giá nội mạc",
        "Dự đoán chọc hút khó"
      ]
    },
    {
      "title": "Hormone",
      "points": [
        "E2 khi nghi high response/OHSS",
        "LH khi nghi surge",
        "Progesterone khi cân nhắc fresh vs freeze",
        "Không cần routine cho mọi lần khám"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 6, 110);
}
module.exports = { createSlide };
