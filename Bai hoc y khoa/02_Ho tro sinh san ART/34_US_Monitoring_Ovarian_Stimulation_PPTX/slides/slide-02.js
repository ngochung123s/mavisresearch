const { renderSlide } = require('./renderer');
const slideData = {
  "type": "toc",
  "title": "Bản đồ bài học",
  "items": [
    "Tổng quan quyết định",
    "Đánh giá trước kích thích",
    "Sinh lý nền",
    "Phác đồ kích thích",
    "Theo dõi bằng siêu âm",
    "Nội tiết trong theo dõi",
    "Trigger và OHSS",
    "Freeze-all và quyết định nhanh"
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 1, 110);
}
module.exports = { createSlide };
