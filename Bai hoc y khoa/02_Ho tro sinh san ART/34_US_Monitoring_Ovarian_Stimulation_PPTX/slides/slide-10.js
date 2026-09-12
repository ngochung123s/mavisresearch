const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "02",
  "title": "Đánh giá trước kích thích",
  "subtitle": "Baseline tốt giúp chọn đúng phác đồ, liều khởi đầu và chiến lược an toàn."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 9, 110);
}
module.exports = { createSlide };
