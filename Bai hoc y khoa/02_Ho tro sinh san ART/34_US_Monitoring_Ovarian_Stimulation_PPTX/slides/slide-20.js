const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "AMH: ưu điểm và giới hạn",
  "points": [
    "AMH tương đối ổn định trong chu kỳ nên thuận tiện hơn FSH đầu chu kỳ.",
    "AMH phản ánh số nang nhỏ có hoạt tính tế bào hạt.",
    "AMH cao trong PCOS có thể đi kèm high response và nguy cơ OHSS.",
    "AMH thấp dự đoán ít noãn hơn nhưng không tự động đồng nghĩa không thể có thai."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 19, 110);
}
module.exports = { createSlide };
