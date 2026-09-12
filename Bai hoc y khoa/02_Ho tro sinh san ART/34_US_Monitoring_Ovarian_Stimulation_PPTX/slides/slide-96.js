const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Freeze-all: đúng chỉ định, không phải mặc định",
  "points": [
    "Vitrification giúp freeze-all trở thành chiến lược khả thi và an toàn hơn trước.",
    "Tuy nhiên freeze-all không nên hiểu là luôn tốt hơn fresh transfer cho mọi bệnh nhân.",
    "Quyết định dựa trên OHSS risk, progesterone, nội mạc, protocol và mục tiêu điều trị.",
    "Nếu quyết định freeze-all, nên ghi rõ lý do trong hồ sơ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 95, 110);
}
module.exports = { createSlide };
