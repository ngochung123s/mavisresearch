const { renderSlide } = require('./renderer');
const slideData = {
  "type": "bullets",
  "title": "Endometrioma trước kích thích",
  "points": [
    "Ghi kích thước, bên, số lượng và quan hệ với đường chọc hút.",
    "Không nhất thiết chọc hút/phẫu thuật nếu không ảnh hưởng tiếp cận noãn.",
    "Cần cân bằng nguy cơ giảm dự trữ sau can thiệp với nguy cơ nhiễm/khó chọc hút.",
    "Tử cung ngả sau cố định và đau khi ấn gợi ý dính/endometriosis."
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 25, 110);
}
module.exports = { createSlide };
