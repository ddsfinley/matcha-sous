"""Report headings whose last visual line holds a single word."""
from playwright.sync_api import sync_playwright

EXE = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PAGES = ["index.html", "about.html", "faq.html", "how-to-use.html", "wholesale.html",
         "stockists.html", "journal/index.html", "journal/how-to-make-a-matcha-latte.html",
         "journal/matcha-without-a-whisk.html", "journal/how-to-choose-matcha.html",
         "journal/usucha-vs-koicha.html"]
WIDTHS = [1440, 1280, 1024, 820, 700, 560, 430, 390, 360]

JS = """() => {
  const out = [];
  document.querySelectorAll('h1, h2, h3').forEach(h => {
    const r = document.createRange();
    r.selectNodeContents(h);
    const rects = [...r.getClientRects()].filter(x => x.width > 0);
    if (rects.length < 2) return;                      // single line, fine
    const lastTop = rects[rects.length - 1].top;
    // words whose own rect starts on the final line
    let words = 0;
    h.textContent.trim().split(/\\s+/).forEach(() => {});
    const walker = document.createTreeWalker(h, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
      const txt = node.textContent;
      let i = 0;
      const re = /\\S+/g; let m;
      while ((m = re.exec(txt))) {
        const rr = document.createRange();
        rr.setStart(node, m.index); rr.setEnd(node, m.index + m[0].length);
        const b = rr.getBoundingClientRect();
        if (b.width && Math.abs(b.top - lastTop) < 2) words++;
      }
    }
    if (words === 1) out.push(h.textContent.trim().replace(/\\s+/g, ' '));
  });
  return out;
}"""

with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=EXE, args=["--no-sandbox"])
    total = 0
    for page in PAGES:
        for w in WIDTHS:
            pg = b.new_page(viewport={"width": w, "height": 900})
            pg.goto(f"http://localhost:8899/{page}")
            pg.wait_for_timeout(350)
            bad = pg.evaluate(JS)
            for t in bad:
                total += 1
                print(f"  {page:40} {w:>5}px  «{t[:60]}»")
            pg.close()
    print(f"\norphaned headings: {total}")
    b.close()
