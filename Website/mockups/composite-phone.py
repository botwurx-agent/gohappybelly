"""Composite a screenshot into a chroma-keyed PHONE screen.

Differs from composite.py in how the quad is found. The laptop screen is a sharp
rectangle, so extreme-of-(x+y) corner picking works. A phone screen has a large
corner radius: those extremes land ON THE ARC, inset from the true corner by
about 0.29r, so the warped image lands short and the bezel shows a magenta rim.

Here the mask is modelled as a ROTATED RECTANGLE instead. Sweep the angle,
take the one with the smallest axis-aligned bounding box, read the corners in
that rotated frame, rotate them back. That recovers the true rectangle,
including the area hidden under the rounded corners.

The paste mask stays the ACTUAL magenta shape (dilated 2px), so the rounded
corners are preserved. The warped image overfills it everywhere, which is what
kills the fringe.

Run with python3.13 — the system python3 has a broken PIL in this container.
"""
from PIL import Image, ImageFilter
import numpy as np, sys

scene_path, out_path, shot_path = sys.argv[1], sys.argv[2], sys.argv[3]
scene = Image.open(scene_path).convert('RGB')
shot  = Image.open(shot_path).convert('RGB')
W, H = scene.size

a = np.array(scene).astype(int)
R, G, B = a[:, :, 0], a[:, :, 1], a[:, :, 2]
mask = (R > 140) & (B > 140) & (G < 130) & ((R - G) > 60) & ((B - G) > 60)
ys, xs = np.nonzero(mask)
pts = np.stack([xs, ys], axis=1).astype(float)

best = None
for deg in np.arange(-20.0, 20.0, 0.1):
    t = np.radians(deg)
    c, s = np.cos(t), np.sin(t)
    rot = pts @ np.array([[c, -s], [s, c]])
    w = rot[:, 0].max() - rot[:, 0].min()
    h = rot[:, 1].max() - rot[:, 1].min()
    if best is None or w * h < best[0]:
        best = (w * h, deg, rot[:, 0].min(), rot[:, 0].max(), rot[:, 1].min(), rot[:, 1].max())

_, deg, x0, x1, y0, y1 = best
t = np.radians(deg)
c, s = np.cos(t), np.sin(t)
back = np.array([[c, s], [-s, c]])          # inverse rotation
corners = np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]]) @ back
TL, TR, BR, BL = [tuple(p) for p in corners]
print(f'angle {deg:+.1f} deg  corners', [(round(p[0]), round(p[1])) for p in corners])

def coeffs(dst, src):
    M = []
    for (dx, dy), (sx, sy) in zip(dst, src):
        M.append([dx, dy, 1, 0, 0, 0, -sx * dx, -sx * dy])
        M.append([0, 0, 0, dx, dy, 1, -sy * dx, -sy * dy])
    return np.linalg.solve(np.array(M, dtype=float),
                           np.array([v for p in src for v in p], dtype=float))

sw, sh = shot.size
cx = sum(p[0] for p in (TL, TR, BR, BL)) / 4.0
cy = sum(p[1] for p in (TL, TR, BR, BL)) / 4.0
def out_(p, k=1.004):                        # a hair of overfill, no more
    return (p[0] + (p[0] - cx) * (k - 1), p[1] + (p[1] - cy) * (k - 1))
quad = [out_(p) for p in (TL, TR, BR, BL)]
cf = coeffs(quad, [(0, 0), (sw, 0), (sw, sh), (0, sh)])
warped = shot.transform((W, H), Image.PERSPECTIVE, cf, Image.BICUBIC)

m = Image.fromarray((mask * 255).astype('uint8'), 'L')
m = m.filter(ImageFilter.MaxFilter(5))       # 2px, keeps the corner radius
out = scene.copy()
out.paste(warped, (0, 0), m)

# faint diagonal sheen so the screen reads as glass, not a decal
yy, xx = np.mgrid[0:H, 0:W]
gp = np.clip(255 * 0.040 * (1.0 - ((xx * 0.7 + yy * 0.9) / (W * 0.7 + H * 0.9))), 0, 255)
gl = np.array(Image.fromarray(gp.astype('uint8'), 'L'))
sheen = Image.composite(Image.new('RGB', (W, H), (255, 255, 255)), out,
                        Image.fromarray((gl * mask).astype('uint8'), 'L'))
out = Image.blend(out, sheen, 0.5)
out.save(out_path)
print('saved', out_path, out.size)
