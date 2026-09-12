const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Ngày 6-7 kích thích: mốc thực hành",
  "points": [
    "Đây thường là thời điểm kiểm tra đáp ứng ban đầu.",
    "Với flexible antagonist, mốc này đặc biệt quan trọng để không bắt antagonist muộn.",
    "Với fixed antagonist, có thể ít phụ thuộc siêu âm sớm hơn nhưng vẫn cần đọc response.",
    "Ngày hẹn tiếp theo phụ thuộc kích thước nang và tốc độ phát triển."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 60, 110);
}
module.exports = { createSlide };
