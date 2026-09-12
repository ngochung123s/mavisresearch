const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Mục tiêu số noãn: không phải càng nhiều càng tốt",
  "points": [
    "Nghiên cứu lớn ghi nhận live birth tăng theo số noãn đến khoảng 15 noãn.",
    "Sau đó hiệu quả plateau khoảng 15-20 và giảm khi số noãn rất cao.",
    "Số noãn cao đi kèm nguy cơ OHSS và gánh nặng điều trị.",
    "Mục tiêu thực hành là tối ưu hiệu quả đi kèm an toàn."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "pearl": "PMID 21558332: số noãn tối ưu là khái niệm cân bằng, không phải càng nhiều càng tốt."
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 93, 110);
}
module.exports = { createSlide };
