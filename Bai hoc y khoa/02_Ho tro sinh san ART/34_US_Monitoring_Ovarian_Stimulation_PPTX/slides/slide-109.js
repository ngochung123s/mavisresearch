const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Take-home 4: trigger là quyết định an toàn",
  "points": [
    "Không chỉ nhìn một nang lớn nhất.",
    "Phải đọc toàn cohort, OHSS risk, nội mạc, progesterone và kế hoạch transfer.",
    "hCG trigger hiệu quả nhưng làm OHSS kéo dài hơn ở high responder.",
    "Agonist trigger giảm OHSS trong antagonist cycle nhưng cần chú ý suy hoàng thể/freeze-all."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 108, 110);
}
module.exports = { createSlide };
