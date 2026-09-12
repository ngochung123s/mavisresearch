const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Khi nào cần bắt antagonist trong flexible protocol?",
  "question": "Nang lớn nhất đã khoảng 14 mm?",
  "options": [
    {
      "title": "Có",
      "text": "Thường nên bắt đầu antagonist theo tiêu chí trung tâm.",
      "level": "ok"
    },
    {
      "title": "Chưa",
      "text": "Có thể theo dõi tiếp nếu LH surge risk thấp.",
      "level": "ok"
    },
    {
      "title": "Khó tái khám",
      "text": "Cân nhắc an toàn logistics, tránh dùng muộn.",
      "level": "warn"
    },
    {
      "title": "LH nghi tăng",
      "text": "Xem hormone và quyết định nhanh.",
      "level": "danger"
    }
  ],
  "answer": "Flexible tốt khi theo dõi sát; nếu logistics không chắc, fixed có thể an toàn vận hành hơn.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 61, 110);
}
module.exports = { createSlide };
