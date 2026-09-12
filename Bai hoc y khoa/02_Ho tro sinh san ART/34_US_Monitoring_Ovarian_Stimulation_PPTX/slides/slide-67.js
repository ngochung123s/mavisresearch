const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Doppler không routine",
  "points": [
    "Doppler không cần áp dụng cho tất cả bệnh nhân theo dõi kích thích.",
    "Có thể hữu ích chọn lọc trong một số tình huống nghiên cứu hoặc đáp ứng kém.",
    "Không nên kéo dài thời gian khám chỉ để có Doppler nếu kết quả không đổi quyết định.",
    "Ưu tiên thông tin quyết định: nang, nội mạc, OHSS, đường chọc hút."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 66, 110);
}
module.exports = { createSlide };
