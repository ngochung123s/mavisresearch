const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "Hình thái nội mạc",
  "columns": [
    {
      "title": "Ba lá",
      "points": [
        "Hình ảnh 3 đường tăng âm và 2 vùng giảm âm",
        "Thường được xem là thuận lợi hơn cho chuyển tươi"
      ]
    },
    {
      "title": "Tăng âm toàn bộ",
      "points": [
        "Không còn vùng giảm âm rõ",
        "Có thể kém thuận lợi tùy thời điểm và bối cảnh"
      ]
    },
    {
      "title": "Trung gian",
      "points": [
        "Có đường tăng âm nhưng phân lớp không rõ",
        "Cần đọc cùng hormone và ngày chu kỳ"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 68, 110);
}
module.exports = { createSlide };
