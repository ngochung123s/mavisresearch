const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Antagonist fixed protocol",
  "points": [
    "Antagonist bắt đầu cố định ngày 5 hoặc 6 kích thích.",
    "Ưu điểm là dễ vận hành, giảm nguy cơ quên/muộn antagonist.",
    "Có thể dùng tốt khi logistics trung tâm đông hoặc bệnh nhân khó tái khám sát.",
    "Nhược điểm là có thể dùng nhiều ngày antagonist hơn flexible."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 44, 110);
}
module.exports = { createSlide };
