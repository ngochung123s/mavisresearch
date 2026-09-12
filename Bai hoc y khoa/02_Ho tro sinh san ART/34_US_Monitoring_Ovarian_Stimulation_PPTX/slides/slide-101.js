const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Freeze-all khi nội mạc không thuận lợi",
  "points": [
    "Nội mạc quá mỏng, hình thái kém hoặc không đồng bộ có thể làm giảm cơ hội làm tổ.",
    "Progesterone tăng sớm củng cố quyết định freeze-all.",
    "Không phải mọi nội mạc không đẹp ở ngày sớm đều cần freeze; thời điểm đánh giá quan trọng.",
    "Khi đã freeze-all, chuyển phôi ở chu kỳ được tối ưu nội mạc."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 100, 110);
}
module.exports = { createSlide };
