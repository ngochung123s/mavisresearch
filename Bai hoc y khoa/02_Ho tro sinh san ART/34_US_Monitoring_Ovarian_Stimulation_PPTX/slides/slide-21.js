const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "FSH đầu chu kỳ: khi nào còn hữu ích?",
  "points": [
    "FSH tăng rõ gợi ý giảm dự trữ buồng trứng.",
    "FSH dao động giữa các chu kỳ nên không nên diễn giải đơn độc.",
    "FSH đặc biệt hữu ích khi AMH/AFC thấp và cần củng cố tiên lượng poor response.",
    "Giá trị FSH cần đọc cùng E2 đầu chu kỳ vì E2 cao có thể che FSH."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 20, 110);
}
module.exports = { createSlide };
