const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Không tăng liều vô hạn ở poor responder",
  "points": [
    "Ở người dự kiến đáp ứng kém, tăng liều rất cao thường không đảm bảo tăng noãn tương xứng.",
    "Cần xem tuổi, AMH/AFC, tiền sử response và số nang thực sự phát triển.",
    "Mục tiêu là chiến lược hợp lý, không phải đuổi theo con số liều.",
    "Nếu nhiều chu kỳ gom noãn, cần tư vấn kỳ vọng và chi phí."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 92, 110);
}
module.exports = { createSlide };
