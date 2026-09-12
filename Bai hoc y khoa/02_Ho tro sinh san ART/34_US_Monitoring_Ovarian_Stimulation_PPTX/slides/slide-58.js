const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Nang không tròn: lấy trung bình hai chiều",
  "points": [
    "Nếu nang tròn đều, một đường kính có thể đủ trong thực hành.",
    "Nếu nang bầu dục/không đều, đo hai đường kính lớn nhất và nhỏ nhất rồi lấy trung bình.",
    "Cách đo nhất quán giữa các lần khám quan trọng hơn cố tìm độ chính xác giả tạo.",
    "Nang méo trong buồng trứng nhiều nang dễ làm sai phân bố kích thước."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 57, 110);
}
module.exports = { createSlide };
