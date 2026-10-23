# Gut Foundations sales page

Sales page for the $27 mini course, the first rung of the value ladder.

- **Page id:** 2152353662 · **Theme id:** 2168000232 · **Slug:** `/gut-foundations`
- **Status:** DRAFT. Stays a draft until the $27 offer (2151464245) is published.
- **Checkout:** `/offers/yYfiaNgo/checkout`
- **Course behind it:** Gut Foundations, course id 2149609329
- Built on `Website/DESIGN-SYSTEM.md`.

---

## Rebuilt 2026-10-23

The first version was rejected. Two separate corrections from Steve, both
recorded here because both are standing rules now.

### Correction 1: it was a copied page, not a designed one

The first build reused the architecture of the thank-you pages written earlier
the same day: eyebrow, centered h1, three stacked prose sections, a short "what
this is not" list, a forest CTA. That is a *confirmation* page shape. Somebody
on a confirmation page has already bought; the page only has to reassure. A
sales page has to argue, and this one never did.

The cause is worth naming because it will recur. The last page built sits in
context fully formed and verified, so it is the cheapest thing to reach for, and
reaching for it takes the whole blob: design system *and* architecture *and*
copy rhythm. Only the first of those should travel.

**Rule: reuse the system, design the page.** The palette, type scale, button
spec, banding and components are shared. Structure and copy are derived from the
offer in front of you, every time.

### Correction 2: stop assuming the reader has had labs

The rejected version opened its second section with "If your labs came back
normal". That is Avatar 1's defining trait, the Dismissed Patient, who has seen
multiple doctors and been told she is fine. She is the **$1,497** buyer:
CLAUDE.md puts her at the highest urgency and the highest willingness to invest.

A $27 front-end offer is the widest net on the ladder and catches people much
earlier than that. Most of them have never had a single test run. Leading with a
lab story tells them the page is not about them.

**Rule: no page may assume the reader has lab results unless the offer itself is
a test.** Avatar 1 framing belongs on the Reset, not on the front end.

### Correction 3: the copy went abstract, and the art was never looked for

The second version was rejected too. Steve: the copy "sounds odd, it's very
vague", and there is "no imagery, no graphics, no visual cues". Both were true
and they had the same cause.

**The copy had drifted one level of abstraction too high.** It argued about
epistemology rather than describing her week: "it is an information problem",
"trying things is not the same as knowing", "you are aiming at something". Those
are propositions. They are how a consultant talks about the problem, not how it
feels at 3pm when the waistband hurts. Compare the $147 sales page, written two
days earlier, which is full of "my safe food list keeps getting shorter" and
"days three to five are the worst, then it drops off a cliff". That page is
good. This one regressed from it.

**The five locked analogies and five locked aha lines went unused.** CLAUDE.md
hands over the car with the engine timing off, the torn screen door, the
squatters in the house, the stove that never gets hot, the bacteria in the wrong
neighborhood, and five aha lines including "The cravings aren't yours. They're
something else's, broadcasting through you." They are pre-approved, they are the
most concrete language the brand owns, and the page used none of them.

**And the art existed.** Fifty-two cut-paper illustrations sit in
`Website/images/gut-reset/` and in the Kajabi media library, five of them
illustrating exactly those five analogies, plus a signpost at a five-way fork
that is the obvious hero for a page about choosing a pattern. A page about the
five patterns shipped with no images while five pictures of the five patterns
sat in the repo.

So this was not a missing skill, and a new one would not have fixed it. The
voice was already demonstrated on the $147 page, the vocabulary was already
locked in CLAUDE.md, and the art was already drawn. All three were in reach and
none were reached for.

**Rule: use the locked analogies and aha lines wherever the five patterns
appear, and inventory the assets before building.** The asset inventory now
lives in `Website/DESIGN-SYSTEM.md`.

---

## Who this page is written for

Four of the seven avatars, by their shared pain rather than one at a time:

| Avatar | What CLAUDE.md says | Why it fits $27 |
|---|---|---|
| 2 · Burned-Out Professional (28-40) | "tried elimination diets and probiotics with partial results. Wants root-cause answers, not more guessing" | "Not more guessing" is the page's whole thesis |
| 3 · Postpartum Rebuilder (28-42) | "Longer conversion path" | A cheap first rung is what a long path needs |
| 4 · Frustrated Dieter (35-55) | "Suspects something deeper is broken" | Has tried diets, not tests |
| 5 · Health-Conscious Optimizer (30-50) | "Close to ready to invest; needs trust-building" | Best fit on the ladder. A $27 purchase is the trust step |

**The shared pain, and the hook:** they have been trying things and nothing
converges. Probiotics, cutting gluten, a cleanse someone swore by. Something
helps for two weeks and then stops. They changed three things at once so they
cannot tell which one mattered. Nobody has explained how the system works, so
every change is a coin flip.

**What the course actually fixes:** it turns guessing into a hypothesis. That is
the honest promise and it needs no labs, no diagnosis and no claim to heal
anything.

Headline:

> The problem is not that you have not tried. It is that nothing told you
> *what* you were working with.

Validates first, names the gap second, and the gap is what the product fills.

---

## Structure (10 sections)

| # | id | Section | BG | Job |
|---|---|---|---|---|
| 1 | `1792070000001` | Hero | `#F8FAF8` | Hook, lead, CTA, **signpost art** |
| 2 | `1792070000006` | Stat Bar | `#162E28` | Chrome. Scope in four facts |
| 3 | `1792070000002` | The drawer | `#EFF7F1` | The pain, in objects |
| 4 | `1792070000007` | The five patterns | `#F8FAF8` | **The centerpiece. 5 illustrated rows** |
| 5 | `1792070000003` | What is inside | `#EFF7F1` | 8 + 3 modules, prompts, group |
| 6 | `1792070000004` | Is and is not | `#F8FAF8` | Two-column cards |
| 7 | `1792070000008` | Who wrote this | `#EFF7F1` | Credential, late, with art |
| 8 | `1792070000009` | FAQ | `#F8FAF8` | Six objections |
| 9 | `1792070000005` | Final CTA | `#162E28` | Close |
| 10 | `1792070000016` | Sticky Mobile CTA | n/a | Fixed buy bar, mobile only |

Eight images on the page. Banding alternates `#F8FAF8` / `#EFF7F1`; forest
appears twice, as the stat bar and the final CTA.

### The five patterns section is the page

Five alternating rows, each one art on one side and copy on the other, flipping
sides down the page (`gh-zig` / `gh-zig-flip`). Every row carries, in order: a
numbered eyebrow, the pattern name, **one line in her words**, Alina's locked
analogy, and the locked aha line in a sage-bordered Playfair italic (`gh-aha`).

| # | Pattern | Her line | Art |
|---|---|---|---|
| 01 | Wired-and-Tired | "Same lunch on a calm day and a bad day, and only one of them hurts." | Car, hood up |
| 02 | Reactive | "My safe food list keeps getting shorter." | Torn screen door |
| 03 | Sugar-Driven | "The 3pm craving does not feel like a choice I am making." | Ransacked kitchen |
| 04 | Underactive | "Food sits like a stone for hours." | Unlit stove |
| 05 | Bloated and Backed-Up | "Flat in the morning, bloated by evening. Every day." | Flooded basement |

Closes on: *"Four of these are not you. Working out which one is, is the whole
job, and it is what the eleven lessons are for."*

**This section is also the ladder's dividing line.** Gut Foundations explains
what each pattern *is*. The $147 Gut Reset Course says what to *do* about it,
week by week. The two pages cover the same five patterns and must not say the
same things about them: explanation here, prescription there.

### Other decisions

- **Credential comes late**, at section 7, not section 2. Her question at the
  top of the page is whether it is about her, not who Alina is. It also carries
  the price justification: the hour she used to spend at the start of every
  client call, written down, for $27.
- **The pain section is made of objects**, not propositions. The drawer of
  half-finished bottles, two-thirds full. Which jeans not to wear after lunch.
  Three things changed in the same week.
- **The FAQ answers "should I buy this or the $147 course"** directly, because
  the ladder only works if the rungs are legible.
- **Sticky mobile buy bar**, matching the $147 page, which had one while this
  page did not.

---

## Facts the copy commits to

All verified against course 2149609329 before writing.

- **Eleven lessons sold.** Eight foundations plus three bonus modules. The
  course holds 14 published lessons; the three in Start Here are front matter
  and are not counted in the sell.
- **No video anywhere.** Every lesson is `media: none`. Said plainly three
  times, in the stat bar, the is/is-not column and the FAQ, rather than left
  for the buyer to discover after paying.
- **About ten minutes per lesson, about two hours in total.**
- **Twelve reflection prompts.**
- **Private group included.**
- **Lifetime access**, phrased as "yours to keep" and "access does not expire".

No testimonials on the page. There are none for this course yet. When there
are, they go between the FAQ and the final CTA in a terracotta-left-border card.

---

## Compliance

Nothing diagnoses the reader. The patterns are described as patterns, the
is/is-not column says the course "is clear about what a pattern can and cannot
tell you", and there is no claim to heal, seal, cure or treat. Alina is named a
Functional Diagnostic Nutrition Practitioner, which is her credential, not a
claim about the reader. Checked for em dashes and the banned word list: clean.

---

## Still to do

1. Publish the $27 offer 2151464245, then publish this page.
2. Point traffic at `/gut-foundations`: Link in Bio, quiz results pages, the
   archetype email sequences.
3. A real photograph of Alina. The credential section currently uses an
   illustration; `Website/Alina_Fence.jpg` and `Website/IMG_8247.jpg` exist on
   disk but are not in the Kajabi library, and MCP cannot upload.
