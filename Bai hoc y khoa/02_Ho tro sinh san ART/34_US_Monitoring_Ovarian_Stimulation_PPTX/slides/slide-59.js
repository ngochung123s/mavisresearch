const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Đếm nang theo nhóm kích thước",
  "points": [
    "Không chỉ ghi một nang lớn nhất.",
    "Nên nhóm: <10 mm, 10-13 mm, 14-16 mm, 17-18 mm, >18 mm nếu cần.",
    "Nhóm kích thước giúp dự đoán số noãn có khả năng thu được.",
    "Phân bố kích thước là nền cho quyết định trigger và OHSS prevention."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 58, 110);
}
module.exports = { createSlide };
