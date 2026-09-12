const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "Long agonist protocol: ưu và nhược",
  "columns": [
    {
      "title": "Ưu điểm",
      "points": [
        "Ức chế LH mạnh",
        "Nang thường đồng đều",
        "Từng là protocol chuẩn trong nhiều trung tâm"
      ]
    },
    {
      "title": "Nhược điểm",
      "points": [
        "Dài ngày",
        "Tốn gonadotropin",
        "Nguy cơ OHSS cao hơn ở nhóm nguy cơ",
        "Không dùng agonist trigger vì tuyến yên đã bị ức chế"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 41, 110);
}
module.exports = { createSlide };
