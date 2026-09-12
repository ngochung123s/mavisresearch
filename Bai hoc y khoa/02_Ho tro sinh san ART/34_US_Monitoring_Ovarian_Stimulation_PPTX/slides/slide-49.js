const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "PPOS: khi nào phù hợp",
  "points": [
    "Progestin dùng từ đầu kích thích để ức chế LH surge.",
    "Hữu ích khi dự kiến freeze-all ngay từ đầu.",
    "Có thể phù hợp bảo tồn sinh sản, nguy cơ OHSS hoặc chiến lược đông phôi toàn bộ.",
    "Không phù hợp nếu mục tiêu là chuyển phôi tươi cùng chu kỳ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 48, 110);
}
module.exports = { createSlide };
