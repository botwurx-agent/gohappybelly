from PIL import Image, ImageFilter
import numpy as np, sys

scene_path, out_path = sys.argv[1], sys.argv[2]
scene = Image.open(scene_path).convert('RGB')
shot  = Image.open(sys.argv[3] if len(sys.argv)>3 else 'course-ui-v2.png').convert('RGB')
W,H = scene.size

a = np.array(scene).astype(int)
R,G,B = a[:,:,0], a[:,:,1], a[:,:,2]
mask = (R>140)&(B>140)&(G<130)&((R-G)>60)&((B-G)>60)
ys,xs = np.nonzero(mask)
s, d = xs+ys, xs-ys
TL = (int(xs[np.argmin(s)]), int(ys[np.argmin(s)]))
BR = (int(xs[np.argmax(s)]), int(ys[np.argmax(s)]))
TR = (int(xs[np.argmax(d)]), int(ys[np.argmax(d)]))
BL = (int(xs[np.argmin(d)]), int(ys[np.argmin(d)]))
print('corners', TL, TR, BR, BL)

def coeffs(dst, src):
    # maps destination quad -> source rectangle, which is what PIL.PERSPECTIVE wants
    M=[]; 
    for (dx,dy),(sx,sy) in zip(dst,src):
        M.append([dx,dy,1,0,0,0,-sx*dx,-sx*dy])
        M.append([0,0,0,dx,dy,1,-sy*dx,-sy*dy])
    A=np.array(M,dtype=float)
    b=np.array([c for p in src for c in p],dtype=float)
    return np.linalg.solve(A,b)

sw,sh = shot.size
# push the quad out from its centre so the screenshot bleeds past the bezel line
cx = sum(p[0] for p in (TL,TR,BR,BL))/4.0
cy = sum(p[1] for p in (TL,TR,BR,BL))/4.0
def out_(p, k=1.018): return (p[0]+(p[0]-cx)*(k-1), p[1]+(p[1]-cy)*(k-1))
TL,TR,BR,BL = out_(TL), out_(TR), out_(BR), out_(BL)
c = coeffs([TL,TR,BR,BL], [(0,0),(sw,0),(sw,sh),(0,sh)])
warped = shot.transform((W,H), Image.PERSPECTIVE, c, Image.BICUBIC)

m = Image.fromarray((mask*255).astype('uint8'), 'L')
# pull the key in by a pixel so no magenta fringe survives the bicubic edge
# dilate: the warped shot must OVERFILL the key, or the bicubic edge
# leaves a magenta ring around the screen
for _ in range(2): m = m.filter(ImageFilter.MaxFilter(5))

out = scene.copy()
out.paste(warped, (0,0), m)

# a faint diagonal sheen so the screen reads as glass rather than a flat decal
gl = Image.new('L',(W,H),0)
gp = np.zeros((H,W),dtype=float)
yy,xx = np.mgrid[0:H,0:W]
gp = np.clip(255*0.055*(1.0-((xx*0.7+yy*0.9)/(W*0.7+H*0.9))),0,255)
gl = Image.fromarray(gp.astype('uint8'),'L')
white = Image.new('RGB',(W,H),(255,255,255))
sheen = Image.composite(white, out, Image.fromarray((np.array(gl)*(mask)).astype('uint8'),'L'))
out = Image.blend(out, sheen, 0.5)
out.save(out_path)
print('saved', out_path, out.size)
