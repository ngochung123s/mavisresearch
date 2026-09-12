const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Khi nào E2 hữu ích?",
  "points": [
    "Nghi high response hoặc OHSS.",
    "Nhiều nang nhỏ/PCOS và cần đánh giá nguy cơ toàn thân.",
    "Đáp ứng siêu âm không tương xứng với triệu chứng hoặc nguy cơ.",
    "Theo dõi E2 đơn độc không thay thế được đếm nang."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 72, 110);
}
module.exports = { createSlide };
