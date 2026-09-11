#!/usr/bin/env python3
"""Bundle the pinned Three.js modules and game into a directly openable HTML file."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'src'

def mapping(items,importing=False):
    result=[]
    for item in items.split(','):
        parts=item.strip().split(' as ')
        if len(parts)==2:
            a,b=parts
            result.append(f'{a}:{b}' if importing else f'{b}:{a}')
        else: result.append(parts[0])
    return ','.join(result)

def wrap(text,imports=False):
    reexports=[]
    def import_replace(m):
        return 'const {'+mapping(m[1],True)+'}=CORE;'
    text=re.sub(r'import\s*\{([^}]+)\}\s*from\s*[\"\'][^\"\']+[\"\'];?',import_replace,text)
    def reexport(m):
        reexports.extend(p.strip() for p in m[1].split(','));return ''
    text=re.sub(r'export\s*\{([^}]+)\}\s*from\s*[\"\'][^\"\']+[\"\'];?',reexport,text)
    exports=[]
    def final_export(m):
        exports.append(mapping(m[1]));return ''
    text=re.sub(r'export\s*\{([^}]+)\};?',final_export,text)
    assert len(exports)==1, 'Unexpected pinned dependency module structure'
    extras=','.join(f'{k}:CORE.{k}' for k in reexports)
    return '(()=>{\n'+text+'\nreturn {'+exports[0]+(','+extras if extras else '')+'};\n})()'
core=wrap((SRC/'vendor/three.core.min.js').read_text())
three=wrap((SRC/'vendor/three.module.min.js').read_text(),True)
soft=(SRC/'software-renderer.js').read_text().replace("import * as T from './vendor/three.module.min.js';",'const T=THREE;').replace('export class SoftwareRenderer','class SoftwareRenderer')
game=(SRC/'game.js').read_text()
game=re.sub(r'^import .*?;\s*','',game,flags=re.M)
js='(()=>{\nconst CORE='+core+';\nconst THREE='+three+';\n'+soft+'\n'+game+'\n})();'
html=(SRC/'template.html').read_text()
css=(SRC/'style.css').read_text().replace("@import url('data:text/css,');",'')
html=html.replace('<link rel="stylesheet" href="style.css">','<style>'+css+'</style>')
html=html.replace('<script type="module" src="game.js"></script>','<script>'+js.replace('</script','<\\/script')+'</script>')
(ROOT/'index.html').write_text(html)
print(f'Built index.html ({len(html.encode()):,} bytes), no external assets.')
