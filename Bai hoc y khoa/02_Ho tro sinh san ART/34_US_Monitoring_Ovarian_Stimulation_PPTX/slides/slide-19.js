const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Buồng trứng xa đầu dò: tại sao phải ghi nhận?",
  "points": [
    "Gợi ý chọc hút noãn có thể khó hơn.",
    "Có thể liên quan dính vùng chậu, endometriosis hoặc buồng trứng bị kéo cao.",
    "Cần ghi hướng tiếp cận, khoảng cách và nguy cơ mạch máu/ruột xen giữa nếu thấy.",
    "Thông tin này quan trọng ngang với số nang trong planning thủ thuật."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 18, 110);
}
module.exports = { createSlide };
