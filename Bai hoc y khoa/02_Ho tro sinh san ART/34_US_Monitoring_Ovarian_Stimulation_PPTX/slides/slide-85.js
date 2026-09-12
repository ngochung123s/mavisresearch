const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Vì sao agonist trigger giảm OHSS?",
  "points": [
    "Đỉnh LH nội sinh ngắn và ít kéo dài hoàng thể hơn hCG.",
    "Giảm kích thích VEGF và giảm nguy cơ OHSS ở high responder.",
    "Hiệu quả phòng OHSS mạnh nhất khi kết hợp freeze-all.",
    "Nếu vẫn chuyển tươi, cần hỗ trợ hoàng thể rất cẩn thận theo protocol trung tâm."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 84, 110);
}
module.exports = { createSlide };
