# Model bake-off: realism, 2026-10-26

Steve asked to compare Nano Banana against the current model, judging on
realism alone: "no hint of AI generation".

Two scenes, three models, **identical prompts** (the exact text already used for
the built set), 16:9, 2k. `comparison.jpg` is the labelled sheet.

## There is no model called "Nano Banana 2 Pro"

The Higgsfield catalog carries a Google family that does not map cleanly onto
that name:

| id | Catalog name | Note |
|---|---|---|
| `nano_banana_2_1` | Nano Banana 2.1 | Newest 2.x. Has `thinking_level` (minimal/medium/high) and a seed |
| `nano_banana_pro` | Nano Banana Pro | **Submits as `nano_banana_2`.** The job came back reporting that id |
| `nano_banana_2` | Nano Banana 2 | Fast next-gen |
| `nano_banana_2_shots` | Nano Banana Pro | Blank provider and description. Not tested |
| `nano_banana` | Nano Banana | Budget tier |

Tested `nano_banana_2_1` (thinking_level high) and `nano_banana_pro`. The
second is an alias: the returned job reports `model: nano_banana_2`, so the
sheet labels it that way rather than claiming a Pro tier was used.

This supersedes the note in `Website/mockups/README.md` from 2026-10-21 saying
Nano Banana was not in the catalog. It was true then. Re-check the catalog
rather than trusting that line.

## Result: the realism question and the direction question split

**Nano Banana 2.1 is visibly more photographic.** Real grain, believable lamp
falloff, skin with texture and asymmetry, rooms that look lived in rather than
styled. GPT Image 2.5 carries a faint even sheen across skin and fabric that
reads as rendered once you look for it. On Steve's actual criterion, Nano
Banana wins, and not narrowly.

**GPT Image 2.5 directed the shot better.** In both Nano Banana frames the
woman looks straight down the lens and presses a hand flat to her stomach,
which is the exact stock-photo cliché the symptom-moment brief exists to avoid.
The GPT frames are observational: she is looking away, caught mid-action, and
the picture reads as something witnessed rather than posed.

**Nano Banana also ignored the no-text rule.** The grocery frame came back with
a legible "Nutrition Facts" panel and a barcode, from a prompt that says
"absolutely no readable text" twice. GPT honoured it in both passes. That
matters here: a half-rendered word on a packet is the giveaway, and it is also
the thing that would make a sales page look cheap.

So Nano Banana has the better camera and GPT has the better director.

## What to do about it

Switch to `nano_banana_2_1` and move the direction into the prompt, since it
will not supply it unasked. Three additions needed on every pattern prompt:

- **"She is looking away from the camera, never at the lens."**
- **"No hand pressed flat to her stomach."** Name the gesture that is wanted
  instead, per pattern.
- Keep the no-text line but expect to re-roll. It is a weaker instruction
  follower on this, so check every frame before use.

Not yet done. Awaiting Steve.
