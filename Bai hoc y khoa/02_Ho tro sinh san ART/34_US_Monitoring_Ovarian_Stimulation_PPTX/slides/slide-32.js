const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "FSH window",
  "points": [
    "Không chỉ cần vượt ngưỡng, FSH còn phải duy trì đủ lâu.",
    "Cửa sổ FSH càng phù hợp, càng nhiều nang có cơ hội phát triển đồng bộ.",
    "Cửa sổ quá ngắn làm mất nang; quá mạnh/quá dài ở high responder tăng nguy cơ OHSS.",
    "Đó là lý do cần theo dõi và điều chỉnh theo đáp ứng thật."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 31, 110);
}
module.exports = { createSlide };
