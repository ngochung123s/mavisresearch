const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Mục tiêu mỗi lần siêu âm",
  "points": [
    "Đánh giá số nang đang phát triển và phân bố kích thước.",
    "Đo nang lớn nhất hai bên và nhóm nang gần trưởng thành.",
    "Đọc nội mạc nếu thông tin này có thể đổi kế hoạch transfer.",
    "Tìm dấu high response/OHSS và khả năng chọc hút khó.",
    "Kết luận phải dẫn đến một quyết định cụ thể."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "small": true
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 54, 110);
}
module.exports = { createSlide };
