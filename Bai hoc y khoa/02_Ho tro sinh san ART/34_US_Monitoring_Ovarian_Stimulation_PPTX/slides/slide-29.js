const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Từ đoàn hệ nang đến nang trội",
  "points": [
    "Đầu chu kỳ có một đoàn hệ nang thứ cấp được tuyển chọn.",
    "Trong chu kỳ tự nhiên, chỉ một nang vượt trội; các nang còn lại thoái hóa.",
    "Kích thích buồng trứng cứu nhiều nang khỏi thoái hóa bằng FSH ngoại sinh.",
    "Theo dõi siêu âm là cách nhìn thấy đoàn hệ này đang đáp ứng ra sao."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 28, 110);
}
module.exports = { createSlide };
