# Gut Foundations — Image Plan

Steve, 2026-10-22: "we dont have to use the generic images of people but there
are drawings, graphs and images we can use so the viewer has a visual experience
as well. my though is since we are not providing video we should atleast provide
an image for almost all of the sections/pages. If we dont have a good image we
should create one using higgsfield."

## What the first pass got wrong

The build note said "the slides themselves are unusable" and salvaged four
images. That conclusion came from reading the *slides*, which are watermarked
and carry banned wording as slide titles. It was never tested against the
*embedded artwork*, which is a separate layer and comes out clean.

Re-running the extraction across all six decks found **163 embedded images**, of
which **48 are usable**. The original four were about 8% of what was there.

| Deck | Pages | Embedded images |
|---|---|---|
| Combined Gut Wellness | 87 | 94 |
| Midlife Women | 13 | 16 |
| High-Stress Lifestyles | 13 | 15 |
| Autoimmune / Chronic Inflammation | 13 | 13 |
| Men | 12 | 13 |
| Kids & Teens | 10 | 12 |

Everything usable is saved under `images/fdn/`, named by role.

## What was deliberately not taken

**Stock photographs of people.** Per Steve. The decks lean on them heavily:
smiling man, woman in yellow sweater, high-fiving colleagues, telehealth call,
couple walking a dog. None of it says anything.

**The prairie.** The same four or five landscape photographs appear roughly 25
times as slide-divider backgrounds. They carry no meaning.

**Five images with problems baked into the artwork.** Raster text cannot be
rewritten, so these were cropped or dropped:

| Image | Problem | Action |
|---|---|---|
| Barrier / tight junction diagram | titled **"LEAKY GUT"**, a CLAUDE.md banned phrase | top 120px cropped, saved as `diagram-gut-barrier.png` |
| Liver pathway diagram | titled **"Detoxication"**, a misspelling | top 105px cropped, saved as `diagram-liver-pathway.png` |
| Autoimmune Protocol Diet chart | diagnostic framing, names a protocol by condition | dropped |
| Trauma Responses wheel | clinical psychology, outside an FDN-P's scope | dropped |
| "WARNING BIOHAZARD" sign | tonally wrong for this brand | dropped |

The digestive anatomy figure is still male, which remains an open decision.

## The coherence problem, stated plainly

The 48 salvaged images are not one visual system. They are 3D medical renders in
blue and purple, flat vector cartoons in pink and coral, clinical diagrams in
primary colors, stock photography, and line-icon sets. None of them is in the
website palette.

Dropped across 14 lessons as-is they will read as a scrapbook, not a course.
That is an argument for generating a consistent set, not for using everything
that was found.

**The recommendation is a split, by job:**

- **Anatomy and mechanism stay with the FDN diagrams.** Image generators are
  unreliable on anatomical accuracy and produce nonsense in diagram labels.
  Asking Higgsfield for "a labeled diagram of the digestive tract" returns
  gibberish text. These are reference figures and should look like reference
  figures, visually set apart in a bordered frame so the mix reads as deliberate.
- **Metaphor, concept and mood get generated**, in one house style, in the
  website palette, across every lesson.

## The highest-value generated set: the five archetype analogies

The locked analogies in CLAUDE.md are the strongest illustration brief this
business has, and no stock library has them:

| Archetype | Analogy |
|---|---|
| Wired-and-Tired | a car with the engine timing off |
| Reactive | a damaged screen door |
| Sugar-Driven | squatters in the house |
| Underactive | a kitchen with a stove that is not hot enough |
| Bloated and Backed-Up | bacteria in the wrong neighborhood, and a flooded basement with an unrepaired leak |

These are reusable well beyond this course: the five quiz results pages, the 35
archetype emails, and social. Worth doing properly once.

## Lesson map

Fourteen lessons. "FDN" means an image already in `images/fdn/`.

| # | Lesson | Hero | Inline |
|---|---|---|---|
| 1 | Start Here | generate | — |
| 2 | Who Is Teaching This | Alina's photo (Steve has one) | — |
| 3 | What I Can And Cannot Do Here | generate | — |
| 4 | 01 Understanding Your Gut | FDN `diagram-digestive-anatomy` | FDN `diagram-gut-barrier`, `diagram-gut-lining-villi` |
| 5 | 02 Whole-Body Health | FDN `diagram-gut-health-venn` | FDN `diagram-organs-labeled` |
| 6 | 03 The Five Common Patterns | generate | **the five analogies**, generated |
| 7 | 04 Everyday Habits | generate | FDN `photo-clock`, `icon-sleep-zzz` |
| 8 | 05 Nutrition Foundations | FDN `illus-intestine-with-foods` | FDN `food-fiber-flatlay`, `food-fermented-jars` |
| 9 | 06 The Gut-Brain Connection | FDN `illus-gut-brain-dark` | FDN `diagram-autonomic-balance`, `metaphor-two-way-cans` |
| 10 | 07 The Gut-Liver Connection | FDN `diagram-liver-in-body` | FDN `diagram-liver-pathway` |
| 11 | 08 Putting It All Together | generate | FDN `metaphor-habit-loop-cubes`, `photo-notebook-tracking` |
| 12 | B1 Midlife, Hormones And Digestion | generate | — |
| 13 | B2 Digestion Under Pressure | FDN `diagram-nervous-system-organs` | FDN `diagram-autonomic-balance`, `food-minerals` |
| 14 | B3 When Your System Stays On Alert | generate | FDN `diagram-body-inflammation` |

Roughly 12 to 14 generated images, 20 or so FDN placements.

## Open

- **House style.** Three treatments of the screen-door analogy generated for
  Steve to choose from: flat vector, cut-paper collage, line-and-watercolor.
  Nothing else gets generated until one is picked, so the set stays consistent.
- **Scope.** This plan is one hero per lesson plus inline figures where they
  earn their place. Steve said "almost all of the sections/pages," which could
  instead mean one per `<h3>`, closer to 70 images. Starting with the smaller
  reading; it scales up if he wants it.
- **Upload.** MCP cannot upload files to Kajabi. Every image here, salvaged or
  generated, needs Steve to put it in the media library before the agent can
  place it by URL.
