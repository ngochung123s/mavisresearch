const { renderSlide } = require('./renderer');
const slideData = {
  "type": "decision",
  "title": "Nang tồn dư trước chu kỳ",
  "question": "Có nang lớn trước khi bắt đầu FSH thì nghĩ gì?",
  "options": [
    {
      "title": "Không vội kích thích",
      "text": "Cần phân biệt nang chức năng, cyst tồn dư hoặc nang bệnh lý.",
      "level": "warn"
    },
    {
      "title": "Đọc hormone nếu cần",
      "text": "E2/progesterone giúp biết nang có hoạt động hay không.",
      "level": "ok"
    },
    {
      "title": "Cân nhắc trì hoãn",
      "text": "Nếu ảnh hưởng đáp ứng hoặc làm sai baseline.",
      "level": "warn"
    },
    {
      "title": "Chọc hút chọn lọc",
      "text": "Chỉ cân nhắc khi nang lớn/tồn tại và có lý do rõ.",
      "level": "ok"
    }
  ],
  "answer": "Không phải nang nào cũng cần chọc hút; quyết định dựa vào kích thước, kéo dài, hormone và kế hoạch chu kỳ.",
  "source": "Source: bản soạn siêu âm theo dõi KTBT, PMID 32395637; 41732035; 33280722; 21558332; 26597569"
};
function createSlide(pres, theme) {
  renderSlide(pres, require('pptxgenjs'), theme, slideData, 24, 110);
}
module.exports = { createSlide };
