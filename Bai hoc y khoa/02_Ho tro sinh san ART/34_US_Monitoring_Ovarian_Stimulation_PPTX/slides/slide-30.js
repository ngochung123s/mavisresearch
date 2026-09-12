const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Kích thích không làm cạn dự trữ buồng trứng",
  "points": [
    "Các nang được kích thích là đoàn hệ đã được tuyển trong chu kỳ đó.",
    "Nếu không kích thích, phần lớn nang trong đoàn hệ này cũng sẽ thoái hóa.",
    "Điểm cần tư vấn: kích thích làm huy động nhiều nang của chu kỳ, không lấy mất nang của tương lai theo nghĩa đơn giản.",
    "Reserve giảm theo tuổi và sinh học buồng trứng, không phải do một chu kỳ IVF làm cạn."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 29, 110);
}
module.exports = { createSlide };
