const { renderSlide } = require('./renderer');
const slideData = {
  "type": "section",
  "number": "03",
  "title": "Sinh lý nền của kích thích buồng trứng",
  "subtitle": "Hiểu FSH/LH giúp đọc đúng vì sao protocol hoạt động."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 27, 110);
}
module.exports = { createSlide };
