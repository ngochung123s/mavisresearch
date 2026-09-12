const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "AFC: nang 2-9 mm",
  "points": [
    "AFC là số nang thứ cấp đường kính khoảng 2-9 mm ở đầu chu kỳ.",
    "Đây là đoàn hệ nang đã được tuyển chọn và có thể đáp ứng với FSH trong chu kỳ.",
    "Đếm AFC nên đi cùng nhận xét độ đồng đều và khả năng tiếp cận buồng trứng.",
    "AFC không chỉ là một con số; chất lượng hình ảnh và kinh nghiệm người đo rất quan trọng."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 14, 110);
}
module.exports = { createSlide };
