const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Trigger checklist",
  "points": [
    "Số nang theo nhóm kích thước đã đủ chưa?",
    "Có bao nhiêu nang nguy cơ đóng góp OHSS?",
    "Nội mạc và progesterone có còn phù hợp fresh transfer không?",
    "Chu kỳ antagonist có thể dùng agonist trigger nếu high risk không?",
    "Giờ chọc hút 34-36 giờ sau trigger đã được lên lịch chưa?"
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "small": true
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 79, 110);
}
module.exports = { createSlide };
