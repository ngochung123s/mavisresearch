const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Freeze-all sau agonist trigger",
  "points": [
    "Agonist trigger làm giảm OHSS nhưng gây suy hoàng thể tương đối.",
    "Freeze-all tránh phụ thuộc vào nội mạc/hoàng thể của chu kỳ đó.",
    "Đây là phối hợp đặc biệt quan trọng ở high responder.",
    "Nếu chuyển tươi sau agonist trigger, cần protocol hỗ trợ hoàng thể chuyên biệt."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 99, 110);
}
module.exports = { createSlide };
