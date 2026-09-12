const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Nhận diện high response",
  "points": [
    "AFC/AMH cao ngay từ baseline.",
    "Nhiều nang nhỏ tăng đồng loạt trong kích thích.",
    "E2 cao nếu được đo.",
    "PCOS hoặc tiền sử OHSS.",
    "Buồng trứng lớn, nhiều nang trung bình và gần trưởng thành."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "small": true
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 89, 110);
}
module.exports = { createSlide };
