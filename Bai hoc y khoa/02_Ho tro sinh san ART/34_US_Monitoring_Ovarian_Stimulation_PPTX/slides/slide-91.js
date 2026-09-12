const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Chiến lược giảm OHSS",
  "points": [
    "Chọn antagonist protocol ở nhóm nguy cơ.",
    "Cá thể hóa và giảm liều FSH khi dự kiến high response.",
    "Dùng GnRH agonist trigger trong antagonist cycle khi nguy cơ cao.",
    "Freeze-all khi nguy cơ OHSS hoặc nội mạc/hormone không phù hợp.",
    "Single embryo transfer khi phù hợp để giảm nguy cơ liên quan thai kỳ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "small": true
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 90, 110);
}
module.exports = { createSlide };
