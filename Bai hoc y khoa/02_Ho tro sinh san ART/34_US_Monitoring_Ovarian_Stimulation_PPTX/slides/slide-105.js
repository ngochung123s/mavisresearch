const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Decision table: nghi chọc hút khó",
  "question": "Buồng trứng xa đầu dò hoặc dính?",
  "options": [
    {
      "title": "Ghi vị trí",
      "text": "Bên nào, khoảng cách, hướng tiếp cận.",
      "level": "ok"
    },
    {
      "title": "Tìm vật cản",
      "text": "Ruột, mạch máu, tử cung, endometrioma.",
      "level": "warn"
    },
    {
      "title": "Báo trước ekip",
      "text": "Chuẩn bị thủ thuật và tư vấn nguy cơ.",
      "level": "ok"
    },
    {
      "title": "Không bỏ qua",
      "text": "Access khó có thể quan trọng hơn số nang.",
      "level": "danger"
    }
  ],
  "answer": "Siêu âm theo dõi phải phục vụ cả quyết định chọc hút, không chỉ trigger.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 104, 110);
}
module.exports = { createSlide };
