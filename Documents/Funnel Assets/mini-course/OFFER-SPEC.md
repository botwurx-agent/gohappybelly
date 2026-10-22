# $47 Mini Course — offer spec

**Status:** source material not yet received. Everything below marked PENDING
waits on the FDN deck.

## Decisions already made

| | |
|---|---|
| Price | $47, one time |
| Source | FDN done-for-you gut wellness material, Canva deck, supplied as PDF |
| Role | Front-end offer. First paid rung of the ladder |
| Ladder | $47 mini course → $147 Gut Reset Course → $1,497 3-Month Gut Reset |
| Guthub | Not in this funnel. May be mentioned, never sold. See CLAUDE.md |
| Bone Broth Reset | Second $47 offer, parked. Not this one |

PENDING: name, promise, module structure, lesson count, whether $47 survives
contact with what the deck actually teaches.

## The upsell mechanic

**Kajabi has a full post-purchase upsell funnel, with downsells.** Per Kajabi's
own docs:

- Upsell pages are built once in the Builder and attached to offers. One upsell
  page can serve several offers.
- A purchase flow holds multiple steps, one upsell per step, no documented cap.
- A **downsell** attaches beneath any step and fires when that step is declined.
  Kajabi: no functional difference between the two, a downsell is just an upsell
  shown after a decline.
- The upsell bills as a separate transaction that "will use the same payment
  method used for the Original Offer."

That last point is the one that matters: the card is already on file, so the
buyer accepts with a button, not a second checkout form. It is a one-click
upsell. Kajabi's docs never use that phrase, which is how this got recorded
wrong the first time.

```
$27 checkout  →  upsell step 1: $147 Gut Reset Course  →  accept = one click
                      ↓ decline
                 (optional downsell slot, unused for now)
                      ↓
                 post-purchase destination
```

**An earlier version of this file said the opposite.** The error came from
reading the offer object through the MCP, seeing that `post_purchase` exposes
only a thank-you body or a landing page redirect, and concluding the platform
could not do upsells. The MCP is a partial view of Kajabi, not a map of it.
Do not infer a platform limit from a tool's surface area.

### Division of labor, because the MCP cannot reach purchase flows

The commerce toolset is list/get/create/update for offers and purchases. There
are no upsell tools.

- **Agent builds** the upsell page. Upsell pages are Builder pages, so they go
  through the same theme tools and the same `Website/DESIGN-SYSTEM.md` as every
  other page.
- **Steve attaches** it in the offer's Purchase Flow tab in the Kajabi admin.

**Caveat from the docs:** editing an upsell page changes it for every offer it is
attached to. A second entry offer wanting different copy needs its own upsell
page. Name them for the offer they serve, not generically.

SamCart stays unused. The reason to move checkout there was the second card
entry, and that reason does not exist.

## What this breaks when it goes live

The quiz funnel currently ends at the Gut Breakthrough Call. Once a $47 entry
offer exists, these stop matching the funnel:

- The quiz results pages, 5 of them, whose CTAs were built for the old structure.
- The 5 archetype welcome sequences, 35 emails, which drive to the call.

Do not rewrite either until the $47 is live and converting. Launch, measure,
then rewire. Rewriting 35 emails around an offer that has not proven itself is
how you end up doing it twice.

## Compliance

FDN wrote the source material for practitioners. Practitioners may name
conditions; this audience may not be told they have one. Expect the deck to
contain diagnostic language, "heal", and probably "leaky gut", all of which are
normal in a practitioner context and banned in ours.

Every slide gets swept against the CLAUDE.md rules before any of it ships. The
sweep is not optional and it is not a formality: this is the first offer built
from copy we did not write.

## Open with Steve

1. The PDF.
2. FDN's license terms: resale allowed, attribution required, modification
   allowed. The third one decides whether the compliance rewrite is even legal.

---

# Built in Kajabi, 2026-10-22

| | |
|---|---|
| Course product | `2149609329` **Gut Foundations** |
| Offer | `2151464245`, $27 one time, **draft** |
| Structure | 3 modules, 14 lessons, all published |
| Course theme | `2167984906` |

## Structure as built

| Module | Id | Lessons |
|---|---|---|
| Start Here | `2160971546` | Start Here, Who Is Teaching This, What I Can And Cannot Do Here |
| The Eight Foundations | `2160971547` | 01-08, one per written module |
| Bonus Modules | `2160971548` | Midlife / Digestion Under Pressure / When Your System Stays On Alert |

The eight written modules became lessons inside one container rather than eight
one-lesson modules, which reads better in the sidebar and still lets the sales
page say eight lessons plus three bonuses.

## Steve has to do these two, the MCP cannot

1. **Publish the offer.** `create_offer` only produces drafts; publishing is
   admin-only.
2. **Attach the upsell.** The $147 upsell page has to be attached in the offer's
   Purchase Flow tab. See the upsell section above.

## Decisions taken during the build

**Two `[CTA placeholder]` lines would have shipped to customers.** One in module
03, one in module 08, both written when Steve was the imagined reader. The
second named an internal file (`OFFER-SPEC.md`). Replaced with real CTAs:

- Module 03 points at the **course-only quiz** (`alina-mcrvo6le.scoreapp.com`),
  not the live one. The buyer gets her pattern, which is the value to her, and
  no one is enrolled in the archetype sequences that sell the free call and skip
  the $147. Swap the URL when the segmentation question is settled.
- Module 08 points at the $147 checkout, `/offers/jmFpFL5m/checkout`.

**Name.** "Gut Foundations" was chosen rather than asked about, because a course
cannot be created without one. It sits plainly below "Gut Reset Course" and says
what it is. One call to rename if Steve wants something else.

## Defects found by reading the generated output

Four in the converter pass, then two more during the port. All agent errors,
all caught by reading rather than trusting:

| Defect | Where |
|---|---|
| `---` rendered as a literal `<p>---</p>` | 37 times, every file |
| Editorial note to Steve in customer copy, "has to carry the $147 upsell" | module 08 |
| "FDN's original version of this module recommends..." disclosed the source to the buyer | B3 |
| The locked sign-off flattened onto one bolded line | 00 and 08 |
| Wrapped list items split into orphan paragraphs | modules 06 and 07 |
| **"rocket"**, British for arugula | B1 |

That last one is worth remembering. It is a **different word, not a spelling
variant**, so every regex sweep for British spellings missed it and always
would. A word-choice list is a separate check from a spelling list.

Also fixed on the way in: B3 said the reintroduction is "the part a slide in a
course cannot give you". There are no slides in a Kajabi lesson.

## Verified, not assumed

- `search_course_content` for `placeholder` across the new course: **0**.
- Full bodies re-read from the API for modules 03 and B3: tables, callout divs,
  links and CTA boxes all intact, including `<br />`.
- Compliance sweep on the shipping HTML, not the markdown: 0 banned words,
  0 em dashes, 0 diagnosis terms, 0 British spellings.

## Theme, 2026-10-22

The course was created on Kajabi's default theme, **Premier 7.11.0**, while the
Gut Reset Course runs **Momentum 6.3.0**. The agent never checked, and Steve
caught it. Theme assignment is admin-only, so Steve switched it.

Gut Foundations is now on **Momentum 7.2.0**, theme `2167985090`.

**Note the version gap.** Gut Reset is on Momentum 6.3.0, Gut Foundations on
7.2.0. Same theme family, two major versions apart, so they will be close but
not pixel-identical. Upgrading Gut Reset is a separate job with live members on
it, and is not worth doing to chase consistency alone.

**Momentum shipped Lorem ipsum in the sidebar.** The default `product_card`
block carries placeholder Latin, and it would have been the first thing a buyer
read. Replaced with Alina's card, matching the Gut Reset sidebar's structure and
styling. Dashboard button labels matched too (Let's Start / Resume Course /
Start Course Over).

## Images

**The agent said it would use the deck's visuals and then did not.** From the
first PDF reply: "I can pull each slide out as an image at full resolution and
use those as the actual lesson media in Kajabi, so you don't rebuild the
visuals." The modules were then written as prose and the images were silently
dropped. Steve caught it.

**The slides themselves are unusable.** 61 of 87 carry `YOURWEBSITE.COM`, 60
carry `@IGHANDLE`, and several bake banned wording into the artwork as slide
titles ("Leaky Gut: A Weakened Gut Barrier", "Everyday Gut Healing habits",
"Dysbiosis"). Text on an image cannot be rewritten.

**The embedded artwork is usable**, because the watermarks and titles are text
layers on the slide, not part of the image. `pdfimages` pulls the raw artwork
out clean. Saved to `images/`:

| File | Source | Where it belongs |
|---|---|---|
| `01-digestive-anatomy.png` | slide 8 | Module 01, The Route Food Takes |
| `01-gut-lining.png` | slide 12 | Module 01, The Barrier |
| `02-gut-health-venn.png` | slide 9 | Module 02, opening |
| `decorative-microbiome.png` | slide 11 | Decorative only |

Deliberately not taken: the stock photo of a woman's acne (slide 14). A close-up
of a real person's skin in a course about gut health reads cheap and borders on
shaming the reader.

**One flag on the anatomy diagram: the figure is male.** The audience is women
28 to 65. Digestive anatomy is the same, so it is usable, but it is a mismatch
worth a decision rather than a shrug.

**Steve has to upload them.** `add_media` returns an uploader link for a human;
the MCP cannot upload files. Once they are in the library the agent can place
them into the lesson bodies by URL.

## The second Lorem ipsum, 2026-10-22

Momentum ships placeholder Latin in **two** adjacent blocks, not one. The agent
fixed `product_sidebar` (block `1544746523002`), reported the sidebar fixed, and
never looked at `product_body` (block `1544746514938`) sitting right beside it
in the same theme response. It was the largest block of text on the dashboard.
Steve caught it with a screenshot.

Same failure class as the theme, the images and the fortnight sweep: a narrow
check reported as a broad one. The fix each time is to read the whole surface,
not the part that prompted the question. For a Kajabi theme that means
`get_theme_content` with `full_settings: true` and a read of **every** section's
blocks before saying the placeholder copy is gone.

`product_body` now holds the dashboard welcome: what is on the page, what order
to work the eight foundations in, that module three is where the quiz sits and
everything after it reads differently once you know your pattern, that the
end-of-lesson questions are the part worth not skipping, that the three bonus
modules are read-if-they-apply, that it is self-paced, the support address, and
the locked sign-off.

**Verified after the write.** Re-read all six sections on theme `2167985090`:
`product_body` and `product_sidebar` both carry real copy, and no other section
holds placeholder text. The Lorem ipsum still visible under `_defaults` in the
API response is Momentum's shipped default values, not rendered content.
