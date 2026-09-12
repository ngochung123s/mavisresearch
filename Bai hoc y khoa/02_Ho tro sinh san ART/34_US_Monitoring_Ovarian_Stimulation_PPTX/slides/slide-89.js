const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "Dual trigger vs double trigger",
  "columns": [
    {
      "title": "Dual trigger",
      "points": [
        "hCG và GnRH agonist cùng thời điểm",
        "Mục tiêu phối hợp tín hiệu trưởng thành noãn",
        "Cần cân nhắc OHSS nếu có hCG"
      ]
    },
    {
      "title": "Double trigger",
      "points": [
        "GnRH agonist trước, hCG sau",
        "Dùng trong một số tình huống đáp ứng kém/tiền sử noãn trưởng thành kém",
        "Không nên dùng routine nếu không có chỉ định"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 88, 110);
}
module.exports = { createSlide };
