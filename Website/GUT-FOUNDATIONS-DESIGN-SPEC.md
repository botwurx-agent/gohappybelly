# Gut Foundations: design spec, 2026-10-28

Proposed changes to `/gut-foundations` (landing page 2152353662, theme
2168000232). Nothing here is applied yet.

Prompted by comparing the page against a competitor's $8 bundle page and asking
whether Go Happy Belly is losing conversions by being visually restrained.

## The finding

It is not. Rendered at phone width the page is typographically better than the
comparison: the headline is large, dark and confident, and the body copy at
17px is well leaded and genuinely easy to read. An earlier read of the theme
JSON suggested the weight-300 body would be too light for an audience that is
mostly 40 to 65. **Seen rendered, it is fine.** That worry is withdrawn.

The real problem is narrower. **The elements that carry the sale are the
quietest things on the page.** Three fail WCAG AA on contrast, and the most
important of them is the buy button.

### Measured, against the live tokens

| Element | Colour | Ratio | AA 4.5 |
|---|---|---|---|
| Headings | `#162E28` on `#F8FAF8` | 13.75 | pass |
| Body copy | `#2E4438` on `#F8FAF8` | 10.01 | pass |
| **CTA button label** | white on `#C07A5A` | **3.40** | **fail** |
| Secondary text, incl. the whole "is not" column | `#6A8278` on `#F8FAF8` | 3.94 | fail |
| Eyebrow labels, incl. the price | `#7AAE86` on `#F8FAF8` | 2.43 | fail |

The eyebrow failure matters more than its size suggests, because
`GUT FOUNDATIONS · $27` is where the price lives. The price is currently the
hardest text on the page to read.

### The button, measured

Computed from the live DOM:

```
font-size: 13px   font-weight: 500   text-transform: uppercase
letter-spacing: 1.82px   background: rgb(192,122,90)   color: #fff
```

13px uppercase letter-spaced inside a 38px-padded slab is caption sizing. It
reads as a label on a coloured rectangle rather than as a button.

## The changes

### 1. Button

| | From | To | Why |
|---|---|---|---|
| Background | `#C07A5A` | `#A85F3E` | 3.40 to **4.80**, clears AA, still the brand terracotta |
| Size | 13px | 16px | caption to button |
| Weight | 500 | 600 | |
| Case | uppercase + 1.82px tracking | sentence case, 0.01em | letter-spaced caps read as captions |
| Label | `START GUT FOUNDATIONS, $27` | `Find your gut pattern, $27` | a benefit, not a filename. Echoes the final CTA's "Find out which one you are" |

Applies to all three instances: hero, mid-page, sticky mobile.

### 2. Two new text tokens, added not replaced

`#7AAE86` (Sage) and `#6A8278` (Muted) stay exactly as they are for rules,
borders and decorative fills, where contrast rules do not apply. The failures
are only where they are used for **text**. So add two darker siblings rather
than changing the palette:

| New token | Value | Ratio on `#F8FAF8` | Replaces, for text only |
|---|---|---|---|
| Sage Text | `#3F7A50` | 4.87 | `#7AAE86` in eyebrow labels |
| Muted Text | `#5E7569` | 4.74 | `#6A8278` in secondary copy |

`#566B60` (5.46) is available if more headroom is wanted; `#5E7569` is the
smallest change that passes.

### 3. The "is not" column up from 14px to 15px

It is the hardest-working copy on the page, and it is currently set in the
smallest, lowest-contrast style on the page.

### 4. Bold the reframe line

In `The drawer` section (`1792070000002`), the closing line:

> None of that was a discipline problem. You were running experiments without
> knowing what you were testing.

is already differentiated (weight 400 / `#162E28` against weight 300 /
`#2E4438`), but not enough to see. Take it to **weight 600**.

It is the hinge the whole sale turns on and it currently scans identically to
the three paragraphs above it.

## Effort, honestly

These are not all the same size of job.

- **The button background** is a theme setting. The final CTA has
  `btn_background_color` set explicitly; the hero CTA inherits a theme-level
  button token. One or two edits.
- **The button size, case and label** are per-block settings. Three edits.
- **The two colour tokens are the real work.** These colours are not theme
  tokens, they are hardcoded in inline `style=""` attributes inside the rich
  text of each block. Changing them means editing the HTML of every block that
  uses them, roughly nine blocks for the eyebrow and ten for the muted text.
  Enumerate exactly at build time rather than trusting that count.

## Deliberately not doing

The comparison page uses saturated magenta, all-caps shouting, struck-through
prices, and a live "someone just purchased" widget.

None of that should be copied, and not on taste grounds. The defining
experience of this audience is having been sold to and let down. Visual
loudness is the signature of the thing that already failed them. The restraint
is not timidity, it is the clinical register a woman whose doctor dismissed her
is actually shopping for.

The live-purchase widget in particular would be actively harmful here: on a
new offer it would either be fabricated or would advertise how few sales there
are, and being caught at it is unrecoverable with this buyer.

## Still open, from the earlier conversation

Separate pieces of work, not token changes:

1. **The missing relief section.** The page runs recognition, then reframe,
   then straight to mechanism. No section paints the destination. It belongs
   after the five patterns and before the price, and it can be written
   compliantly because the claimable relief is a change in how she relates to
   the problem, not a health outcome.
2. **A mid-page CTA after the five patterns**, which is the peak "that is me"
   moment and currently has no buy button.
3. **Eleven lessons shown as eleven things.** Quantity is told, not shown.

## Verification note

The live site can now be screenshotted. Cloudflare returns 403 to curl and to
plain fetches, but a real Chromium browser through Playwright loads the page
normally. The before and after images behind this spec were produced by
injecting the proposed CSS into the live page in a headless browser, which
changes nothing on the server.

This retires the "nobody has visually checked the live site" limitation
recorded in `DESIGN-SYSTEM.md`.

---

## Applied, 2026-10-28

All of it is live. Verified against the rendered page, not the API response.

| Change | Verified on the live DOM |
|---|---|
| Button background | `rgb(168,95,62)` = `#A85F3E` |
| Button type | 16px, weight 600, `text-transform: none` |
| Button label | `Find your gut pattern, $27`, 4 instances, 0 of the old label |
| Eyebrow / price | `rgb(63,122,80)` = `#3F7A50` |
| Secondary text | `rgb(94,117,105)` = `#5E7569` |
| Both panel columns | 15px |
| Reframe line | weight 600 |
| Relief section | present, between the five patterns and What is inside |

CTA count went from 3 to 4, since the relief section carries one. That closes
the mid-page gap as well.

### Two things that cost a round trip

**1. The page is cached, and the cache does not clear on save.**

Immediately after the update the API read back the new section correctly while
`https://www.gohappybelly.com/gut-foundations` still served the entirely old
page: old button labels, no relief section, old colours. Nothing had failed.
The same URL with `?v=<timestamp>` served the new version at once.

`cf-cache-status` reads `DYNAMIC`, so this is Kajabi's own page cache rather
than Cloudflare. **Verify theme edits against a cache-busted URL**, and expect
to tell anyone checking the page to hard-refresh. A plain load proves nothing
for several minutes.

**2. A nested block addressed at the wrong level fails silently.**

`1792070000004_b` lives inside the group block `1792070000004_g`, not directly
under the section. The first write addressed it as
`sections.1792070000004.blocks.1792070000004_b`, which is a path that does not
render. **`update_theme_content` returned `{"updated": true}`** and the stored
text was unchanged.

This is the same class of failure as `update_course_content` silently dropping
`poster_image: null` earlier in this project. The rule holds across both tools:
a success response means the payload was accepted, never that the field landed.
Check the rendered page.

The correct path is the full nesting, as used successfully for the hero CTA in
the same payload:
`sections.<id>.blocks.<group>.blocks.<block>.settings`

### One correction to the spec above

The spec said to take the `is not` column from 14px to 15px. The `what it is`
column alongside it is also 14px, so moving only one would have left two
side-by-side cards visibly mismatched. **Both** columns were moved to 15px.
