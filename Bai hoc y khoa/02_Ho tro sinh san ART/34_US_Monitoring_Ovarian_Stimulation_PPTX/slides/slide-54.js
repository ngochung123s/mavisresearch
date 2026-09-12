const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "05",
  "title": "Theo dõi bằng siêu âm trong kích thích",
  "subtitle": "Slide cá nhân cần đủ checklist để áp dụng khi đọc ca."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 53, 110);
}
module.exports = { createSlide };
