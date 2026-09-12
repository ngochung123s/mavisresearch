const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Mild stimulation",
  "points": [
    "Kết hợp thuốc uống với FSH liều thấp.",
    "Có thể phù hợp một số bệnh nhân giảm dự trữ hoặc cần tối ưu chi phí/trải nghiệm.",
    "Không nên hiểu là luôn tốt hơn conventional stimulation.",
    "Đánh giá bằng mục tiêu thực tế: số noãn kỳ vọng, chi phí, thời gian và khả năng gom phôi."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 47, 110);
}
module.exports = { createSlide };
