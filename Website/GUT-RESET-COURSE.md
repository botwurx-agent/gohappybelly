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
| Hero | 50/50 split with a product image, or centred | 62/38 split, copy against a numeric rail | There is no product shot for a course, and the four numbers do more selling than a stock image would |
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
