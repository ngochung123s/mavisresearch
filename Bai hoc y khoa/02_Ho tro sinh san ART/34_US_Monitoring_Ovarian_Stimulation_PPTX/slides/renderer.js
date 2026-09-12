const pptxgen = require('pptxgenjs');

const W = 10;
const H = 5.625;
const FONT = 'Arial';

function addBg(slide, theme) {
  slide.background = { color: theme.bg };
}

function addText(slide, text, x, y, w, h, opts = {}) {
  slide.addText(text || '', {
    x, y, w, h,
    fontFace: opts.fontFace || FONT,
    fontSize: opts.fontSize || 16,
    color: opts.color || '17313A',
    bold: !!opts.bold,
    italic: !!opts.italic,
    margin: opts.margin === undefined ? 0.04 : opts.margin,
    breakLine: opts.breakLine,
    fit: opts.fit || 'shrink',
    valign: opts.valign || 'top',
    align: opts.align || 'left',
    bullet: opts.bullet,
  });
}

function rect(slide, pptx, x, y, w, h, fill, line = fill, radius = false, transparency = 0) {
  slide.addShape(radius ? 'roundRect' : 'rect', {
    x, y, w, h,
    fill: { color: fill, transparency },
    line: { color: line, transparency: line === fill ? 100 : 0, width: 1 },
  });
}

function line(slide, pptx, x, y, w, color, width = 1) {
  slide.addShape('line', { x, y, w, h: 0, line: { color, width } });
}

function title(slide, pptx, theme, text, kicker) {
  if (kicker) addText(slide, kicker.toUpperCase(), 0.45, 0.22, 3.2, 0.22, { fontSize: 7.5, bold: true, color: theme.accent, margin: 0 });
  addText(slide, text, 0.45, 0.45, 8.7, 0.48, { fontSize: 21, bold: true, color: theme.primary, margin: 0 });
  rect(slide, pptx, 0.45, 1.02, 0.55, 0.05, theme.accent);
}

function page(slide, theme, n, total) {
  return;
}

function bullets(slide, items, x, y, w, h, theme, fontSize = 15) {
  const runs = [];
  items.forEach((item, i) => {
    runs.push({ text: item, options: { bullet: { indent: 12 }, breakLine: i < items.length - 1 } });
  });
  slide.addText(runs, { x, y, w, h, fontFace: FONT, fontSize, color: theme.body, margin: 0.05, fit: 'shrink', breakLine: false, valign: 'top' });
}

function footer(slide, theme, source) {
  addText(slide, source || 'Source: bài soạn đã verify PMID', 0.45, 5.12, 8.8, 0.16, { fontSize: 6.6, color: theme.muted, margin: 0 });
}

function renderCover(pres, pptx, theme, d) {
  const s = pres.addSlide(); addBg(s, theme);
  rect(s, pptx, 0, 0, 3.05, H, theme.primary);
  rect(s, pptx, 3.05, 0, 0.08, H, theme.accent);
  for (let i = 0; i < 8; i++) rect(s, pptx, 7.5 + (i % 4) * 0.45, 0.55 + Math.floor(i / 4) * 0.35, 0.07, 0.07, theme.light);
  addText(s, d.kicker || 'ART / IVF-ICSI', 0.55, 0.62, 2.0, 0.25, { fontSize: 11, bold: true, color: theme.light, margin: 0 });
  addText(s, d.title, 0.55, 1.25, 2.35, 2.3, { fontSize: 30, bold: true, color: 'FFFFFF', margin: 0 });
  addText(s, d.subtitle, 3.55, 1.55, 5.7, 0.95, { fontSize: 23, bold: true, color: theme.primary, margin: 0 });
  addText(s, d.note, 3.55, 2.85, 5.55, 0.8, { fontSize: 16, color: theme.body, margin: 0 });
  addText(s, d.author || 'Bác sĩ Ngọc Hưng', 3.55, 4.72, 3.3, 0.22, { fontSize: 10, bold: true, color: theme.accent, margin: 0 });
  addText(s, d.date || '2026-07-03', 8.55, 4.72, 0.9, 0.2, { fontSize: 9, color: theme.muted, align: 'right', margin: 0 });
}

function renderToc(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme); title(s, pptx, theme, d.title, 'map');
  const items = d.items || [];
  items.forEach((it, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.55 + col * 4.75, y = 1.35 + row * 0.82;
    rect(s, pptx, x, y, 4.15, 0.58, i % 2 ? 'F5FBFA' : 'ECF7F5', theme.border, true);
    addText(s, String(i + 1).padStart(2, '0'), x + 0.18, y + 0.13, 0.45, 0.18, { fontSize: 14, bold: true, color: theme.accent, margin: 0 });
    addText(s, it, x + 0.76, y + 0.1, 3.05, 0.24, { fontSize: 12.5, bold: true, color: theme.primary, margin: 0 });
  });
  footer(s, theme, d.source); page(s, theme, n, total);
}

function renderSection(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme);
  rect(s, pptx, 0, 0, W, H, theme.primary);
  rect(s, pptx, 0, 0, 2.15, H, theme.accent);
  addText(s, d.number || '', 0.25, 1.55, 1.65, 1.15, { fontSize: 64, bold: true, color: 'FFFFFF', align: 'center', margin: 0 });
  addText(s, d.title, 2.65, 1.58, 6.6, 0.75, { fontSize: 31, bold: true, color: 'FFFFFF', margin: 0 });
  addText(s, d.subtitle || '', 2.68, 2.62, 5.95, 0.6, { fontSize: 17, color: theme.light, margin: 0 });
  page(s, theme, n, total);
}

function renderBullets(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme); title(s, pptx, theme, d.title, d.kicker);
  if (d.lead) addText(s, d.lead, 0.6, 1.25, 8.75, 0.4, { fontSize: 17, bold: true, color: theme.primary, margin: 0 });
  rect(s, pptx, 0.6, d.lead ? 1.83 : 1.35, 8.75, d.lead ? 2.95 : 3.42, 'FFFFFF', theme.border, true);
  bullets(s, d.points || [], 0.86, d.lead ? 2.08 : 1.64, 8.15, d.lead ? 2.4 : 2.85, theme, d.small ? 12.4 : 14.4);
  if (d.pearl) { rect(s, pptx, 0.6, 4.72, 8.75, 0.32, theme.light, theme.light, true); addText(s, d.pearl, 0.78, 4.78, 8.35, 0.16, { fontSize: 9.2, bold: true, color: theme.accent, margin: 0 }); }
  footer(s, theme, d.source); page(s, theme, n, total);
}

function renderCompare(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme); title(s, pptx, theme, d.title, d.kicker);
  const cols = d.columns || [];
  cols.slice(0, 3).forEach((c, i) => {
    const w = cols.length === 2 ? 4.15 : 2.75;
    const x = cols.length === 2 ? 0.7 + i * 4.55 : 0.65 + i * 3.05;
    rect(s, pptx, x, 1.35, w, 3.55, i === 0 ? 'ECF7F5' : i === 1 ? 'FFF7E8' : 'F8F5FF', theme.border, true);
    addText(s, c.title, x + 0.18, 1.52, w - 0.36, 0.32, { fontSize: 15.5, bold: true, color: theme.primary, margin: 0 });
    bullets(s, c.points || [], x + 0.25, 2.02, w - 0.48, 2.45, theme, cols.length === 2 ? 12.6 : 11.1);
  });
  footer(s, theme, d.source); page(s, theme, n, total);
}

function renderMatrix(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme); title(s, pptx, theme, d.title, d.kicker);
  const rows = d.rows || [];
  const x = 0.55, y = 1.3, colW = [1.8, 2.55, 2.55, 2.0];
  ['Mục', 'Dự đoán tốt', 'Không nên suy ra', 'Ghi nhớ'].forEach((h, i) => {
    const xx = x + colW.slice(0, i).reduce((a,b)=>a+b,0);
    rect(s, pptx, xx, y, colW[i], 0.36, theme.primary, theme.primary);
    addText(s, h, xx + 0.06, y + 0.08, colW[i] - 0.12, 0.13, { fontSize: 8.2, bold: true, color: 'FFFFFF', margin: 0 });
  });
  rows.slice(0, 7).forEach((r, ri) => {
    const yy = y + 0.36 + ri * 0.47;
    [r[0], r[1], r[2], r[3]].forEach((cell, ci) => {
      const xx = x + colW.slice(0, ci).reduce((a,b)=>a+b,0);
      rect(s, pptx, xx, yy, colW[ci], 0.47, ri % 2 ? 'FFFFFF' : 'F6FBFA', theme.border);
      addText(s, cell, xx + 0.06, yy + 0.07, colW[ci] - 0.12, 0.26, { fontSize: 8.0, color: ci === 0 ? theme.primary : theme.body, bold: ci === 0, margin: 0 });
    });
  });
  footer(s, theme, d.source); page(s, theme, n, total);
}

function renderTimeline(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme); title(s, pptx, theme, d.title, d.kicker);
  const steps = d.steps || [];
  line(s, pptx, 0.85, 2.45, 8.25, theme.border, 2);
  steps.slice(0, 6).forEach((st, i) => {
    const x = 0.75 + i * 1.58;
    rect(s, pptx, x, 2.18, 0.52, 0.52, i % 2 ? theme.light : theme.accent, i % 2 ? theme.light : theme.accent, true);
    addText(s, String(i + 1), x, 2.31, 0.52, 0.12, { fontSize: 11, bold: true, color: i % 2 ? theme.accent : 'FFFFFF', align: 'center', margin: 0 });
    addText(s, st.label, x - 0.22, 1.52, 0.98, 0.34, { fontSize: 10.2, bold: true, color: theme.primary, align: 'center', margin: 0 });
    addText(s, st.text, x - 0.35, 2.92, 1.22, 0.68, { fontSize: 8.7, color: theme.body, align: 'center', margin: 0 });
  });
  if (d.note) addText(s, d.note, 0.8, 4.35, 8.1, 0.35, { fontSize: 12.4, bold: true, color: theme.accent, align: 'center', margin: 0 });
  footer(s, theme, d.source); page(s, theme, n, total);
}

function renderDecision(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme); title(s, pptx, theme, d.title, d.kicker);
  addText(s, d.question, 0.7, 1.35, 8.5, 0.35, { fontSize: 17.5, bold: true, color: theme.primary, align: 'center', margin: 0 });
  const items = d.options || [];
  items.slice(0, 4).forEach((op, i) => {
    const x = 0.75 + (i % 2) * 4.35, y = 2.02 + Math.floor(i / 2) * 1.15;
    rect(s, pptx, x, y, 3.95, 0.82, op.level === 'warn' ? 'FFF4DE' : op.level === 'danger' ? 'FDECEC' : 'ECF7F5', theme.border, true);
    addText(s, op.title, x + 0.18, y + 0.12, 3.55, 0.2, { fontSize: 11.3, bold: true, color: op.level === 'danger' ? theme.danger : theme.primary, margin: 0 });
    addText(s, op.text, x + 0.18, y + 0.37, 3.45, 0.3, { fontSize: 9.3, color: theme.body, margin: 0 });
  });
  if (d.answer) { rect(s, pptx, 1.4, 4.52, 7.2, 0.37, theme.primary, theme.primary, true); addText(s, d.answer, 1.62, 4.59, 6.76, 0.16, { fontSize: 9.8, bold: true, color: 'FFFFFF', align: 'center', margin: 0 }); }
  footer(s, theme, d.source); page(s, theme, n, total);
}

function renderReferences(pres, pptx, theme, d, n, total) {
  const s = pres.addSlide(); addBg(s, theme); title(s, pptx, theme, d.title, 'references');
  (d.refs || []).forEach((r, i) => {
    rect(s, pptx, 0.75, 1.28 + i * 0.57, 8.5, 0.42, i % 2 ? 'FFFFFF' : 'F6FBFA', theme.border, true);
    addText(s, `${i + 1}. ${r}`, 0.95, 1.40 + i * 0.57, 8.1, 0.16, { fontSize: 9.3, color: theme.body, margin: 0 });
  });
  page(s, theme, n, total);
}

function renderSlide(pres, pptx, theme, d, n, total) {
  if (d.type === 'cover') return renderCover(pres, pptx, theme, d);
  if (d.type === 'toc') return renderToc(pres, pptx, theme, d, n, total);
  if (d.type === 'section') return renderSection(pres, pptx, theme, d, n, total);
  if (d.type === 'compare') return renderCompare(pres, pptx, theme, d, n, total);
  if (d.type === 'matrix') return renderMatrix(pres, pptx, theme, d, n, total);
  if (d.type === 'timeline') return renderTimeline(pres, pptx, theme, d, n, total);
  if (d.type === 'decision') return renderDecision(pres, pptx, theme, d, n, total);
  if (d.type === 'references') return renderReferences(pres, pptx, theme, d, n, total);
  return renderBullets(pres, pptx, theme, d, n, total);
}

module.exports = { renderSlide };
