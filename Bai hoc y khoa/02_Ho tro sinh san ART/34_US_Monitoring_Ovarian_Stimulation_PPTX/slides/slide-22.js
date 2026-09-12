const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Tuổi: yếu tố chất lượng noãn",
  "points": [
    "Tuổi không đếm trực tiếp số nang nhưng dự đoán chất lượng noãn tốt hơn marker nội tiết.",
    "Sau 35 tuổi, nguy cơ lệch bội tăng và live birth giảm dù số noãn có thể còn khá.",
    "AMH/AFC tốt ở bệnh nhân lớn tuổi không xóa bỏ nguy cơ chất lượng noãn.",
    "Tư vấn nên tách rõ số noãn kỳ vọng và xác suất phôi nguyên bội/live birth."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 21, 110);
}
module.exports = { createSlide };
