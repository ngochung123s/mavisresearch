const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "Fixed vs flexible: bảng so sánh thực hành",
  "columns": [
    {
      "title": "Fixed",
      "points": [
        "Dễ nhớ",
        "Dễ chuẩn hóa",
        "Giảm nguy cơ dùng muộn",
        "Có thể nhiều ngày thuốc hơn"
      ]
    },
    {
      "title": "Flexible",
      "points": [
        "Cá thể hóa hơn",
        "Có thể ít ngày thuốc hơn",
        "Cần theo dõi sát",
        "Phụ thuộc logistics và kinh nghiệm"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 46, 110);
}
module.exports = { createSlide };
