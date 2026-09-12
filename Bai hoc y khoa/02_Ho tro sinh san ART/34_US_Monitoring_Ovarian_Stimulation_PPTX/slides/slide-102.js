const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Decision table: đáp ứng thấp",
  "question": "Ít nang phát triển hơn kỳ vọng?",
  "options": [
    {
      "title": "Kiểm tra lại baseline",
      "text": "Tuổi, AMH, AFC, FSH, tiền sử response.",
      "level": "ok"
    },
    {
      "title": "Đếm nang thật",
      "text": "Có nang nhỏ bị bỏ sót không?",
      "level": "ok"
    },
    {
      "title": "Liều rất cao?",
      "text": "Không chắc tăng thêm sẽ có ích.",
      "level": "warn"
    },
    {
      "title": "Tư vấn mục tiêu",
      "text": "Có thể cần gom noãn hoặc đổi chiến lược.",
      "level": "warn"
    }
  ],
  "answer": "Poor response cần tư vấn kỳ vọng, không chỉ phản xạ tăng liều.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 101, 110);
}
module.exports = { createSlide };
