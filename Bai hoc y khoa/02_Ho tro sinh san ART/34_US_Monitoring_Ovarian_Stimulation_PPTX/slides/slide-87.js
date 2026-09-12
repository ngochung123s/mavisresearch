const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Khi nào không dùng agonist trigger?",
  "question": "Có phải chu kỳ antagonist và tuyến yên còn đáp ứng?",
  "options": [
    {
      "title": "Long agonist",
      "text": "Không phù hợp vì tuyến yên bị ức chế.",
      "level": "danger"
    },
    {
      "title": "Antagonist",
      "text": "Có thể dùng nếu high response/OHSS risk.",
      "level": "ok"
    },
    {
      "title": "LH rất thấp/ức chế mạnh",
      "text": "Cần cẩn thận nguy cơ trigger failure.",
      "level": "warn"
    },
    {
      "title": "Muốn fresh transfer",
      "text": "Phải có chiến lược luteal support rõ.",
      "level": "warn"
    }
  ],
  "answer": "Agonist trigger là công cụ an toàn mạnh, nhưng không phải dùng được trong mọi protocol.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 86, 110);
}
module.exports = { createSlide };
