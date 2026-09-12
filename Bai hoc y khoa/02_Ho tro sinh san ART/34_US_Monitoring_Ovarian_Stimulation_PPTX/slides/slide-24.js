const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Baseline ultrasound checklist",
  "points": [
    "AFC hai buồng trứng.",
    "Nang tồn dư hoặc cyst chức năng.",
    "Endometrioma, u buồng trứng hoặc bất thường vùng chậu.",
    "Tử cung: polyp, u xơ, vách ngăn, dịch lòng tử cung nếu thấy.",
    "Đường tiếp cận buồng trứng dự kiến cho chọc hút."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "small": true
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 23, 110);
}
module.exports = { createSlide };
