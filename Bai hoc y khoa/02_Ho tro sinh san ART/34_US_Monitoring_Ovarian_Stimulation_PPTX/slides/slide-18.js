const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Nang không đồng đều: ý nghĩa thực hành",
  "points": [
    "Đoàn hệ không đồng đều dễ dẫn đến nang trưởng thành xen lẫn noãn non hoặc thoái hóa.",
    "Cần theo dõi phân bố kích thước, không chỉ nang lớn nhất.",
    "Một số chiến lược đồng bộ hóa có thể được cân nhắc tùy protocol và trung tâm.",
    "Khi lệch pha rõ, quyết định trigger phải cân bằng nhóm nang lớn và nhóm nang còn nhỏ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 17, 110);
}
module.exports = { createSlide };
