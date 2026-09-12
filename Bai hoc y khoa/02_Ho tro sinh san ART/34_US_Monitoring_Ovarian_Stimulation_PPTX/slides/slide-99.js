const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Freeze-all trong PPOS/random start",
  "points": [
    "PPOS dùng progestin nên nội mạc không phù hợp chuyển tươi.",
    "Random start thường không đồng bộ với nội mạc.",
    "Mục tiêu của hai chiến lược này là gom noãn/phôi, không phải fresh transfer cùng chu kỳ.",
    "Tư vấn trước giúp tránh hiểu nhầm khi bệnh nhân hỏi vì sao chưa chuyển phôi."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 98, 110);
}
module.exports = { createSlide };
