# gohappybelly.com replica on Kajabi

Built 2026-10-13. This is the copy of the live site that was asked for.

## Source verified

`curl https://www.gohappybelly.com` returns HTTP 200, 53,201 bytes, and
`Website/index.html` in this repo is **byte-identical** to it (`diff`
reports zero differences). The live site is a **single page**: 14 sections,
and its only internal links are the `#about` and `#offers` anchors. There
are no inner pages.

## Where the replica lives

| | |
|---|---|
| Landing page | `2152330575` |
| Theme | `2167878495` (Nova v0.2.7) |
| Slug | `/home-v2` |
| Preview | https://go-happy-belly.mykajabi.com/home-v2 |
| Builder | https://app.kajabi.com/admin/themes/2167878495/settings/edit |
| Status | **DRAFT.** Publishing is admin-UI work. |

**Root is still served by the old landing page `2150005693` ("Home", last
updated June 2025).** Swapping it is the final step and is an admin
setting; nothing here changes the live domain, which is still on Netlify.

## Why this replaces the earlier attempt

The first homepage build went into the **Encore Site** theme's `index`
template (`2156348838`, `content_for_index`). It is stored correctly and
renders nothing, because this site overrides its homepage with a published
landing page. See `KAJABI-REBUILD.md`.

This rebuild is on a landing page, which is the surface that can actually
become the homepage, and on Nova, which is what new landing pages use.

## Copy is verbatim

Every headline, bullet, FAQ answer, testimonial, price and button label is
lifted from the live page without rewriting. The one content change is the
last FAQ: the live version says functional testing is "always optional and
never a prerequisite", which contradicts the GI-MAP being bundled into the
$1,497 (confirmed by Steve). The replica says the GI-MAP is included and
the other four panels are the optional ones.

**The live copy contains em dashes**, which CLAUDE.md forbids ("NO em
dashes anywhere in copy"). They are preserved here because this is a copy,
not a rewrite. Nine of them, in the hero CTA, the validation heading, the
How It Works sub and step 1, the archetypes CTA, and three FAQ answers.
Say the word and they come out.

## Palette: the live site is NOT on the CLAUDE.md palette

CLAUDE.md's "Brand Design System (Locked)" is navy and cream
(`#1B2D4F` / `#FAF6F0`). **The live website is forest green.** Its real
tokens, used here:

| Token | Value |
|---|---|
| bg | `#F8FAF8` |
| bg-alt | `#EFF7F1` |
| sage-pale | `#EAF5EC` |
| forest (headings, dark sections) | `#162E28` |
| body | `#2E4438` |
| muted | `#6A8278` |
| border | `#C8DDD0` |
| sage | `#7AAE86` |
| sage-light | `#A8CAB2` |
| terracotta (buttons) | `#C07A5A` |

Fonts: Playfair Display headings, DM Sans body, both as on the live site.

That navy/cream block in CLAUDE.md appears to describe the **email**
system, which does use it. Worth reconciling, because the Private Coaching
page (`2152330511`) was built on the navy/cream palette and therefore does
**not** match this replica. One of the two needs to move.

## Sections

`1791930000001`–`1791930000011`, in render order: Hero, Validation, Early
Testimonial, How It Works, The Five Gut Patterns, What Changes, About
Alina, Testimonials, Work With Alina, FAQ, Final CTA. Nav and footer are
fixed chrome outside `content_for_index`.

Verified after writing: 11 sections in `content_for_index`, 54 rendered
blocks, every `block_order` id resolves to a real block, and the only two
`btn_action` targets on the page are the quiz and the Calendly link. No
dead `#` buttons.

## Where it deviates from the live page

Disclosed rather than glossed. **Not visually verified** either: the
sandbox cannot reach the Kajabi domain, so all of the above is verified as
JSON, not as pixels.

1. **Hero portrait and the "Credential / FDN-P" badge are missing.** The
   Kajabi API cannot upload files. The hero is therefore a single centred
   column instead of the live two-column text-plus-photo layout. Source
   file is `Website/IMG_8247.jpg`. Upload via the media library, then add
   an `image` block.
2. **About portrait missing**, same reason, same single-column result.
   Source is `Website/Alina_Fence.jpg`.
3. **Footer link row is gone** (Free Quiz / Book a Call / Instagram /
   Guthub.ai). Nova's footer schema accepts only `copyright`, `link_list`,
   `logo` and `social_icons`, with no text block, so arbitrary links cannot
   go there. The tagline and the medical disclaimer were folded into the
   copyright string. Restoring the row needs a Kajabi navbar plus a
   `link_list` block.
4. **Nav menu is gone.** The live nav has About / Work With Me anchors plus
   a quiz button. The header here is the wordmark plus the quiz CTA. The
   anchors need section ids, and the eventual inner pages need a navbar.
5. **The decorative leaf divider between hero and validation is omitted.**
   It is an inline SVG, and Nova strips inline SVG from rich-text bodies.
6. **The arrow between the Before and After columns is omitted.**
7. **The five pattern cards render 3 then 2**, centred, rather than the
   live `repeat(auto-fit, minmax(...))` flow. Nova has no column-count
   setting and text blocks cannot take a custom width, so the row is split
   into two groups. Tablet widths will differ from the live site.
8. **Scroll-reveal animations not applied.** The live page uses a custom
   IntersectionObserver. Nova dropped AOS; the equivalent is Tailwind
   transition utilities via `custom_classes`.
9. The six test cards link straight to their SamCart checkouts, as on the
   live site. Only the Bone Broth Reset moved to Kajabi checkout.

## Nova gotchas hit on this build

- **The footer and header have restricted block vocabularies.** Sending a
  `text` block to the footer failed the whole write with a "Missing Schema"
  guard, and **nothing was saved**. The guard is helpful: it refuses rather
  than rendering a broken section. Header takes `cta`, `logo`, `menu`.
- Toolsets get evicted silently at the 3-toolset cap; `themes` had to be
  re-enabled mid-build.
- `section_filter` suppresses the top-level keys, so verifying tokens and
  `content_for_index` needs `full_settings: true` with no filter.
- A second write that omits the Style Guide tokens does **not** wipe them;
  deep merge preserved them here. Verified rather than assumed.
