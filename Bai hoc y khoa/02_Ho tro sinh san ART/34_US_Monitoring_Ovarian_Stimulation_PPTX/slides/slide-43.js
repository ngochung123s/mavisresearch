const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Flare-up protocol: logic và giới hạn",
  "points": [
    "Tận dụng flare ban đầu của GnRH agonist để tăng FSH nội sinh.",
    "Thường phối hợp với FSH ngoại sinh.",
    "Tăng FSH đi kèm tăng LH nên kiểm soát LH surge không tốt bằng antagonist.",
    "Hiện ít dùng routine, có thể gặp trong nhóm lớn tuổi/giảm dự trữ tùy trung tâm."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 42, 110);
}
module.exports = { createSlide };
