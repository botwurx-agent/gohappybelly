# Offer audit, 2026-10-22

Triggered by Steve asking whether the $147 checkout carries a $1,497 upsell.
It does not, and the audit turned up more than the upsell question.

## The ladder as it exists in Kajabi

| Offer | Id | Price | Status | Products attached |
|---|---|---|---|---|
| Gut Foundations | `2151464245` | $27 | **draft** | Gut Foundations course |
| Happier Belly Gut Reset Program | `2149370663` | $147 | published | Gut Reset Course |
| 3 Month Private 1 on 1 Coaching Package | `2149705539` | $1,497 | published | **none** |
| 3 Month ... Webinar Package (discounted) | `2149874369` | $1,297 | published | none |
| 6 Month Private 1 on 1 | `2149705545` | $2,497 | published | none |
| 12 Month Private 1 on 1 | `2149705550` | $4,497 | published | none |

**Steve, 2026-10-22:** only the $1,497 is relevant. The $2,497 and $4,497 are
not, and nothing should be attached to them.

## There is no upsell anywhere

The $147 checkout goes straight to a thank-you landing page. No Kajabi Upsell
exists on any offer.

The only upsell ever specced is $27 to $147, in
`Documents/Funnel Assets/mini-course/UPSELL-PAGE.md`. The copy is written and
the Upsell shell was never created. It could not go live regardless, because
the $27 offer is still a draft.

**The MCP cannot build Upsells.** There is no upsells toolset. Creating the
shell is a human step at Sales, Pricing, Upsells. The agent can write the copy
and nothing else.

## Was a product deleted from the $1,497?

Steve wondered whether he had deleted one. Evidence says no:

- Six products exist on the entire site and **none has ever been a Coaching
  type**
- The $1,497 offer has **zero purchases, ever**, so nothing was lost and no
  customer has broken access
- The $2,497, $4,497, $1,297 and all seven test kits are configured
  identically. One accidental deletion would not produce that across eleven
  offers
- They share a last-updated timestamp of 2026-09-22 07:50 to 07:51 UTC, which
  reads as one bulk operation touching every offer rather than a deletion

The API exposes no deletion log, so this is circumstantial rather than proof.

## Does a service offer need a product?

No. A Kajabi offer with no products still takes payment, creates the contact,
fires offer-based automations and reports revenue. That is a legitimate setup
for something delivered offline, and it is how the physical test kits are
configured.

What it does not do is put anything in the buyer's Library. She pays and sees
an empty shelf when she logs in.

**But the $1,497 is not purely a service.** Two of its seven inclusions are
Kajabi products that already exist and are not attached:

| Inclusion | Where it lives | Attached |
|---|---|---|
| 60-min consult, monthly follow-ups | offline, Alina | n/a |
| GI-MAP test and reading | physical kit | n/a |
| Meal and supplement plans | offline | n/a |
| Guthub access | external | n/a |
| **Gut Reset Course access** | product `2148514926` | **no** |
| Private community access | **a Facebook group**, not Kajabi | n/a |

**Corrected by Steve, 2026-10-22.** The agent initially read AccessGroup
`2148816202` ("Happier Belly Gut Reset Program", description "Group Chat") as
the community deliverable and recommended attaching it. That was wrong. The
private group in this bundle is a **Facebook group**, and the buyer is given
access to it outside Kajabi.

So only one product needed attaching, not two. AccessGroup `2148816202` is
genuinely orphaned, attached to no offers, and is not part of this or any
current flow. Leave it alone or retire it; do not wire it into an offer.

## What the flow looks like now

1. **Checkout.** Was a $1,497 page with an empty description. **Fixed:** the
   offer description now lists what is included, prices the GI-MAP at its
   standalone $497, keeps the optional-clinical-recommendation framing on
   further testing, and tells her the consult is booked on the next page.
2. **Payment.** Works.
3. **Thank-you page**, `2150005925`, shared by all four coaching offers.
   Better than expected: confirms the purchase, shows Alina's photo, and
   **embeds a Google Calendar scheduler for the 60-minute new client
   consultation**. The booking step works. Note it is Google Calendar here,
   not the Calendly used for the Gut Breakthrough Call.
4. **Product access.** Nothing. This is the gap.
5. **Welcome email.** The thank-you page says "Check your inbox for your
   welcome email." **No such automation exists.** The site has exactly two
   automations and both are for the Gut Secrets webinar.

## Outstanding

Both resolved on 2026-10-22. See the Resolved section at the end.

**Open question before anything else is built:**

The welcome email. Kajabi can send a product-grant welcome email configured on
the product itself, separate from automations. Attaching the two products above
may therefore satisfy the page's promise on its own. Building an automation now
risks double-emailing a $1,497 buyer, so check what arrives after the products
are attached before adding one.

## Two naming mismatches worth a decision

- CLAUDE.md calls the $1,497 the **3-Month Gut Reset**. The live offer is
  **3 Month Private 1 on 1 Coaching Package**. Steve used the live name in
  conversation, so the doc may be the thing that is out of date.
- CLAUDE.md calls the $147 the **Gut Reset Course**. The live offer is
  **Happier Belly Gut Reset Program**, though the product underneath it is
  correctly named Gut Reset Course.

Left alone. Renaming a published offer changes the checkout page and the
receipt, so it is Steve's call.

## On an upsell at the $147 checkout

Recommendation: a one-click $1,497 straight after a $147 purchase is the wrong
shape. It is a ten times jump on a high-touch service, sold to someone who
bought on impulse and has not opened a lesson. The funnel already routes that
sale through the Gut Breakthrough Call, and the course's final lesson, When You
Have Finished, points there.

Better order: fix the delivery gap, rebuild the $147 thank-you page to get her
into the course and book the call, and only then consider a paid upsell. If one
is wanted, the $1,297 already exists and gives a real reason for the lower
price rather than an arbitrary discount.


---

## Resolved, 2026-10-22

**$1,497, offer `2149705539`.** Steve attached Gut Reset Course `2148514926` in
the Kajabi UI. Verified: the offer is published, carries the course, and keeps
its live checkout URL `/offers/442eXHU6/checkout`. The checkout description the
agent wrote is live on it.

Only the course needed attaching. The private group is on Facebook, so there is
no second Kajabi product in this bundle.

**$2,497 `2149705545` and $4,497 `2149705550`.** Unpublished at Steve's
instruction, now `draft`. They were live and purchasable while delivering
nothing. Reversible: set a `publish_at` to bring either back.

## Still open

1. **How does the buyer get the Facebook group link?** Nothing delivers it. The
   thank-you page does not mention the group, and there is no welcome email.
   The checkout description promises "access to the Gut Reset Course and to the
   private group", so right now the second half of that is a promise with no
   mechanism behind it. Easiest fix is a line and a link on the thank-you page,
   which needs the group URL from Steve.

2. **The welcome email.** The thank-you page says "Check your inbox for your
   welcome email" and the site has only two automations, both for the webinar.
   Now that a product is attached, Kajabi's own product-grant welcome email may
   cover this. Worth a test purchase to see what actually arrives before
   building an automation that would double up.

3. **The $1,297, offer `2149874369`.** Still published, still has no products.
   It is the discounted version of the same three-month package, so a buyer
   there would now get less than a buyer at $1,497, who gets the course. Either
   attach the course to it as well or unpublish it. Not raised with Steve yet.
