const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Nang >24 mm: nguy cơ giảm yield",
  "points": [
    "Nang quá lớn có thể không đồng nghĩa thêm noãn tốt.",
    "Khi nhiều nang đã quá lớn, cần cân nhắc không trì hoãn chỉ để chờ nhóm nhỏ.",
    "Nếu chỉ một vài nang lớn vượt trội, phải đánh giá cohort còn lại.",
    "Thông điệp: trigger là cân bằng toàn cohort, không tối ưu một nang riêng lẻ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 63, 110);
}
module.exports = { createSlide };
