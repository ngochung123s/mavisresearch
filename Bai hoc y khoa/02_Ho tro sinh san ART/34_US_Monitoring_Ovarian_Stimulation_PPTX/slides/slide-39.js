const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "04",
  "title": "Các phác đồ kích thích",
  "subtitle": "Protocol là cách phối hợp FSH và kiểm soát LH surge."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 38, 110);
}
module.exports = { createSlide };
