const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Follicular waves và cơ sở random start",
  "points": [
    "Không phải mọi nang chỉ được tuyển một lần duy nhất đầu chu kỳ.",
    "Có thể có nhiều làn sóng tuyển nang trong một chu kỳ.",
    "Đây là cơ sở của random start trong bảo tồn sinh sản hoặc tình huống cần rút ngắn thời gian.",
    "Dù vậy random start không phải protocol routine cho mọi bệnh nhân IVF."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 37, 110);
}
module.exports = { createSlide };
