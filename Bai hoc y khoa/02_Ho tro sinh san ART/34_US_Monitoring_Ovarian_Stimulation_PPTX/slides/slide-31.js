const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "FSH threshold",
  "points": [
    "Mỗi nang cần nồng độ FSH vượt một ngưỡng để tiếp tục phát triển.",
    "Ngưỡng FSH khác nhau giữa các nang trong cùng đoàn hệ.",
    "Nếu FSH không vượt ngưỡng, nang nhỏ sẽ thoái hóa.",
    "FSH ngoại sinh nhằm đưa nhiều nang vượt ngưỡng hơn nang tự nhiên."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 30, 110);
}
module.exports = { createSlide };
