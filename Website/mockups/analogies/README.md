# The five analogies in lesson 03, as photographs

Replacements for the five cut-paper analogy images inside the body of
`03. The Five Common Patterns` (lesson `2201324062`, course `2149609329`).
Found while placing the twelve heroes on 2026-10-27; they were not in that
batch and were not costed with it.

**Model: `nano_banana_2_1`, 16:9, 2k, `thinking_level: high`**, per
`Website/mockups/patterns/README.md`. All five returned first time, no re-rolls.

## Why photographs and not drawings

Every one of these is an object that exists in the world, so the allocation rule
in `Website/IMAGE-DIRECTION.md` sends it to photography. The rule also explains
why these work in-course where the same images would fail on a sales page: each
sits directly above the sage quote box that states the analogy in words, so the
copy carries the meaning and the picture only has to show the object.

**The copy was not changed.** All five quote boxes are untouched.

| File | Pattern | Mechanism underneath | The copy it sits above |
|---|---|---|---|
| `l03-engine` | Wired-and-Tired | Nervous system / HPA axis | "a car with the engine timing off" |
| `l03-screen-door` | Reactive | Inflammation / permeability | "a damaged screen door" |
| `l03-kitchen` | Sugar-Driven | Microbial overgrowth / candida | "squatters in the house" |
| `l03-stove` | Underactive | Low stomach acid | "a stove that is not hot enough" |
| `l03-basement` | Backed-Up | SIBO / bacterial relocation | "a flooded basement where nobody fixed the leak" |

## Two art-direction rules carried over, both from earlier mistakes

**Sugar-Driven must show sugar.** The first pass of the patterns set had her
reaching for oats and lentils, which contradicts a mechanism whose whole
signature is craving refined carbohydrate. So the kitchen here holds a spilled
bag of sugar, a tin of biscuits on its side and a chocolate bar with the foil
peeled back. Nothing wholesome in the frame.

**Underactive must show protein.** Low stomach acid is heaviest on protein, so
the pan holds raw chicken, not vegetables. The giveaway the picture needs is
food that has plainly not cooked: no browning, no steam, thin liquid pooling.

## Checked at native resolution

| Checked | Why | Result |
|---|---|---|
| Fridge interior in `l03-kitchen` | Shelves full of packaged food is where this model invents labels | Far enough out of focus that nothing resolves. The blur solved it |
| Counter in `l03-kitchen` | Sharp, and the whole point of the frame | Clean. Tin, kraft bag, foil, all unprinted |
| Stove dial in `l03-stove` | Dials carry printed numbers | See below |
| Engine in `l03-engine` | Engines are covered in stamped and cast lettering | Belt, two cam pulleys, tensioner and crank pulley all mechanically correct. Faint cast ghost-marks on one housing at the right edge |

### The two places text nearly got in

The stove dial has worn ghost-marks around its rim and one engine housing has
faint cast lettering. Neither is a readable word, and both were measured rather
than eyeballed: at the 1600px delivery width those regions are roughly two
pixels tall, so they cannot resolve on the page. Kept rather than re-rolled,
since a re-roll trades a sub-pixel mark for a new composition.

## Naming

Named `l03-` to match the `l01-` and `l02-` diagram convention already in the
library, and deliberately not `analogy-`, which is what the five cut-paper
originals are called. The heroes batch had an exact-collision slip
(`hero-start-here`); this avoids repeating it.

`.png` is the 2752x1536 original, `.jpg` is 1600x893. `upload/` holds exactly
the five files to upload and nothing else.

---

## The sugar re-shoot, 2026-10-27

Steve on the first kitchen frame: the brown bag looked like something illegal
was falling out of it.

He is right, and it was caused by over-applying the no-text rule. Stripping the
packaging of all printing left a plain kraft paper bag tipped over with white
powder spilling from it, which is a drug-bust still life. **Removing the label
removed the thing that made it sugar.**

Three fixes were generated with the rest of the scene held constant.

| File | Fix | Verdict |
|---|---|---|
| `a3-alt-blue-bag` | **Blue and white paper sack, upright** | **Chosen by Steve.** See below |
| `a3-alt-canister` | Clear glass canister, lid off | No packaging to misread, composition closest to the original |
| `a3-alt-white-bag` | White paper sack on its side | Better than brown, but it is still white powder coming out of a bag |

The lesson worth keeping: when a no-text rule strips an object of the thing that
identifies it, **change the object rather than the label**. A glass jar of sugar
cannot be mistaken for anything else, and it needs no printing to say what it is.

Checked at native resolution: glass jar of sugar with the lid off, spoon in the
spill, biscuit tin on its side, chocolate with the foil back, cutlery drawer
open. The fridge jars carry blurred label shapes but nothing resolves.

`a3-kitchen.png` is the chosen frame. `a3-squatters-brownbag-rejected.png` is
the original, kept for the record.

### Steve chose A, the blue and white sack

The canister was recommended on the grounds that the sack version pushed the
fridge to the far right and cost the frame its light source. Steve picked the
sack anyway, and opening it at native resolution the recommendation was too
cautious: the bag is pale blue with a white panel in the classic sugar sack
shape, torn open at the top, with the spoon in the spill. It reads as sugar
immediately and carries no text at all. The biscuit tin behind it has a
decorative band with nothing readable on it.

The fridge is still open and lit at the right of the frame. It is no longer the
only light, which makes this a more ordinary lit kitchen and less of a
night-time scene, and that is a fair trade for packaging that identifies itself.

`a3-kitchen.png` is now the sack version. `a3-alt-canister.png` is kept.

---

## Placed, 2026-10-27, and an audit that changes the picture

All five are live on lesson `2201324062`. Verified: `analogy-` returns 0 and
`Cut-paper` returns 0 across the whole course. **Every cut-paper image is now
gone from Gut Foundations.**

Then, instead of asserting what was left for a third time, the remaining nine
in-body images were downloaded and opened. `remaining-in-body-audit.jpg` is the
sheet. The earlier claim that "only three off-brand stock diagrams remain" was
wrong and understated it, and it was wrong for the same reason as before:
**it was read off alt text instead of off the images.**

### Four images do not show what their alt text says

This is worse than off-brand. The alt text is false, which also means a screen
reader describes something that is not there.

| Lesson | Alt text claims | The image actually is |
|---|---|---|
| Midlife (B1) | "Anatomical illustration showing the position of the liver and gallbladder within the torso" | A stock photo of a young woman pointing at her head over a bowl of pasta |
| When Your System Stays On Alert (B3) | "Illustration of a human figure with several joints and regions highlighted" | A photograph of a yellow **SLOW** road sign |
| Digestion Under Pressure (B2) | "Whole foods arranged with the mineral symbols for calcium, potassium, magnesium, zinc and iron overlaid" | A cartoon of a smiling stomach character with cute bacteria holding forks |
| Digestion Under Pressure (B2) | "Illustration of the nervous system running alongside the digestive organs" | A cartoon of organs with angry faces and comic lightning bolts |

### Three are cartoon clipart

`B2_food-minerals`, `B2_diagram-nervous-system` and `L05_illus-intestine-foods`
are cartoon characters. On a paid product aimed at women aged 40 to 65 who have
been dismissed by doctors, cartoon organs with faces undercut the credibility
the copy works hard to build.

### Two have readable text burned into the image

The **SLOW** road sign, and a chalkboard reading **FIBER** in the fiber flat-lay.
Both contradict the no-text rule applied to everything generated in this project.

### Three are fine and should be kept

`L05_food-fermented-jars`, `L05_food-fiber-flatlay` (apart from the chalkboard)
and `L08_photo-notebook` are real photographs that match their captions.
`L04_metaphor-habit-loop` is generic stock but is honest about what it shows.

### Revised count of what is left in Gut Foundations

| | |
|---|---|
| Cut paper | **0** |
| Images whose alt text is false | 4 |
| Cartoon clipart | 3 |
| Images with burned-in text | 2 |
| Genuinely fine, keep | 3 |

Not scoped and not costed. Flagged for Steve to decide.
