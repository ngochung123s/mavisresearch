const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Take-home 3: antagonist giúp an toàn và linh hoạt",
  "points": [
    "Antagonist protocol ngắn và thuận tiện cho nhiều bệnh nhân.",
    "Fixed dễ vận hành, flexible cá thể hóa hơn nhưng cần theo dõi sát.",
    "Antagonist mở đường cho GnRH agonist trigger nếu nguy cơ OHSS cao.",
    "Long agonist vẫn có vai trò chọn lọc nhưng không nên là mặc định cho mọi ca."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 107, 110);
}
module.exports = { createSlide };
