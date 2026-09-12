const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "4 mục tiêu của theo dõi",
  "columns": [
    {
      "title": "Hiệu quả",
      "points": [
        "Đủ số nang phát triển",
        "Tối ưu số noãn kỳ vọng",
        "Không kích quá ít hoặc quá muộn"
      ]
    },
    {
      "title": "Chất lượng",
      "points": [
        "Tránh hoàng thể hóa sớm",
        "Tránh noãn quá non hoặc quá già",
        "Cân nhắc tuổi và chất lượng noãn"
      ]
    },
    {
      "title": "An toàn",
      "points": [
        "Nhận diện high response",
        "Giảm OHSS",
        "Chọn freeze-all khi cần"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 5, 110);
}
module.exports = { createSlide };
