const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Take-home 5: freeze-all là công cụ cá thể hóa",
  "points": [
    "Rất hợp lý khi OHSS risk, P4 tăng, PPOS, random start, agonist trigger hoặc nội mạc không thuận lợi.",
    "Không mặc định freeze-all tốt hơn fresh cho mọi bệnh nhân.",
    "Quyết định tốt là quyết định có lý do rõ và được tư vấn trước.",
    "Mục tiêu cuối cùng là hiệu quả đi cùng an toàn."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 109, 110);
}
module.exports = { createSlide };
