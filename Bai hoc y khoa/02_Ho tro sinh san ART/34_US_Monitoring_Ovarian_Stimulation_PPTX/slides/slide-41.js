const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Long agonist protocol: logic",
  "points": [
    "Dùng GnRH agonist từ pha hoàng thể để down-regulation tuyến yên.",
    "Khi tuyến yên bị ức chế, bắt đầu FSH ngoại sinh.",
    "Tiếp tục agonist liều giảm để kiểm soát LH surge.",
    "Tạo cohort khá đồng đều nhưng thời gian dài và dùng nhiều thuốc."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 40, 110);
}
module.exports = { createSlide };
