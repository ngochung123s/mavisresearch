const { renderSlide } = require('./renderer');
const slideData = {
  "type": "references",
  "title": "Tài liệu tham khảo đã verify",
  "refs": [
    "ESHRE guideline: ovarian stimulation for IVF/ICSI. PMID: 32395637.",
    "ESHRE guideline: ovarian stimulation for IVF/ICSI: an update in 2025. PMID: 41732035.",
    "Testing and interpreting measures of ovarian reserve: a committee opinion. PMID: 33280722.",
    "Association between the number of eggs and live birth in IVF treatment. PMID: 21558332.",
    "Consensus statement on prevention and detection of ovarian hyperstimulation syndrome. PMID: 26597569."
  ]
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 110, 110);
}
module.exports = { createSlide };
