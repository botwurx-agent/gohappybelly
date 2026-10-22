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

---

## Decisions and build, 2026-10-22

**House style: cut-paper collage** (Steve's pick from three samples).
**Scope: one hero per lesson plus key figures.**

### Locked style string

Every generated image used this verbatim, which is why the set matches. Reuse it
for any future image so new work does not drift:

> Textured cut-paper collage illustration, layered matte paper with visible
> deckled torn edges and soft drop shadows. Strict limited palette: sage green
> #7AAE86, deep forest green #162E28, terracotta #C07A5A, warm off-white
> #F8FAF8. Handmade, tactile, warm and reassuring rather than clinical.
> Absolutely no text, no words, no letters, no numbers, no labels, no signage.
> No people, no faces, no hands.

Model `gpt_image_2`, 16:9, 2k, quality high. About 6.5 credits each.

### The five archetype analogies, now drawn

These are the asset worth the most beyond this course. They are brand property
and belong in the quiz results pages, the 35 archetype emails and social.

| Archetype | File | What it shows |
|---|---|---|
| Wired-and-Tired | `analogy-1-wired-tired-engine-timing` | a timing belt and gears, one gear rotated out of the belt path |
| Reactive | `analogy-2-reactive-screen-door` | a screen door torn with holes, light coming through |
| Sugar-Driven | `analogy-3-sugar-driven-squatters` | a lit house, door ajar, someone else's crates on the porch, a crumb trail |
| Underactive | `analogy-4-underactive-cold-stove` | a full pan on an unlit burner, dial off, no steam |
| Bloated and Backed-Up | `analogy-5-backed-up-flooded-basement` | standing water, a dripping pipe, a bucket already overflowing |

### Lesson heroes generated

`hero-start-here`, `hero-scope-gate` (What I Can And Cannot Do Here),
`hero-03-five-doors`, `hero-04-everyday-habits`, `hero-08-orchestra` (drawn to
match module 08's own orchestra line), `hero-B1-midlife-tree`,
`hero-B3-house-lights-on` (every window lit, nothing switched off).

### Folders

| Folder | Contents |
|---|---|
| `images/fdn/` | 48 salvaged deck images, full resolution |
| `images/generated/` | 12 generated images, full resolution (2688x1520) |
| `images/web/` | **upload this one.** 60 files, 24MB, resized and stripped |
| `images/style-samples/` | the three rejected style tests, kept for reference |

Originals are kept because the web copies are lossy and capped in size.

### One miss worth noting

`hero-04-everyday-habits` was asked for a wall clock with a blank face. It
rendered the clock as an empty round frame, so the time-of-day meaning is gone.
The image still works as a calm-morning scene. Not worth a regeneration unless
Steve wants the clock back.

### Blocked on Steve

MCP cannot upload files to Kajabi; `add_media` only returns an uploader link.
All 60 files in `images/web/` need uploading to the media library in one go,
after which the agent can place them into lesson bodies by URL.

**Do not reference the Higgsfield CDN URLs directly in lesson HTML.** They are
unsigned and look stable, but they are someone else's CDN and a purge would
break images inside a paid product.

---

## Placed, 2026-10-22

29 images placed across 13 of the 14 lessons. Only "Who Is Teaching This" is
without one, deliberately: it wants Alina's photograph, which Steve has.

### The two treatments

The salvaged FDN images are a different visual language from the generated
cut-paper set, and no amount of wishing makes them match. Rather than hide that,
the layout makes it deliberate:

**Cut-paper images run full width**, no border, 3px radius. These are the lesson
heroes and the five analogies. They read as part of the page.

**FDN images sit inside a bordered figure**, `1px solid #C8DDD0` on `#F8FAF8`,
centered, with a 12px caption in `#6A8278` underneath. They read as reference
figures, which is what they are. The frame is why the mixture looks intentional
instead of accidental.

Every image carries real alt text describing what is shown, not the filename.

### Per lesson

| Lesson | Hero | Figures |
|---|---|---|
| Start Here | `hero-start-here` | — |
| Who Is Teaching This | *(awaiting Alina's photo)* | — |
| What I Can And Cannot Do Here | `hero-scope-gate` | — |
| 01 Understanding Your Gut | *(framed)* `diagram-digestive-anatomy` | `diagram-gut-lining-villi`, `diagram-gut-barrier` |
| 02 Whole-Body Health | *(framed)* `diagram-gut-health-venn` | `diagram-organs-labeled` |
| 03 The Five Common Patterns | `hero-03-five-doors` | **all five analogies**, one per archetype |
| 04 Everyday Habits | `hero-04-everyday-habits` | `metaphor-habit-loop-cubes` |
| 05 Nutrition Foundations | *(framed)* `illus-intestine-with-foods` | `food-fiber-flatlay`, `food-fermented-jars` |
| 06 The Gut-Brain Connection | *(framed)* `illus-gut-brain-dark` | `metaphor-two-way-cans`, `diagram-autonomic-balance` |
| 07 The Gut-Liver Connection | *(framed)* `diagram-liver-in-body` | `diagram-liver-pathway` |
| 08 Putting It All Together | `hero-08-orchestra` | `photo-notebook-tracking` |
| B1 Midlife | `hero-B1-midlife-tree` | `diagram-liver-gallbladder` |
| B2 Digestion Under Pressure | *(framed)* `diagram-nervous-system-organs` | `food-minerals` |
| B3 When Your System Stays On Alert | `hero-B3-house-lights-on` | `diagram-body-inflammation` |

In module 03 each analogy sits between the archetype's description and its sage
callout box, so the picture lands before the words name it.

### Verified

- All 24 distinct image URLs return 206 to a ranged request. None is a 404.
- `search_course_content` for `kajabi-cdn` returns 13 lessons, matching the plan.
- Every write used `lesson_body_format: "html"`; without it the HTML is
  re-parsed as markdown and the markup is destroyed.

### Duplicates in the media library

Steve warned he may have uploaded some twice. Six pairs confirmed, identical
file sizes:

`hero-B1-midlife-tree`, `hero-08-orchestra`, `diagram-liver-gallbladder`,
`diagram-body-inflammation`, `illus-intestine-with-foods`, `illus-happy-sad-gut`,
`metaphor-detective`, `metaphor-blueprint-gears`.

The newer ID of each pair is the one referenced. **Nothing was deleted.** The
spares are harmless, show `used_count: 0`, and are Steve's to clear whenever he
wants: Media Library, filter to unused.

### Six lessons lead with a framed diagram rather than a cut-paper hero

01, 02, 05, 06, 07 and B2. They look deliberate, but they are not as strong as
the seven that open with a generated image. Six more cut-paper heroes would cost
about 39 credits and ten minutes, and would make every lesson open the same way.
Worth doing before launch if Steve wants it.

### Still unused from the salvage

About 20 FDN images remain unplaced, among them `illus-happy-sad-gut`,
`metaphor-detective`, `metaphor-blueprint-gears`, `icons-allergens`,
`food-buddha-bowl`, `food-produce-flatlay` and the decorative microbe set. They
are in the library and in `images/fdn/` if a second pass wants them.

---

## The six remaining heroes, 2026-10-22

Six lessons were opening with a framed FDN diagram rather than a cut-paper hero.
All six now have one, generated against the same locked style string so the set
stays consistent.

Where the lesson already had its own analogy, that was drawn rather than
inventing a new one.

| Lesson | Hero | Why this subject |
|---|---|---|
| 01 Understanding Your Gut | `hero-01-sieve` | a fine sieve over a bowl, grain passing through and larger pieces staying behind. The selective barrier, in a vessel rather than a wall, so it does not repeat the screen door |
| 02 Whole-Body Health | `hero-02-smoke-alarm-toast` | **the lesson's own analogy.** Toast in a toaster with a smoke alarm above it. Nothing is burning down |
| 05 Nutrition Foundations | `hero-05-laid-table` | an overhead table laid with a composed plate, a jar of ferment, berries, nuts and vegetables. Variety is the lesson's point |
| 06 The Gut-Brain Connection | `hero-06-two-houses-lit-line` | two houses on a hillside joined by one taut line of lights, lit at both ends. A line that runs both ways |
| 07 The Gut-Liver Connection | `hero-07-sink-and-drain` | **the lesson's own analogy.** A sink with the tap running and the water draining freely. The liver is the sink, the gut is the drain |
| B2 Digestion Under Pressure | `hero-B2-untouched-plate` | a chair pushed back from an untouched meal in a still room. Eating interrupted, which is the whole module |

Every lesson in the course now opens with a cut-paper image except **Who Is
Teaching This**, which is waiting on Alina's photograph.

### Still blocked on upload

MCP cannot upload to Kajabi. The six web-sized files are in `images/web/` and in
`gut-foundations-heroes-2.zip`. Once they are in the media library the agent
places them, and demotes each lesson's current framed diagram from the top of
the page to an inline position where it supports the relevant section instead of
leading.

### The six placed, 2026-10-22

All six uploaded cleanly, one copy each, no new duplicates.

Each lesson now opens with its cut-paper hero, and the FDN diagram that was
previously leading the page has dropped to where it belongs:

| Lesson | Hero at top | Demoted diagram moved to |
|---|---|---|
| 01 Understanding Your Gut | sieve | `diagram-digestive-anatomy` now sits under "What We Mean By Your Gut", beside the one-continuous-tube paragraph it illustrates |
| 02 Whole-Body Health | smoke alarm and toast | `diagram-gut-health-venn` moved to the *end*, after the five areas, where it works as a summary rather than an opener |
| 05 Nutrition Foundations | laid table | `illus-intestine-with-foods` now sits under "Every Meal Is An Input" |
| 06 The Gut-Brain Connection | two houses, one lit line | `illus-gut-brain-dark` now sits under "A Line That Runs Both Ways" |
| 07 The Gut-Liver Connection | sink and drain | `diagram-liver-in-body` now sits under "The Part Nobody Mentions" |
| B2 Digestion Under Pressure | untouched plate | `diagram-nervous-system-organs` now sits under "What Chronic Pressure Actually Does" |

**One figure was removed, not moved.** Module 06 had `metaphor-two-way-cans`, a
tin-can telephone. The new hero is two houses joined by a single lit line, which
is the same idea in the house style. Running both would have made the same point
twice on one page, so the cans came out. The asset is still in the library and
in `images/fdn/` if it is wanted elsewhere.

**Verified:** all six new URLs return 206, `two-way-cans` returns 0 results
across the course, and a search for `hero-` returns 13 lessons, which is every
lesson except **Who Is Teaching This**.

### The course is now visually complete

14 lessons. 13 open with a cut-paper hero. The fourteenth is waiting on Alina's
photograph, which is the only image in this course the agent cannot make.
