const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Take-home 1: reserve khác response",
  "points": [
    "AFC/AMH cho biết số lượng tiềm năng, không thay thế tuổi khi tư vấn chất lượng noãn.",
    "Response thật phải đọc bằng số nang đang phát triển và tiền sử chu kỳ.",
    "Không nên hứa live birth chỉ từ AMH/AFC tốt.",
    "Tách rõ số noãn kỳ vọng và tiên lượng phôi/live birth."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 105, 110);
}
module.exports = { createSlide };
