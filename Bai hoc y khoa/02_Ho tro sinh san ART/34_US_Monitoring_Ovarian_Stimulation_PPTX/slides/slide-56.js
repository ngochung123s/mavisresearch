const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Checklist mỗi lần khám",
  "points": [
    "Số nang theo nhóm kích thước: nhỏ, trung bình, gần trưởng thành.",
    "Nang lớn nhất mỗi bên và tốc độ tăng so với lần trước.",
    "Độ dày/hình thái nội mạc.",
    "Dấu nguy cơ OHSS: nhiều nang, buồng trứng lớn, dịch tự do nếu có.",
    "Kế hoạch tiếp theo: liều, antagonist, ngày hẹn, dự kiến trigger."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569",
  "small": true
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 55, 110);
}
module.exports = { createSlide };
