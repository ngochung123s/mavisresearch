const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "DuoStim: không phải routine",
  "points": [
    "Kích thích hai lần trong cùng một chu kỳ để gom noãn nhanh.",
    "Có thể cân nhắc ở poor prognosis/giảm dự trữ cần tối đa hóa số noãn trong thời gian ngắn.",
    "Cần hiểu đây là chiến lược chọn lọc, không phải chuẩn cho mọi bệnh nhân.",
    "Tư vấn phải rõ về chi phí, số lần chọc hút và kế hoạch đông phôi."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 51, 110);
}
module.exports = { createSlide };
