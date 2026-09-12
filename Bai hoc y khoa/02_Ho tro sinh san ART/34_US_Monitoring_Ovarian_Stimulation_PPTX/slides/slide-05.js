const { renderSlide } = require('./renderer');
const slideData = {
  "type": "timeline",
  "title": "Bản đồ quyết định của một chu kỳ IVF/ICSI",
  "steps": [
    {
      "label": "Baseline",
      "text": "AFC, nang tồn dư, tử cung, đường chọc hút"
    },
    {
      "label": "Start FSH",
      "text": "Chọn liều theo dự trữ và đáp ứng dự kiến"
    },
    {
      "label": "Day 5-7",
      "text": "Đọc tốc độ nang và quyết định antagonist"
    },
    {
      "label": "Late stim",
      "text": "Theo dõi nang, nội mạc, OHSS, P4"
    },
    {
      "label": "Trigger",
      "text": "Chọn thời điểm và loại trigger"
    },
    {
      "label": "OPU/ET",
      "text": "Chọc hút, fresh hay freeze-all"
    }
  ],
  "note": "Mỗi mốc siêu âm phải trả lời một câu hỏi điều trị.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 4, 110);
}
module.exports = { createSlide };
