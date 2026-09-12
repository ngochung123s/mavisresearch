const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Những quyết định cần đưa ra trong kích thích",
  "points": [
    "Có tiếp tục liều hiện tại hay điều chỉnh?",
    "Có cần bắt đầu antagonist chưa?",
    "Nang đang đồng bộ hay lệch pha?",
    "Đã đủ điều kiện trigger chưa?",
    "Nguy cơ OHSS có làm đổi loại trigger không?",
    "Fresh transfer còn phù hợp hay nên freeze-all?"
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "kicker": "decision map"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 7, 110);
}
module.exports = { createSlide };
