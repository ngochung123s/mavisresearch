const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Vì sao agonist trigger gây suy hoàng thể?",
  "points": [
    "Đỉnh LH ngắn làm hoàng thể kém được duy trì.",
    "Nội mạc có thể không được hỗ trợ đủ nếu chuyển tươi.",
    "Do đó high-risk agonist trigger thường đi cùng freeze-all.",
    "Điểm này phải được giải thích trước để bệnh nhân hiểu vì sao không chuyển tươi."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 85, 110);
}
module.exports = { createSlide };
