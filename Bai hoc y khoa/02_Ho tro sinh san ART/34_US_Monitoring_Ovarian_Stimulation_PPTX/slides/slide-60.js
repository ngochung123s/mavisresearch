const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Tốc độ phát triển nang 1-2 mm/ngày",
  "points": [
    "Tốc độ trung bình thường khoảng 1-2 mm/ngày.",
    "Nếu nang lớn nhanh bất thường, kiểm tra lại đo lường và hormone khi cần.",
    "Nếu nhiều nang đứng yên, nghĩ poor response hoặc liều chưa đủ, nhưng tăng liều muộn không luôn cải thiện kết quả.",
    "Theo dõi tốc độ cần so với cùng nang/nhóm nang qua các lần khám."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 59, 110);
}
module.exports = { createSlide };
