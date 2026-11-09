# Offer: Continued 1 on 1 Coaching

Created 2026-11-09 at Steve's request: a continuation for clients who have
finished the 3-Month Gut Reset and want to keep working with Alina.
$997, six 1 on 1 sessions across nine months.

**Status: DRAFT.** Kajabi's `create_offer` only ever makes drafts; publishing
is a human step in the admin.

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

## THE ONE THING TO SETTLE BEFORE PUBLISHING

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
