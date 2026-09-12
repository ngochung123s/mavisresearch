const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "GnRH agonist trigger: cơ chế",
  "points": [
    "Dùng flare effect của GnRH agonist tạo đỉnh LH nội sinh.",
    "Chỉ khả thi khi tuyến yên còn đáp ứng, điển hình trong antagonist cycle.",
    "Đỉnh LH nội sinh ngắn hơn tác dụng hCG nên giảm nguy cơ OHSS sớm.",
    "Không dùng trong long agonist down-regulation vì tuyến yên đã bị ức chế."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 83, 110);
}
module.exports = { createSlide };
