# The five patterns, as symptom moments

Photoreal replacements for the five cut-paper archetype illustrations on
`/gut-foundations`. Decision and reasoning: `Website/IMAGE-DIRECTION.md`.
Steve chose the symptom moment over photoreal metaphor on 2026-10-26.

| File | Pattern | The moment |
|---|---|---|
| `p1-wired-tired` | The Wired-and-Tired Gut | Eating lunch at a desk without stopping work, fork up, other hand still on the trackpad |
| `p2-reactive` | The Reactive Gut | Reading an ingredients label closely, basket holding three or four things |
| `p3-sugar-driven` | The Sugar-Driven Gut | Caught mid-reach at an open cupboard in the late afternoon |
| `p4-underactive` | The Underactive Gut | A barely touched plate, fork already set down across the rim |
| `p5-backed-up` | The Bloated and Backed-Up Gut | Changed out of jeans into soft clothes by evening, jeans folded beside her |

`.png` is the 2688x1520 original, `.jpg` is 1600x905, which is the size every
other image in this slot already uses.

Each one is built from the quoted line already on the page, not from the
analogy. `p2` is "my safe food list keeps getting shorter", so she is reading a
label. `p4` is "food sits like a stone for hours", so the plate is full and
abandoned. The car, the screen door and the squatters stay in the copy beside
the picture, where they work.

## How they were made

`gpt_image_2_5` via Higgsfield, 16:9, quality high, 2k, one prompt each through
`generate_image_batch`. No reference images: the brand look is carried by the
grade and the light, not by a style transfer.

## The first pass was thrown away, and why

Version one came back as **five photographs of what looked like the same woman
in the same sage-green sweater.** The shared style line ended with "warm muted
color grade in sage green, warm cream, soft terracotta and pale wood", and the
model read that as wardrobe direction rather than as a grade.

**Put the palette in the room, never in the clothing.** The fix was to say so
explicitly ("the warm cream, pale wood and soft terracotta tones are in the
room, the light and the furnishings, NOT in her clothing") and then to name a
different garment colour, a different age and a different woman in each of the
five prompts. Without that, a shared style suffix will quietly collapse a set
into one person.

The five now span roughly 32 to 58, which is the range the seven avatars in
CLAUDE.md actually cover, instead of one woman in her forties five times.

`p4` also needed its plate called out in capitals. The first pass gave a nearly
empty plate, which reads as "ate too much" and says the opposite of what the
Underactive pattern is about. The prompt now states the plate is almost
completely full with only a forkful or two missing.

## Compliance

Nobody is diagnosed. These are moments, not symptoms attributed to a named
condition, and the pattern framing lives in the copy beside them. Alt text must
follow the same rule: describe what is in the photograph, never tell the reader
what she has.
