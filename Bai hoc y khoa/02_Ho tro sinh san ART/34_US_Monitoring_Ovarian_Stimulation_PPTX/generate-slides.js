const fs = require('fs');
const path = require('path');
const { slides } = require('./deck-data');

const dir = path.join(__dirname, 'slides');
for (const f of fs.readdirSync(dir)) {
  if (/^slide-\d+\.js$/.test(f)) fs.unlinkSync(path.join(dir, f));
}

slides.forEach((slide, i) => {
  const num = String(i + 1).padStart(2, '0');
  const body = `const { renderSlide } = require('./renderer');\nconst slideData = ${JSON.stringify(slide, null, 2)};\nfunction createSlide(pres, theme) {\n  renderSlide(pres, require('pptxgenjs'), theme, slideData, ${i === 0 ? 'null' : i}, ${slides.length - 1});\n}\nmodule.exports = { createSlide };\n`;
  fs.writeFileSync(path.join(dir, `slide-${num}.js`), body, 'utf8');
});

console.log(`Generated ${slides.length} slide modules.`);
