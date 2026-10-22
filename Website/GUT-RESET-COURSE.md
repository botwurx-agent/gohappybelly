# Gut Reset Course sales page

| | |
|---|---|
| Page | `2152348302` |
| Theme | `2167971291` (Nova, `nova_blank` preset) |
| URL | `https://www.gohappybelly.com/gut-reset-course` |
| Status | **Published** |
| Offer | `2149370663`, published, $147 one time |
| Checkout | `/offers/jmFpFL5m/checkout` |
| Replaces | `2150211650` `/happier-belly-gut-reset`, unpublished 2026-10-21 |

## Design intent

Built on `Website/DESIGN-SYSTEM.md`, but **composed from the system rather than
copied from another page.** The first build of this page was a near-clone of The Gut Fix: same
hero shape, same forest symptom band, same three-up card grids, same portrait About row, same
two-panel is/is-not. Steve called it, correctly, and also caught that the About paragraph was
close to word-for-word from that page.

A design system is a palette, a type scale and a component vocabulary. It should produce pages
that look like relatives, not pages with the same skeleton. What differs here, and why:

| Element | Elsewhere on the site | Here | Why |
|---|---|---|---|
| Hero | 50/50 split with a product image, or centred | 50/50, headline against a generated course mockup, with the four numbers pulled out into a thin forest stat bar beneath | A course has no product shot, so one is generated from the real UI. The numbers work harder as a rule between the hero and the first section than as a rail inside it |
| The five patterns | Card grid | **Correspondence table**: her sentence left, the answer right | The product's whole claim is that these two columns differ per person. The page sets them side by side instead of asserting it |
| The weeks | Three-up cards | **Vertical step spine** using the system's step divider | Four weeks are a sequence, not a set. The system already had this component and no page had used it |
| About | Portrait + third-person bio | **A signed letter**, no portrait | The bio is on two other pages already. This answers a different question, and uses the locked sign-off, which no other page does |
| Proof | Plain quote cards | Quote cards to the **system's actual spec**, with the 60px Playfair quotation mark at 18% sage | The spec existed; the first build simplified it away |

## The methodology

At $1,497 the sales mechanism is the free call. At $147 there is no call, so the page does the
call's job alone, ordered as the questions a buyer asks silently, because she stops reading at the
first one left unanswered.

| # | Question | Section |
|---|---|---|
| 1 | Is this me? | Hero |
| 2 | Which problem do I actually have? | One of these is your week |
| 3 | Why has nothing worked? | One bowl of lentil soup, five right answers |
| 4 | What do I actually do? | The four weeks, in order |
| 5 | What else is in it? | And the parts you keep going back to |
| 6 | What does it cost, and what is the risk? | Offer panel |
| 7 | Can I trust her? | A note from Alina, then the testimonials |
| 8 | What is this *not*? | Is and is not |
| 9 | Remaining objections | FAQ |
| 10 | Decide | Final CTA |

### CTA placement

Earned, not sprinkled: one after each section that creates belief, never between two that are both
still building it.

| Placement | Variant |
|---|---|
| Header | standard, small |
| Hero | standard |
| After the correspondence table | standard |
| Offer panel | **`gh-cta-strong`**, the one per page |
| Final CTA | standard |
| Sticky mobile bar | standard, full width |

## The hero mockup and stat bar

The hero carries `Website/mockups/course-hero-laptop.png` (Kajabi media `4689230`), a
photoreal laptop on a desk with the real course dashboard composited into the screen. The
scene is generated; the screen is not. See `Website/mockups/README.md` for how the chroma
key works, and for the warning to rebuild it whenever a module is renamed.

It replaced `course-mockup-angled.png`, a drawn facsimile that read too small in the column
and carried a phone and a printed tracker alongside the desktop, which split the attention
the hero has to spend on one thing.

Kajabi media URLs differ by type, which matters:

- **Images** come back as a clean permanent CDN URL with no signing.
- **Files** come back signed with a 7-day expiry, and the unsigned path is 403.

So an image can be referenced directly in a theme; a PDF cannot, and has to be attached as a
lesson download instead.

The photo is opaque and carries no shadow of its own, so the page gives it the design
system's hero image treatment: 3px radius, `0 24px 60px rgba(22,46,40,0.14)`. Nova's
`image-wrapper` ships Tailwind `overflow-hidden`, which clips that shadow flush to the
photo, so the wrapper needs `overflow: visible !important` on the same rule.

The block's own padding is zeroed in its block settings, not in CSS, per the gutter finding
below. At 1440 that leaves the image 659x371 against a 513px text column, so the graphic
reads larger than the copy, which is what the hero needs.

**It must not overrun its column.** An earlier version let it run 118% wide to read larger;
the section clips at the content width, so the right edge was simply cut off. The clip line
read as a grey seam around the image.

The stat bar is a deliberate deviation from the banding rule, which reserves forest for the
validation band and the final CTA. This is chrome, 82px tall, acting as a rule between the
hero and the first light section. On a phone four nowrap stats stacked to 326px, which is a
block rather than a bar, so they go two-up with wrapping labels: 170px.

## Platform findings, the hard way

These cost render cycles. Written down so the next page does not pay again.

- **Nova landing pages do not inject `custom_js`.** It saves to the theme and never reaches the
  page. Verified by grepping the rendered HTML for a unique string from the script.
- **The rich-text field strips `span`, `id`, `class`, and in-page anchor hrefs.** External `href`s
  survive. Verified with a deliberate probe block. Block-level `custom_classes` are unaffected,
  because those are a block setting rather than markup.
- Those two together mean **no interactivity is possible on this surface**: not scripted, and not
  a CSS `:target` or checkbox trick either, since both need ids or anchors. The first draft of this
  page had a working pattern picker designed; it had to be rebuilt as the static correspondence
  table, which is the better design anyway.
- **Specificity trap.** A desktop rule written `> *:first-child` outranks a mobile override written
  `> *`, even with `!important` on both, because the pseudo-class adds specificity. The hero rail
  and the correspondence rows both stayed in narrow columns on mobile until the stacking overrides
  repeated the same pseudo-classes. Fixing it cut 2,170px off the mobile page.
- **Nova's default-gutter reset beats a one-class rule.** `.nova-block.md\:pt-\[10px\]` is two
  classes with `!important`, so `.gh-rail { padding-left }` loses. Per-block padding belongs in the
  block's own settings.
- **The public page is cached.** Two screenshot rounds showed stale content after confirmed writes.
  Append a cache-busting query string when verifying.

## Verified

Rendered and inspected at 1440 and 390 with a cache-buster, not asserted from JSON:

- No horizontal overflow at either width.
- 5 correspondence rows present, 0 leftover elements from the replaced section.
- Hero rail, correspondence rows, offer panel and reference grid all stack full width on mobile.
- Step spine, quotation marks and the sticky bar all render.
- `/gut-reset-course` 200, `/happier-belly-gut-reset` 404, checkout 200.

Chromium would not trust the session's egress CA, so screenshots pin that CA by its public-key
hash (`--ignore-certificate-errors-spki-list`) rather than disabling certificate verification.

## Honesty decisions

- **Testimonials are labelled "1:1 client"**, with a closing line saying plainly that 1:1 includes
  testing and calls, that the course is a different thing at a different price, and that results
  differ. All three quotes are from coaching clients; there are no course testimonials yet.
- **The letter protects the $1,497** rather than undercutting it: it says outright that a $147
  course does not replace a practitioner, and that its value for the women who do need testing is
  arriving with four weeks of evidence instead of a vague history.
- **The FAQ sends people away** where that is the right answer.
- **No unsubstantiated numbers.** The only figures are counts of what is in the course, plus the
  GI-MAP's own $497 price as the anchor.

## Open

**Terms copy reads "One payment of $147. Nothing recurring."** That matches offer `2149370663` as
configured (`payment_type: single`). Steve's intent is one payment then annual auto-renew, which
the course FAQ already promises. Until the offer is converted to a subscription the page states
the one-time terms, because a renewal claim against a non-renewing offer is false at the point of
sale.

On conversion, replace block `1792100000005 > rs_panel > op_price > op_p2` with:

> $147 today, then $147 a year unless you cancel. Cancel any time from your account, and you keep
> access to the end of the year you paid for.

A renewing charge needs price, interval and cancellation route beside the button, not in an FAQ.

**Not mine to do:** the offer is titled "Happier Belly Gut Reset Program" while the site says Gut
Reset Course, and the buyer meets that mismatch on the payment screen. `/happier-belly-gut-reset`
now 404s and Kajabi redirects are not reachable through MCP. The page is not in the main menu.

## 2026-10-21: hero image swapped

`course-hero-laptop.png` is live. Rendered and measured at 1440 and 390 with a cache-buster,
not asserted from the write returning `updated: true`:

| | 1440 | 390 |
|---|---|---|
| Horizontal overflow | none (`scrollWidth` 1440 = `clientWidth`) | none (390 = 390) |
| Image box | 659 x 371 at x 673 | 350 x 197 at x 20 |
| Text column | 513 at x 108 | 350, stacked above |
| Wrapper `overflow` | `visible` | `visible` |
| Computed shadow / radius | `rgba(22,46,40,0.14) 0 24px 60px` / `3px` | same |

The CSS was diffed line by line against the previously rendered page before and after the
write: two hunks, both intended. `custom_css` is a single string setting, so a deep merge
replaces the whole thing, and an edit made by retyping rather than diffing is how a page
silently loses a rule.

## 2026-10-21: in the main menu

Added to the Kajabi **Main Menu** navbar (`2148458013`) as link `2151213502`, a
`LandingPageLink` to `gid://kajabi-portals/LandingPage/2152348302`, then reordered to sit
second: Home, Gut Reset Course, Private Coaching, Shop. Price order, ascending, which puts
the cheapest paid offer where it gets scanned first.

**One edit covers the whole site.** The Nova landing page headers read the same navbar as
the Encore website header; they do not carry their own hardcoded menu. That is not obvious
from the rendered markup, which inlines the items as plain `<li><a>` with no sign of where
they came from, and a first grep for `>Gut Reset Course<` on one line found nothing because
Nova breaks the anchor across lines. Checked properly, all five Nova pages and the home page
picked it up with no further writes.

Verified on the live pages: Home, Private Coaching, Shop, The Gut Fix, Link in Bio and the
sales page itself all show four items. Header holds without wrapping at 1440 and at 1024,
where it is tightest because the page's own terracotta CTA sits beside it. The mobile drawer
lists it too.

---

## Week 1 rebuilt, 2026-10-22

Steve sent a voice note of the Week 1 video and flagged that it did not match
the written week. He was right, and the cause was worse than a wording problem.

**Five of the eight Week 1 sections were sitting in draft**, invisible to
members, while the video promised all eight. They had been retitled into pattern
language and never rewritten: the titles said "Reactive Gut Pattern", the bodies
were still the original FDN leaky-gut text, untouched. Week 3 was fully rebuilt
and Week 2 mostly, so Week 1 was the least finished week in the course.

Published, rewritten, and reordered into the video's running order:

| Position | Lesson | Was |
|---|---|---|
| 0 | Week 1: Take The Pressure Off *(video)* | already published |
| 1 | What The Reactive Gut Pattern Is, And What "Leaky Gut" Means | draft, Section 2/8 |
| 2 | The 11 Signs Of The Reactive Gut Pattern | draft, Section 3/8 |
| 3 | How Your Digestive System Works | already published |
| 4 | Week 1: This Week For Your Pattern | already published |
| 5 | Ten Supplements That Support The Gut Barrier | draft, Section 6/8 |
| 6 | The Named Diets, And Why This Course Does Not Pick One | draft, Section 7/8 |
| 7 | Stress And Your Gut Microbiome | draft, Section 8/8 |

The "Section N/8" numbering is gone, matching how Weeks 2 and 3 were rebuilt.

### What was wrong with the source text, beyond the terminology

- **Section 3/8** was headed **"11 Signs You Have Leaky Gut"**, the exact banned
  construction, and attributed rheumatoid arthritis, lupus and Hashimoto's to it,
  closing by telling the reader to "develop a treatment plan".
- **Section 7/8** promoted **clean keto** at length as good for the gut lining.
  That argues against this course's own position, is low in the plant fiber a
  strained lining needs, and is aimed at the exact avatar who has already failed
  keto. Rewritten as why this course does not pick a named diet.
- **Section 8/8 was raw ChatGPT output with the chat markup still in it**:
  `data-message-author-role="assistant"`, `group/conversation-turn`,
  `prose dark:prose-invert`, and the model's own **"Outline"** section left
  pasted at the bottom. Publishing it would have shown a buyer the scaffolding
  of an AI chat session inside a $147 product.
- **Section 6/8** put all ten supplements in Week 1, contradicting the course's
  own sequence of subtract in Week 1, rebuild in Week 2. The rewrite leads with
  the timing and says plainly that nothing new starts this week.

### Still draft elsewhere, and worth checking against their own videos

Four look like genuine gaps rather than superseded content:

| Lesson | Module |
|---|---|
| Options For Vegetarians & Vegans | Your Pattern, In Detail |
| Week 2: Section 2/8: 5 Foods That Support The Gut Barrier | Week 2 |
| Week 2: Section 6/8: Tips For Reducing Stress | Week 2 |
| Week 4: Section 3/6: Support Your Liver | Week 4 |

These are superseded and can stay as they are: Section 4/8 and 8/8 of Week 2
(replaced by "Collagen: What It Is And Whether You Need It" and "What Works
Against Your Gut Bacteria"), the duplicate Reintroduction Tracker in Week 4, and
the old combined Shopping List, replaced by five per-pattern lists.

**Week 2's Section 8/8 also still contains the ChatGPT markup.** It is draft and
superseded, so it is harmless, but it should not be published as-is.

### Week 2 Section 8/8 emptied, 2026-10-22

Steve asked for the ChatGPT markup to be cleaned out of this lesson. Reading it
against its published replacement changed the answer.

**It is fully superseded.** "What Works Against Your Gut Bacteria", published in
the same module, covers every sound point it made and adds the one it missed
completely: that a narrow diet held for months is itself among the biggest
things working against your bacteria. That is the most useful idea on the topic
and the old version does not contain it.

**Its four unique points are its four worst.** Cleaning it up would have produced
a second lesson on the same subject whose only distinguishing content was:

| Claim | Problem |
|---|---|
| GMO crops have "pesticides and herbicides embedded in their DNA" | Factually wrong. Not how any of it works, and the kind of error that costs a practitioner credibility with the one reader who knows better |
| Tap water chlorine and fluoride wipe out the microbiome | Not supported at drinking-water concentrations, and it closes by recommending a filter purchase |
| Limit grains "until your gut is healed" | Argues against this course's own position, and uses a healing claim |
| Switch household and personal care products | Thin evidence, drifts into product recommendations outside the course's scope |

It also carried **"If you have leaky gut"**, the banned construction, and the
ChatGPT page markup.

So the body was replaced with an internal note rather than rewritten, the title
prefixed `[Superseded]`, and the lesson left in draft. **The MCP cannot delete a
lesson**, so Steve can remove it in the admin whenever he wants; until then
nothing publishable survives in it.

### Site-wide sweep for pasted AI markup

Searched every lesson on the site, drafts included, for four ChatGPT page
signatures: `data-message-author-role`, `conversation-turn`, `prose-invert`,
`text-token-text-primary`.

**Two lessons had it, both now dealt with:** Week 1 Section 8/8, rewritten and
published, and this one. No others anywhere on the site.

### British spelling sweep, 2026-10-22

Steve caught **"draught"** in the Week 1 barrier lesson. Checking for others
found two more, one of them a repeat of an error fixed earlier the same day.

| Word | Lesson | Fixed to |
|---|---|---|
| draught | What The Reactive Gut Pattern Is | draft |
| **fortnight** | Stress And Your Gut Microbiome | two weeks |
| recognise | Questions People Ask | recognize |

**The fortnight one is the bad one.** Earlier today a sweep found 21 instances of
that exact word across five content surfaces and fixed every one, including
renaming a module for it. Hours later the agent typed it again into a brand new
lesson. Finding and fixing an error is not the same as learning it.

`recognise` was in pre-existing published copy, so the earlier sweep missed it
too. That sweep searched for `fortnight` specifically rather than for British
spellings as a class.

Searched and clean: realise, recognise, colour, behaviour, practise, fibre,
flavour, favour, grey, amongst, learnt, optimise, whilst.

**Rule for next time:** after writing any new customer-facing copy, run the
spelling check as a class rather than re-checking the one word that was wrong
last time. The word that catches you is never the word you are looking for.

### Weeks 2, 3 and 4 checked against their videos, 2026-10-22

Steve supplied the Week 2, 3 and 4 transcripts. Each week's published lessons
were mapped against what Alina promises on camera.

**Week 2 video:** foods to heal leaky gut, apple cider vinegar, collagen, bone
broth, tips for reducing stress, probiotics versus prebiotics, what destroys
good bacteria.

| Promised | Status |
|---|---|
| Foods to support the barrier | **was the one real gap.** Rewritten and published as "Five Foods That Support The Gut Barrier" |
| Apple cider vinegar | published |
| Collagen | published |
| Bone broth | published |
| Tips for reducing stress | covered, but in Week 1 and Week 3 rather than Week 2 |
| Probiotics versus prebiotics | published |
| What destroys good bacteria | published, as "What Works Against Your Gut Bacteria" |

**Week 3 video:** chronic digestive issues, bowel movements and what is normal,
gut healing smoothies, fermenting vegetables, adrenal fatigue, leaky gut,
constipation and chronic diarrhea. **Complete.** All seven are published, and
Week 3 carries no drafts at all. It is the most finished week in the course.

Worth noting: "adrenal fatigue" from the video became **Stress, Tiredness And
Your Gut** in the written course, and the term itself appears nowhere. That is
the right call and should stay that way. Adrenal fatigue is not a recognized
diagnosis, and using it would put Alina in exactly the position the compliance
rule exists to avoid. The mechanism is covered without the label.

**Week 4 video:** a strong microbiome supporting probiotic growth, nature and
eating dirt, fasting, gratitude. **Complete.** The microbiome topic is carried
by the Week 4 lesson body itself, the 30-plants count, plus "Getting Outside,
And The Dirt Question". Fasting is "Giving Your Gut A Break". Gratitude has its
own lesson.

### The remaining question is not a video mismatch

**Week 4: Section 3/6: Support Your Liver** is still draft, and no video promises
it, so it is not a gap in the sense the other five were. It is worth a decision
anyway, because of an inversion it creates:

**The $27 mini course has a full gut-liver module. The $147 course has no liver
lesson at all**, only a passing mention of bile inside "How Your Digestive System
Works". The cheaper product covers something the more expensive one does not.

The draft would need the same rewrite as the other five before it could ship.
It opens on "filtering out toxins", which is the detox framing this course
otherwise avoids.

### Draft inventory after this pass

| Lesson | Why it is still draft |
|---|---|
| Week 4: Section 3/6: Support Your Liver | real content, awaiting Steve's decision |
| Options For Vegetarians & Vegans | not promised by any video, vegetarian guidance is already on each pattern page |
| Week 2: Section 4/8: Benefits Of A Collagen Supplement | superseded by the published collagen lesson |
| Week 2: Section 6/8: Tips For Reducing Stress | superseded, body already a marker |
| Week 2: Section 8/8: What Destroys Good Bacteria | superseded, emptied |
| Week 4: Your Reintroduction Tracker | duplicate of the published one |
| Section 1/2: Shopping List | superseded by five per-pattern lists |
| Section 2/2: Advanced Goal Weight Calculator | dropped deliberately |

Nothing in that list is a hole in what a buyer was promised.

### The liver lesson rewritten and moved to Week 3, 2026-10-22

Steve left the placement to the agent. It went to **Week 3: Digestion Itself**,
at position 2, directly after the pattern page and ahead of the three lessons on
what comes out.

**Why Week 3 and not Week 4.** Week 4 is about widening range, time outdoors,
fasting and gratitude; the liver belongs to none of those. Week 3 already owns
clearance, with "Bowel Movements: What Is Normal", "When Things Are Not Moving"
and "When Things Are Too Loose". The liver story is the missing reason behind
all three: the gut is the liver's exit route, so a skipped day is not only a
comfort problem. Placing it ahead of those three makes them land differently.

**The API cannot move a lesson between modules.** Addressing lesson
`2178660602` under a different module id returns "Record not found". So the new
lesson was created in Week 3 (`2201347203`, published) and the Week 4 original
retitled `[Superseded]` and left in draft. Steve can delete it; MCP cannot.

**Why the original could not be reused.** It was built on the detox framing this
course rejects: "filtering out toxins", dandelion to "flush out toxins", lemon
water to "flush out toxins", microgreen chlorophyll "cleansing the liver", milk
thistle to "repair liver cells".

The replacement takes the opposite position, and says so out loud: the liver is
the thing that does the detoxing, it is not clogged, and the useful question is
whether its exit route is open. It then goes through milk thistle, dandelion,
lemon water and juice cleanses one by one and says what each actually does,
which is mostly "it is a bitter, and bitters prompt bile".

**It also contradicted the course.** The original told every reader to eat garlic
and cruciferous vegetables. Both are among the first foods the Bloated and
Backed-Up pattern is asked to ease off in Week 1, because they ferment readily.
The replacement carries that caveat explicitly and says the pattern page takes
precedence.

Smaller: the original heading promised "10 Natural Ways" and listed twelve.

**Verified:** no em dashes, US spellings throughout, no banned vocabulary, no
diagnostic language, published and in position.

### The $27 / $147 liver inversion is closed

The mini course had a full gut-liver module while the $147 course had none. Both
now cover it, from their own angle: Gut Foundations explains the connection,
the Gut Reset explains why daily clearance is the thing to act on.

---

## Tier 1 images placed, 2026-10-22

Fourteen cut-paper images, 29 placements, across 19 lessons. Full map in
`GUT-RESET-VISUAL-PLAN.md`.

While placing the five pattern portraits, the five pattern pages in Your
Pattern, In Detail also got their palette corrected: `#DDD8CE` and `#F5F1EA`
(email system) to `#C8DDD0` and `#EFF7F1`, and `#44564E` on the affiliate
disclosure line (neither system) to `#6A8278`. Those were the last email colors
anywhere in the course content; a site-wide search now returns zero.

The Supplement Reference had to be resent whole to take its hero, since
`update_course_content` replaces bodies rather than patching them. It carries
clinical doses, so it was re-fetched and checked line by line afterwards. All
fifteen dose ranges and every caution are byte-identical to what was there
before.

---

## Fermenting lesson corrected, 2026-10-22

`2178660472` **How To Ferment Your Own Vegetables**, Week 3.

The page told members to eat fermented vegetables daily and closed on "your gut
will thank you" with no caution at all. Five Foods says, in Alina's voice, "I
say this in every lesson that touches fermented food, because it is the single
most common way people make themselves worse while believing they are helping."
This was a lesson that touches fermented food, and it did not, so the copy was
making a promise the course then broke.

The placement made it sharper. Fermented foods come in during Week 2, and the
Bloated and Backed-Up pattern is told to park them until Week 4. The how-to
sits in Week 3, so the one pattern told to avoid them right now was meeting an
uncaveated page in the middle of that window.

**Three changes.**

1. **The caution, added above the method**, in the standard sage callout:
   start with a spoonful not a serving, the headache / flushing / itching /
   racing heart stop signal, and a direct line telling the Bloated and
   Backed-Up pattern their Week 2 instruction still holds. They can make a jar
   now and leave the eating until Week 4.
2. **Deleted the "Benefits of Fermented Vegetables for Gut Health" listicle.**
   Five generic bullets claiming improved digestion, boosted immunity and
   better absorption. Weakest writing in the course, and redundant: Probiotics
   And Prebiotics covers it properly in Week 2 including the pattern
   exception. Replaced with one line pointing back there.
3. **Rewrote the opening and closing**, the two places the register slipped.

**The method was left alone on the substance.** 2% salt by weight, the brine
ratio, 65 to 75F, keeping everything under the brine to prevent mold, and
loosening the lid to let gas escape are all correct. Only the register was
touched: "veggies" to "vegetables" throughout, a handful of contractions
expanded, one exclamation mark removed.

Three of the four lessons flagged as imported generic copy remain:
`2178659968`, `2178660503`, `2178660709`. Those are voice problems rather than
safety ones.

---

## The last three imported lessons rewritten, 2026-10-22

All three kept their existing image. Each still fits the rewritten content, so
nothing was regenerated and no upload was needed.

### How Your Digestive System Works, `2178659968`, Week 1

Was four paragraphs of textbook anatomy. Correct, and it gave a member no
reason to care.

Rewritten around one idea: **your digestive tract is a tube, and the inside of
it is not technically inside you.** Everything is in the corridor until it
crosses the wall, which is what makes the barrier language in the rest of Week
1 click.

The real addition is a map of **where each pattern lives**: Underactive at the
stomach, Reactive and Bloated and Backed-Up in the small intestine, Sugar-Driven
in the large intestine, Wired-and-Tired in the nerve supply running all of it.
That mapping existed nowhere else in the course, and it turns a filler page
into the one that explains why the course sorts people before it gives them a
plan. Every fact from the original is kept: thirty feet, the three sections,
villi and microvilli, pancreatic enzymes and bile, five feet of colon, water
and salts, fermentation.

Image: copper pipework. Still right, and now earns its place.

### When Things Are Not Moving, `2178660503`, Week 3

Was an omega-3 and flax listicle that also said waste sitting there lets
"toxins build up in your system". That contradicts The Gut-Liver Loop two
lessons earlier, which says plainly that the liver does not need detoxing.

Rewritten as the **troubleshooting page**, which is what it should always have
been, since Bowel Movements already covers the basics and the two were
overlapping. Now: you have done the basics and it still is not happening, so
what next.

- Replaced the toxin claim with the actual mechanism from The Gut-Liver Loop:
  bile carries packaged waste out through the gut, and a slow exit means some
  of it is unpacked and reabsorbed
- Ordered the steps so **water comes before fiber**, which is the single most
  common thing people get backward
- Added what to look at when all five steps are in place: slow motility, thyroid,
  medication, ignoring the urge, stress, very low fat eating
- Added an honest paragraph on laxatives, including that daily use for months
  is a doctor conversation
- Added per-pattern notes and a when-to-get-it-checked block

Image: the stopped water wheel. Unchanged and still apt.

### Practice Gratitude, `2178660709`, Week 4

Was three paragraphs claiming gratitude lowers cortisol, improves the
microbiome, and improves nutrient absorption, followed by ten generic
exercises. The microbiome claim is not supportable.

Rewritten to say so. It now opens by stating that gratitude has reasonable
evidence for mood and sleep and none for changing gut bacteria, which matches
how the course already handles bone broth, blueberries, ACV, detoxes and the
dirt question.

The page now leads with **the twenty seconds before a meal**, which is the one
version with a digestive rationale, and connects it to the breathing exercise
already taught in Week 1. The ten exercises are cut to four, with an explicit
instruction to pick one. Added the same mental-health line the Wired-and-Tired
page carries.

Image: the posy in a jam jar. Unchanged.

### Checks

`veggies` and `fortnight` both return zero across the site. All 62 published
lessons still carry an image.
