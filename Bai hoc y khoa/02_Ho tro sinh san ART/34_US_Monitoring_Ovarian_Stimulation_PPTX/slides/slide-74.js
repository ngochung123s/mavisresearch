const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "LH surge: khi nào cần nghi?",
  "points": [
    "Flexible antagonist dùng muộn hoặc tái khám trễ.",
    "Nang lớn nhanh, bệnh nhân có dấu rụng noãn hoặc hormone bất thường.",
    "Progesterone tăng kèm LH thay đổi.",
    "Khi nghi surge, cần quyết định nhanh về antagonist/trigger/hủy hoặc rescue tùy trung tâm."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 73, 110);
}
module.exports = { createSlide };
