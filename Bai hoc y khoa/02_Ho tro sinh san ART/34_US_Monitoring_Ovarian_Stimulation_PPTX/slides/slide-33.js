const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Mỗi nang có một ngưỡng FSH khác nhau",
  "points": [
    "Nang nhạy FSH sẽ phát triển trước và có thể vượt trội.",
    "Nang kém nhạy cần nồng độ FSH cao hơn hoặc thời gian dài hơn.",
    "Khi đoàn hệ không đồng bộ, chỉ nhìn nang lớn nhất dễ trigger quá sớm.",
    "Đọc phân bố kích thước giúp biết cohort đang đồng bộ hay tách nhóm."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 32, 110);
}
module.exports = { createSlide };
