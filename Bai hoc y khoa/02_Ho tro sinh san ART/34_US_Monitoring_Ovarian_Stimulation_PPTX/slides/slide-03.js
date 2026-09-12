const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "01",
  "title": "Bức tranh tổng quan",
  "subtitle": "Theo dõi kích thích buồng trứng là chuỗi quyết định theo thời gian."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 2, 110);
}
module.exports = { createSlide };
