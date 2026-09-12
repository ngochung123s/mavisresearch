const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "LH quá thấp và quá cao đều có vấn đề",
  "columns": [
    {
      "title": "LH quá thấp",
      "points": [
        "Steroidogenesis kém",
        "Estrogen có thể thấp",
        "Nang phát triển không tối ưu"
      ]
    },
    {
      "title": "LH quá cao/surge",
      "points": [
        "Hoàng thể hóa sớm",
        "Progesterone tăng",
        "Nguy cơ rụng trước chọc hút",
        "Ảnh hưởng kế hoạch fresh transfer"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 35, 110);
}
module.exports = { createSlide };
