const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Có cần E2/LH/P4 mỗi lần không?",
  "points": [
    "Không nhất thiết định lượng hormone trong mọi lần khám cho mọi bệnh nhân.",
    "Siêu âm vẫn là nền tảng theo dõi nang.",
    "Hormone có giá trị khi nghi đáp ứng bất thường, OHSS, LH surge hoặc progesterone tăng sớm.",
    "Làm xét nghiệm nên có kế hoạch: kết quả sẽ đổi quyết định gì?"
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 71, 110);
}
module.exports = { createSlide };
