const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Khi nào nội mạc thật sự ảnh hưởng quyết định?",
  "question": "Nội mạc xấu vào giai đoạn trigger?",
  "options": [
    {
      "title": "Fresh transfer còn hợp lý?",
      "text": "Xem lại độ dày, hình thái, P4 và nguy cơ OHSS.",
      "level": "warn"
    },
    {
      "title": "Freeze-all",
      "text": "Nên cân nhắc khi nội mạc không thuận lợi.",
      "level": "ok"
    },
    {
      "title": "Không quá sớm kết luận",
      "text": "Đo quá sớm ít giá trị hơn ngày trigger.",
      "level": "ok"
    },
    {
      "title": "Ghi rõ lý do",
      "text": "Quyết định freeze cần có lý do cụ thể.",
      "level": "ok"
    }
  ],
  "answer": "Nội mạc quan trọng nhất khi nó làm đổi kế hoạch fresh transfer sang freeze-all.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 69, 110);
}
module.exports = { createSlide };
