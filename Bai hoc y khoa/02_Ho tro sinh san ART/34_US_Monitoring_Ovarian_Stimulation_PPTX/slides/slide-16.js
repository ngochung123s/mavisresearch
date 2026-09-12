const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Cách đếm AFC đúng",
  "points": [
    "Dùng đầu dò âm đạo nếu có thể để tối ưu độ phân giải.",
    "Quét toàn bộ buồng trứng theo một chiều có hệ thống.",
    "Tránh đếm lặp cùng một nang khi xoay đầu dò.",
    "Ghi riêng hai buồng trứng nếu có bất đối xứng, dính, endometrioma hoặc khó tiếp cận."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 15, 110);
}
module.exports = { createSlide };
