const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Two-cell two-gonadotropin theory",
  "points": [
    "LH kích thích tế bào vỏ tạo androgen.",
    "FSH kích thích tế bào hạt thơm hóa androgen thành estrogen.",
    "FSH và LH phối hợp để nang phát triển và sản xuất estrogen phù hợp.",
    "Thiếu LH hoặc LH quá cao đều có thể làm giảm chất lượng phát triển nang."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 33, 110);
}
module.exports = { createSlide };
