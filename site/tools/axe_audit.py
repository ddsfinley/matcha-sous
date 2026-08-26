#!/usr/bin/env python3
"""Real WCAG 2.1/2.2 A/AA audit via axe-core against every page in /site,
rendered with Playwright rather than parsed as static text (so CSS-computed
contrast, lazy images, etc. are evaluated as a browser actually sees them).

Setup (once):
    npm install axe-core          # run from anywhere; adjust AXE_JS below
                                    # to wherever node_modules lands, or run
                                    # it inside this tools/ dir and leave the
                                    # default path as-is.

Usage:
    python3 site/tools/axe_audit.py

Prints a summary grouped by rule; writes full per-page violation detail to
axe_results.json next to this script for follow-up (exact selectors,
computed colors, failure summaries).

This only catches what automated tooling CAN catch - roughly half of real
WCAG issues per axe-core's own documentation. It found one thing on this
site (color-contrast) across every page in one pass. It did NOT and cannot
find the missing skip link or the unpausable autoplay video - those were
found by knowing WCAG 2.4.1 and 2.2.2 exist and checking for them by hand.
A clean run of this script is a floor, not a certificate - see README
"Accessibility" for what else that implies.
"""
import json, glob, os, subprocess, sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'


def find_axe_js():
    candidates = [
        os.path.join(HERE, 'node_modules', 'axe-core', 'axe.min.js'),
        os.path.join(ROOT, 'node_modules', 'axe-core', 'axe.min.js'),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    print("axe-core not found. Run: cd site/tools && npm install axe-core", file=sys.stderr)
    sys.exit(1)


def main():
    axe_js = open(find_axe_js()).read()
    pages = sorted(glob.glob(ROOT + '/*.html') + glob.glob(ROOT + '/journal/*.html'))

    results = {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=['--no-sandbox'])
        for path in pages:
            rel = os.path.relpath(path, ROOT)
            pg = b.new_page(viewport={'width': 1280, 'height': 900})
            pg.goto('file://' + path)
            pg.wait_for_timeout(500)
            pg.evaluate("()=>document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')")
            pg.wait_for_timeout(300)
            pg.add_script_tag(content=axe_js)
            axe_result = pg.evaluate("""async () => {
                return await axe.run(document, {
                    runOnly: { type: 'tag', values: ['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa'] }
                });
            }""")
            results[rel] = axe_result['violations']
            pg.close()
        b.close()

    out = os.path.join(HERE, 'axe_results.json')
    json.dump(results, open(out, 'w'), indent=2)

    total = 0
    by_rule = {}
    for page, viols in results.items():
        for v in viols:
            total += len(v['nodes'])
            d = by_rule.setdefault(v['id'], {'impact': v['impact'], 'help': v['help'], 'count': 0, 'pages': set()})
            d['count'] += len(v['nodes'])
            d['pages'].add(page)

    print(f"{total} total violating elements across {len(pages)} pages")
    print(f"(full detail written to {out})\n")
    for rule, d in sorted(by_rule.items(), key=lambda kv: -kv[1]['count']):
        print(f"[{d['impact']:>8}] {rule:32s} x{d['count']:<4} ({len(d['pages'])} pages) - {d['help']}")


if __name__ == '__main__':
    main()
