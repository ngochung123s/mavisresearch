const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "06",
  "title": "Nội tiết trong theo dõi",
  "subtitle": "Hormone nên trả lời câu hỏi lâm sàng, không làm vì thói quen."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 70, 110);
}
module.exports = { createSlide };
