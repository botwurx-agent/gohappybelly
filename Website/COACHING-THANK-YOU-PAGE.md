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

---

# Revamp, 2026-10-22

Rebuilt on `Website/DESIGN-SYSTEM.md`. Landing page `2150005925`, theme
`2156349886`, **Encore 2.1.0** (not Nova, despite that being the engine for new
inner pages; this page predates the switch and there was no reason to move it).

## What it was

A seeded template that had never been brought onto the system:

| | Was | Now |
|---|---|---|
| Heading + body font | Poppins / Poppins | Playfair Display 400 / DM Sans 300 |
| Primary color | `#a9d7db` pale blue | `#7AAE86` sage |
| Button | `#a9d7db` on `#2c3e50`, radius 50 | `#C07A5A` terracotta on white, radius 2 |
| Body text | `#000000` | `#2E4438` |
| Heading | `#161E2A` | `#162E28` |
| Section background | `#9acdaa` mint | `#F8FAF8` |
| Page background | `#ffffff` | `#F8FAF8` |
| Footer | `#95a5a6` grey | `#112420` |
| Confetti | `#dbdedf` / `#b59755` gold / `#ffe3de` pink | sage / sage light / terracotta |
| Header | overlay, `rgba(251,251,251,0.02)`, logo 200px | static + sticky, white, logo 104px, `#C8DDD0` bottom rule |
| Type scale | 56/42/30/24/20/16, body 18 | design system 58/38/26/20/17/15, body 16 |

The footer copyright block still read **"Penny In Your Pocket"**, left over from
whatever template this page was seeded from. It was hidden, so it never showed,
but it was sitting in the file.

## Structure now

One section (`1573259369662`, renamed "Welcome and first step"), six blocks,
all full width and centred, `#F8FAF8`, padding 88/100 desktop and 56/64 mobile:

| Block | Type | What |
|---|---|---|
| `1573261197744` | text | Sage eyebrow, `<h1>` "You're in.", lead line capped 560px |
| `1761100000001` | text | "First step" eyebrow, `<h3>` heading, 15px muted sub capped 520px |
| `1726510473910` | code | The Google Calendar scheduler, now in a white card: `1px #C8DDD0`, radius 3, medium shadow, width 10 of 12 |
| `1761100000002` | text | "Then check your inbox", above a `#C8DDD0` hairline |
| `1602561429254` | image | Alina, 132px, centred |
| `1761100000003` | text | The locked sign-off, Playfair italic |

Headings are real `<h1>`/`<h3>` with no pinned font size, so they inherit the
Style Guide and stay responsive, per §2.

## Two deviations from the design system, on purpose

**The portrait.** §4 specifies 380px at 3/4 with a drop shadow, or 486px at
4/5. The image on this page is a circle-cropped transparent PNG
(`Alina_Fence_Jacket_Circle.png`). A box shadow on a circular PNG renders as a
rectangle behind the circle, and a 3px corner radius does nothing to it. So it
sits at 132px, centred, no shadow, no radius, as a small sign-off portrait
rather than a hero portrait. Replacing it with a rectangular crop would let the
page follow §4 exactly; it is not worth a render cycle on a page whose job is
instructions.

**The footer.** §6 wants logo, tagline, link row and a three-line legal block.
Encore's footer schema only offers `copyright`, `link_list` and `social_icons`,
so there is nowhere to put a logo or a free text block. The FDN-P disclaimer
rides in the copyright slot instead, which is what §8 actually requires
("the footer says so on every page"). The social icon row is hidden, per §6.

## Wording

Replaces "WooHoo - Cue the Confetti... / You're in the private 1 on 1 coaching
program!" and its trailing ellipses. The register was wrong for Alina: cutesy
where she is warm and direct, and three exclamation-adjacent flourishes in four
lines.

What is live now is the honest version of this page **while the two links are
missing**: one thing to do (book the consultation), and a plain statement that
the welcome email carries the rest. It is a complete page, not a page with holes
in it. The "Then check your inbox" block names the GI-MAP step specifically, so
the buyer knows what is still coming and why the email matters.

The full numbered three-step version is written out in
`Website/COACHING-ONBOARDING-COPY.md`. When the lab-profile and Facebook-group
URLs land, one `update_theme_content` call does all of it:

1. Add two text blocks after `1726510473910`, with a terracotta button each.
2. Renumber the step eyebrows: "First step" becomes "Step 01", and the two new
   blocks carry "Step 02" and "Step 03".
3. Change block `1573261197744`'s lead to add "Three things to do now, in this
   order. Fifteen minutes in total."
4. Rewrite `1761100000002` from "the email carries the rest" to "all three of
   these are in your welcome email as well".

If Alina has an intake form, it becomes Step 02 and the other two shift down.

## Verification

JSON verified: all six block ids present in both `blocks` and `block_order`,
the section still listed in `content_for_index`, top-level tokens intact.

**The render was not visually verified.** Cloudflare returns 403 to this
container's IP for `www.gohappybelly.com`, with and without a browser user
agent, so the page could not be fetched and compared. Steve should open
`/private-one-on-one-thank-you-page` and check three things in particular:

- The `#section-header` bottom-rule selector is a reasoned guess at Encore's
  markup, not a verified one. If the header has no hairline under it, the
  selector is wrong and needs the real one from the home page theme
  (`2156348838`), which is the reference implementation on this same engine.
- Playfair Display and DM Sans both load. Kajabi pulls Google Fonts from the
  Style Guide tokens, so they should, but a typo in a family name fails silently
  to a system serif.
- The scheduler iframe still loads inside its new white card.

## Scheduler swapped to Calendly, 2026-10-22

The Calendly question is settled. Alina has a real **60 Minute Consultation**
event at `calendly.com/gohappybelly/60-minute-consultation`, so this was not a
guess after all, and code block `1726510473910` (renamed "Calendly scheduler")
now carries the Calendly inline widget instead of the Google Calendar iframe.

Embed settings chosen in Calendly's "Add to website" dialog:

| Setting | Value | Reasoning |
|---|---|---|
| Hide Page Details | on | The page already supplies the heading and "Sixty minutes". Leaving it off stacked a second "60 Minute Consultation / 60 min" header directly under our `<h3>` |
| Hide Cookie Banner | off | Turning it on tells Calendly the site handles consent itself, and it has no banner. No upside to taking that on |
| Background | white (default) | The widget sits inside a white card, so the seam stays invisible. Calendly omits the param when it is the default, which is why it is absent from the URL |
| Text | `2e4438` | Was black. Black is not in the palette and is the same thing that was stripped out of the course lessons |
| Button & Link | `c07a5a` | Terracotta, per §3: every primary button, nothing else |

These bake into the `data-url` as query parameters at copy time, so the settings
have to be chosen **before** Copy Code. A block copied first and adjusted after
carries none of them.

**The Google Calendar scheduler is no longer on the page.** Its URL, kept here
because nothing else now records it:

```
https://calendar.google.com/calendar/appointments/schedules/AcZssZ33z_foYnhld6LCFrykQAJQdVjPfMlRmAjKUPtnX5pZgFrxlhQYSiC7gWFUp1kn1sAKr_JzLk6y?gv=true
```

**Open, and worth closing quickly.** If that Google appointment schedule is
still accepting bookings, two systems are now writing to the same hours of
Alina's day with no knowledge of each other, and she will eventually be
double-booked. Removing it from the page does not switch it off. It has to be
turned off in Google Calendar, or Calendly has to be pointed at the same
calendar so it reads the existing busy blocks.

Also still open: if Alina keeps prep instructions in the Calendly event
description, `hide_event_type_details=1` hides them. That copy belongs in the
grey sub-line under the step heading instead.

## Private group added, 2026-10-22

`https://www.facebook.com/groups/gohappybelly/` is live on the page as block
`1761100000004`, sitting between the scheduler and the inbox note: sage eyebrow,
`<h3>`, a 15px muted line, and a terracotta button that opens in a new tab.

**It is not "Step 03", and that is deliberate.** Alina's view is that the group
goes to anybody who buys anything, which makes it a standing thing every
customer gets rather than a rung in this program's onboarding. So its eyebrow
reads "Your community", a category label, not a position in a sequence. The two
things that genuinely gate something, the consultation and the lab profile, keep
the ordinals. That also means the lab profile slots in as "Second step" when its
URL lands without renumbering anything below it.

The copy says plainly that it is a Facebook group and needs a Facebook account.
Some buyers do not have one and will not want one, and it is cheaper to say so
here than to field the support email.

The inbox note shrank accordingly: "the short setup steps that come next"
became "the one setup step left", since the group is no longer waiting in the
email.

Buttons now pick up §3 (uppercase, `0.13em`, 12px, 14/34 padding) from a `.btn`
rule in `settings.css`. Like the `#section-header` rule, that selector is a
reasoned guess at Encore's markup and is unverified until someone opens the page.

### Where else the group link has to go

Alina's decision reaches past this page. Every surface a buyer lands on after
paying needs it, and right now only this one has it:

| Surface | Offer | State |
|---|---|---|
| Coaching thank-you page `2150005925` | $1,497 `2149705539` | **Done** |
| Course thank-you page `2150005720` | $147 `2149370663` | Missing. This is the one with live buyers |
| Happy Belly Essentials Club | $9.97/mo `2149750878` | Missing, thank-you page not yet identified |
| Gut Foundations | $27 `2151464245` | Still draft. Add before it is published |

The $147 page is likely the same seeded Encore template this one was, so it
probably wants the same revamp rather than a link dropped into off-palette
chrome. Worth confirming before deciding how much to spend on it.
