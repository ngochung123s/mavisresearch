const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Trigger failure: phải nhớ nguy cơ này",
  "points": [
    "Sau agonist trigger vẫn có thể thu được ít/noãn không như kỳ vọng.",
    "Nguy cơ tăng khi đáp ứng LH không đủ hoặc tuyến yên bị ức chế quá mạnh.",
    "Trung tâm cần quy trình kiểm tra và rescue tùy protocol.",
    "Không nên xem agonist trigger là hoàn toàn không có rủi ro."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 87, 110);
}
module.exports = { createSlide };
