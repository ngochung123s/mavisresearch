const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Nang 14-24 mm: vùng kỳ vọng noãn thu được",
  "points": [
    "Nhiều thực hành xem nhóm nang 14-24 mm là nhóm có khả năng đóng góp noãn tốt.",
    "Không phải mọi nang trong khoảng này đều có noãn trưởng thành.",
    "Cần đọc cùng số nang nhỏ hơn còn có thể bắt kịp.",
    "Trigger quá muộn có thể làm nhóm lớn quá già; quá sớm làm nhóm nhỏ non."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 62, 110);
}
module.exports = { createSlide };
