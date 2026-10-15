# Go Happy Belly — Website Design System

**Status: locked as of 2026-10-14.** Everything below is measured off the
finished Kajabi home page (Encore Site theme `2156348838`). Every inner page
built from this point matches it. Nothing from any earlier Kajabi page carries
forward; those designs are retired.

> **This is the WEBSITE system. It is not the email system.** CLAUDE.md's
> "Brand Design System (Locked)" section (navy `#1B2D4F`, cream `#FAF6F0`,
> Georgia) describes the Mailchimp email templates. The website is a different
> palette and a different typeface pairing. Do not mix them.

---

## 1. Palette

| Token | Hex | Used for |
|---|---|---|
| Page background | `#F8FAF8` | Default section background |
| Alt background | `#EFF7F1` | Every other section, for banding |
| Deep background | `#E4F0E7` | Image frame backing |
| Forest | `#162E28` | Dark sections, headings, the featured panel, badges |
| Footer panel | `#112420` | Footer only. One step darker than forest, so the footer separates from a forest section above it |
| Body text | `#2E4438` | Paragraphs |
| Muted | `#6A8278` | Secondary copy, card body, captions, legal |
| Border | `#C8DDD0` | Hairlines, card borders, the header rule |
| Sage | `#7AAE86` | Eyebrows, accents, prices, bullet dots, links |
| Sage light | `#A8CAB2` | Accents on dark, offer-card left bar, badge labels |
| Sage pale | `#EAF5EC` | Divider badge fill |
| Terracotta | `#C07A5A` | Every primary button. Nothing else |
| White | `#FFFFFF` | Cards |

On a forest background, text is white at an opacity rather than a flat grey:
`rgba(255,255,255,0.86)` for a lead line, `0.78` for body, `0.76` for list
items, `0.48` for a risk note, `0.45` for footer links, `0.25` for legal.

## 2. Type

**Headings — Playfair Display, weight 400, line-height 1.12, `#162E28`.**
**Body — DM Sans, weight 300, line-height 1.8, `#2E4438`.**

| Level | Desktop | Mobile |
|---|---|---|
| h1 | 58px | 36px |
| h2 | 38px | 28px |
| h3 | 26px | 22px |
| h4 | 20px | 19px |
| h5 | 17px | 16px |
| h6 | 15px | 14px |
| body | 16px | 15px |

Recurring roles that are not headings:

| Role | Spec |
|---|---|
| Eyebrow | 11px, weight 500, `0.20em`–`0.24em`, uppercase. Sage on light, `#A8CAB2` on forest |
| Hero eyebrow rule | A 22 x 1.5px sage bar inline before the text, 10px gap |
| Section sub | 15px, weight 300, line-height 1.7, `#6A8278`, capped 460–560px and centred |
| Card body | 13px, weight 300, line-height 1.65, `#6A8278` |
| Aha / pull quote | Playfair, italic, weight 400 |
| Price | 18px sage on a card; Playfair 50px white on the featured panel |
| Micro note | 11px, `#6A8278`, `0.05em` |
| Legal | 10px, line-height 1.7 |

Headings are authored as real `<h1>`–`<h6>` so they inherit the Style Guide and
stay responsive. Never pin a font size on a heading.

## 3. Buttons

One button style across the whole site:

```
background #C07A5A   color #FFFFFF   12px / weight 500
letter-spacing 0.13em   text-transform uppercase
padding 14px 34px   border-radius 2px
```

The only variant is **outline-light**, used on forest backgrounds:
transparent fill, white text, `1.5px solid rgba(255,255,255,0.45)`.

## 4. Layout

- **Content width 1044px.** Container is 1100px with 28px gutters; 20px gutters
  under 768px. Every column, gap and portrait is derived from 1044.
- **Section padding:** 88–100px top and bottom on desktop, 56–64px on mobile.
  Hero 88/80. Validation and About 90. Patterns and Work With 96. Final CTA 100.
  A quote band is lighter: 56.
- **Two-column split:** `1fr 1fr`. Gap 60px in the hero, 72px in About. At
  1044 that gives 492px columns in the hero and 486px in About.
- **Card grids:** three across on desktop. Six items run as two rows of three,
  never five-and-an-orphan.
- **Backgrounds alternate** `#F8FAF8` → `#EFF7F1` down the page, with forest
  reserved for the validation band and the final CTA.

### Portraits

| | Hero | About |
|---|---|---|
| Width | 380px | 486px |
| Ratio | 3 / 4 | 4 / 5 |
| Crop | `object-position: 72% center` | `object-position: center top` |
| Shadow | `0 24px 60px rgba(22,46,40,0.14)` | `0 16px 48px rgba(22,46,40,0.1)` |
| Radius | 3px | 3px |

The shadow belongs on the image box, never on the column that holds it.

## 5. Components

**Archetype / pattern card.** White, 3px radius, padding 26/22,
`box-shadow: 0 2px 12px rgba(22,46,40,0.07)`. A 3px accent bar runs along the
top edge, full bleed. The closing aha line is Playfair italic 13px with a
`1px solid #C8DDD0` rule above it and 12px of space.

**Testimonial card.** White, 3px radius, padding 28/24, `0 2px 12px
rgba(22,46,40,0.06)`, a `3px solid #7AAE86` bar down the left edge, and a
Playfair `"` at 60px sage at 18% opacity pinned top-left behind the text.
Author line 10px, `0.18em`, uppercase, sage.

**Offer card.** White, 3px radius, padding 22/18, `0 2px 10px
rgba(22,46,40,0.06)`, `3px solid #A8CAB2` left bar. Title Playfair 16px,
note 11px muted, price 18px sage. Equal height across the row.

**Featured offer panel.** Forest, 4px radius, padding 42/38, `0 16px 48px
rgba(22,46,40,0.18)`. Two columns: the inclusion list left, the price stack
right. Each inclusion carries a 14px sage dot. Price is Playfair 50px white
over an 11px `#A8CAB2` "Investment" label, then the button, then a 12px
italic risk-reversal note capped at 180px.

**Validation band.** Forest. Playfair italic heading. The symptom grid is
capped at 840px and centred. Each line leads with a 5px sage dot. Closes with
a Playfair italic quote capped at 540px and an outline-light button.

**Step divider.** A 1px `#C8DDD0` line 60px tall, a 36px circle filled
`#EAF5EC` with a `1px solid #C8DDD0` border and a 14px sage arrow, then another
60px line.

**Credential badge.** Forest card hanging off a portrait's lower-left corner,
padding 30/18/14, 3px radius, `0 8px 28px rgba(22,46,40,0.28)`. Label 9px
`0.18em` `#A8CAB2`; value Playfair 20px white.

## 6. Chrome

**Header.** Logo 104 x 65 (deliberately larger than the original 64 x 40 — the
wordmark was unreadable at that size). 16px padding top and bottom, so ~100px
tall. A `1px solid #C8DDD0` rule along the bottom. Sticky, with
`backdrop-filter: blur(10px)`. Nav links 13px, `0.04em`. One terracotta button
on the right.

**Footer.** Background `#112420`, padding 44/32, everything centred in a single
column:

1. Logo, `filter: brightness(0) invert(1)`, opacity 0.8, 18px below it
2. Tagline — Playfair italic 15px `rgba(255,255,255,0.42)`, 24px below it
3. One horizontal row of links — 11px, `0.1em`, uppercase,
   `rgba(255,255,255,0.45)`, 24px gaps
4. Legal — 10px, line-height 1.7, `rgba(255,255,255,0.25)`, three lines,
   capped 620px

No social icon row, no Kajabi badge.

## 7. Behaviour

- **Every content link opens in a new tab**, with `rel="noopener"`. Site
  navigation (logos, menu items) stays in the same tab.
- Offer links use **root-relative Kajabi checkout paths**
  (`/offers/<token>/checkout`) so they survive the DNS cutover.
- **CTA routing.** The free call is the sales mechanism everywhere except the
  Investment panel on the Private Coaching page, which goes straight to the
  Kajabi checkout for the $1,497 offer (`/offers/442eXHU6/checkout`). Someone
  who has read that far has already had the call offered to them four times.
  A secondary "Rather talk first? Book a free call" link sits under that
  button so the call path is never closed off.
- **The commerce CTA is its own variant** (`.gh-cta-strong`): 13px, `0.14em`,
  18px/38px padding, with a terracotta lift shadow. One per page, maximum.
  Every other button on the site is the standard house button.

## 8. Compliance, inherited from CLAUDE.md

Pattern and archetype language only. Never "you have SIBO / Candida / Leaky
Gut", never a diagnosis, never "cure" or "treat". Alina is an FDN-P, not a
physician, and the footer says so on every page.

**Open decision:** the home page carries em dashes because it mirrors the live
site, which conflicts with CLAUDE.md's no-em-dash rule. Until Steve rules on it,
new pages follow CLAUDE.md and avoid them.

---

## 9. Implementing this on a new page

Kajabi gives each surface its own theme, so the system is **replicated per
theme, not inherited**. This file is the source of truth; the themes are copies.

| Surface | Theme | Engine |
|---|---|---|
| Home page | `2156348838` | Encore Site v1.4.3 |
| Private Coaching | `2167882803` | Nova v0.2.7 |

Every new landing page Kajabi creates today comes up on the **`nova_blank`**
preset, so Nova is the engine for inner pages from here on. The two engines
reach the same design by different means:

| | Encore | Nova |
|---|---|---|
| Grid | 12-column flex, `col-1`..`col-12` | Tailwind flex groups, `width: fit/fill/custom` |
| Content width | Hardcoded 1260px per section, overridden with `!important` | Set directly, no fight |
| Card accent bars | Negative-margin wrapper divs in rich text | Tailwind border utilities in `custom_classes` |
| Type scale | Style Guide tokens | Style Guide tokens (same values) |
| Custom CSS | `settings.css` | `settings.css` |

### Nova traps that cost a render cycle each

| Trap | Symptom | Fix |
|---|---|---|
| Footer takes no `text` block | Whole write rejected | Draw the tagline as a `::before` |
| Section gutters sit INSIDE the width cap | Content 56px narrow | Cap at 1100, not 1044 |
| Every block has a default 10px/20px padding | Columns 20px narrow | Zero it only on blocks still on the defaults |
| `image-wrapper` does not hug its image | Portrait cannot centre, badge lands on the column corner | `width: fit-content !important` |
| `image-wrapper` also ships Tailwind `overflow-hidden` | Anything hanging off the photo (the credential badge) is clipped flush to its edges | `overflow: visible !important` on the same rule; the `img` keeps its own radius |
| Deep-merging a nested block needs the full path | Edit silently creates an orphan, API still returns success | Address the real depth, then verify in the rendered page |
| `custom_classes` land on the block wrapper, not the flex row | `.hook > *` sizes an intermediate div; children stack | Reach through with `.hook .nova-group > *` |
| The `feature` block hides an `<article>` in its flex chain | `margin-top: auto` resolves to zero, buttons unaligned | Give the `<article>` `flex: 1 1 auto` too |

**Setting up a new Nova page:** copy the Style Guide tokens in §2 and §3 into
the new theme first, then build sections, then port only the CSS the page
actually needs. Do not copy the home page's `settings.css` wholesale — most of
it is Encore-specific workarounds (the 1260px container override, the
`box_shadow`-on-`.block` portrait fix, the clipped-badge `overflow` release)
that have no equivalent problem in Nova.
