const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Take-home 2: siêu âm cần ghi theo checklist",
  "points": [
    "Số nang theo nhóm kích thước.",
    "Nang lớn nhất hai bên và tốc độ phát triển.",
    "Nội mạc nếu liên quan fresh/freeze.",
    "OHSS risk và đường chọc hút.",
    "Kết luận quản lý cho lần khám tiếp theo."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "small": true
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 106, 110);
}
module.exports = { createSlide };
