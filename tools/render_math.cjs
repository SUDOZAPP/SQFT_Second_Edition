const fs = require('fs');
const path = require('path');
const katex = require(path.join(__dirname, '../assets/katex/katex.js'));
const expressions = JSON.parse(fs.readFileSync(0, 'utf8'));
const escapeAttribute = value => String(value).replace(/&/g, '&amp;')
  .replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const results = expressions.map((item, index) => {
  try {
    const rendered = katex.renderToString(item.tex, {
      displayMode: item.display, throwOnError: true, trust: false,
      strict: 'ignore', output: 'html'
    });
    // One visual representation only. Some previews expose both HTML and MathML.
    // Keep a nonvisual TeX label; structured MathML is intentionally not emitted.
    return {html: rendered.replace('<span class="katex">',
      `<span class="katex" role="math" aria-label="${escapeAttribute(item.tex)}">`)};
  } catch(error) { return {error: String(error), index, tex: item.tex}; }
});
process.stdout.write(JSON.stringify({version: katex.version, results}));
