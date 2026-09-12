const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Sai số thường gặp khi đếm AFC",
  "points": [
    "Bỏ sót nang nhỏ khi buồng trứng nhiều nang hoặc hình ảnh kém.",
    "Đếm lặp nang khi không giữ mặt cắt có hệ thống.",
    "Nhầm nang tồn dư/cyst với nang thứ cấp.",
    "Không ghi nhận buồng trứng xa đầu dò, làm người chọc hút bị bất ngờ."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 16, 110);
}
module.exports = { createSlide };
