const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Freeze-all khi nguy cơ OHSS",
  "points": [
    "High response là chỉ định kinh điển để tránh làm nặng OHSS sau chuyển phôi/thai kỳ.",
    "Đặc biệt hợp lý sau agonist trigger trong antagonist cycle.",
    "Giúp tách nguy cơ kích thích buồng trứng khỏi thai kỳ sớm.",
    "Cần tư vấn bệnh nhân trước trigger nếu nguy cơ đang tăng."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 96, 110);
}
module.exports = { createSlide };
