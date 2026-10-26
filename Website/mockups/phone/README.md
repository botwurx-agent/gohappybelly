# The phone shot

For `wi_img` in **"What is inside"** on `/gut-foundations`, replacing the
cut-paper digestive-tract diagram. Steve chose the product shot over redrawing
the anatomy, 2026-10-26, working from a reference he supplied: a hand holding a
phone, real UI on screen, blurred warm kitchen behind.

`foundations-phone-b.jpg` is 1600x905, the size that slot already uses.
`scene-b.png` is the raw generated scene with the magenta screen, kept so the UI
can be re-composited without paying for generation again.

## Same chroma-key method as the laptop, one change

The scene is generated (`nano_banana_2_1`, 16:9, 2k, thinking_level high) with
the screen prompted as a flat `#FF00FF` fill. `foundations-phone-ui.html`
renders the real lesson at 450x975 logical, 2x, and `composite-phone.py` warps
it into the key.

**`composite-phone.py` exists because `composite.py` fits the quad wrongly on a
phone.** The laptop screen is a sharp rectangle, so picking corners by the
extremes of `x+y` and `x-y` works. A phone screen has a large corner radius, and
those extremes land *on the arc*, inset from the true corner by roughly `0.29r`.
The warped image then lands short and a magenta rim survives along the bezel.

The fix models the mask as a **rotated rectangle**: sweep the angle in 0.1 degree
steps, keep the one with the smallest axis-aligned bounding box, read the corners
in that frame and rotate them back. That recovers the real rectangle including
the area hidden under the rounded corners. Scene B measured -11.5 degrees.

The paste mask stays the actual magenta shape, dilated 2px, so the rounded
corners are preserved; the warped image overfills it everywhere, which is what
kills the fringe. Overfill drops from the laptop's 1.8% to 0.4%, because the
quad is now correct and a large push would bleed over the bezel.

Residual magenta: 0 pixels.

## What is on the screen, and what is deliberately not

Lesson **01. Understanding Your Gut**, real title, real module eyebrow, real body
copy pulled from lesson 2201324060, including Alina's screen-door take. Momentum
fonts (Fira Sans Extra Condensed and Lato), website palette, which is what the
lesson bodies actually use inline.

**The lesson's own hero image is left off deliberately.** It is
`hero-01-sieve.jpg`, cut paper, the style Alina rejected. Showing it on a sales
page mockup would put rejected art back on the page through the back door. The
shot opens at a text section instead, which also does a better job: it
demonstrates the writing, and the writing is the product.

Two sizing notes. Content must run to the bottom edge; the first pass stopped
two thirds down and read as a half-empty page rather than a scroll position.
And type has to be generous, because the screen is roughly 490x1090 in a
2752-wide frame.

## Flagged, not fixed

**The course lesson bodies are full of cut-paper images.** Lesson 01 alone
carries `hero-01-sieve.jpg` plus three diagrams. This is the same rejection
reaching inside the product, not just the sales pages, and it is bigger than the
52 thumbnails already noted in `Website/IMAGE-DIRECTION.md`. Nobody has scoped
it yet.
