const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Theo dõi tối giản nhưng không mất an toàn",
  "points": [
    "Có thể giảm số lần khám/xét nghiệm ở bệnh nhân nguy cơ thấp và đáp ứng điển hình.",
    "Giảm xét nghiệm không có nghĩa giảm chất lượng theo dõi.",
    "Điều kiện là có lịch siêu âm hợp lý và tiêu chí gọi bệnh nhân quay lại rõ.",
    "Nhóm high responder, PCOS, poor response hoặc logistics khó cần theo dõi cá thể hóa."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 75, 110);
}
module.exports = { createSlide };
