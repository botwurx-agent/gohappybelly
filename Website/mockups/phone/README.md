# The phone shot

For `wi_img` in **"What is inside"** on `/gut-foundations`, replacing the
cut-paper digestive-tract diagram. Steve chose the product shot over redrawing
the anatomy, 2026-10-26, working from a reference he supplied: a hand holding a
phone, real UI on screen, blurred warm kitchen behind.

`foundations-phone.jpg` is 1600x905, the size that slot already uses.
`scene-b.png` is the raw generated scene with the magenta screen and
`img0678.png` is Steve's screenshot, both kept so the shot can be rebuilt
without paying for generation again.

## Same chroma-key method as the laptop, one change

The scene is generated (`nano_banana_2_1`, 16:9, 2k, thinking_level high) with
the screen prompted as a flat `#FF00FF` fill. `composite-phone.py` warps
**Steve's real iPhone screenshot** (`img0678.png`, 1290x2796) into the key.

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

## The first attempt was drawn, and it was wrong

Before Steve supplied the screenshot, this was built from a hand-rolled
`foundations-phone-ui.html` that rendered the lesson from live course copy. The
copy was real. **The chrome and the type were invented, and both were wrong.**

- The real lesson page is a **browser** page: Safari, the gohappybelly.com URL
  bar, a pale green search bar with a hamburger, then a nav row carrying a
  **Complete Lesson** button and prev/next arrows. The drawn version had none of
  that and invented a native-app header instead.
- Lesson headings are a **serif**, not Fira Sans Extra Condensed. The condensed
  sans is the *dashboard* template. Two different Momentum surfaces, two
  different type systems, and the laptop screenshot only ever showed the first.

This is the same mistake `Website/mockups/README.md` already records from
2026-10-21, when a drawn facsimile used the website fonts and "looked like the
brand but not like the product". It recurred because the laptop had a real
screenshot and the phone did not.

**Rule: do not draw a surface nobody has screenshotted.** Ask for the
screenshot. Real copy in invented chrome still misrepresents the product, and
it is not obvious it is wrong until the real thing turns up beside it.

The drawn HTML and its render script are deleted rather than kept, so no one
reaches for them again.

## What is on the screen

Lesson **05. Nutrition Foundations**, scrolled to "Every Meal Is An Input",
with the lesson's own food photograph. Safari chrome included on purpose: the
visible `gohappybelly.com` is evidence it is the real site rather than a
mockup.

Nothing was retouched. The laptop shot needed a member's name painted out;
this one carries nothing personal, just a tab count and a clock.

## Flagged, not fixed

**The course lesson bodies carry cut-paper images throughout.** Verified with
`search_course_content`: **13 of the 14 lessons** reference "Cut-paper" in their
body alt text.

The course is a *mix*, which the screenshot made clear: lesson 05 opens with a
real food photograph and still carries a cut-paper image further down. So this
is not a wholesale replacement, it is a per-lesson audit. Nobody has scoped it.
