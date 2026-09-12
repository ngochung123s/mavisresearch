const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "hCG trigger: cơ chế và điểm mạnh",
  "points": [
    "hCG gắn thụ thể LH/hCG và thay thế đỉnh LH để trưởng thành noãn.",
    "Dễ dùng, quen thuộc, hiệu quả trong nhiều chu kỳ.",
    "Có thể dùng urinary hoặc recombinant hCG tùy thực hành.",
    "Phù hợp khi nguy cơ OHSS không cao và kế hoạch hoàng thể/fresh transfer rõ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 81, 110);
}
module.exports = { createSlide };
