# Image direction

Opened 2026-10-26, after Alina saw the pages and rejected the cut-paper
illustration style outright, all 52 of them. Steve also said the analogy images
he looked at did not explain themselves.

**Status: the first piece is built and the rest is a proposal. Steve has not
decided it yet.** Do not treat the plan below as agreed.

---

## Two problems, not one

They arrived in the same sentence and they need different fixes. Conflating them
is how we end up regenerating 52 images and still having the second problem.

### 1. The style. Alina's call, and it is already made.

She is the face of the practice and she does not want cut-paper. That settles it.
Nothing below argues with it.

### 2. The analogy did not read. Photorealism makes this one worse, not better.

This is the one worth slowing down for.

A cut-paper screen door is obviously standing in for something, because nothing
in the picture is literal. A *photorealistic* screen door is just a screen door.
Raising the realism raises the literalism, and the viewer's question changes from
"what does this mean" to "why am I looking at a door". Swapping 52 metaphors into
52 photoreal metaphors multiplies the problem Steve spotted instead of fixing it.

The analogies in CLAUDE.md are locked as **language**. Nothing ever specced them
as art direction. "The food is fine, the system processing it isn't" works in a
headline, said out loud, on camera. It does not work as a silent picture of a
car engine with no copy beside it.

---

## What the 52 actually are

Reading `GUT-RESET-VISUAL-PLAN.md`, they split in two, and the split decides the
work:

**Metaphor, roughly two in three.** The five patterns, and most of the module
and lesson art: a five-armed fingerpost, a drystone wall part-repaired, a mantel
clock opened up, a keyhole door with four keys, stepping stones, five identical
doors, a lantern at dusk, a closed five-bar gate, cracks spreading across a wall,
a kettle boiling hard. Every one of these needs the copy next to it to mean
anything.

**Literal still life, roughly one in three.** A stockpot simmering with a ladle
on the rim. Five ingredients in a row on a board. Amber bottles on a shelf. A jar
bubbling beside fibrous roots. Specimen jars and a magnifying glass. These are
already self-explanatory, and they are the ones that translate straight to
photography and get *better* for it.

---

## The proposal

**Stop doing a one-for-one swap. Decide what each image is for, then pick its
kind.**

| Where | What the image is for | What it should be |
|---|---|---|
| Sales pages | Proof. Make the thing feel real and worth $27 / $147 / $1,497 | Product shots (the laptop banner), and Alina |
| Course lesson thumbnails | Pacing and warmth. Nobody buys off these | Photoreal still life of the literal subject |
| The five patterns | The hardest case. See below | **Decided: the symptom moment** |

**On the five patterns.** My recommendation is to stop illustrating the metaphor
and photograph the *symptom moment* instead: the 3pm slump at a desk, the waist
button undone, the plate pushed away, a bed at 4am. Those read instantly, they
are about the reader rather than about a door, and they carry the emotional
weight the archetype is actually trading on. Keep the car and the screen door
and the squatters in the headline and the voiceover, where they land. **Steve chose this on 2026-10-26.** Built and awaiting upload:
`Website/mockups/patterns/`, with the prompt traps recorded in its README.

**On sequencing.** Sales pages first: there are few images, they are the ones
prospects see, and they are the ones Alina reacted to. The 52 course thumbnails
are low leverage (nobody sees them until after they have paid) and high volume,
so they come last and can go in batches.

---

## What is built

### The Gut Foundations laptop banner (2026-10-26)

`Website/mockups/foundations/foundations-hero-{a,b,c}.jpg`, 2400x1357. Three
angles of the same scene. **Steve picked B on 2026-10-26 and it is live** on the
sales page hero, the offer image and the course thumbnail (Kajabi media id
4829069). Placement detail and the share-image dead end:
`Website/GUT-FOUNDATIONS-PAGE.md`.

Built on the pipeline already documented in `Website/mockups/README.md`, which is
the right one and should be reused for every device shot:

1. The **scene** is generated. `gpt_image_2_5` via Higgsfield, 16:9, quality
   high, 2k, prompted for a photoreal laptop on a pale oak desk in a soft warm
   kitchen, with the screen asked for as a **flat `#FF00FF` fill**.
2. The **screen is not generated.** `foundations-ui.html` renders the real
   dashboard, Playwright screenshots it at 2000x1126, and `composite2.py` finds
   the magenta, reads its four corners and perspective-warps the screenshot into
   the quad. No model is ever asked to draw the UI, because it would invent
   lesson names.
3. `demagenta.py` pulls the magenta spill out of the laptop body.

Residual magenta after the fix: 0 pixels on all three.

**The UI is faithful, not decorative.** Real lesson titles from course 2149609329,
the real welcome copy from the `product_body` section of theme 2167985090, the
real sidebar card text, and Alina's actual photograph. The same rule as last
time holds: a mockup that shows copy the product does not contain is a lie on a
sales page.

Fonts matter here and were the mistake last time round. The course runs the
**Momentum** theme: Fira Sans Extra Condensed for the sidebar title, section
headings and nav; Lato for body; a serif for the green banner title. Not the
website's Playfair / DM Sans. Loaded from Google Fonts, which the container can
reach.

Colors sampled from the real dashboard screenshot rather than guessed:

| | |
|---|---|
| Sidebar pale | `#C3EFD0` |
| Sidebar module row | `#9ACEAA` |
| Banner gradient | `#7EAC8D` to `#BDDCC6` |
| Welcome strip | `#76A684` |
| Body heading | `#B1BECD` |
| Dark text | `#2D3C50` |
| Panel grey | `#F2F2F2` |
| Dashboard pill | `#B0C96C` |

### Container notes

- **System `python3` has a broken PIL** (`cannot import name '_imaging'`).
  Use **`python3.13`**, which has working Pillow and numpy. Every composite
  script here must be run with it.
- `ghb-logo.png` is 1000x625 with a large transparent margin; its real content
  is 664x239. `ghb-logo-trim.png` is the cropped version, which is what to size
  against.
- Google Fonts is reachable from this container. The live site is not
  (Cloudflare 403), so none of this is visually verified on the page.

---

## Open questions for Steve

1. The 52 course thumbnails: replace all of them, or only the ones a buyer sees
   early (Start Here, Find Your Pattern, the five pattern pages)?
3. Does the Gut Reset course sales page get a matching re-shoot, so the $27 and
   $147 pages look like one family?
