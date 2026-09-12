const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Freeze-all khi progesterone tăng sớm",
  "points": [
    "Progesterone tăng sớm có thể làm lệch pha nội mạc.",
    "Noãn/phôi có thể vẫn tốt nhưng cửa sổ làm tổ không tối ưu cho fresh transfer.",
    "Freeze-all giúp chuyển phôi ở chu kỳ nội mạc được chuẩn bị phù hợp hơn.",
    "Không nên bỏ qua P4 nếu đang cân nhắc fresh transfer trong ca nguy cơ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 97, 110);
}
module.exports = { createSlide };
