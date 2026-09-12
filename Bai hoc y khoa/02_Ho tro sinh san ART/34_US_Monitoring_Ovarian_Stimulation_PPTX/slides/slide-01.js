const { renderSlide } = require('./renderer');
const slideData = {
  "type": "cover",
  "title": "Siêu âm theo dõi quá trình kích thích buồng trứng",
  "subtitle": "Deck học cá nhân: từ baseline đến trigger và freeze-all",
  "note": "Tập trung vào cách đọc siêu âm, cách ra quyết định và các điểm cập nhật từ guideline.",
  "author": "Bác sĩ Ngọc Hưng",
  "date": "2026-07-03"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, null, 110);
}
module.exports = { createSlide };
