const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Decision table: progesterone/nội mạc",
  "question": "Fresh transfer còn phù hợp?",
  "options": [
    {
      "title": "P4 tăng",
      "text": "Nghĩ lệch pha nội mạc.",
      "level": "warn"
    },
    {
      "title": "Nội mạc kém",
      "text": "Cân nhắc freeze-all.",
      "level": "warn"
    },
    {
      "title": "OHSS risk",
      "text": "Freeze-all thường hợp lý hơn.",
      "level": "danger"
    },
    {
      "title": "Không có nguy cơ",
      "text": "Fresh vẫn có thể phù hợp tùy ca.",
      "level": "ok"
    }
  ],
  "answer": "Fresh vs freeze là quyết định cá thể hóa dựa trên cả noãn, hormone, nội mạc và an toàn.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 103, 110);
}
module.exports = { createSlide };
