const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Đo nang: bờ trong đến bờ trong",
  "points": [
    "Đường kính nang nên đo từ bờ trong bên này đến bờ trong bên đối diện.",
    "Không đo cả thành nang vì sẽ làm tăng giả kích thước.",
    "Nên đo mặt cắt lớn nhất của nang.",
    "Khi có nhiều nang, ưu tiên ghi có hệ thống để không bỏ sót nhóm gần trigger."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 56, 110);
}
module.exports = { createSlide };
