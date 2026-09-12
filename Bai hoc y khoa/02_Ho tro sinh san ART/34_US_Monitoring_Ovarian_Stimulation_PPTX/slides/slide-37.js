const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Vì sao cần kiểm soát LH surge?",
  "points": [
    "Đỉnh LH sớm có thể làm noãn trưởng thành lệch thời điểm.",
    "Có thể gây hoàng thể hóa sớm và tăng progesterone.",
    "Có thể làm giảm khả năng tiếp nhận nội mạc nếu chuyển tươi.",
    "GnRH agonist dài, antagonist và PPOS là ba cách kiểm soát trục LH theo logic khác nhau."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 36, 110);
}
module.exports = { createSlide };
