# Gut Foundations mockups

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
