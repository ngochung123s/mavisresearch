const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Vai trò siêu âm 3D",
  "points": [
    "3D ultrasound có thể giúp lập bản đồ nang và giảm sai số trong buồng trứng nhiều nang.",
    "Mỗi nang có thể được hiển thị/đo bán tự động tùy máy.",
    "Hạn chế là chi phí và không phải cơ sở nào cũng có.",
    "Trong thực hành thường quy, 2D có hệ thống vẫn là nền tảng."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 65, 110);
}
module.exports = { createSlide };
