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

3. **The $1,297, offer `2149874369`.** Unpublished at Steve's instruction,
   now `draft`. The only live coaching offer is the $1,497.


---

## The order bump on the $1,497 checkout, 2026-10-22

Steve: a "Happy Belly Essentials Club" offer at $9.97/month shows up under
**ADD TO YOUR PURCHASE** on the $1,497 checkout, and he could not find where to
remove it.

**It is a Kajabi order bump, and the MCP cannot see or remove it.** Confirmed by
elimination:

- `get_offer` on the $1,497 (`2149705539`) returns no bump field
- `get_offer` on the Essentials Club (`2149750878`) returns no bump field
- The checkout theme `2167629152` has no bump section. Its sections are Hero,
  `offer_embedded_checkout`, header, footer, exit pop, two step, and the
  checkout section's settings cover only button color, borders, column width,
  tracking code and mobile order

So it is offer-level configuration that the commerce toolset does not expose.
In the Kajabi admin it lives on the checkout settings of the offer whose
checkout displays it:

`https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149705539&resource_type=Offer&view=checkout`

## Problems found in the checkout copy while looking

The left column of that page is a theme Text block
(`1746107473790` in theme `2167629152`), not the offer description. It carries
its own "What You Will Get" list, and it has three issues:

1. **It calls a one-time payment a subscription.** The offer is
   `price_type: one_time`, a single $1,497 charge. The copy says "This is a 3
   month subsription", with that typo, and then "You can cancel anytime within
   your account". There is nothing to cancel on a one-time charge.
2. **It contradicts itself.** Non-refundable and cancel anytime in the same
   paragraph. On a $1,497 purchase that is a dispute risk, not just untidy.
3. It promises "3 Month Access To The Happier Belly Gut Reset Course". Whether
   the course grant is actually time-limited to three months depends on the
   access duration set when the product was attached, which the MCP cannot read.

## Open question on the description the agent wrote

The checkout section has `sync_checkout_block_to_offer: false`, and the page
already carries its own list in the theme block above. Where the offer
description renders on this custom Encore checkout, if at all, is not visible
from the API. If it does render, it now duplicates the theme block's list.

Resolve by looking at the live preview before changing anything. If the
description is redundant, the better fix is to correct the theme block and
clear the description rather than keep both.

---

## Checkout copy fixed, 2026-10-22

Theme `2167629152`, section `1744906803654`, text block `1746107473790`.
Verified after writing: both blocks present, `block_order` and section settings
untouched.

**The payment terms, which were the real problem.** Was:

> Note: This is a 3 month subsription. The full $1497 is charged upon purchase
> and is non-refundable. You will gain access immediately upon signup. You can
> cancel anytime within your account, or by sending us an email.

Now:

> Note: this is a one-time payment of $1497 for the three month program. There
> is no recurring billing and nothing to cancel. The payment is non-refundable,
> and your access starts as soon as you sign up.

The offer is `price_type: one_time`. Calling it a subscription and offering
cancel-anytime alongside non-refundable was a contradiction a buyer could
screenshot and dispute.

**The inclusions list**, tightened to match CLAUDE.md:

- Consultation durations stated: 60 minutes initial, 30 minutes monthly
- "GI Map Stool Test At Home Kit" and "Free Lab Results Reading Included"
  folded into one line, spelled GI-MAP, with the $497 standalone value
- Guthub added. CLAUDE.md permits naming it among the Reset inclusions, where
  three months of it is genuinely part of what the buyer gets
- "Access To Private Community Support" is now "Access to the private Facebook
  community", so she knows to expect an invite rather than a Kajabi login

**Left alone deliberately:** the price heading is `#e60202`, a bright red that
belongs to no palette in this business. Changing it is styling rather than copy
and was not asked for. Worth a decision.

## The order bump: removed by Steve, 2026-10-22

**The MCP cannot touch order bumps.** They are offer-level configuration
exposed nowhere in the commerce toolset, and `update_offer` has no field for
them. Not readable either, so the removal cannot be verified from here. Steve
confirmed it visually.

**Where it actually lives, corrected.** The agent guessed the offer's
**Checkout** tab. Wrong. It is under **Settings** on that offer's checkout
page:

`https://app.kajabi.com/admin/cofounder/deep_link?offer_id=2149705539&resource_type=Offer&view=settings`

Two things made this hard to find, worth remembering:

1. It is configured on the **offer whose checkout displays it**, the $1,497,
   not on the Happy Belly Essentials Club offer being bumped
2. It is under Settings, not under Checkout, even though it is a checkout
   element

Unpublishing the Essentials Club would also have cleared it, but that offer is
a live $9.97/month subscription that may have subscribers, so that was the
wrong lever.

## The empty image slot on the $1,497 checkout, 2026-10-22

Steve spotted an empty image placeholder at the top of the left column and
asked whether it should match the photo on the right. They are two separate
things:

| | What it is | Set where |
|---|---|---|
| **Right**, the small photo in the order summary card | the **offer's own image**, rendered by Kajabi's checkout block | the offer record, not the theme |
| **Left**, the empty placeholder | theme image block `1744906803654_0`, with `image: ""` | theme `2167629152` |

The left one is a leftover slot someone added and never filled. Hidden rather
than filled, for two reasons: a second photo of Alina six inches from the first
is noise, and nothing else in the media library belongs at the top of a
checkout. Reversible by setting `hidden` back to `"false"` on that block.

**Likely only visible in the builder.** The pale blue box with an image icon is
Kajabi's editor affordance for an empty image block. An Encore image block with
an empty `image` setting normally renders nothing on the live page. Not
confirmed, since the live page cannot be loaded from here. Open
`/offers/442eXHU6/checkout` in a private window to see what a buyer actually
gets.

If that slot is ever wanted, the thing most worth putting there on a $1,497
page is a client testimonial rather than another photograph.

---

## $147 checkout copy rewritten, 2026-10-23

Offer `2149370663`, checkout theme `2167629154`, text block `1746107473790`.

### What it said, live, on a published checkout

> Note: This is a subscription membership is a **1 year subscription**. The full
> **$197** is charged upon purchase and is non-refundable. You will gain access
> immediately upon signup. You can cancel anytime within your account, or by
> sending us an email.

Four things wrong at once. The offer is `price_type: one_time` at **$147**, so
it is not a subscription, there is nothing to cancel, and the stated price was
**$50 higher than the amount actually charged**. The sentence is also
ungrammatical ("This is a subscription membership is a"). The heading still read
"Happier Belly Gut Reset Program" after Steve renamed the offer to "Gut Reset
Course".

This is the same failure found on the $1,497 checkout on 2026-10-22. Two of two
checkouts inspected have described a one-time payment as a cancellable
subscription. **Assume the remaining published checkouts do too** until each is
read.

### What replaced it

Title corrected, plus a one-line positioning statement and six inclusion
bullets, each checkable against what is actually in the course:

> Most gut programs hand everyone the same plan. This one asks which of the five
> patterns is yours first, then gives you the four weeks written for that one.

The terms now read:

> Note: this is a one-time payment of $147. There is no subscription and nothing
> to cancel. Your access starts as soon as you sign up, and the payment is
> non-refundable.

Copy changes from Steve's draft of the bullet list, and why:

| Was | Now | Reason |
|---|---|---|
| "Personalized protocol tailored to your specific gut pattern" | "The four weeks written five separate ways" | The course is pattern-specific, not personalized. "Personalized" at $147 sets an expectation of something made for her individually, and that gap becomes a refund |
| "four week plan to ease symptoms" | "self-paced video lessons, start whenever you want" | The only outcome claim in the list, removed rather than softened |
| Reintroduction listed fourth | Promoted, with the tracker named | It is the course's best feature and the thing the $27 explicitly cannot give her. The upsell copy already leads with it |
| No mention of the group | "The private group, for questions as you work through it" | Alina's decision: the group goes to anybody who buys anything. It was a real inclusion that was not being sold |

### The value stack was dropped, deliberately, and it is reversible

The old block carried a seven-item stack totalling "$4200", including "The
Happier Belly Program (Value $1297)". That number sits just under the $1,497
1:1 coaching price, which muddies the ladder: it implies the self-paced course
is worth almost as much as three months of Alina's time. The figures were also
not traceable to anything.

Dropping it is a conversion decision, not a cleanup, and it was made without
asking. **Flagged to Steve.** Easy to reinstate if he wants it.

### Two open questions

1. **Does $147 access expire?** The 3-Month Gut Reset grants "3-month Gut Reset
   Course access", so bundled access is time-limited. Whether the standalone
   $147 is permanent is not recorded anywhere. The new copy says access starts
   at signup and deliberately says nothing about it ending.
2. **Refund policy is inconsistent across the suite.** This checkout says
   non-refundable, carried over from the old copy. The Gut Fix ebook advertises
   a 30 day refund guarantee. Not resolved here.

### The order summary panel is not in the theme

The "What's included" list Steve pasted, with the Subtotal line, is the Kajabi
checkout block's own panel on the right. `sync_checkout_block_to_offer` is
`false` on this section and the offer `description` is empty, so that list is
configured on the **offer's Checkout tab in the admin**, the same area where the
order bump turned out to live. It is not reachable through the theme tools, so
Steve pastes that one.


---

## Gut Foundations checkout, 2026-10-23

Offer `2151464245`, checkout theme `2167984952`, `/offers/yYfiaNgo/checkout`.

Found live, on a published checkout taking money, still carrying **Kajabi's raw
placeholder template**:

```
[Offer title]
[ Insert a call to action statement that will encourage the customer to purchase ]
What you'll get:
  [ Insert value 1 ]
  [ Insert value 2 ]
  [ Insert value 3 ]
[ Add any additional disclaimers or details about the purchase ]
```

Plus an empty image block rendering nothing, the same fault fixed earlier on the
$1,497 checkout.

Replaced with real copy: the eight foundations and three bonus modules, twelve
reflection questions, the private community, lifetime access, and a closing line
that it is written rather than video. The cut-paper dashboard image now fills the
image block.

The checkout button was on Kajabi's default dark grey pill (`#343332`, radius
50). Set to terracotta `#C07A5A` at radius 2, per the standing design system
rule.

### Price is deliberately not written into the copy

`sync_checkout_block_to_offer` is true and `show_checkout_block_price_text_override`
is false, so the checkout block renders the offer's real price by itself. The
prose says "One payment, nothing recurring" and names no number.

That is the lesson from the $147 checkout, which had a hardcoded $197 and the
word subscription sitting on a $147 one-time offer. A number typed into checkout
prose drifts the moment the offer changes and nothing warns you.

### Three of three

Every checkout inspected in this session has been wrong in a way a buyer would
see:

| Offer | Fault |
|---|---|
| $1,497 3-Month Gut Reset | Bad copy, empty image block |
| $147 Gut Reset Course | Stated $197 and "subscription" on a $147 one-time offer |
| $27 Gut Foundations | Raw Kajabi placeholder text, empty image block |

**The remaining published checkouts are unaudited**: eight lab test offers from
$250 to $639, and anything else published. On a three for three record it is
reasonable to assume several are broken. Worth a sweep.


---

## Checkout button colour, normalised across all 16 offers, 2026-10-25

Steve asked whether `#16a085` was the correct colour for checkout buttons. It
was not, and it was live.

`Website/DESIGN-SYSTEM.md` is unambiguous:

| Terracotta | `#C07A5A` | Every primary button. Nothing else |

`#16a085` is a teal. It appears in no Go Happy Belly spec, website or email.
It was found on the **$147 Gut Reset Course checkout**, which is almost
certainly where Steve saw it.

### What every checkout was actually on

Three different wrong colours were in play, none of them the brand's:

| Was | Where |
|---|---|
| `#16a085` teal | $147 Gut Reset Course |
| `#76a685` old sage | The eight lab tests, Essentials Club, Group Coaching, E-Book |
| `#343332` Kajabi default grey | H. Pylori and anything with no value set, which falls through to the schema default |

All sixteen published offers are now `#C07A5A` at `border_radius: 2`, matching
the button spec in §3 of the design system.

### Why the radius matters too

Kajabi's default is `checkout_block_btn_border_radius: 50`, a full pill. The
design system specifies radius 2, a near-square corner, everywhere. Both values
were set together on every checkout, so the buttons now match the ones on the
sales pages rather than looking like a different brand at the moment of payment.

### Still unverified

Cloudflare blocks this environment from the live site, so the settings are
confirmed stored and the rendering is not. One checkout opened in a browser
settles it for all sixteen, since they now carry identical values.
