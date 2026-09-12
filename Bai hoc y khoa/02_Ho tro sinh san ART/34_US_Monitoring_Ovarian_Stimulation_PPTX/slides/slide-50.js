const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Vì sao PPOS cần freeze-all?",
  "points": [
    "Progestin làm nội mạc không đồng bộ với tuổi phôi.",
    "Mục tiêu của PPOS là kiểm soát LH surge, không phải chuẩn bị nội mạc chuyển tươi.",
    "Do đó phôi nên được đông và chuyển ở chu kỳ khác.",
    "Điểm này phải nói rõ trước chu kỳ để bệnh nhân không kỳ vọng fresh transfer."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 49, 110);
}
module.exports = { createSlide };
