# Gut Reset course: image audit

Course `2148514926`, the $147 product. 9 modules, 70 lessons (61 published,
9 draft). **4 paying members**, unlike Gut Foundations which had none, so
every change here is live to real customers.

Audited 2026-10-27 by downloading all 52 images and opening them, not by
reading alt text. The three contact sheets are in this directory.

## The count is exactly 52

The number in `GUT-RESET-VISUAL-PLAN.md` was right. All are `reset-` prefixed,
all 1600x905 jpg, all cut-paper, all with "in cut-paper collage" in their alt
text.

| Group | Count |
|---|---|
| Module covers (`reset-module-*`) | 9 |
| The five patterns (`reset-pattern-*`) | 5 |
| Lesson images | 38 |

## Six are already built and cost nothing

The five pattern images are **the same five analogies photographed this morning**
for Gut Foundations lesson 03, and the quiz image is the five doors already shot
as that lesson's hero.

| Reset asset | Reuse |
|---|---|
| `reset-pattern-reactive` | `l03-screen-door` |
| `reset-pattern-backed-up` | `l03-basement` |
| `reset-pattern-sugar-driven` | `l03-kitchen` |
| `reset-pattern-underactive` | `l03-stove` |
| `reset-pattern-wired-tired` | `l03-engine` |
| `reset-gut-pattern-quiz` | `hero-l03-doors` |

`reset-gut-liver-loop` is a farmhouse sink and is close to `hero-l07-gut-liver`,
but the Reset version shows the pipes under an open cupboard, which is the point
of that lesson. Treat it as new.

## How these are wired, and why it matters

**Each image is used twice: as the lesson's `poster_image` and again inline in
the lesson body HTML.** This is different from Gut Foundations, where the images
were inline only and `used_count` was 0.

That difference was tested rather than assumed. `replace_media` on
`reset-pattern-reactive` repointed **three `poster_image` fields in one call**
and reported no failures. A follow-up search then found the old filename still
present in **four lesson bodies**, so the inline copies were untouched.

| Job | Tool | Cost |
|---|---|---|
| Poster images | `replace_media`, one call per image | Cheap |
| Inline images + alt text | Full lesson body rewrite | Expensive, and the real bottleneck |

The alt text has to change regardless, because every one of the 52 ends with
"in cut-paper collage" and would be describing an image that no longer exists.
That is the same false-alt-text defect found in Gut Foundations, except here it
would be self-inflicted.

## What has already changed, live

`reset-pattern-reactive` was replaced with `l03-screen-door`. Three lesson
thumbnails now show the photograph. Those lessons still carry the cut-paper
screen door inline in their bodies, so they are half-converted right now. This
is a partial improvement rather than a regression, since Alina rejected the
cut-paper style outright, but it is an inconsistency and it is named here rather
than left to be discovered.

## What the 52 actually are

Opening them, the split is better than the Gut Foundations one: far more of
these are literal still life, which photograph well and need no metaphor work.

| Kind | Roughly | Examples |
|---|---|---|
| **Literal still life or a real scene** | ~31 | Stockpot simmering, amber bottles on a shelf, jar of kraut beside cabbage, blender and fruit, tools on a bench, pots on a windowsill, a made bed, a bathroom, tea cups from above |
| **Metaphor** | ~15 | Cracks across a wall, a fingerpost, stepping stones, five keys on hooks, blank luggage tags, a closed five-bar gate, a jammed water wheel, an overflowing gutter, a lantern at dusk, a kettle boiling hard, a part-rebuilt drystone wall |
| **Already built** | 6 | Above |

The literal ones are the same job as the Gut Foundations heroes and should run at
a similar hit rate. The metaphors need the treatment lesson 03 got: photograph
the real object, and check each frame against the sentence beside it.

## Honest cost

| Step | Volume |
|---|---|
| Generate | ~46 new images |
| Upload | 46 files, Steve, since MCP cannot upload |
| Repoint posters | 52 `replace_media` calls, fast |
| Rewrite bodies | ~50 lesson bodies, slow, and where transcription errors would creep in |

This is several times the size of the twelve heroes done this morning. It is
worth agreeing the pace before spending it.

---

## Wave 1 in progress, 2026-10-27

Steve chose waves, module covers first. Wave 1 is the six that cost nothing.

### Posters: done, 16 placements

Six `replace_media` calls, no failures.

| Old | New | Placements |
|---|---|---|
| `reset-pattern-reactive` | `l03-screen-door` | 3 |
| `reset-pattern-backed-up` | `l03-basement` | 3 |
| `reset-pattern-sugar-driven` | `l03-kitchen` | 3 |
| `reset-pattern-underactive` | `l03-stove` | 3 |
| `reset-pattern-wired-tired` | `l03-engine` | 3 |
| `reset-gut-pattern-quiz` | `hero-l03-doors` | 1 |

### Bodies: 3 of 17 done

**The images were free. The placement is not.** Those six assets appear inline
in seventeen lesson bodies, and each one needs a full rewrite because there is
no partial-update API and the alt text ends "in cut-paper collage" on every one.

| Done | Remaining |
|---|---|
| The Gut Pattern Quiz | The 5 Gut Patterns (carries all five inline) |
| Working With The Reactive Gut | Working With: Sugar-Driven, Underactive, Wired-And-Tired |
| Working With The Bloated And Backed-Up Gut | 5 Shopping List lessons |
| | 5 Three Days Of Meals lessons |

Until the rest are done those lessons show a photographic thumbnail and a
cut-paper image inside. Same subject, different style. Not broken, but
inconsistent, and the reference-shelf pages are the lower-traffic ones so they
are last deliberately.

### A note on reuse across both courses

The five pattern photographs and the five-doors image now appear in both Gut
Foundations and Gut Reset. Someone who owns both will see the same images twice.
That is a deliberate trade: one consistent visual language for the same five
analogies, against six images of generation cost and the risk of two different
screen doors meaning the same thing. Worth revisiting only if Steve dislikes it.

---

## Wave 2 placed, and one body deliberately left alone

### Module covers: 9 posters, 8 of 9 bodies

All nine `replace_media` calls succeeded. Eight of the nine lesson bodies that
carry a cover inline are rewritten with the photograph and honest alt text:
Welcome, What We Are Actually Doing, The 5 Gut Patterns, Weeks 1 to 4, and How
Reintroduction Works.

`The 5 Gut Patterns` was held back until the covers existed so it could be done
in one pass rather than two: it carries the workbench cover **and** all five
pattern images. All six are now correct in a single rewrite.

### The Supplement Reference: stopped on purpose

**`The Supplement Reference` (2201292374) has its poster swapped and its body
left as it was, and that is a judgement rather than an oversight.**

The only change it needs is one `img src` in the first paragraph. But there is
no partial-update API, so making it means hand-reproducing a 400-line document
containing roughly 25 rows of supplement dosing: milligram ranges, durations,
and drug-interaction cautions for berberine, oregano oil, grapefruit seed
extract, betaine HCl and ashwagandha.

Weigh that honestly. The upside is a decorative hero image stops being cut
paper. The downside, if a single number or caution is mistyped, is wrong dosing
information shown to paying customers. That trade is bad, and the risk is one I
cannot fully verify after the fact.

**The safe fix is Steve swapping that one image in the Kajabi admin UI**, which
is two clicks and carries no transcription risk at all. The asset is already in
the library as `mod-reference-shelf`.

This is worth remembering as a general rule for the rest of this conversion:
where a lesson body carries clinical detail, the admin UI beats a rewrite.

### Running total

| | Posters | Bodies |
|---|---|---|
| Wave 1, the six reusable | 16 of 16 | 8 of 17 |
| Wave 2, module covers | 9 of 9 | 8 of 9, one declined |

Wave 1 bodies still to do: four Shopping Lists and five Three Days Of Meals
pages. All are short and carry no clinical detail, so they are low risk.

---

## Waves 1 and 2 complete, 2026-10-27

All nine remaining bodies are done: five Shopping Lists and four Three Days Of
Meals pages, plus the Wired-and-Tired meal plan.

### Verified by filename, not alt text

| Search | Result |
|---|---|
| `reset-pattern-` | **0** across the whole course |
| `reset-module-` | **1**, and it is the known exception |

The single remaining hit is `The Supplement Reference` (2201292374), whose body
was left alone on purpose. Its poster is already the photograph; only the inline
image is stale. The reasoning is above: a 400-line body of supplement dosing is
not worth a hand transcription to swap one decorative image, and the admin UI
does it in two clicks with no risk.

### Where the course stands

| | Done | Left |
|---|---|---|
| The five pattern images | 16 poster placements, 16 bodies | 0 |
| The quiz image | 1 poster, 1 body | 0 |
| Module covers | 9 posters, 8 bodies | 1 body, declined |
| **Cut paper remaining** | | **37 lesson images, plus the one declined body** |

### A note on the small-format treatment

The Shopping List and Three Days Of Meals pages render their pattern image at
`max-width:340px`, centered, rather than full width. That styling was preserved
exactly; only the `src` and the alt text changed. Worth knowing before anyone
"tidies" those into full-width heroes, because the small format is what keeps
a reference page feeling like a reference page.

### Next

Wave 3 is the ~31 literal still lifes, which photograph directly and should run
at the hit rate the module covers just did. Wave 4 is the ~15 metaphors, which
need the lesson 03 treatment: photograph the real object, then check each frame
against the sentence beside it.
