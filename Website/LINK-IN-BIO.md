# Link in Bio page

| | |
|---|---|
| Page | `2152336186` |
| Theme | `2167908665` (Nova v0.2.7) |
| URL | `https://www.gohappybelly.com/links` |
| Status | Published, **not** in the main menu (reached from Instagram only) |
| Form | `2148673482` "Contact Form Opt In" |

## What it is

The landing page behind Alina's Instagram link in bio. Five things to click,
an introduction above them, and a way to reach her below. It follows the
design system in `Website/DESIGN-SYSTEM.md`; nothing new was invented for it.

## Structure

| Section | Background | Contents |
|---|---|---|
| `1791980000001` Intro | `#F8FAF8` | Portrait with the FDN-P credential badge, eyebrow, h1, one paragraph |
| `1791980000002` Links | `#EFF7F1` | Five `feature` blocks, stacked, capped at 640px |
| `1791980000003` Contact | `#F8FAF8` | Heading, Kajabi form, a line offering the free call instead |

### The five links

**Updated 2026-10-28.** This file previously listed five cards and omitted Gut
Foundations, which had been live since 2026-10-23. It also still showed two `#`
placeholders that have since been filled. Both corrected against the live page.

| # | Card | Destination | New tab |
|---|---|---|---|
| 1 | **Gut Foundations** ("Start here", $27) | `/gut-foundations` | no (internal) |
| 2 | What's Your Gut Pattern? | `https://gut-pattern-quiz.scoreapp.com` | yes |
| 3 | My Favourite Products | `/shop` | no (internal) |
| 4 | Free 7-Day Lifestyle Workbook | `/7-day-lifestyle-workbook` | no (internal) |
| 5 | Watch Me on The Block, Season 17 | Facebook video | yes |

Block ids in theme `2167908665`, section `1791980000002`, in render order:
`_l6`, `_l1`, `_l3`, `_l4`, `_l5`. Note `_l6` is the Gut Foundations card
and leads the stack despite its id, so trust `block_order`, not the numbering.

### The Gut Fix card was removed, 2026-10-28

Steve's call, once The Gut Fix became the $10 order bump on the $27 checkout.
A $10 alternative sitting two cards below the $27 front door competes with it;
as a bump it adds to the same order instead. This also resolves the pricing
tension flagged on this page earlier, a cheaper offer sitting under the front
door.

**How it was removed, and how to put it back.** Block `_l2` was taken out of
`block_order` and set `hidden: "true"`. The block itself was NOT deleted, so
restoring it is two changes: set `hidden` back to `"false"` and re-insert
`1791980000002_l2` into `block_order` at the position you want.

**The standalone offer is untouched.** `/the-gut-fix` is still published and
its checkout (`JnHcWPaw`, $10) still works. It is simply no longer promoted
here. Leave that page live: the bump needs a reference page, and any existing
links to it would otherwise break.

Verified on the live page after the change: five cards, and the string "Gut
Fix" appears nowhere in the body text, with zero links to `/the-gut-fix`.

**Gut Foundations leads, per the front-door decision of 2026-10-28** (see
CLAUDE.md). It carries a terracotta "START HERE" eyebrow above the heading. The
quiz sits second: it is free and still the segmentation engine, so it keeps a
high slot without taking the lead one.

### Card 1 carries the featured treatment, 2026-10-29

**The problem it solves.** Every card rendered identical chrome and an identical
terracotta button, so the front door had position but no visual weight on a
scan.

**What was rejected, and why.** Steve asked whether to recolor the button or add
a photo. Neither:

- **Recoloring the button works against you.** `DESIGN-SYSTEM.md` §1 reserves
  terracotta `#C07A5A` for "every primary button. Nothing else." Since every
  button on the page is already terracotta, making the front door's button a
  different color would mark it as *less* primary, not more.
- **A photo costs about 190px of height** at phone width, pushing the quiz and
  everything under it down the page. Rendered and compared before discarding.

**What was used instead: the system's own featured offer panel** (§5), which
exists for exactly this job. Card 1 only:

| | |
|---|---|
| Background | `#162E28` forest |
| Radius | 4px |
| Shadow | `0 16px 48px rgba(22,46,40,0.18)` |
| Eyebrow | `#A8CAB2` (was terracotta, too low contrast on forest) |
| Heading | `#FFFFFF` |
| Body | `rgba(255,255,255,0.78)`, the §1 body value for forest |
| Button | **unchanged** terracotta, which is the point |

All confirmed on the live DOM, and the other four cards confirmed still white.

**How it is built.** `custom_classes` gains `gh-featured`, and the background,
radius and shadow come from a scoped `<style>` tag inside the block's own text
field. `custom_css` is untouched, for the same reason as the eleven-tile grid on
`/gut-foundations`: the only available copy of that ~500-line string is a DOM
scrape, and rewriting it wholesale to add three rules is a bad trade. Text
colors are set inline rather than in the `<style>`, because the block's existing
inline colors would otherwise win on specificity.

The `<style>` targets three elements, `.gh-featured` plus its inner `> div` and
`[data-nova-role='details']`, because the white background sits on an inner
element rather than on the wrapper.

**A false alarm worth recording.** In the screenshot the button looked like it
was hanging below the forest card. Measured, it is not: the button sits inside
the card and the gap below it is 0. The same gap is 0 on all five cards and the
`.gh-link-card` wrapper has `padding: 0` on all five, so the padding lives on an
inner element and the flush button is this component's normal rendering. It
simply reads more sharply where terracotta meets forest than where it meets
white. No change made. Card 1's only real geometric difference is 23px above the
heading, which is the eyebrow line.

**Resolved 2026-10-28:** the $10 Gut Fix card was the cheaper-offer tension
noted here. It is now the order bump on the $27 and no longer a card.

**Corrected 2026-10-28:** `/the-gut-fix` now checks out through Kajabi
(`/offers/JnHcWPaw/checkout`), verified on the live page. The SamCart note below
is stale and kept only for history.

The Gut Fix link points at SamCart with the trailing slash. Without it the
store 301s, and the Location header it returns is malformed
(`https://mystore2429.mysamcart.com:/the-gut-fix/`, with a stray colon).
Browsers tolerate it, but linking to the canonical form skips the hop.

## Decisions made while building

**Voice is first person.** The rest of the site talks about Alina in the third
person ("the brands Alina keeps in her own kitchen"). This page is reached from
her own Instagram profile, where she speaks as herself, so it says "I work with
women who..." instead. It is the one page on the site that does this, and it is
deliberate.

**The portrait is smaller than the hero spec.** 260 x 347 rather than 380 x 507,
same 3/4 ratio, same crop, same shadow. The page is a single centred column and
a full hero portrait would push the first link below the fold on a phone.

**Downloads are direct, not gated.** Clicking goes straight to the file. See
"Open question" below.

**The free call sits under the form, not in the stack.** Steve specified five
cards. The call is the site's sales mechanism per the design system, so it is
offered as one line beneath the contact form rather than as a sixth card that
was not asked for.

## Nova traps hit on this page

Four, all now fixed and worth knowing for the next Nova build.

**1. Block padding fought the gutter-zeroing rule.** The shared CSS zeroes
Nova's default block padding with `.nova-block.md\:pt-\[10px\]`, specificity
(0,2,0). A `.gh-link-card { padding: ... !important }` is (0,1,0) and lost, so
cards rendered with no padding. Fixed by setting `padding_desktop` /
`padding_mobile` on each block, which is the settings-first approach the Nova
guide asks for anyway, and removing the padding from the CSS class.

**2. A short card collapsed and re-centred.** The `feature` block's inner
wrapper sizes to its content. Card 5's copy was short enough not to wrap, so
the wrapper shrank to the text width and the parent centred it, putting its
text 167px from the card's left edge while the other four sat at 29px. Fixed
with `.gh-link-card > div, .gh-link-card [data-nova-role='details'] { width: 100% }`.

**3. The form's submit button is not a `cta`.** It carries
`data-nova-role='form-submit'`, so the site-wide button rule missed it and it
rendered in sentence case at the default size. The rule now names both roles.

**4. `link_to_form_embed` defaults to true, and turning it off exposes
placeholder copy.** With it false, the block renders its own `title_text` and
`description_text`, whose defaults are "Join Our Free Trial" and "Get started
today before this once in a lifetime opportunity expires." Both have to be set
to empty strings explicitly.

Also worth repeating: `mobile_text_align` is a **separate setting** and
defaults to `left` on text blocks and `center` on feature blocks. Setting
`text_align` alone leaves mobile wrong, which is the breakpoint that matters
most on this page.

## Verified

Measured on the rendered page at 1440 and 390, not by eye:

- All five cards identical: 24px top and bottom padding, 29px left, 26px right,
  left-aligned, buttons flush to the same left edge
- Portrait centred exactly (65/65 at 390, 590/590 at 1440)
- h1 and h2 centred at both widths
- No horizontal overflow at 390; cards 350px wide, buttons full width at 347px
- Submit button renders "Send", uppercase, 12px, 1.56px tracking (0.13em)
- Placeholder form copy gone

## Open question, answered 2026-10-23

The workbook is now being gated behind an email capture. Steve chose a Kajabi
form synced to Mailchimp by Zapier. It is built as a dedicated opt-in page
rather than a form swapped into card 4, so the card keeps its shape and simply
points at the new page. See `Website/WORKBOOK-LEAD-MAGNET.md`.

Note the card never worked in the first place: `btn_action` was `"#"`.

The ebook is a $10 SamCart product, not a lead magnet, so nothing changes there.

## Still needed from Steve

1. ~~The Gut Fix ebook URL~~ supplied, wired to SamCart
2. The 7-day lifestyle workbook file. **Still outstanding**, and it blocks
   publishing the whole opt-in flow
3. The URL for the Block Season 17 segment. A Facebook URL is saved in card 5's
   `img_action`, which is the image click target on a card with the image
   hidden, so nothing reaches it. Needs confirming and moving to `btn_action`
4. ~~Whether the workbook should capture an email first~~ yes, decided
   2026-10-23

## The Gut Fix SamCart page

`https://mystore2429.mysamcart.com/the-gut-fix/` is public and readable. It
sells the ebook at **$10** with a 30 day refund guarantee, CTA "Beat the Bloat
Now". The card copy on `/links` was corrected: it had said "Free to download",
which was wrong.

That page is not on the website design system and conflicts with CLAUDE.md in
four ways. None of it is broken, and none of it was changed, but it is
inconsistent with every other surface:

| Issue | Detail |
|---|---|
| Credential | Calls Alina a "Certified Gut Health Specialist & Holistic Wellness Educator". Every other surface, and the locked sign-off, says FDN-P |
| Banned word | "empowering" appears in the mission line |
| Em dashes | Used throughout, against the hard style rule |
| Offer suite | A $10 ebook is not in CLAUDE.md's offer table at all |

Also worth checking before it gets more traffic: "has helped thousands of
women" is a specific social-proof claim, and "Thousands of women silently
struggle" is a second one.
