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
