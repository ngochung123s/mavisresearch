const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Trigger không chỉ dựa vào nang lớn nhất",
  "points": [
    "Cần xem toàn bộ phân bố kích thước nang.",
    "Một nang lớn nhất chưa nói đủ số noãn trưởng thành kỳ vọng.",
    "Cần xem nguy cơ OHSS, loại trigger, kế hoạch fresh/freeze và giờ chọc hút.",
    "Mục tiêu là tối ưu cohort, không tối ưu một nang."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 78, 110);
}
module.exports = { createSlide };
