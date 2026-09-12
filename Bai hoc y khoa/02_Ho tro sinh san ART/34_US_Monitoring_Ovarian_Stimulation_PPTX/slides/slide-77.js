const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Quy tắc thực hành cho hormone",
  "question": "Kết quả xét nghiệm có thể đổi quyết định không?",
  "options": [
    {
      "title": "Có",
      "text": "Nên làm, đặc biệt E2/LH/P4 trong tình huống nghi ngờ.",
      "level": "ok"
    },
    {
      "title": "Không",
      "text": "Không nên làm chỉ để có thêm số.",
      "level": "warn"
    },
    {
      "title": "High response",
      "text": "E2 có thể hỗ trợ đánh giá OHSS.",
      "level": "danger"
    },
    {
      "title": "Fresh transfer?",
      "text": "P4 có thể đổi sang freeze-all.",
      "level": "warn"
    }
  ],
  "answer": "Hormone là công cụ ra quyết định, không phải thủ tục bắt buộc ở mọi lần siêu âm.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 76, 110);
}
module.exports = { createSlide };
