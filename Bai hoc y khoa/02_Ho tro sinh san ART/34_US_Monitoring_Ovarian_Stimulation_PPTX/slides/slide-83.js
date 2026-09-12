const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "hCG trigger: nguy cơ OHSS kéo dài",
  "points": [
    "hCG có thời gian tác dụng hoàng thể hóa dài hơn LH sinh lý.",
    "Ở high responder, hCG trigger có thể kéo dài kích thích hoàng thể và tăng OHSS.",
    "Giảm liều hCG không loại bỏ hoàn toàn nguy cơ.",
    "Nếu nguy cơ OHSS cao trong antagonist cycle, nên nghĩ đến agonist trigger và freeze-all."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 82, 110);
}
module.exports = { createSlide };
