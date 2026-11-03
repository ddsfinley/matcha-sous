"""Copy the static site to a publish folder, leaving out internal files and
stripping HTML comments. Usage: build_public.py <source dir> <output dir>"""
import pathlib, re, shutil, sys

PRIVATE = {'README.md', 'proposals', 'tools', 'node_modules', 'axe_results.json'}

src, out = map(pathlib.Path, sys.argv[1:3])
if out.exists():
    shutil.rmtree(out)
shutil.copytree(src, out, ignore=lambda d, names: [n for n in names if n in PRIVATE])

for f in out.rglob('*.html'):
    s = f.read_text(encoding='utf-8')
    f.write_text(re.sub(r'<!--.*?-->\n?', '', s, flags=re.S), encoding='utf-8')

for p in sorted(out.iterdir()):
    print(p.name)
