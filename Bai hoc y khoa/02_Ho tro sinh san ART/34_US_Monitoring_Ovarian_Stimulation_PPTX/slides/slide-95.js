const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "08",
  "title": "Freeze-all và quyết định nhanh",
  "subtitle": "Freeze-all là chiến lược cá thể hóa, không phải khẩu hiệu."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 94, 110);
}
module.exports = { createSlide };
