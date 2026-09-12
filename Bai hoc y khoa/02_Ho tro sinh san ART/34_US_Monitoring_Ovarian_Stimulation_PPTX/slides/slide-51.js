const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Random start: chỉ định chọn lọc",
  "points": [
    "Bắt đầu kích thích không nhất thiết ngày 2-3 nếu có lý do cần rút ngắn thời gian.",
    "Hữu ích nhất trong bảo tồn sinh sản trước điều trị gonadotoxic.",
    "Cần dự kiến freeze-all vì nội mạc không đồng bộ.",
    "Không phải lựa chọn routine cho mọi bệnh nhân IVF thông thường."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 50, 110);
}
module.exports = { createSlide };
