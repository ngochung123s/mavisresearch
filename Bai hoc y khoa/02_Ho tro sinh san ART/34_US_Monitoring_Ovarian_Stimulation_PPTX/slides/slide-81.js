const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Tiêu chuẩn trigger trong bài gốc: cách hiểu thận trọng",
  "points": [
    "Bài gốc nêu các mốc như ít nhất 3 nang >17 mm hoặc 2 nang >18 mm và tỷ lệ nang >14 mm.",
    "Các tiêu chuẩn này thay đổi theo protocol và thực hành trung tâm.",
    "Không nên áp máy móc nếu cohort lệch pha hoặc high response.",
    "Slide này dùng để nhớ logic, không thay protocol nội bộ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 80, 110);
}
module.exports = { createSlide };
