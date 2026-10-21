# Course product mockups

Device mockups of the Gut Reset Course, generated rather than photographed, so they
stay correct when the course changes.

| File | What it is |
|---|---|
| `course-mockup-angled.png` | **The chosen one.** Angled screen, with the phone and the printed tracker tucked into the bottom-right |
| `course-mockup-angled-solo.png` | Angled screen alone |
| `course-mockup-flat-pair.png` | Straight-on screen with phone |

## Regenerating

    node render.mjs      # writes mock-A/B/C/D.png next to the script

`build-mockups.html` holds all four compositions. It renders the course UI from
HTML rather than screenshotting the real course, because the course sits behind a
member login.

## Why it is drawn, not screenshotted

Steve's original reference was a stock mockup of the **old** course. Its sidebar read
"Week 1: How To Heal And Seal Leaky Gut", "Discover Your Gut Type", "5 Gut Type
Protocols" — the pre-rebuild structure, and a title that breaks two CLAUDE.md rules at
once (a diagnosis term, and "heal"). On a sales page, at that size, it is legible.

These render the course as it is now: Start Here, Find Your Pattern, Your Pattern In
Detail, the four weeks, The Reintroduction Fortnight, Your Reference Shelf. The lesson
on screen is the Reactive Gut page with its locked aha line, and the phone shows the
apple cider vinegar lesson. The tracker is the real PDF, not a drawing of one.

**If the course modules are ever renamed, regenerate these.** The whole point is that
they show the real product.

## Build notes

- Shadows use `filter: drop-shadow`, not `box-shadow`. On a transparent canvas
  Playwright quantizes large box-shadow alpha into visible concentric bands.
- They render on `#F8FAF8`, the hero background, rather than transparent. Opaque
  compositing was what finally killed the banding. **They will not sit correctly on a
  forest section** without being regenerated on that colour.
- The monitor frame has 14px padding, so its width must be at least the UI width
  (980px) plus 28, or the screen clips its own content.
- In the angled composition the phone and sheet carry the same `rotateY`/`rotateX` as
  the monitor and are scaled down, because they sit on the receding side of the
  vanishing point. Without that they read as flat cutouts laid on top.
