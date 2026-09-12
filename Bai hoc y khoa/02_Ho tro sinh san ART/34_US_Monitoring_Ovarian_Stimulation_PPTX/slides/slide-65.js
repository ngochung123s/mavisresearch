const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Buồng trứng nhiều nang/PCOS: nguy cơ đếm sai",
  "points": [
    "Nhiều nang nhỏ làm tăng nguy cơ bỏ sót hoặc đếm lặp.",
    "Cần quét có hệ thống và chia nhóm kích thước.",
    "Đây cũng là nhóm cần cảnh giác OHSS từ sớm.",
    "Không nên chỉ dựa vào E2 hoặc chỉ dựa vào một mặt cắt siêu âm."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 64, 110);
}
module.exports = { createSlide };
