# Offer: Continued 1 on 1 Coaching

Created 2026-11-09 at Steve's request: a continuation for clients who have
finished the 3-Month Gut Reset and want to keep working with Alina.
$997, six 1 on 1 sessions across nine months.

**Status: PUBLISHED 2026-11-09 18:56Z.** Created as a draft, then published
via `update_offer` once Steve confirmed the shape. See "Why it was published"
below: a draft checkout is not a sendable link.

| | |
|---|---|
| Offer id | `2151501641` |
| Title | Continued 1 on 1 Coaching: 6 Sessions Over 9 Months |
| Price | $997.00 USD, one time |
| Grants | Gut Reset Course (`2148514926`) |
| Checkout | https://www.gohappybelly.com/offers/oMoNrunF/checkout |
| Admin | https://app.kajabi.com/admin/offers/2151501641/edit |

Read back and verified: `price_type: one_time`, `price_strategy: fixed`,
`interval: null`, `number_of_payments: null`, `trial_period_days: null`,
`setup_fee: null`. Clean. Worth stating because this file previously recorded
that two of two published checkouts inspected carried a subscription or price
misconfiguration.

---

## RESOLVED: Steve's confirmation, 2026-11-09

Steve confirmed the shape and answered the open questions:

- **Pricing logic is right.** A returning client pays less per session than a
  new one. The ~$166 per session below is the intended rate.
- **These are maintenance calls.** Someone who wants to keep going with Alina
  and have follow-ups to check things are going as planned. Not a new
  engagement.
- **Upsells happen on the calls.** If a client needs further testing or
  supplements, that comes up in conversation, not in the offer. The offer copy
  already matches this: testing is framed as "an optional clinical
  recommendation, decided between you and Alina, rather than something to
  order up front."
- **It is not placed anywhere.** No sales page, no site navigation, no funnel
  position. It is a checkout link Alina sends directly to an existing client.

### Why it was published

A **draft offer's checkout URL does not work**. Verified: the draft link
redirected to `/login` with "You need to sign in or sign up before
continuing." Since the entire purpose is a link Alina can send to a client,
publishing was required to deliver what was asked for.

It is reversible: `update_offer` with `publish_at: null` reverts it to draft.
Because it is placed nowhere, a published offer is only reachable by someone
who has the link.

## The booking gap, and how it was handled

**There is no booking destination.** `post_purchase.preference` is `disabled`,
so a buyer lands on Kajabi's default confirmation and is told nothing about
how to book.

The existing coaching thank-you page (`2150005925`) is **not** reusable as is.
Per `COACHING-THANK-YOU-PAGE.md` it is built for new-client onboarding:

- a 60-minute **New Client Consultation** booking, which a continuing client
  does not need
- a lab-ordering profile step, which gates the GI-MAP arriving
- joining the private group

and it still carries three unresolved blockers (the group URL, the real lab
site, and the Calendly vs Google Calendar conflict).

A returning client needs one thing: a way to book the next of their six
sessions. Three ways to resolve it, in rough order of effort:

1. **Alina books manually.** She is selling this in conversation anyway, so
   she can put the first session in the diary herself. Publish as is. Lowest
   effort, no new page, but nothing stops a buyer sitting waiting.
2. **A short custom confirmation message** on the offer (`thank_you_preference:
   custom_message`), saying Alina will be in touch to book. One field, no page.
3. **Its own thank-you page** with a booking embed for follow-up sessions.
   Cleanest, but needs a booking link that does not exist yet: the only
   Calendly in the business is the free 20-minute Gut Breakthrough Call, and
   the Google Calendar embed on `2150005925` is the New Client Consultation.

**A booking link for continuing-client sessions does not exist anywhere yet.**
That is the actual blocker, not the page.

---

## What was written into the offer, and why

### It grants the Gut Reset Course

Deliberate. CLAUDE.md records that the $1,497 includes **three months** of Gut
Reset Course access, so a client reaching the end of their three months may
have just lost it. Re-granting keeps their library alive through the nine
months.

Caveat: whether that access is actually time-limited is an offer **setting**,
visible in the admin under Settings, and not exposed through MCP. Worth a
glance; if the original grant never expires, this grant is simply a harmless
no-op.

### Nothing else was carried over from the $1,497

The 3-Month package also includes a GI-MAP test with reading, the private
group, and three months of Guthub. **None of those are in this offer**,
because Steve specified six sessions over nine months at $997 and nothing
else. Adding inclusions he did not ask for would change the offer's
economics.

Each is a real decision he may want to make:

- **Guthub.** CLAUDE.md records that it carries a real per-user inference
  cost, which is why it is not bundled anywhere at the front of the funnel.
  Nine months of it per client is the largest cost of the three.
- **A GI-MAP retest.** Clinically the most defensible addition, since
  re-testing after a protocol is how you find out whether anything moved. But
  it is $497 of cost against a $997 price, which changes this from a
  high-margin renewal into roughly a break-even one.
- **The private group.** Probably should continue, and costs nothing, but it
  is not something the Kajabi offer grants: the $1,497 offer grants only the
  course, so group access is handled outside Kajabi.

### The copy

Written to the brand rules: no em dashes, no banned words, no diagnostic or
cure language, testing framed as "an optional clinical recommendation" per the
hard style rule. It leans on the one thing that makes a renewal different from
a new engagement:

> This is the version of working together that suits someone who already has
> the groundwork in place. The history has been taken, the pattern is known,
> and the plan exists. These sessions are for adjusting it as things change,
> rather than starting again.

It also sets expectations on pacing at the point of payment, which is the
cheapest refund prevention available:

> Six sessions across nine months is roughly one every six weeks, though they
> are yours to place.

---

## Open questions for Steve

1. **Unused sessions at nine months.** What happens? This will come up, and
   the answer is better decided now than in a support email. The offer
   currently says nothing about it.
2. **Is this sold publicly or privately?** Nothing in the request suggests a
   sales page, and a renewal is a conversation Alina has with a client who is
   finishing. Treated here as a private checkout link, which means no page is
   needed, just the URL above. If it should be public, it needs a sales page
   and a place on the site.
3. **A purchase automation?** The two courses now have one each. This is a
   high-touch sale where Alina knows the buyer by name, so an automated
   welcome may be unnecessary or even odd. A tag would still be worth having
   for segmentation.

## Pricing sanity check

Not a recommendation, just the arithmetic, since it was not given:

$997 over six sessions is about **$166 per session**. The $1,497 package
includes a $497 GI-MAP, so roughly $1,000 buys four calls, about **$250 per
session**. The continuation is cheaper per session, which is coherent for a
renewal rate to an existing client who needs no intake.

---

## What changed on 2026-11-09, after Steve's confirmation

### 1. A custom confirmation message replaced the blank default

`post_purchase.preference` was `disabled`, so a buyer saw Kajabi's bare
confirmation. Since Alina drives the booking personally, the page now says so
rather than leaving them waiting:

> Thank you, and welcome back.
>
> Alina will be in touch to get your next session in the diary. If you already
> know roughly when you want it, reply to your receipt and say which week
> suits you.
>
> Your six sessions are yours to place across the next nine months, so there
> is no need to book them all now.
>
> Your Gut Reset Course access continues, and everything is where you left it
> in your library.

This is the cheap version of the three options recorded above. No page, one
field. A dedicated booking page still has nowhere to point, because **no
booking link for follow-up sessions exists anywhere in the business**: the
only Calendly is the free 20-minute Gut Breakthrough Call and the Google
Calendar embed is the New Client Consultation.

### 2. The checkout page was still Kajabi's template

**Caught only by loading the live page.** A new offer's checkout theme
(`2168204747`) ships with placeholder copy, and it was serving verbatim:

> [Offer title] · [ Insert a call to action statement... ] · [ Insert value 1 ]
> · [ Insert value 2 ] · [ Insert value 3 ]

Confirmed in the raw HTML, not just the render: `grep` found "Offer title"
once and "Insert value" three times in the served markup. Alina would have
sent a $997 payment link showing template text.

Fixed in section `1744906803654`:

- **Text block `1746107473790`**: real copy, restating the six sessions, the
  nine-month window, the pacing, and that testing is decided on the calls.
- **Image block `1744906803654_0`**: was empty. Now Alina's portrait at 320px,
  the same CDN file used on the sales pages. A page selling her time should
  show her.
- **Pay button**: was `#343332`, Kajabi's default grey, not the brand
  terracotta. Set to `#C07A5A` with border radius 2, matching this theme's own
  `btn_background_color` token and the rest of the site.

The $1,497 checkout was checked at the same time and is clean, so this is a
new-offer default rather than a site-wide problem. **Any future offer created
through MCP will have the same placeholder checkout and needs the same pass.**

### 3. Verified on the live page

| Check | Result |
|---|---|
| Checkout reachable logged out | 200, no login wall |
| Placeholders | gone, in render and raw HTML |
| Heading | "Continued coaching with Alina" |
| Alina's portrait | 320x480, centred |
| Price | $997.00, five places on the page |
| Horizontal overflow | none |

**Not verifiable from here: the pay button's colour.** The button renders
disabled in this environment, so its live colour could not be sampled. The
setting is `#C07A5A`; worth one glance on a real browser.

### The "Payments are paused" message: the agent got this wrong

**Corrected 2026-11-09 by Steve**, who supplied the actual cause: the offer's
**Payment providers** setting, under Pricing, must be **Kajabi Payments** and
not **None**. He confirmed with a screenshot that it is set correctly on this
offer.

What the agent said, and why it was not good enough:

The live render shows "Payments are paused on this site" with the pay button
disabled. **This is the documented artifact, not a real state.** Per
`THE-GUT-FIX.md`, the message is injected client side when Stripe's endpoints
refuse this container's proxy. Checked as that note prescribes: the phrase
appears **zero** times in 55KB of raw HTML. Payments are connected.

That reasoning was weaker than it was presented. The Kajabi checkout is a
**client-mounted React app**, verified on 2026-11-09: the served HTML carries
no payment-provider state on any checkout tested. So "the phrase is not in the
raw HTML" only establishes that the message is not server-rendered, which is
true of almost everything on that page. It cannot distinguish a proxy artifact
from a genuinely unset provider, and it was reported as if it could.

The one honest signal the agent did have was inconsistency: the same run
reported the message for this checkout and not for the $1,497. That is
suggestive, not conclusive, and it should have been described that way.

**The check that actually works is in the admin**, per offer: Pricing,
Payment providers, Kajabi Payments. It cannot be read through MCP: `get_offer`
returns pricing, products and post-purchase settings, and no provider field.
Full detail in `THE-GUT-FIX.md`.

---

## Still open

1. **Unused sessions at nine months.** Still undecided. The offer and the
   checkout say nothing about it. This will arrive as a support email
   eventually, and it is cheaper to decide now.
2. **A tag for continuation clients.** No automation was built: this is a
   high-touch sale where Alina knows the buyer by name, so an automated
   welcome would read oddly. But a tag would still be worth having, to answer
   "who is on continued coaching?" without digging through purchases. The two
   courses both got one.
3. **The offer has no thumbnail**, so the checkout's order summary shows a
   grey placeholder icon next to the product name. Cosmetic, on an otherwise
   finished page.
