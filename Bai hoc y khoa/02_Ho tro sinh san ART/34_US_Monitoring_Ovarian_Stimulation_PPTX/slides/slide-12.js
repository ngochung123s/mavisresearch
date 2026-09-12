const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Ovarian reserve: đo số lượng tiềm năng",
  "points": [
    "AFC và AMH là hai marker thực hành phổ biến nhất.",
    "Reserve thấp thường gợi ý nguy cơ đáp ứng kém, nhưng không nói hết khả năng có thai.",
    "Reserve cao gợi ý high response, cần nghĩ sớm đến OHSS prevention.",
    "Tuổi vẫn là biến lớn nhất khi nói về chất lượng noãn và lệch bội."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 11, 110);
}
module.exports = { createSlide };
