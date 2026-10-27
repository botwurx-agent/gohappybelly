# Gut Reset, wave 3: the literal still lifes

24 photoreal replacements for cut-paper lesson images in the Gut Reset course
(2148514926). Generated 2026-10-27 on `nano_banana_2_1`, 16:9, 2k,
`thinking_level: high`.

## Why 24 and not the 31 first estimated

The earlier figure in `Website/GUT-RESET-IMAGE-AUDIT.md` was taken before the
remaining 37 were sorted subject by subject. The honest split is **24 literal**
(this wave) and **13 metaphor** (wave 4). The metaphors are the ones that need
the lesson-03 treatment: a photograph of the real object, trusted to carry
meaning because the surrounding copy does the explaining.

## The name collision, and the prefix

The existing cut-paper assets are themselves named `reset-*`. Uploading these
as `reset-apple-cider-vinegar` and so on would have collided with all 24 at
once. They carry a **`photo-`** prefix instead, which also distinguishes the
photoreal replacement from the cut-paper original at a glance in the media
library.

This is the second collision caught on this project by listing media before
naming an upload rather than after. It is worth doing every time.

## What `used_count` does and does not count

Every remaining cut-paper asset reads `used_count: 1`, but each is used twice:
as the lesson `poster_image` and again inline in the lesson body. Kajabi counts
only the tracked model placement. Inline HTML is a bare CDN URL inside a body
string and is invisible to the counter.

So `used_count: 1` is not a reason to skip the body rewrite, and the count
dropping to 0 after `replace_media` does not mean a lesson is finished. Every
swap is still two operations:

1. `replace_media` for the poster
2. a body rewrite for the inline image and its alt text

Assets already converted in waves 1 and 2 (`reset-pattern-*`, `reset-module-*`,
`reset-gut-pattern-quiz`) correctly read `used_count: 0`.

## Direction rules carried over

From `Website/mockups/patterns/README.md`:

- palette lives in the room and the light, never in clothing
- blank packaging stated object by object, since the model follows text
  instructions weakly
- when a no-text constraint strips an object of the thing that identifies it,
  change the object rather than the label (the sugar-bag lesson)

Applied here to the bottles, jars, blender, kettle and vials, all of which
would otherwise have arrived carrying invented branding.

## Duplication avoided

Two subjects collided with module covers already placed, and were re-directed
before generation rather than after:

| Subject | Module cover already in place | What was shot instead |
|---|---|---|
| `week4-your-pattern` | `mod-week4`, a kitchen garden from above | a trug of mixed harvest, low and close on grass |
| `week3-your-pattern` | `mod-pattern-in-detail`, tools laid out on a bench | tools hung in a row on a shed wall rack |

## Re-rolled after looking

Twenty-two of twenty-four passed on the first generation. Two did not, and were
caught by building a contact sheet and looking at it rather than trusting the
prompts:

- **collagen** came back as a bowl of soup. The lesson's whole point is that
  broth *sets*, and the wobble had not survived. Re-shot as a spoon lifting a
  trembling cube clear of the dish, with the spoon-shaped hollow it came from
  still visible below. Unambiguous now.
- **testing** came back as a bare, cold lab bench with a crumpled glove on a
  wide empty counter. Re-shot close and warm on a kitchen table, vials in a
  wooden rack beside blank envelopes and a cup of tea.

The rule from `Website/diagrams/README.md` holds for photography too: render
and look before shipping. Nothing in either prompt predicted either fault.

## Files

- `raw/` 2752x1536 PNG as generated. Local only, gitignored: regenerable, and
  roughly 10MB each
- `upload/` 1600px JPEG q82, what Steve uploads
- `sheets/` contact sheets used for the review above

## Still to place

Upload, then per lesson: `replace_media` for the poster, then a body rewrite
for the inline image and alt text. The exception recorded in
`Website/GUT-RESET-IMAGE-AUDIT.md` still stands: where a lesson body carries
clinical detail, the admin UI beats a rewrite.
