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

## Structure (9 sections)

| # | id | Section | BG | Job |
|---|---|---|---|---|
| 1 | `1792070000001` | Hero | `#F8FAF8` | Hook, two-line lead, CTA |
| 2 | `1792070000006` | Stat Bar | `#162E28` | Chrome. Scope in four facts |
| 3 | `1792070000002` | The guessing | `#EFF7F1` | The pain, specific and unflattering |
| 4 | `1792070000007` | Five patterns | `#F8FAF8` | Why the internet contradicts itself |
| 5 | `1792070000003` | What is inside | `#EFF7F1` | 8 + 3 modules, prompts, group |
| 6 | `1792070000004` | Is and is not | `#F8FAF8` | Two-column cards |
| 7 | `1792070000008` | Who wrote this | `#EFF7F1` | Credential, late and brief |
| 8 | `1792070000009` | FAQ | `#F8FAF8` | Five objections |
| 9 | `1792070000005` | Final CTA | `#162E28` | Close |

Banding alternates `#F8FAF8` / `#EFF7F1`. Forest appears twice: the stat bar
(chrome, 28px, acting as a rule under the hero, same deviation the $147 page
documents) and the final CTA.

### Decisions inside the structure

- **Credential comes late, not early.** Section 7, not section 2. The reader's
  question at the top of the page is "is this about me", not "who are you". The
  credential only becomes interesting once she believes the diagnosis of her
  problem. It also carries the price justification: "the groundwork, written down
  so you can have it for $27 instead of an hour of her time."
- **"Five patterns, not one problem" is the argument section.** It explains why
  everything she has read disagrees with everything else she has read: the
  patterns want opposite things, so eat-more-fermented-food and
  avoid-fermented-food are both correct, for different people. This reframes her
  past failures as an information problem rather than a willpower problem, which
  is the pivot the sale turns on.
- **Is / is not is two columns, not a list.** Same device as the $147 page
  because it is a system component, with its own content. Sub reads "The
  right-hand column is the reason to believe the left." The no-video admission
  lives here, up front, not buried.
- **The FAQ answers the two real objections.** "Why is it only $27" (it is the
  groundwork, not the plan, and it is meant to be the first thing you buy rather
  than the last) and "Is this just the free quiz" (the quiz gives you an answer,
  this gives you the reasoning, which is what you need when the answer does not
  quite fit). Also: no video, two hours total, and why it does not hand you a
  food list.
- **"Will it tell me what to eat" is answered with a no and a reason.** Removing
  foods before you know your pattern "is how people end up with nine safe foods
  and no answers." Turns a missing feature into a point of discipline, and keeps
  the page clear of protocol promises.

---

## Facts the copy commits to

All verified against course 2149609329 before writing.

- **Eleven lessons sold.** Eight foundations plus three bonus modules. The
  course holds 14 published lessons; the three in Start Here are front matter
  and are not counted in the sell.
- **No video anywhere.** Every lesson is `media: none`. Said plainly twice, in
  the is/is-not column and again in the FAQ, rather than left for the buyer to
  discover after paying.
- **About ten minutes per lesson, about two hours in total.**
- **Twelve reflection prompts.**
- **Private group included.**
- **Lifetime access**, phrased as "yours to keep" and "access does not expire".

No testimonials on the page. There are none for this course yet. When there are,
they go between the FAQ and the final CTA in a terracotta-left-border card.

---

## Compliance

Nothing on the page diagnoses the reader. It describes patterns, says the course
"is clear about what a pattern can and cannot tell you", and makes no claim to
heal, seal, cure or treat. Alina is named a Functional Diagnostic Nutrition
Practitioner, which is her credential, not a claim about the reader. Checked for
em dashes and the banned word list: clean.

---

## Known gap

**No image anywhere on this page.** The course has no thumbnail and there is no
mockup. The hero is a centered column where the $147 hero has a cover shot
beside the copy, and the page would read better with one. Options: a cut-paper
cover in the locked style, or a photo of Alina. Flagged, not resolved.

---

## Still to do

1. Publish the $27 offer 2151464245, then publish this page.
2. Point traffic at `/gut-foundations`: Link in Bio, quiz results pages, the
   archetype email sequences.
3. An image in the hero.
