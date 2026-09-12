const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Đánh giá tử cung trước chu kỳ",
  "points": [
    "U xơ dưới niêm, polyp, vách ngăn hoặc dịch lòng tử cung có thể làm đổi kế hoạch chuyển phôi.",
    "Mục tiêu baseline không chỉ là buồng trứng mà còn là khả năng fresh transfer.",
    "Nếu phát hiện bất thường có ý nghĩa, có thể kích thích thu phôi nhưng trì hoãn chuyển phôi.",
    "Ghi nhận sớm giúp tránh quyết định vội vào ngày trigger."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 26, 110);
}
module.exports = { createSlide };
