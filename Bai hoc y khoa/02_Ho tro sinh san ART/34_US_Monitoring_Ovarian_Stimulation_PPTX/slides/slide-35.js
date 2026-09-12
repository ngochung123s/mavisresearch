const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Vai trò LH trong phát triển nang",
  "points": [
    "LH không chỉ là hormone cần chặn; LH sinh lý vẫn cần cho steroidogenesis.",
    "Vấn đề trong IVF là đỉnh LH sớm gây hoàng thể hóa sớm hoặc rụng noãn trước chọc hút.",
    "Protocol khác nhau chủ yếu ở cách kiểm soát LH surge.",
    "Khi đọc LH, cần đặt trong bối cảnh protocol đang dùng."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 34, 110);
}
module.exports = { createSlide };
