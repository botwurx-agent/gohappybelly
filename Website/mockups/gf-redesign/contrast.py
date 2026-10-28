def lin(c):
    c = c/255
    return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055)**2.4
def L(hexs):
    h = hexs.lstrip('#')
    r,g,b = (int(h[i:i+2],16) for i in (0,2,4))
    return 0.2126*lin(r) + 0.7152*lin(g) + 0.0722*lin(b)
def ratio(fg,bg):
    a,b = L(fg), L(bg)
    hi,lo = max(a,b), min(a,b)
    return (hi+0.05)/(lo+0.05)

pairs = [
 ("#162E28","#F8FAF8","headings (forest on page bg)","h2/h3"),
 ("#2E4438","#F8FAF8","body copy","17px / weight 300"),
 ("#6A8278","#F8FAF8","secondary + 'is not' column","14px / weight 300"),
 ("#7AAE86","#F8FAF8","eyebrow labels","11px / uppercase"),
 ("#2E4438","#EFF7F1","body on alt bg (drawer)","17px / weight 300"),
 ("#6A8278","#EFF7F1","secondary on alt bg","15px / weight 300"),
 ("#FFFFFF","#C07A5A","button label","terracotta CTA"),
 ("#FFFFFF","#162E28","final CTA heading","white on forest"),
]
print(f"{'ratio':>6}  {'AA 4.5':>6}  {'AA-lg 3.0':>9}   element")
print("-"*78)
for fg,bg,label,note in pairs:
    r = ratio(fg,bg)
    aa  = "PASS" if r>=4.5 else "FAIL"
    aal = "PASS" if r>=3.0 else "FAIL"
    print(f"{r:6.2f}  {aa:>6}  {aal:>9}   {label}  ({note})  {fg} on {bg}")
