const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Các điểm cập nhật chính",
  "points": [
    "AMH/AFC hữu ích để dự đoán oocyte yield, nhưng không dự đoán tốt reproductive potential nếu tách khỏi tuổi.",
    "Antagonist protocol thường thuận tiện và an toàn hơn long agonist cho nhiều nhóm bệnh nhân.",
    "Mục tiêu không phải kích càng nhiều noãn càng tốt; số noãn rất cao đi kèm nguy cơ OHSS.",
    "Freeze-all là công cụ cá thể hóa, không phải mặc định luôn tốt hơn fresh transfer."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "kicker": "clinical update"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 8, 110);
}
module.exports = { createSlide };
