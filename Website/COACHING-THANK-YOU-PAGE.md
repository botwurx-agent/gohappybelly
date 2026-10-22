# The $1,497 thank-you page: what goes on it

Landing page `2150005925`, "Private 1 on 1 Thank You Page", theme `2156349886`.
Public at `/private-one-on-one-thank-you-page`.

Spec from Steve, 2026-10-22, confirmed with Alina.

## It is effectively a dedicated page now

The page is wired as the post-purchase destination for all four coaching
offers, but the $2,497, $4,497 and $1,297 were unpublished on 2026-10-22. Only
the $1,497 is live, so the page can be made specific to that package without
affecting anything else.

## What is on it today

1. "WooHoo, cue the confetti. You're in the private 1 on 1 coaching program."
2. "Check your inbox for your welcome email."
3. "Make sure to schedule your 60 minute New Client Consultation below."
4. A **Google Calendar appointment scheduler**, embedded as a code block
   (`1726510473910`), for the 60-minute New Client Consultation
5. Alina's photo, support email, confetti effect

## What Steve wants on it

Three things the buyer has to do after paying:

1. **Book the initial consultation.** Already there, see the conflict below
2. **Create a profile on a lab-ordering site.** The buyer enters name, address,
   phone and so on. Alina is notified when the profile exists, and only then
   can she order the GI-MAP stool test to be sent out. **This is the step that
   gates the test arriving**, so it is time-sensitive and currently has no
   mechanism at all
3. **Join the private Facebook group.** The checkout now promises this
   explicitly and nothing delivers it

## Blocked on three inputs from Steve

Steve is getting these from Alina, 2026-10-22.

| Needed | Status |
|---|---|
| The Facebook group URL | waiting on Alina |
| The lab-ordering site: real name and URL | waiting on Alina. Steve recalls it as "Better Yourself" or similar and is not sure. The two portals that match the described behavior, buyer self-registers and the practitioner is notified, are **Rupa Health** and **Evexia Diagnostics** |
| Whether the consultation booking is Calendly or the existing Google Calendar embed | **conflict, see below** |
| Is there a health history or intake form to complete before the initial consultation? | **not yet asked.** Most FDN practices have one, and if Alina does, it is a fourth step and belongs in the sequence |

Nothing gets built until these land. A wrong or placeholder link on a page that
paying customers hit is worse than no link, and the lab site in particular asks
for a home address and phone number, so a guessed URL is not acceptable.

## The Calendly conflict

Steve said there should be "a link to Calendly in order to set an appointment
for their initial consultation."

But the page already embeds a **Google Calendar** appointment scheduler for
exactly that, the 60-minute New Client Consultation, and it works.

Calendly is used elsewhere in this business, for the free 20-minute **Gut
Breakthrough Call** at `calendly.com/gohappybelly/gut-breakthrough-call`. That
is a different appointment: a free pre-sale call, not the paid client's initial
consultation.

So either Alina has moved the initial consultation to Calendly, in which case
the Google Calendar embed should be replaced, or Steve is thinking of the
Breakthrough Call, in which case the embed stays as it is. **Do not rip out a
working scheduler on a guess.**

## Proposed structure, once the inputs land

The page currently presents one action. It needs to present three, in the order
that matters, because the lab profile is the one with a delivery deadline
attached and it is the one most likely to be forgotten.

1. **Book your initial consultation** — the existing scheduler, kept in place
2. **Set up your lab profile** — so Alina can order your GI-MAP. Say plainly
   that the test cannot be sent until this is done
3. **Join the private Facebook group**

Numbered, each with one link, above the fold where possible. Alina's photo and
the support email stay.

## The welcome email carries the same three steps

**Decided by Steve, 2026-10-22.** The same numbered sequence goes in an
automated welcome email as well as on the page, with whatever else the buyer
needs to know.

The reasoning is worth writing down, because it decides the format. The
thank-you page is a tab she can close. The email is the thing she can find
again at 9pm when she finally sits down to do the lab profile. So the email is
not a courtesy note, it is the durable copy of the instructions, and it has to
stand alone rather than say "see the page you just left".

Same three steps, same order, same numbers, every link repeated in full.

**Before building it, check what Kajabi already sends.** A product is now
attached to the offer, so Kajabi may send its own product-grant welcome. A new
automation on top of that would double-email a $1,497 buyer. Make a test
purchase, see what arrives, then build.

**How it gets built.** `create_automation` on the Kajabi MCP, triggered on
purchase of offer `2149705539`. It always creates a **draft** and never
publishes, so nothing sends until Steve arms it in the admin. That satisfies
the standing rule about not sending email without explicit confirmation.
