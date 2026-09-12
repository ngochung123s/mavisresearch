const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Ovarian response: đáp ứng thật sau gonadotropin",
  "points": [
    "Một bệnh nhân có reserve tương đối tốt vẫn có thể đáp ứng không như kỳ vọng.",
    "Response nên được đọc bằng số nang đang phát triển, tốc độ lớn lên và phân bố kích thước.",
    "Tiền sử chu kỳ trước có giá trị mạnh trong cá thể hóa liều.",
    "FOI/FORT là cách diễn đạt hiệu suất huy động nang thành noãn/nang trưởng thành."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 12, 110);
}
module.exports = { createSlide };
