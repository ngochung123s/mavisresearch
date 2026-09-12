const { renderSlide } = require('./renderer');
const slideData = {
  "type": "compare",
  "title": "Tổng quan các phác đồ",
  "columns": [
    {
      "title": "Agonist",
      "points": [
        "Long protocol",
        "Flare-up protocol",
        "Ức chế hoặc tận dụng flare ban đầu"
      ]
    },
    {
      "title": "Antagonist",
      "points": [
        "Fixed hoặc flexible",
        "Ngắn, thuận tiện, giảm OHSS",
        "Cho phép agonist trigger"
      ]
    },
    {
      "title": "Khác",
      "points": [
        "Mild stimulation",
        "PPOS",
        "Random start / DuoStim chọn lọc"
      ]
    }
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 39, 110);
}
module.exports = { createSlide };
