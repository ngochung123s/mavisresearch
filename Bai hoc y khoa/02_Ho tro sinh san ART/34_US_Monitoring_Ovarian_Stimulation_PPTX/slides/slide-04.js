const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Vì sao bài này quan trọng?",
  "points": [
    "Kích thích buồng trứng quyết định số noãn, chất lượng noãn kỳ vọng và an toàn điều trị.",
    "Theo dõi đúng giúp điều chỉnh liều, chọn thời điểm antagonist, chọn trigger và dự phòng OHSS.",
    "Sai ở một mốc nhỏ có thể dẫn đến noãn non, quá kích, progesterone tăng sớm hoặc bỏ lỡ thời điểm tối ưu.",
    "Siêu âm là công cụ không xâm nhập, lặp lại được và không thể thay thế trong theo dõi nang."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "kicker": "why"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 3, 110);
}
module.exports = { createSlide };
