# Gut Foundations sales page

Sales page for the $27 mini course, the first rung of the value ladder.

- **Page id:** 2152353662 · **Theme id:** 2168000232 · **Slug:** `/gut-foundations`
- **Status:** LIVE since 2026-10-23. https://www.gohappybelly.com/gut-foundations
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

## Went live 2026-10-23

Offer 2151464245 published by Steve, page published straight after. Verified at
publish time:

- Offer is `published`, **$27.00 one_time** (not the subscription misconfiguration
  found on two other checkouts), course 2149609329 attached
- `checkout_url` still `/offers/yYfiaNgo/checkout`, so every CTA on the page is live
- Post-purchase points at landing page 2152353598, the Gut Foundations thank-you page
- All eight image URLs on the page return 200
- SEO metadata set at publish: title and description. **The share image was
  not**, and still is not. See "The share image, and an MCP dead end" below

## Fixed 2026-10-26

### The two-column "is and is not" row shipped broken

Section `1792070000004` rendered its two cards as narrow strips hugging the left
edge with half the page blank, and had done since launch. Cause: `.gh-grid-2`
carried `display: grid; grid-template-columns: 1fr 1fr`, but a `custom_classes`
value lands on the block *wrapper*, not on the flex row Nova renders inside it.
So the wrapper became the two-column grid, its single child (the row) took
column one, column two rendered empty, and the flex row then split that half
into two quarters.

The fix leaves the row alone and sizes the cards: wrapper and row at `width:
100%`, each `.gh-card` at `flex: 1 1 0; min-width: 0`, column direction under
767px.

This is the second time this trap has been walked into. It was already written
down in `LINK-IN-BIO.md` from the first occurrence, and is now in
`DESIGN-SYSTEM.md` where it will actually be read before building.

### A photograph of Alina in the credential section

Section `1792070000008` held the cut-paper illustration of two chairs turned
toward each other (`reset-qa-with-alina.jpg`). It is a good illustration and it
was the wrong one: the section exists to say who wrote the course, so it should
show her.

`Website/Alina_Fence.jpg` and `Website/IMG_8247.jpg` are on disk but not in the
Kajabi library, and MCP cannot upload. The portrait that is already live on Link
in Bio solved it without an upload:

```
.../themes/2167908665/settings_images/
  c74f5a-84b6-5ad1-ccb7-8b4bc30408_00804c32-ad07-4104-a21a-c23e7ef2733e.jpg
960x1440 JPEG, kitchen, squeezing a lemon into a glass of juice
```

Nova accepts a full CDN URL, so one theme's `settings_images` path serves
another theme's page. That is how the five archetype illustrations already work
on this page.

It is sized rather than left to fill its column. A 2:3 photo at `width: fill`
in a 940px row renders roughly 450x675 and would dominate a section that is
there to support the copy. New `.gh-bio-portrait` hook, following the locked
Link in Bio portrait treatment:

```css
.gh-bio-portrait { flex: 0 0 340px !important; }
.gh-bio-portrait img {
  width: 340px; height: 453px;
  object-fit: cover; object-position: center 12%;
  border-radius: 3px;
  box-shadow: 0 24px 60px rgba(22,46,40,0.14);
}
.gh-bio-copy { flex: 1 1 0 !important; min-width: 0 !important; }
```

`center 12%` rather than Link in Bio's `72% center`: the source is 2:3 and the
target 3:4, so `cover` crops vertically here, not horizontally, and the crop has
to be pulled up to keep her face in frame. Mobile drops to the 260x347 Link in
Bio size and centers.

`.gh-bio-portrait img` sits after `.gh-zig img` in the stylesheet at equal
specificity, so the heavier portrait shadow wins over the illustration shadow.
Fragile if the file is ever reordered; worth a comment there if it moves.

**It is the only photograph on a page otherwise entirely cut-paper.** That reads
as deliberate for the one human moment on the page rather than as an
inconsistency, but it is Steve's call once he has looked at it.

---

## The photoreal banner is in (2026-10-26)

`foundations-hero-b.jpg`, media id **4829069**, 2400x1357. Steve uploaded it;
MCP cannot upload, only hand back an uploader link.

Three placements, all verified by reading back:

| Where | How |
|---|---|
| Hero art, `hs_shot` on section `1792070000001` | `update_theme_content`, image + alt |
| Offer 2151464245, `image` | `replace_media` |
| Course 2149609329, `thumbnail` | `replace_media` |

`replace_media` did the last two in one call, because both pointed at the same
retired cut-paper file (`foundations-laptop`, 4754760, now unused). That tool is
the right instrument whenever an asset is being swapped rather than a slot being
filled: it rewrites every tracked placement at once.

It does **not** catch raw URLs sitting in Nova `image` settings. The hero was
invisible to `where_used` for exactly that reason, which is why it had to be
done by hand with `update_theme_content`. Do not trust a `used_count` of 0 to
mean an asset is unplaced on a Nova page.

The old alt text described the art as "rendered in cut paper". Replaced.

### The share image, and an MCP dead end

`page_image` on landing page 2152353662 is still `null`, so the $27 page shares
with no image into Facebook, iMessage or Slack.

**`update_landing_page` accepts `page_image` and silently discards it.** Tried
twice, once with the full CDN URL and once with the `file-uploads/...` S3 key
that other Kajabi image columns use. Both returned a clean 200 with the field
absent from the response body, and both left `page_image` null with `updated_at`
unmoved. `place_media` is not a way round it either: its own docs say LandingPage
has no image column.

So this one is Steve's, in the admin UI: landing page settings, SEO, social
share image, pick `foundations-hero-b`. Do not burn calls retrying the tool.

---

## Still to do

1. **Point traffic at it.** Nothing links here yet: Link in Bio, the five quiz
   results pages and the archetype email sequences all still route elsewhere.
   Until that is done the page is live but unreachable in practice.
2. Swap the hero art for one of the cut-paper mockups in
   `Website/mockups/foundations/` once uploaded, and move the signpost down to
   the five-patterns heading.
3. Testimonials, when there are any, between the FAQ and the final CTA.
5. **Five cut-paper pattern images are still on this page** (`fp_1i` to `fp_5i`),
   and the hero above them is now photoreal, so the page currently mixes two
   styles. This is the next job, not a later one. Blocked on Steve deciding
   between photoreal metaphors and the symptom moment: `Website/IMAGE-DIRECTION.md`.
6. Set the social share image in the admin UI (see above).
4. **Nobody has seen the page.** Cloudflare returns 403 to this environment on
   every path, so the two fixes of 2026-10-26 are verified only against what the
   theme reads back, not against a render. Steve checks the cards sit side by
   side and the portrait is cropped sensibly on a phone.
