const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Progesterone tăng sớm: ý nghĩa",
  "points": [
    "Progesterone tăng trước trigger có thể làm nội mạc lệch pha với phôi.",
    "Tác động chính là quyết định fresh transfer hay freeze-all.",
    "Cần đọc cùng số nang, E2, ngày kích thích và kế hoạch chuyển phôi.",
    "Không nên chỉ ghi P4 tăng mà không nêu hệ quả điều trị."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 74, 110);
}
module.exports = { createSlide };
