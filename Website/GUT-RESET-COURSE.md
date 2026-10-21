# Gut Reset Course sales page

| | |
|---|---|
| Page | `2152348302` |
| Theme | `2167971291` (Nova, `nova_blank` preset) |
| URL | `https://www.gohappybelly.com/gut-reset-course` |
| Status | **Published** |
| Product | Gut Reset Course, $147 |
| Offer | `2149370663` "Happier Belly Gut Reset Program", published, $147 one time |
| Checkout | `/offers/jmFpFL5m/checkout` |
| Replaces | `2150211650` `/happier-belly-gut-reset`, **unpublished 2026-10-21** |

Built on `Website/DESIGN-SYSTEM.md` per the standing rule. First page built as a
deliberate template for the offers that follow.

## The methodology

At $1,497 the sales mechanism is the free call. At $147 there is no call, so this page has to do
the call's job by itself. It is ordered as the questions a buyer asks silently, because she stops
reading at the first one that goes unanswered.

| # | Question | Section |
|---|---|---|
| 1 | Is this me? | Hero, then The Problem |
| 2 | What is actually wrong? | The Five Patterns |
| 3 | Why has nothing worked? | The Five Patterns subhead, and the aha line above it |
| 4 | What exactly do I get? | The Four Weeks, then the offer panel |
| 5 | Can I trust her? | Testimonials, About Alina |
| 6 | What if it does not work? | Terms in the offer panel, the refund FAQ |
| 7 | What is this *not*? | Is And Is Not |
| 8 | Remaining objections | FAQ |
| 9 | Decide | Final CTA |

Identification comes before any claim. The avatars this sells to have been dismissed for years, so
the page has to describe her week accurately before it is allowed to assert anything.

## CTA placement

A CTA is earned, not sprinkled. Each one sits immediately after a section that creates belief,
never between two sections that are both still building it.

| Placement | Section | Variant |
|---|---|---|
| Header | sticky chrome | standard, small |
| After the promise | Hero | standard |
| After the mechanism lands | The Five Patterns | standard |
| At the price | Offer panel | **`gh-cta-strong`**, the one per page |
| Last word | Final CTA | standard |
| Mobile only | Sticky bottom bar | standard, full width |

The design system allows one `gh-cta-strong` per page. It goes on the offer panel, where the price
and the button sit together, rather than the final CTA.

The sticky mobile bar is new to the system. Most traffic is Instagram, and on a page this long the
buy action would otherwise be a scroll away at all times. It is `position: fixed`, mobile only, and
the footer gets 76px of bottom padding so it never covers the disclaimer.

## Sections

| ID | Section | Background |
|---|---|---|
| `1792000000001` | Hero | `#F8FAF8` |
| `1792000000002` | The Problem | Forest `#162E28` |
| `1792000000003` | The Five Patterns | `#EFF7F1` |
| `1792000000004` | The Four Weeks | `#F8FAF8` |
| `1792000000005` | The Offer | `#EFF7F1`, forest panel inside |
| `1792000000006` | Testimonials | `#F8FAF8` |
| `1792000000007` | About Alina | `#EFF7F1` |
| `1792000000008` | Is And Is Not | `#F8FAF8` |
| `1792000000009` | FAQ | `#EFF7F1` |
| `1792000000010` | Final CTA | Forest |
| `1792000000011` | Sticky Mobile CTA | fixed, mobile only |

Forest is used twice, for the validation band and the final CTA, as the design system reserves it.
The offer panel is the system's **featured offer panel**: a forest card on a light section, not a
third forest band.

The five patterns run as **six** cards, not five. A 3-up grid with five items leaves an orphan,
which the design system forbids, so the sixth is a quiz card in terracotta. It fills the grid and
gives the undecided reader a free next step instead of a dead end.

## Honesty decisions

**Testimonials are labelled "1:1 client".** Linda, Hanna and Tiffani are the only testimonials the
business has, and all three are from one-to-one coaching, not the course. Using them to sell a
self-paced course without disclosure is the kind of claim the FTC treats as deceptive. They are
kept, attributed accurately, and the section closes with a line saying plainly that 1:1 includes
testing and calls, that the course is a different thing at a different price, and that results
differ. Steve chose this over dropping them.

**The FAQ sends people away.** The refund answer ends "if what you actually need is one-to-one work
with testing behind it, say so and we will point you at that instead of selling you this twice."
A $147 buyer who should have bought the $1,497 program refunds and does not come back.

**No numbers that cannot be substantiated.** No student counts, no success rates, no "thousands of
women". The only figures on the page are counts of what is in the course.

## Verified

Rendered and inspected at 1440 and 390, not asserted from JSON:

- No horizontal overflow at either width (`scrollWidth == clientWidth`).
- 3-up and 2-up grids wrap correctly; all stack full width on mobile.
- The offer panel's two columns stack on mobile.
- The About row stacks and the FDN-P credential badge renders unclipped.
- The sticky bar computes to `position: fixed`, `z-index: 60`, pinned to the viewport bottom.
- `/gut-reset-course` 200, `/happier-belly-gut-reset` 404, checkout 200.

Chromium would not trust the session's egress CA, so the screenshots were taken with that CA
pinned by its public-key hash (`--ignore-certificate-errors-spki-list`) rather than by disabling
certificate verification.

## Open, and blocking a copy change

**The terms copy currently reads "One payment of $147. Nothing recurring."** That is accurate to
offer `2149370663` as configured: `payment_type: single`, one time, no renewal.

Steve's intent is **one payment, then annual auto-renew**, which the course FAQ already promises.
Those two do not match today. Until the offer is converted to an annual subscription, the page
states the one-time terms, because publishing a renewal claim against a non-renewing offer would
be a false statement at the point of sale.

When the offer is converted, two things change together:

1. The terms block `1792000000005 > o_panel > o_price > o_p2` becomes:
   "$147 today, then $147 a year unless you cancel. Cancel any time from your account, and you
   keep access to the end of the year you paid for."
2. The course FAQ stops being wrong.

A renewing charge needs the renewal price, the interval and the cancellation route disclosed next
to the buy button, not in an FAQ. The replacement copy above does that, which is why it is written
out here rather than left to be improvised later.

**Not done, and not mine to do:**

- The offer is titled "Happier Belly Gut Reset Program" while the site calls it the Gut Reset
  Course. The buyer meets that mismatch on the payment screen. Renaming is an offer change.
- Access duration was not verifiable through the API. The page says one year on Steve's word.
- `/happier-belly-gut-reset` now 404s. Any ad or link pointing at it is dead; Kajabi redirects are
  not reachable through MCP.
- The new page is not in the main menu. Adding it is a site-wide nav change nobody asked for.
