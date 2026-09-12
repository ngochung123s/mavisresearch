const { renderSlide } = require('./renderer');
const slideData = {
  "type": "matrix",
  "title": "Bảng chọn phác đồ theo nhóm bệnh nhân",
  "rows": [
    [
      "Nguy cơ OHSS",
      "Antagonist",
      "Long agonist routine",
      "Cho phép agonist trigger"
    ],
    [
      "Poor responder",
      "Cá thể hóa",
      "Tăng liều vô hạn",
      "Xem tiền sử response"
    ],
    [
      "Bảo tồn sinh sản",
      "Random start",
      "Chờ đúng ngày nếu gấp",
      "Freeze-all"
    ],
    [
      "Dự kiến freeze-all",
      "PPOS/antagonist",
      "PPOS nếu muốn fresh",
      "Tư vấn trước"
    ],
    [
      "Logistics khó",
      "Fixed antagonist",
      "Flexible quá sát",
      "Giảm lỗi vận hành"
    ],
    [
      "Endometriosis/dính",
      "Cá thể hóa",
      "Bỏ qua đường chọc hút",
      "Ghi access"
    ]
  ],
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 52, 110);
}
module.exports = { createSlide };
