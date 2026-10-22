import re, os, glob, json, html as H

SAGE = 'border-left:3px solid #7AAE86; background:#EAF5EC; padding:16px 20px; margin:22px 0;'
REFL = 'border:1px solid #C8DDD0; background:#F8FAF8; padding:18px 22px; margin:26px 0;'
TD   = 'border:1px solid #DDD8CE; padding:10px 12px; vertical-align:top;'
TH   = 'border:1px solid #DDD8CE; background:#F5F1EA; padding:10px 12px; text-align:left; font-weight:bold; vertical-align:top;'

def inline(t):
    t = H.escape(t, quote=False)
    t = t.replace('&lt;br /&gt;', '<br />')
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
               r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t

def table(rows):
    cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
    head, body = cells[0], cells[2:]
    w = max(140 * len(head), 420)
    out = [f'<div style="overflow-x:auto; margin:16px 0 22px 0;">',
           f'<table style="width:100%; min-width:{w}px; border-collapse:collapse; font-size:15px;">', '<tbody>', '<tr>']
    out += [f'<td style="{TH}">{inline(c)}</td>' for c in head]
    out.append('</tr>')
    for r in body:
        out.append('<tr>' + ''.join(f'<td style="{TD}">{inline(c)}</td>' for c in r) + '</tr>')
    out += ['</tbody>', '</table>', '</div>']
    return '\n'.join(out)

def blocks(md):
    """Split into (kind, lines) blocks."""
    out, buf, kind = [], [], None
    def flush():
        nonlocal buf, kind
        if buf: out.append((kind, buf)); buf = []
        kind = None
    for line in md.split('\n'):
        s = line.rstrip()
        if not s.strip():
            flush(); continue
        k = ('quote' if s.startswith('> ') or s == '>' else
             'table' if s.lstrip().startswith('|') else
             'ul'    if re.match(r'^\s*[-*] ', s) else
             'ol'    if re.match(r'^\s*\d+\. ', s) else
             'h'     if s.startswith('#') else 'p')
        if k != kind: flush(); kind = k
        buf.append(s)
    flush()
    return out

def render(bs):
    out = []
    for kind, lines in bs:
        if kind == 'h':
            lvl = len(lines[0]) - len(lines[0].lstrip('#'))
            txt = lines[0].lstrip('#').strip()
            out.append(f'<h3>{inline(txt)}</h3>' if lvl <= 3 else f'<h4>{inline(txt)}</h4>')
        elif kind == 'table':
            out.append(table(lines))
        elif kind == 'ul':
            items = [re.sub(r'^\s*[-*] ', '', l) for l in lines]
            out.append('<ul>\n' + '\n'.join(f'<li>{inline(i)}</li>' for i in items) + '\n</ul>')
        elif kind == 'ol':
            items = [re.sub(r'^\s*\d+\. ', '', l) for l in lines]
            out.append('<ol>\n' + '\n'.join(f'<li>{inline(i)}</li>' for i in items) + '\n</ol>')
        elif kind == 'quote':
            inner = [re.sub(r'^> ?', '', l) for l in lines]
            is_refl = any(l.strip().lower().startswith('### reflection') for l in inner)
            body = [l for l in inner if not l.strip().startswith('###')]
            style = REFL if is_refl else SAGE
            ps = []
            if is_refl:
                ps.append('<p style="margin:0 0 8px 0; font-size:12px; letter-spacing:0.14em; '
                          'text-transform:uppercase; color:#6A8278;"><strong>Before you move on</strong></p>')
            # regroup inner paragraphs on blank lines
            para, chunks = [], []
            for l in body + ['']:
                if l.strip(): para.append(l)
                elif para: chunks.append(' '.join(para)); para = []
            for i, c in enumerate(chunks):
                m = '0' if i == len(chunks) - 1 else '0 0 10px 0'
                ps.append(f'<p style="margin:{m};">{inline(c)}</p>')
            out.append(f'<div style="{style}">\n' + '\n'.join(ps) + '\n</div>')
        else:
            out.append(f'<p>{inline(" ".join(lines))}</p>')
    return '\n'.join(out)

def strip_meta(md):
    md = md.split('### What changed from FDN')[0].split('### Notes')[0]
    keep, skipping_note = [], False
    for l in md.split('\n'):
        if l.startswith(('**FDN title:**', '**FDN source:**', '**New title:**',
                         '**Avatars:**', '**Pattern:**')):
            continue
        if l.startswith('> **This is the module') or l.startswith('> **Retitled') or \
           l.startswith('> Maps directly onto') or l.startswith('> The cleanest file'):
            skipping_note = True; continue
        if skipping_note:
            if l.startswith('>') or not l.strip(): continue
            skipping_note = False
        if l.startswith('# '): continue
        if l.strip() == '---': continue
        keep.append(l)
    # anything quoted before the first ## heading is an editorial note to Steve,
    # not lesson copy. Leaked the "$147 upsell" note into module 08 once already.
    out, seen_heading = [], False
    for l in keep:
        if l.startswith('## '): seen_heading = True
        if not seen_heading and l.lstrip().startswith('>'): continue
        out.append(l)
    return '\n'.join(out)

ORDER = ['00-welcome','01-understanding-your-gut','02-whole-body','03-the-five-patterns',
         '04-daily-habits','05-nutrition-foundations','06-gut-brain','07-gut-liver',
         '08-putting-it-together','B1-midlife','B2-high-stress','B3-system-on-alert']

os.makedirs('html', exist_ok=True)
index = []
for name in ORDER:
    md = open(f'modules/{name}.md').read()
    title = md.split('\n')[0].lstrip('# ').strip()
    body = render(blocks(strip_meta(md)))
    open(f'html/{name}.html','w').write(body)
    index.append({'file': name, 'title': title, 'chars': len(body)})
print(json.dumps(index, indent=1))
