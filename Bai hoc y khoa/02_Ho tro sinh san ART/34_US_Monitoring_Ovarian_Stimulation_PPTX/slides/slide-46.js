const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Antagonist flexible protocol",
  "points": [
    "Antagonist bắt đầu khi nang lớn nhất khoảng 14 mm hoặc theo tiêu chí trung tâm.",
    "Giảm số ngày dùng antagonist ở một số bệnh nhân.",
    "Đòi hỏi siêu âm đúng thời điểm, thường quanh ngày 6 kích thích.",
    "Nếu tái khám muộn có nguy cơ bắt antagonist chậm."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 45, 110);
}
module.exports = { createSlide };
