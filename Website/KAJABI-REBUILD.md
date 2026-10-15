# Go Happy Belly homepage on Kajabi

Built 2026-10-13. Option A: native Encore blocks plus a Style Guide CSS layer for the
decorative flourishes. Fully editable in the Kajabi builder.

**This did not touch gohappybelly.com.** The domain still points at Netlify. Moving it is a
separate decision, deliberately deferred.

## Where it lives

| | |
|---|---|
| Site theme | `2156348838` (Encore **Site** v1.4.3) |
| Template | `index` (Class A, pure dynamic) |
| Render array | `content_for_index` |
| Live at | **NOT LIVE.** See "Built on the wrong surface" below. |
| Builder | https://app.kajabi.com/admin/themes/2156348838/settings/edit |

Note the Site surface is a different theme and a different version from the Bone Broth Reset
landing page (`2167624377`, Encore **LandingPage** v2.14.8). They have separate `sections` maps
and separate settings files. Editing one does not affect the other.

## Built on the wrong surface (2026-10-13)

The twelve sections below are correctly stored and `content_for_index` holds exactly them, with
the old 2024 sections orphaned out. But **nothing renders them**, because this site does not
serve its homepage from the theme's `index` template.

The root URL is served by a **published landing page called "Home"** (`2150005693`, theme
`2156348907`, page title "Go Happy Belly - Gut Reset Program", one attached opt-in form, last
updated June 2025). The theme `index` sections it replaced are all from 2024, which fits:
the homepage was rebuilt as a landing page and the theme template was abandoned.

The Encore Site skill file's template map says `index.liquid` renders `content_for_index`, and
that is true. What it cannot tell you is whether a given site actually uses that template, or
overrides the homepage with a landing page. That has to be checked against the site itself, and
was not.

**What is still worth keeping:** the Style Guide tokens on this theme (Playfair Display, DM
Sans, forest/sage/terracotta) did take effect and do apply to the Site templates that render
from this theme: login, library, blog, store, member directory. Those are now on brand.

**What to do:** port the twelve sections into a landing page theme instead. The block
vocabulary is identical, so it is a transcription job rather than a redesign. Safest route is a
new landing page, reviewed at its own URL, then switch the homepage setting to point at it,
leaving the current live Home untouched until the swap.

## Sections

| ID | Section |
|---|---|
| 1791900000001 | Hero |
| 1791900000002 | Section Break |
| 1791900000003 | Validation |
| 1791900000004 | Early Testimonial |
| 1791900000005 | How It Works |
| 1791900000006 | The Five Gut Patterns |
| 1791900000007 | What Changes |
| 1791900000008 | About Alina |
| 1791900000009 | Testimonials |
| 1791900000010 | Work With Alina |
| 1791900000011 | FAQ |
| 1791900000012 | Final CTA |

## The CSS layer, and why it is fragile

Six decorative effects from the Netlify site are pseudo-elements. Encore's rich-text sanitizer
strips `class` attributes and `::before` cannot be inline-styled, so none can live in the
content layer. They now live in the theme's Style Guide CSS field, each targeting a section id:

- Hero: twin radial washes (sage upper right, terracotta lower left)
- Validation: sage corner wash
- How It Works: the hairline connecting the three numbered steps
- Final CTA: centred sage glow
- Nav: `backdrop-filter: blur(10px)`

**These rules target section IDs.** If a section is deleted and rebuilt in the builder its ID
changes and the matching rule goes dormant (silently, with no error). Update the ID in the CSS
rather than deleting the rule. Reordering sections is safe; deleting and recreating is not.

## Where it deviates from the Netlify original

1. **The five archetype cards.** The original uses `repeat(auto-fit, minmax(196px, 1fr))`,
   fitting as many as will go. Encore's grid is 12 columns and 12 does not divide by 5. All
   five are now `width: 4` in a centre-aligned section, so they render 3 then 2 centred. Even
   card widths, different arrangement.
2. **Responsive reflow.** The original's `auto-fit` grids step down 4 to 3 to 2 to 1 as the
   viewport narrows. Encore holds its widths then collapses to a single column at 768px. **The
   two sites will differ noticeably on a tablet.**
3. **Scroll animations.** The original uses a custom IntersectionObserver with a staggered hero
   load. Encore offers AOS presets at block level. Not yet applied; add `animation_type` and
   `animation_direction` per block if wanted.
4. **The FAQ is now better.** Native accordion blocks instead of custom JavaScript, editable in
   the builder.

## Outstanding

- **Two image slots are empty**: the Hero portrait (`1791900000001_1`) and the About portrait
  (`1791900000008_0`). The source files are `Website/IMG_8247.jpg` and `Website/Alina_Fence.jpg`.
  Kajabi's API cannot upload files, so these go through the media library uploader, then
  `place_media` can set them.
- **Not visually verified.** The sandbox cannot reach the Kajabi domain. Check it in a browser.
- The test-kit buttons in Work With Alina still point at SamCart checkout URLs, which is
  correct: only the Bone Broth Reset moved to Kajabi checkout.

## Blast radius worth knowing

The Style Guide tokens (Playfair Display, DM Sans, forest/sage/terracotta) are **site-wide**.
They now apply to every Site template: login, library, blog, store, member directory, thank-you
pages. That is brand consistency rather than a bug, but it is wider than the home page.

The ~70 sections from the 2024 Kajabi site are still in the `sections` map. They are no longer
in `content_for_index`, so nothing renders them. Harmless, but they will clutter the builder
sidebar until someone deletes them.

---

## Correction (2026-10-13): the port is not a transcription job

"Outstanding" above says to port the twelve sections into a landing page theme and
that "the block vocabulary is identical, so it is a transcription job rather than a
redesign." **That is wrong.**

New landing pages on this site are created on **Nova v0.2.7**, a Tailwind-first theme,
not Encore. Confirmed by building the Private Coaching page (`2152330511`, theme
`2167878184`). Nova and Encore share almost no setting names, so the port is a
re-authoring job.

The trade is worth taking anyway. Nova runs Tailwind v4 with the browser JIT, so
arbitrary utilities and arbitrary-variant selectors work straight from a block's
`custom_classes`. The six pseudo-element effects that had to live in Encore's Style
Guide CSS field, and the section-ID-targeted rules that go dormant without warning
when a section is deleted and recreated, are simply unnecessary there. Nova should
beat the ~90% fidelity Encore reached.

See `Website/PRIVATE-COACHING.md` for the Nova authoring notes.

---

## Colour and alignment pass (2026-10-13)

Steve reported this build looks better than the Nova one but that section colours
and some alignment did not match the live site. Audited all 12 sections against
`Website/index.html` and fixed the following.

### Three wrong section backgrounds

| Section | Was | Now (live value) |
|---|---|---|
| Validation `…003` | `#EFF7F1` light | **`#162E28` forest** |
| Early Testimonial `…004` | `#162E28` forest | **`#EFF7F1` light** |
| Work With Alina `…010` | `#162E28` forest | **`#EFF7F1` light** |

Validation and Early Testimonial were straight **swapped**: on the live site
Validation is the dark forest block and Early Testimonial is the light one. Both
sections' text colours had to be swapped with them (`validation__heading` is
white on forest, `early-testi__text` is `#162E28` on light).

Work With Alina was wrong for a subtler reason: on the live site only the
**featured offer card** is forest (`.offers__featured`), while the section around
it is light `--bg-alt`. The build had painted the whole section dark. Fixed by
lightening the section and giving the two featured blocks their own `#162E28`
card background, then recolouring the six test cards back to white with
`#162E28` headings, `#6A8278` notes and `#7AAE86` prices (live `.offer-card`).

The other nine backgrounds were already correct.

### Grid widths that did not match

The live site uses `repeat(auto-fit, minmax(Npx, 1fr))`, which fits as many
columns as will go. Encore has a fixed 12-column grid, so the column count has
to be chosen deliberately.

| Section | Live columns | Was | Now |
|---|---|---|---|
| Five Gut Patterns | 5 (`minmax(196px)` in 1100px) | width 4 → 3 then 2 | **width 2 → 5 across** |
| Work With Alina test cards | 6 (`minmax(180px)`) | width 4 → 3 then 3 | **width 2 → 6 across** |
| Hero | `1fr 1fr` | text 6 + image 5 = 11 | **6 + 6 = 12** |
| About Alina | `1fr 1fr` | image 5 + text 6 = 11 | **6 + 6 = 12** |

Validation (3 across), Testimonials (3 across), What Changes (5+2+5) and FAQ
(width 8, close to the live 760px cap) were already right.

### Both portraits are now in place, without an upload

The hero and About image blocks were empty, which is why those two sections
looked unbalanced: the text sat in half the row with blank space beside it.

The Kajabi API cannot upload files, **but Encore image blocks accept a URL, and
the photos are already served publicly by the live site**:

- `https://gohappybelly.com/IMG_8247.jpg` (hero)
- `https://gohappybelly.com/Alina_Fence.jpg` (About)

Both verified HTTP 200, `image/jpeg`. They are referenced directly.

**This is interim and will break.** Those URLs are served by Netlify. If the
domain moves to Kajabi, they die and both sections lose their photo. Upload the
two files to the Kajabi media library and repoint the blocks **before** any DNS
cutover.

### Still different from the live site

- Validation's CTA is solid terracotta; live uses an outline-light button.
  Encore's outline colour semantics were not worth guessing against a possibly
  invisible button.
- The six test cards carry small "Order" buttons. On the live site the whole
  card is a link, which an Encore `text` block cannot do, so the buttons are how
  the SamCart links survive.
- The five-pattern row is 10 of 12 columns wide (5 × width 2), centred, rather
  than filling the container as the live `auto-fit` does.
- Scroll-reveal animations still not applied.

### Gotchas worth keeping

- **`get_theme_content` with `full_settings: true` silently truncates on this
  theme.** It returned "38 of 62 sections" with `truncated: true` and the rest in
  `remaining_section_ids`. A section missing from that payload reads as absent,
  which looks exactly like data loss. It cost one wrong diagnosis here: section
  `…010` appeared to have lost its settings when it had not. **Always check the
  `truncated` flag before concluding anything from a full read**, and confirm a
  specific section with `section_filter` instead.
- That 62 is also the reminder that ~50 orphaned 2024 sections are still in the
  `sections` map. They are not in `content_for_index` so nothing renders them.
- Encore values are strings: `"width": "2"`, `"make_block": "true"`.

### Header and footer chrome (2026-10-13)

Steve reported the top nav was "some sort of lime green". It was: the `header`
and `footer` fixed sections were **untouched leftovers from the 2024 Kajabi
site**. The twelve-section rebuild only ever wrote dynamic sections, so the
chrome had never been looked at.

They are also easy to miss on a read. `header` and `footer` always exist in
`settings.sections` but they are not in `content_for_index`, and on this theme
a `full_settings: true` read truncates before reaching them, so they looked
absent. `section_filter: ["header","footer"]` is how to see them.

| | Was (2024 leftover) | Now (live value) |
|---|---|---|
| Header background | **`#9acdaa` lime** | `#F8FAF8` |
| Header text | unset | `#2E4438` |
| Header layout | `horizontal: left` | `between` (logo left, nav and CTA right) |
| Header sticky | `false` | `true`, with matching sticky colors |
| Header CTA | "Book a call" → `/resource_redirect/landing_pages/2150005710` | "Take the Free Quiz" → the quiz, terracotta |
| Footer background | **`#76a685` green** | `#162E28` forest |
| Footer copyright | "Go Happy Belly" | the full three-line legal and disclaimer text |
| Footer social | **Kajabi's own Facebook, Twitter and Instagram** | Alina's Instagram only |
| Footer links | Main Menu (Home, Private Coaching) | the `footer` navbar: Free Quiz, Book a Call, Instagram, Guthub.ai |

The header's **User Menu block was removed from `block_order`**, not deleted,
because the live nav has no "Log In". Put `1555988487706` back in `block_order`
if a member login is ever wanted there.

The `footer` navbar (`2148458014`, a default menu) was empty and is now
populated with the four links the live footer carries, as PathLinks to their
real URLs. The footer `link_list` was repointed from `main-menu` to `footer`.

**The header nav links are still wrong and were deliberately left alone.**
Main Menu (`2148458013`) holds "Home" → landing page `2150005693` and "Private
Coaching" → landing page `2150005719`, both 2024 pages. The live site's nav is
"About" and "Work With Me", which are **in-page anchors** (`#about`, `#offers`).
Encore has no per-section HTML id setting (its "anchor sections" are a different
concept entirely), so those two anchors cannot be reproduced. Pointing the
labels at nothing would be worse than leaving links that at least resolve.
Decide this when the real inner pages exist.

Other chrome deviations: the live nav's 1px bottom border and `backdrop-filter:
blur(10px)` have no Encore header setting, and the nav font size is a select
whose allowed values are not documented, so it stays at 18px against the live
13px.

### Sizing pass (2026-10-13)

Steve sent a side-by-side screenshot: the Kajabi build read roughly a fifth
larger than the live site, with the hero portrait running past the fold and
shoving the headline down the page.

**Root cause: container width.** Encore caps section content at **1260px**;
the Netlify site caps at **1100px** with 28px gutters, so 1044px of real
content. Every column, card, gap and portrait scales off that number. Measuring
the two screenshots confirmed it: Kajabi's content band was ~1.2x wider, and
1260/1044 = 1.21.

Fixed with one rule in the theme's `settings.css`:

```css
.container { max-width: 1100px; padding-left: 28px; padding-right: 28px; }
```

The narrower cap always wins over Encore's outer wrapper, so capping
`.container` is enough and the wrapper's own selector is not needed.

**The portraits needed two separate fixes.** Encore renders an image at its
natural aspect ratio and has no crop setting, while the live site crops both
with `aspect-ratio` + `object-fit: cover`. So the photo was both too wide and
far too tall.

| | Live | Now |
|---|---|---|
| Hero photo | `max-width: 380px`, 3/4, `object-position: 72% center` | `image_width: "380"` + CSS crop |
| About photo | ~486px column, 4/5, `object-position: center top` | `image_width: "486"` + CSS crop |

`image_width` (a real Encore image-block setting, px, blank = 100% of column)
does the width; the crop has to be CSS because no setting exposes it.

Also: body type 17px → **16px** desktop, 15px mobile (live base is 16px); the
hero sub-paragraph was 18px in `#6A8278` and is now 16px in `#2E4438` with the
live 460px measure; the eyebrow regained its 22px sage rule; `findable.` is
terracotta italic again; and the header logo went **200px → 90px**.

### Correction: the portraits are no longer hotlinked

An earlier note here warned that referencing the photos by their Netlify URLs
was interim and would break at DNS cutover. **That is wrong.** Kajabi
side-loaded both images into its own storage when the URLs were saved. They now
read:

- `file-uploads/themes/2156348838/settings_images/3a0315a-…_IMG_8247.jpg`
- `file-uploads/themes/2156348838/settings_images/c38abe-…_Alina_Fence.jpg`

No upload step is outstanding and nothing breaks when the domain moves.

### Nav links: anchors are possible, but the validator blocks the useful form

An earlier note said Encore cannot reproduce the live nav's `#about` /
`#offers` anchors. That was too strong: Encore renders every section as
`#section-<id>`, which the decorative CSS above already relies on.

The real blocker is the navbar validator, which rejects a bare `#fragment`:
*"Url must be a URL or a path"*. A `/`-rooted `/#section-1791900000008` would
satisfy it, but `/` currently serves the old 2024 Home landing page, so those
links would leave the page and land nowhere useful. They stay as they are until
the homepage override is resolved, at which point they become:

- About → `/#section-1791900000008`
- Work With Me → `/#section-1791900000010`

### Section-by-section pass: 02 Validation (2026-10-13)

| | Live | Was | Now |
|---|---|---|---|
| Heading | italic, `clamp(22px, 3.2vw, 34px)` | upright, Style Guide 38px | italic, same clamp |
| Heading text | has the em dash | dash removed | dash restored |
| Label | 10px, 0.24em | 11px, 0.22em | 10px, 0.24em |
| Bullet grid | `max-width: 840px` | full 1044px | capped 840px |
| Bullet text | 15px, `rgba(255,255,255,0.78)`, weight 300 | default body | matched |
| Bullet marker | 5px sage circle | `&#9679;` glyph at text size | 5px inline-block circle |
| Quote | `max-width: 540px` | uncapped, one line | capped 540px |
| CTA | `btn--outline-light` | solid terracotta | outline, white 45% border |
| All buttons | 12px uppercase, 0.13em | sentence case | matched globally |

The 840px cap uses `#section-1791900000003 .row:has(> .col-4)`. That works
because the guide confirms **`make_block` forces a block onto its own row**, so
the heading, quote and CTA are each in their own row and `:has()` reaches only
the row holding the six width-4 bullets. Capping `.row` outright would have
squeezed the heading too.

The outline button and the global uppercase both had to be CSS: Encore's button
schema has no `text-transform`, and no setting produces an `rgba()` border.

**Em dashes restored here.** CLAUDE.md forbids them, but the live site uses them
(nine times) and matching the live site is the current instruction. Flagged to
Steve; if he prefers, they come out of both the Encore build and the Nova one
together.

### Section-by-section pass: 05 The Five Gut Patterns (2026-10-13)

Steve called out the thin accent line on each card. On the live site that is
`border-top: 3px solid` with a **different colour per card**, set by
`:nth-child()`, and card three is deliberately terracotta:

| # | Card | Accent |
|---|---|---|
| 1 | The Wired-and-Tired Gut | `#7AAE86` |
| 2 | The Reactive Gut | `#8EBF9A` |
| 3 | The Sugar-Driven Gut | `#C07A5A` (terracotta) |
| 4 | The Underactive Gut | `#6A9E78` |
| 5 | The Bloated and Backed-Up Gut | `#9AC8A6` |

Encore's `feature` block only exposes a whole-box `border_type` / `border_width`
/ `border_color`, so a top-only rule in brand-varying colours is not reachable
from settings. The accent is instead a flush bar as the first element of each
card's rich text:

```html
<div style="height: 3px; background-color: #7AAE86; margin: -26px -22px 22px;"></div>
```

The negative margins cancel the block's 26px/22px padding so the bar sits hard
against the card edge. Verified present on all five after the write.

**This is the fragile bit.** The sanitizer that strips markup runs on *editor
round-trips*, not API writes. If someone opens this section in the Kajabi
builder and saves, these empty `<div>`s may be dropped and the accents vanish
silently. If that happens, re-apply from here, or move the accents into
`settings.css` keyed on `#section-1791900000006` column `:nth-child()`.

Everything else in the section was oversized or missing:

| | Live | Was | Now |
|---|---|---|---|
| Heading | `clamp(26px, 3.8vw, 42px)`, `max-width: 560px` | Style Guide 38px, full width | matched |
| Sub | 15px, `max-width: 480px` | 17px, full width | matched |
| Card box | no border, soft shadow | 1px `#C8DDD0` border, no shadow | border none, shadow small |
| Icon | 20px | 24px | 20px |
| Card title | Playfair 18px / 500 | 20px | 18px / 500 |
| Card body | 13px | inherited 16px | 13px |
| Aha line | 13px italic **+ 1px top divider** | 16px italic, no divider | matched |
| Card padding | 26px 22px | 26px 20px | 26px 22px |
| CTA label | em dash | comma | em dash |
| CTA note | 11px | 13px | 11px |

### Section-by-section pass: 06 What Changes (2026-10-13)

The visible miss was the middle divider. The live site is not a bare arrow: it
is a 36px circle in sage-pale `#EAF5EC` with a 1px `#C8DDD0` border and a sage
arrow, flanked above and below by 1px x 60px rules in `#C8DDD0`. Rebuilt in
rich text as nested flex divs, verified present after the write, and set
`hide_on_mobile` to match the live `display: none` below 768px.

| | Live | Was | Now |
|---|---|---|---|
| Heading | `clamp(26px, 3.6vw, 42px)`, `max-width: 600px` | Style Guide 38px, full width | matched |
| Sub | 15px, `max-width: 460px` | 17px, full width | matched |
| Column padding | `0 32px` | none | `0 32px` |
| Column label | 10px, 0.22em, mb 24; muted / sage | 11px, 0.2em | matched |
| List items | 15px, lh 1.65, weight 300, 14px gap | inherited 16px | matched |
| Before marker | `—` in `#C8DDD0` at 13px | `—` in `#C8DDD0` | sized to 13px |
| After marker | `✓` in `#7AAE86` at 13px / 500 | `✓` in `#7AAE86` | sized and weighted |
| Before text | `#6A8278` | `#6A8278` | unchanged |
| After text | `#2E4438` | default | `#2E4438` |
| Section padding | 96px | 90px | 96px |

**Deliberately not matched:** the live grid is `1fr auto 1fr` capped at 900px,
which gives ~352px of text per column. Encore's 12-column grid has no `auto`
track, and capping the row at 900px would have squeezed the columns to ~311px,
*narrower* than the original. Left at 5/2/5 inside the 1100px container, which
yields ~371px per column, within about 5% of the live measure. The divider
column is correspondingly wider than the live 68px.

### Section-by-section pass: 08 Testimonials (2026-10-13)

| | Live | Was | Now |
|---|---|---|---|
| Card accent | `border-left: 3px solid #7AAE86` | 1px `#C8DDD0` box border | 3px sage left bar |
| Card shadow | `0 2px 12px rgba(22,46,40,0.06)` | none | `box_shadow: small` |
| Quote mark | Playfair 60px sage at **0.18 opacity, absolutely positioned** top 10 / left 18 | 48px at 0.25, in normal flow | matched, absolute |
| Quote text | 15px, lh 1.8, **italic**, weight 300, `#2E4438` | inherited 16px, upright | matched |
| Attribution | 10px, 0.18em, **`#7AAE86` sage**, weight 500 | 12px, 0.14em, `#6A8278` grey | matched |
| Card padding | 28px 24px | 32px 28px | 28px 24px |
| Heading | `clamp(26px, 3.4vw, 38px)`, 52px below | 38px fixed, 32px below | matched |
| Section padding | 96px | 90px | 96px |

Same constraint as the archetype cards: Encore's `feature` block border is all
four sides, so a left-only accent is not reachable from settings. Each card's
content is wrapped in a div carrying the left border, with `margin: -28px -24px`
cancelling the block padding and the padding re-applied inside, so the bar sits
flush at the card edge. The quote mark is absolutely positioned inside that
wrapper, with the text at `z-index: 1`, so it reads as a watermark behind the
first lines exactly as the live card does.

The wrapper also carries `height: 100%; box-sizing: border-box`. Without it, the
section's `equal_height: "true"` stretches the card boxes but not the
content-height wrapper, so the accent bar would stop short of the bottom on the
two shorter quotes while running full height on Linda's.

Same editor-round-trip fragility as the archetype accents: these wrappers are
rich-text markup, and opening the section in the Kajabi builder and saving may
strip them.

### Section-by-section pass: 09 Work With Alina (2026-10-13)

Two structural misses, not just styling.

**The featured offer was two boxes, not one.** The live `.offers__featured` is a
single forest panel (`grid-template-columns: 1fr auto`, radius 4, padding
42/38, a deep shadow) holding the includes on the left and the price plus CTA
on the right. The build had them as two separate width-7 and width-5 blocks,
each with its own dark background, so Encore's column gutter cut a visible gap
straight down the middle.

Rebuilt as **one width-12 block** with an internal flex layout. Block
`1791900000010_2` is orphaned out of `block_order` rather than deleted.

That forces one compromise: the Book a Free Call button is now an inline
styled `<a>` inside the rich text, which the Encore guide explicitly calls an
antipattern. There is no alternative here, because a `cta` block renders at
block level and cannot sit inside the right-hand column of a flex layout that
lives in another block. **Consequence: that button will not appear in the
builder's button controls**, and its URL has to be edited in the rich text.

**The bullets were the wrong mark.** The live list uses a 14px sage filled
circle via `::before`, not a checkmark. Replaced.

**The risk-reversal line was missing entirely** — "The call is a real
conversation…", 12px italic Playfair at 48% white, capped at 180px under the
button. Added.

| | Live | Was | Now |
|---|---|---|---|
| Featured panel | one box, radius 4, padding 42/38, deep shadow | two boxes with a gutter | one box, matched |
| Bullets | 14px sage circle | `✓` glyph | matched |
| Title | Playfair 28px | 30px | 28px |
| Includes text | 13px, 76% white, 8px gap | default | matched |
| Price | Playfair 50px | 44px | 50px |
| Risk line | 12px italic, 180px cap | absent | added |
| Offer cards | `border-left: 3px solid #A8CAB2` | 1px box border | left accent |
| Offer cards | no button, whole card links | terracotta ORDER buttons | buttons removed, title links |
| Card name | Playfair 16px | 18px | 16px |
| Card note | 11px | 14px | 11px |
| Card price | 18px sage | 22px `#A8CAB2` | 18px `#7AAE86` |
| Section padding | 96px | 90px | 96px |

**Grid deviation:** the live `.offers__grid` is `auto-fit, minmax(180px, 1fr)`,
which lands on 5 per row in a 1044px container and wraps the sixth onto its own
line. Encore's 12-column grid cannot express 5 equal columns (12/5 is not an
integer), so the six cards sit at width 2 and fill one row of six. Arguably
tidier than a lone orphan card, but it is a difference.

### Offer cards: equal height and 3-up (2026-10-13)

Steve asked whether the "Other ways to start" cards could be made the same
size. Two separate causes were in play:

1. **Ragged heights.** Encore has a section-level `equal_height` setting that
   stretches every block in a row to the tallest. The Archetypes and
   Testimonials sections already used it; this section did not, because it was
   not carried through when the section was rebuilt. Now `"true"`.
2. **Cramped titles.** At width 2 (six across) each card is ~174px wide, about
   138px of usable text after padding, so "Food Sensitivity Test" and
   "GI-MAP Stool Test" wrapped to two lines, which was most of the apparent
   size difference. Cards are now **width 4, three per row, two rows**, giving
   ~312px of text so every title sits on one line.

`equal_height` works because the card wrappers already carry
`height: 100%; box-sizing: border-box` from the testimonial fix. Without that
the column stretches but the wrapper does not, and the left accent bar stops
short of the card bottom.

This moves further from the live `auto-fit` grid (5 across plus an orphan), but
that layout was already unreachable in a 12-column grid. Two clean rows of three
is the closest tidy equivalent.

---

## 01 Hero, and the sizing bug underneath it

### The container cap: why the first fix did nothing

The earlier sizing pass added `.container { max-width: 1100px }` to the theme
CSS and it had no effect at all. The note left behind said "the narrower cap
always wins over Encore's outer wrapper", which was wrong.

Reading the rendered page settles it. Encore does not style sections from a
shared stylesheet. Every section prints its **own `<style>` tag** just above
its markup:

```css
#section-1791900000001 .container {
  max-width: calc(1260px + 40px + 40px);
  padding-right: 40px;
  padding-left: 40px;
}
```

That selector carries an id, so it outranks any plain `.container` rule no
matter where the rule sits or how late it loads. The site base `.container` in
`stylesheets/components/container.scss` is 1340px, but section content never
reaches it. All 12 sections print the same literal 1260px; there is no setting
behind it.

The fix is the one thing that beats an id-scoped rule we do not control:

```css
.section .container:not(.container--full) {
  max-width: 1100px !important;
  padding-left: 28px !important;
  padding-right: 28px !important;
}
```

`.container--full` is excluded so a `full_width: "true"` section can still run
edge to edge. Measured after: container 1100px, content 1044px, matching the
live site exactly. Every section on the page narrowed with it, which is what
the "overall sizing is incorrect, Kajabi is too big" note was about.

### Hero differences, live vs Kajabi

| Element | Live | Kajabi before | Now |
|---|---|---|---|
| Content band | 1044px | 1260px | 1044px |
| Text column | 492px | 507px | 492px |
| Headline | 58px Playfair, breaks after "symptoms" | 58px, broke after "are" | matches |
| Button label | "...Yours — Free" | "...Yours, Free" | matches |
| Trust note | 11px, `#6A8278` | missing | added |
| "Book a free call" link | 13px underlined | missing | added |
| Portrait | 380px, 3/4 crop, soft drop shadow | 380px photo inside a full-column white card | matches |
| Credential badge | forest card on the lower left corner | missing | added |
| Logo | 64 x 40 at x=198 | 90 x 56 at x=210 | 64 x 40 at x=198 |
| Nav font | 13px, 0.04em | 18px, none | 13px, 0.04em |
| Header height | 73px | 99px | 75px |

### The button had to come out of the schema

Encore's `text` block renders its rich text first and the `use_btn` button
after it, always. The live hero puts the trust note and the "Book a free call"
link **below** the button, which that order cannot express. The alternatives
were a third block (flex-wraps onto its own line, leaving a gap under the
button) or a flex `order` trick on `.block` (which breaks the paragraph widths).

So `use_btn` is now `false` and the button is an inline `<a>` in the rich text,
styled to the live `.btn--terra`: 12px, 500, 0.13em, uppercase, 14px/34px
padding, 2px radius, `#C07A5A`. This is the same antipattern already accepted
for the featured offer panel. It costs the Style Guide link, but that link was
already broken here: the block carried an explicit `btn_background_color`.

### The portraits were wearing their shadow in the wrong place

`box_shadow` is a **block** setting, and Encore hangs it on `.block`, which is
the whole six-column cell. With the photo capped at 380px inside a ~492px
column, the medium shadow drew a white card around the photo rather than under
it. Visible in the before screenshot as a pale rectangle wider than the image.

Both portraits are now `box_shadow: "none"`, with the shadow moved onto
`.image`, which is the photo's own box. The crop moved there too:

```css
#block-1791900000001_1 .image { aspect-ratio: 3 / 4; box-shadow: 0 24px 60px rgba(22,46,40,0.14); }
#block-1791900000008_0 .image { aspect-ratio: 4 / 5; box-shadow: 0 16px 48px rgba(22,46,40,0.1); }
```

The About portrait's 486px is not a guess: the live About grid is `1fr 1fr` at
a 72px gap inside 1044px, so (1044 - 72) / 2 = 486 exactly.

### The credential badge

No Encore block can overlap another block, so the badge is two pseudo-elements
on `.image`: `::after` is the forest card carrying "FDN-P", `::before` is the
"CREDENTIAL" label sitting on top of it. The label offsets are derived from the
card's own padding (30/18/14 around a 20px line), so the two move together if
that padding is ever changed.

Two overflow traps had to be released for it. `.image` has `overflow: hidden`
so the crop clips, and **`.block` clips too** and is exactly as tall as the
photo, so the first attempt rendered the badge hanging correctly off the left
edge but sliced off flat at the bottom.

### Still open on the hero

- Nav reads "Home" and "Private Coaching" pointing at the 2024 landing pages.
  The live nav is "About" and "Work With Me", which are in-page anchors. Encore
  renders every section as `#section-<id>`, so the anchors exist, but the
  navbar validator rejects a bare `#fragment`. The full path form
  (`/#section-1791900000008`) only works once root is served by this theme, and
  root is still overridden by the published landing page `2150005693`.
- The button label now carries the live site's em dash, against the CLAUDE.md
  rule. Flagged, not decided.

---

## 10 Other ways to start: cards now point at Kajabi checkout

The six cards carried the live site's SamCart links
(`mystore2429.mysamcart.com/checkout/...`), and the Gut Reset Course card had
no link at all. All six have a published Kajabi offer behind them already, at
prices that match CLAUDE.md exactly.

| Card | Kajabi offer | Offer id | Price | Checkout path |
|---|---|---|---|---|
| Gut Reset Course | Happier Belly Gut Reset Program | 2149370663 | $147 | `/offers/jmFpFL5m/checkout` |
| GI-MAP Stool Test | GI MAP STOOL TEST | 2149722769 | $497 | `/offers/3GQbFKiS/checkout` |
| SIBO Test | SIBO BREATH TEST | 2149722775 | $425 | `/offers/2nD5jeRz/checkout` |
| Food Sensitivity Test | FOOD SENSITIVITY TEST | 2149722672 | $639 | `/offers/eSqyvf9S/checkout` |
| OAT Test | ORGANIC ACIDS TEST (OAT) | 2149722771 | $497 | `/offers/LFzVoPte/checkout` |
| H. Pylori Test | H. PYLORI ONLY | 2149722778 | $250 | `/offers/MMmzKX3D/checkout` |

Each checkout was fetched and confirmed to return 200 with the matching offer
title and price on the page. Zero SamCart references remain anywhere in the
theme.

Three deliberate choices:

- **Root-relative paths, not absolute.** `/offers/<token>/checkout` keeps
  working after the DNS cutover, when the site is served from
  gohappybelly.com instead of go-happy-belly.mykajabi.com. An absolute
  mykajabi.com URL would bounce buyers off the custom domain mid-purchase.
- **The whole card is the link.** The card wrapper `<div>` became an `<a>` with
  `display: block` and `color: inherit`, matching how the live site wraps its
  offer cards. Previously only the title text was clickable. The
  `height: 100%; box-sizing: border-box` that makes `equal_height` work on the
  left accent bar carried over unchanged, and the rendered cards still line up.
- **Same tab, not a new one.** The live site opens SamCart in a new tab because
  it is a different domain. Kajabi checkout is the same site now, so a new tab
  buys nothing and breaks the back button.

The unused `btn_action` on each card was also repointed. `use_btn` is `false`
so no button renders, but a stale SamCart URL sitting in the setting is a trap
for whoever turns that button on later.

Not touched: the featured 3-Month Gut Reset panel still goes to Calendly. The
call is the current sales mechanism per CLAUDE.md, and offer 2149705539
($1,497, published) is there whenever that changes.

---

## Every content link now opens in a new tab

Audited by parsing the rendered page rather than the settings, so inline
rich-text anchors and schema buttons were both caught. Sixteen links on the
page, split two ways.

**Schema buttons** (`cta` blocks and the header CTA) have a `new_tab` setting,
now `"true"`:

| Block | Link |
|---|---|
| `header/1612902775268` | Take the Free Quiz |
| `1791900000003_8` | Validation CTA |
| `1791900000006_6` | Five Gut Patterns CTA |
| `1791900000012_1` | Final CTA |

**Inline rich-text anchors** have no setting behind them, so each one took
`target="_blank" rel="noopener"` written into the markup:

| Block | Link |
|---|---|
| `1791900000001_0` | Hero quiz button, and the "Book a free call" link |
| `1791900000010_1` | Featured panel, Book a Free Call |
| `1791900000010_4` to `_9` | All six offer cards |

`rel="noopener"` goes with every one. Without it the opened tab gets a handle
on `window.opener` and can navigate the original tab out from under the
visitor.

The footer links (quiz, Calendly, Instagram, Guthub) were already `_blank` and
were left alone.

**Deliberately not changed: the four site-navigation links.** The header logo,
the two header menu items (Home, Private Coaching) and the footer logo all
still open in the same tab. A site whose own nav spawns tabs stacks up a new
window every time someone moves around it, and the back button stops working
the way people expect. One word and they flip; the menu items live in the
navbar record rather than the theme, so they are a separate edit.

---

## Course checkout: text size matched to the GI-MAP page

Theme `2167629154` (offer 2149370663, Happier Belly Gut Reset Program), against
theme `2167629155` (offer 2149722769, GI-MAP).

The two themes compile to **byte-identical stylesheets**: same Raleway/Roboto,
same 48/36/30/24/20/16 heading scale, same 18px body. So nothing in the Style
Guide was at fault. The difference was entirely in the rich text of the course
page's text block (`1746107473790`):

- Every `<li>` and two `<p>` elements carried `style="font-size: 2rem"`, which
  is **32px** against the theme's 18px body. That is the whole complaint: the
  body copy was nearly twice the size of the GI-MAP page's.
- "Gut Health Made Easy" was a second `<h1>`, so it rendered at 48px, the same
  size as the page title.
- "With this program, you'll get:" was an `<h2>` at 36px.

Retagged to the GI-MAP page's own hierarchy, with the wording untouched:

| Line | Was | Now | GI-MAP equivalent |
|---|---|---|---|
| Program name | h1, 48px | h1, 48px | h1 page title |
| Gut Health Made Easy | h1, 48px | h3, 30px | h3 "Client Pricing: $497.00" |
| With this program, you'll get: | h2, 36px | h4, 24px | h4 card title |
| All list items | 32px inline | 18px body | body paragraphs |
| Total Value = ($4200) | h3, 30px | h5, 20px | h5 free-consultation line |
| Join Today For Just: $147 | h2, 36px | h4, 24px | h4 card title |
| Subscription note, support line | 32px inline | 18px body | body paragraphs |

Measured after: both pages now render h1 48, h3 30, h4 24, h5 20, body 18.

### Two things found on that page, not changed

**1. The order bump headline is still oversized.** "Exclusive Limited-Time
Offer: Join our monthly Happy Belly Essentials Club" renders at 48px inside a
~330px column, so it wraps to six lines. It is an `<h1>` at the top of the
**Happy Belly Essentials Club offer description** (offer 2149750878), not
anything in this checkout theme. Dropping it to `<h4>` fixes it, but that
description renders anywhere that offer appears, including its own checkout at
`/offers/4xLPe5Pj/checkout`, so it is a wider change than the page asked about.

**2. The subscription note contradicts the offer.** It reads "This is a
subscription membership is a *1 year subscription*. The full **$197** is
charged upon purchase and is non-refundable." The offer record is
`payment_type: single` at **$147**, the checkout panel shows $147.00, and the
heading directly above says "Join Today For Just: $147". So the note promises a
different price and a different billing model than the buyer is actually
agreeing to, and carries a grammar error in its first clause. Left alone per
the CLAUDE.md rule against changing pricing or offer details unasked, but this
one is worth Steve's attention: it is live copy on a page that takes money.

---

## Header logo enlarged, footer rebuilt

### Logo

Both logo assets are 1000 x 625, so a 1.6 ratio. The header logo was matched to
the live site's 64 x 40 earlier in the build, and at that size the wordmark
under the mark was unreadable. Now `logo_width: "104"`, which renders 104 x 65.
The header grows from 75px to 100px to carry it. This is a deliberate
divergence from the live site, not a match; one number changes it again.

### Footer

The Kajabi footer was Encore's default horizontal media row, which put the logo
hard left, squeezed the four links into a narrow vertical column, and ran the
copyright off the right edge of the viewport. Five separate problems:

| Problem | Fix |
|---|---|
| Row layout, left-aligned | `vertical_layout: "true"` plus a flex-column `.footer__container` |
| "© 2026 © 2026 Go Happy Belly" | Kajabi prints its own `&copy; <year>` ahead of the stored string. The setting now holds only `Go Happy Belly. All rights reserved.` |
| Legal text ran as one long line | The other two lines come from `.copyright::after` with `\A` and `white-space: pre-line` |
| Tagline missing entirely | `#block-1602193175296::before`, so it lands between the logo and the link row |
| Instagram appeared twice, as an icon and a text link | The `social_icons` block is now `hidden: "true"`; the live footer has no icon row |
| "Powered by Kajabi" | `.powered-by { display: none }` |

**Why pseudo-elements again.** Encore's footer schema accepts exactly four
block types: `logo`, `link_list`, `copyright` and `social_icons`. There is no
`text` block, so the tagline has nothing to live in, and the `copyright` block
renders a single `<span>` that cannot carry a line break. Both are drawn in CSS
for that reason, not by preference.

**Spacing.** Encore gives `.footer__content` 20px of vertical padding, every
`.footer__block` a 10px vertical margin, and the link list a 15px column
gutter, which roughly doubled every gap against the live design. All zeroed, so
the only spacing left is the live rhythm: 18px under the logo, 24px under the
tagline, 24px above the legal block.

**Background.** The footer was `#162E28`, the same colour as the Final CTA
section directly above it, so the two read as one unbroken dark field with a
200px void in the middle. The live site uses `#112420` for the footer, one step
darker, which is what separates them. Changed to match.

**Logo treatment.** The footer mark is a dark lockup on a dark panel. The live
site renders it `filter: brightness(0) invert(1)` at 75% opacity; here it is
the same filter at 80%. The mark flattens to a solid white disc either way,
which is what the live site does too.

### Flagged

`.powered-by { display: none }` hides the badge rather than switching it off.
Kajabi has a real toggle for this under Settings, and on some plans it is not
removable at all. Turning it off there is the clean way; the CSS is a stopgap.

---

## Home link and logo were landing on the old home page (2026-10-15)

Steve: "The home button and when clicking on the gohappybelly logo are going to
the old home page. it needs to go to the new home page."

There were two separate causes, not one.

### Cause 1: the Home nav link pointed at the old landing page (fixed)

Navbar `main-menu` (2148458013), link **2149405317 "Home"** was a
`LandingPageLink` to `gid://kajabi-portals/LandingPage/2150005693`, i.e. the
2024 `/Home` landing page. Repointed to a `PathLink` at `/`, which is where the
logo already goes, so the two can never drift apart again.

Verified live in the rendered nav on `/shop`:

```html
<a href='https://go-happy-belly.mykajabi.com/' data-nova-role='menu-link'
   target='_blank' rel='noopener'>Home</a>
```

### Cause 2: the site root itself still serves the old landing page (blocked)

This is the one that matters, and it is not a link problem.

| Record | Value |
|---|---|
| Site `active_theme_id` | **2156348838** (Encore, holds the new 12-section home) |
| Website page 2154501976 "Home" | `path: ""`, published, `public_url` = site root |
| Landing page 2150005693 "Home" | `path: "Home"`, published, `active_theme_id` **2156348907** |

What the live HTML shows:

- `GET /` returns 181,404 bytes, references `themes/2156348907`, and contains
  **zero** occurrences of `section-1791900000001`.
- `GET /Home` returns 181,414 bytes and is byte-identical to `/` once the CSRF
  token, reCAPTCHA widget id and canonical/`og:url` are normalised away.
- `GET /admin_index_preview?preview_theme_id=2156348838` returns 213,593 bytes
  and contains all 12 new sections.

So the new home build is intact on the active site theme, and the only public
URL it can ever render at is `/`. The old landing page is occupying `/` through
Kajabi's site-level homepage setting: no landing page has `path: ""`, so the
binding is by record id, not by slug.

**No API surface exposes it.** `update_landing_page` writes only title, slug,
SEO fields and `publish_at`. There is no `update_website_page` tool and no
site-settings write tool at all. Confirmed against the loaded schemas, not
assumed.

The only lever the API does give is unpublishing landing page 2150005693 so
root falls through to the website home page. That was attempted and **denied by
the permission layer** (Unrequested Commit in a Connected App). It was not
retried. Its `publish_at` is `2024-06-13T22:34:40Z` if it ever needs restoring.

Worth noting for risk: `gohappybelly.com` is served by Netlify (301 from
`www`, `server: Netlify`), entirely separate from `go-happy-belly.mykajabi.com`.
No public traffic reaches the Kajabi root, so changing what it serves does not
touch the live site.

### What still has to happen

One dropdown in Kajabi admin, Settings → Site Details → Home page: point it at
the website **Home** page (2154501976) instead of the **Home** landing page
(2150005693). The moment that flips, both the nav link and the logo land on the
new build with no further changes, because both already point at `/`.

Alternatively, granting the unpublish of landing page 2150005693 achieves the
same fall-through from here.
