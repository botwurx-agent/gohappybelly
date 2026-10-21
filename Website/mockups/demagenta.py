from PIL import Image, ImageFilter
import numpy as np, sys

scene_path, comp_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
scene = np.array(Image.open(scene_path).convert('RGB')).astype(int)
R,G,B = scene[:,:,0], scene[:,:,1], scene[:,:,2]
key = (R>140)&(B>140)&(G<130)&((R-G)>60)&((B-G)>60)
km = Image.fromarray((key*255).astype('uint8'),'L')
for _ in range(3): km = km.filter(ImageFilter.MaxFilter(5))
protect = np.array(km) > 0

comp = np.array(Image.open(comp_path).convert('RGB')).astype(float)
r,g,b = comp[:,:,0], comp[:,:,1], comp[:,:,2]
cast = np.clip(np.minimum(r,b) - g, 0, None)
k = 0.9
r2 = r - k*cast
b2 = b - k*cast
sel = ~protect
comp[:,:,0] = np.where(sel, r2, r)
comp[:,:,2] = np.where(sel, b2, b)
out = Image.fromarray(np.clip(comp,0,255).astype('uint8'),'RGB')
out.save(out_path)
print('saved', out_path, out.size, 'cast px:', int((( cast>8) & sel).sum()))
