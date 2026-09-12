const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Antagonist protocol: vì sao hiện dùng nhiều",
  "points": [
    "Bắt đầu FSH đầu chu kỳ, thêm antagonist khi cần chặn LH surge.",
    "Thời gian ngắn hơn long agonist.",
    "Ít OHSS hơn và thân thiện với bệnh nhân hơn trong nhiều bối cảnh.",
    "Cho phép GnRH agonist trigger khi nguy cơ OHSS cao."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 43, 110);
}
module.exports = { createSlide };
