const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "07",
  "title": "Trigger và phòng OHSS",
  "subtitle": "Trigger là quyết định an toàn, không chỉ là mũi tiêm cuối."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 77, 110);
}
module.exports = { createSlide };
