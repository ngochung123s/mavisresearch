const { renderSlide } = require('./renderer');
const slideData = {
  "type": "timeline",
  "title": "Antagonist + agonist trigger + freeze-all",
  "steps": [
    {
      "label": "Risk",
      "text": "AFC/AMH cao hoặc nhiều nang"
    },
    {
      "label": "Protocol",
      "text": "Ưu tiên antagonist"
    },
    {
      "label": "Monitor",
      "text": "Theo dõi nang và E2 nếu cần"
    },
    {
      "label": "Trigger",
      "text": "GnRH agonist trigger"
    },
    {
      "label": "Embryo",
      "text": "Đông phôi toàn bộ"
    },
    {
      "label": "Transfer",
      "text": "Chuyển phôi chu kỳ sau"
    }
  ],
  "note": "Đây là trục an toàn quan trọng ở bệnh nhân high response.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 91, 110);
}
module.exports = { createSlide };
