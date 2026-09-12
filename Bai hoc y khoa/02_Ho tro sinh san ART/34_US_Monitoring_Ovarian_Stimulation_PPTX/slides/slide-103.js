const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Decision table: đáp ứng cao",
  "question": "Nhiều nang và nguy cơ OHSS?",
  "options": [
    {
      "title": "Giảm nguy cơ",
      "text": "Xem liều, antagonist, lịch theo dõi.",
      "level": "ok"
    },
    {
      "title": "E2 nếu cần",
      "text": "Hỗ trợ đánh giá nguy cơ toàn thân.",
      "level": "warn"
    },
    {
      "title": "Agonist trigger",
      "text": "Nếu antagonist cycle và phù hợp.",
      "level": "ok"
    },
    {
      "title": "Freeze-all",
      "text": "Nên nghĩ sớm, không đợi sát chuyển phôi.",
      "level": "danger"
    }
  ],
  "answer": "High response phải được xử lý trước trigger, không phải sau khi đã quá kích.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 102, 110);
}
module.exports = { createSlide };
