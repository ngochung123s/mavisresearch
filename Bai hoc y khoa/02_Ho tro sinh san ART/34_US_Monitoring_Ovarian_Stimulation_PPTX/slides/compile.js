const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');

const pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.author = 'Bác sĩ Ngọc Hưng';
pres.company = 'mavisresearch';
pres.subject = 'Siêu âm theo dõi kích thích buồng trứng';
pres.title = 'Siêu âm theo dõi quá trình kích thích buồng trứng';
pres.lang = 'vi-VN';
pres.theme = {
  headFontFace: 'Arial',
  bodyFontFace: 'Arial',
  lang: 'vi-VN'
};
pres.defineLayout({ name: 'LAYOUT_16x9', width: 10, height: 5.625 });

const theme = {
  primary: '17313A',
  secondary: '315D63',
  accent: '00977A',
  light: 'DDF3EE',
  bg: 'F7FCFB',
  body: '243B40',
  muted: '6F878A',
  border: 'CFE5E1',
  danger: 'C02020'
};

const files = fs.readdirSync(__dirname)
  .filter(f => /^slide-\d+\.js$/.test(f))
  .sort((a, b) => Number(a.match(/\d+/)[0]) - Number(b.match(/\d+/)[0]));
for (const f of files) require(path.join(__dirname, f)).createSlide(pres, theme);

const out = path.join(__dirname, 'output', 'Sieu_am_theo_doi_kich_thich_buong_trung_PPTXGenJS_2026-07-03.pptx');
pres.writeFile({ fileName: out }).then(() => console.log(`Saved ${out}`));
