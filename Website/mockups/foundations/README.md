# Gut Foundations mockups

> **2026-10-26: the cut-paper mockups below are dead.** Alina rejected the style
> outright. They are kept only as a record. The live banner is
> `foundations-hero-{a,b,c}.jpg`, photoreal, built the same way as the $147
> laptop. Direction and reasoning: `Website/IMAGE-DIRECTION.md`.


Cut-paper product mockups for the $27 Gut Foundations course, generated
2026-10-23 to match the 52 existing illustrations.

Three directions, all 1600x905 (the same size as every other illustration in
`Website/images/gut-reset/web/`). `.png` is the 2688x1520 original, `.jpg` is
the web version to upload.

| File | What it shows | Best for |
|---|---|---|
| `foundations-laptop` | Open laptop, lesson list down the left, lines of text, terracotta button | The closest parallel to the $147 `course-hero-laptop.png` |
| `foundations-phone` | Phone propped up beside a mug, a single lesson on screen | The hero slot. Matches "Read on your phone" and does not imply video |
| `foundations-flatlay` | Overhead: phone, open notebook with pen, mug, leaves | A full-width band. The notebook is the twelve reflection prompts |

## Dashboard renders (added later the same day)

Steve asked for the actual Gut Foundations course dashboard rendered in the same
style, rather than a generic device. The real screenshot went in as an image
reference alongside the two style references.

| File | What it is | Verdict |
|---|---|---|
| `dashboard-angled` | The layout on a paper desk at a three-quarter angle, mug and leaves beside it | **Best.** Warmest and most finished. Heading legible, and the right panel carries an abstract shape where Alina's photo sits in the real UI |
| `dashboard-text` | Flat, full view, straight on | Good. Both headings legible and the layout is faithful. Top banner strip is mush and the right card is blank |
| `dashboard-notext` | Flat, no lettering at all | **Weakest.** Cropped too tight, clipping the sidebar title and the right panel. Texture only |

### Text turned out to be fine

An earlier note here said to keep letters out of these prompts entirely because
image models garble them. That was too cautious for this model. `gpt_image_2_5`
is tagged `text-rendering` and produced GUT FOUNDATIONS and WELCOME TO GUT
FOUNDATIONS as clean cut-paper letterforms at the first attempt.

The rule that still holds: **name the exact words you want and keep them few and
large.** Body copy and the sidebar lesson titles are left as paper strips in all
three, and that is where garbling would start. Asking for eleven small lesson
titles is the pass that would break.

Alina's photograph is deliberately absent. All 52 illustrations are objects and
places with no people in them, and a cut-paper likeness of a real person would
sit badly in the set as well as risking a poor likeness.

---

## How they were made

`gpt_image_2_5` via Higgsfield, 16:9, quality high, 2k, with two of the
existing illustrations passed as `image_references` (the ransacked kitchen and
the car engine) to lock the paper texture and palette.

The prompts carry one non-obvious instruction: **absolutely no letters, words,
numbers or typography anywhere.** Image models garble text, and the cut-paper
style has no room for real UI copy. Screen content is built from paper strips
that read as lines of text without being any. Keep that constraint on any
re-roll.

Palette held to sage green, deep forest, warm cream, soft grey-green and
terracotta, which is the illustration palette, not the website token set.

## Note on the product

Gut Foundations has **no video**. A mockup showing a video player or a play
button would misrepresent it. The laptop and phone screens here show reading
layouts only, which is deliberate.


---

## 2026-10-26: the photoreal laptop banner

`foundations-hero-a.jpg`, `-b`, `-c` (2400x1357). Three angles of one generated
scene with the **real** dashboard composited into the screen. A is straightest
and most legible, B a touch more angled, C sits further right.

Build, in full, with the traps: `Website/IMAGE-DIRECTION.md`. In short:

    node render-foundations.mjs                                         # UI -> foundations-ui.png
    python3.13 composite2.py foundations/scene-a.png foundations/comp-a.png foundations-ui.png
    python3.13 demagenta.py  foundations/scene-a.png foundations/comp-a.png foundations/foundations-hero-a.png

Both scripts are run from `Website/mockups/`, and **must** be run with
`python3.13`: the system `python3` has a broken PIL in this container.

`composite2.py` is `composite.py` with the screenshot path taken as `sys.argv[3]`
instead of hardcoded to `course-ui-v2.png`. Everything else, including the
dilate-not-erode key handling and the 1.8% quad push, is unchanged and still
correct.

Source files kept: `scene-{a,b,c}.png` are the raw generated scenes with the
magenta screens, so the UI can be re-composited without paying for generation
again. `alina.jpg` is her portrait pulled from the Link in Bio theme.

**Regenerate the UI whenever the course changes.** `foundations-ui.html` hardcodes
the lesson titles and welcome copy that were live on 2026-10-26. The whole point
is that it shows the real product.
