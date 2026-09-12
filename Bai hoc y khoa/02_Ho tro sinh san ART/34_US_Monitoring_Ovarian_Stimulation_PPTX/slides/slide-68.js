const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Nội mạc tử cung: đo thế nào?",
  "points": [
    "Đo trên mặt cắt dọc tử cung ở vị trí dày nhất.",
    "Đặt caliper tại ranh giới nội mạc-cơ tử cung, đo vuông góc với đường nội mạc.",
    "Ghi độ dày bằng mm và hình thái.",
    "Đo nội mạc có ý nghĩa nhất khi gần quyết định trigger/chuyển phôi."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 67, 110);
}
module.exports = { createSlide };
