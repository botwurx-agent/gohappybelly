# Offer Spec: 3-Day Bone Broth Fast

**Status:** Landing page BUILT as a draft in Kajabi. SamCart and Mailchimp not yet built.
**Created:** 2026-09-21
**Price updated:** 2026-09-21, $87 to $47 (Alina's decision)
**Stack decision (Steve, 2026-09-21):** Content, courses, and landing pages live on Kajabi.
Checkout runs through SamCart, surfaced from the Kajabi page. Mailchimp keeps email. ScoreApp
keeps the quiz. Calendly keeps call booking.

---

## 1. Offer summary

| Field | Value |
|---|---|
| Public name | The 3-Day Bone Broth Reset |
| Internal name | BBF-[COHORT-MONTH] (e.g. BBF-2026-10) |
| Price | $47 |
| Early-bird | None. Flat $47, urgency comes from the capped seat count |
| Format | Live cohort, 3 days, 50 seats |
| Delivery | 2 Zoom calls, private group, 3 daily check-ins, written guide |
| Position in suite | Entry / ascension offer. Sits above Guthub ($13/mo), below Gut Reset Course ($147) |
| Ascension path | Closing call soft-pitches 1:1 coaching and GI-MAP as optional next steps |

### Naming conflict: RESOLVED 2026-09-22

The offer was originally "The 3-Day Gut Reset: Bone Broth Fast", which sat one character from
the "3-Month Gut Reset" ($1,497) and risked refund disputes from buyers who thought they had
bought the flagship. It also meant the page's biggest headline never said what the offer
actually was.

Renamed to **The 3-Day Bone Broth Reset** across the page H1, SEO title, Kajabi landing page
title, and this spec. The slug `broth-reset` was already rename-proof and did not change.

Current ladder: Guthub ($13/mo), Bone Broth Reset ($47), Gut Reset Course ($147),
3-Month Gut Reset ($1,497).

---

## 2. Kajabi build

Kajabi write actions through MCP land as **drafts**. Everything below can be drafted by Claude
once the connector is live, then reviewed and published by Steve in the Kajabi admin.

### 2.1 Product (content container)

**Product name:** 3-Day Gut Reset: Bone Broth Fast

| Module | Contents |
|---|---|
| Start Here | Welcome video/text, what to expect, screening reminder |
| Before You Start | Written guide PDF, broth ratios and recipes, grocery and sourcing list, hydration and electrolyte plan |
| Your Calls | Kickoff Zoom link + replay, Closing Zoom link + replay |
| Day by Day | Day 1, Day 2, Day 3 posts (each holds that day's check-in and tip) |
| After the Reset | How to break the fast, what to eat first, where to go from here |

### 2.2 Offer (access grant)

**Offer name:** BBF-[COHORT-MONTH] Access
**Grants:** the Product above, plus community/group access
**Pricing in Kajabi:** set to $0 / free, or leave unpublished for direct sale.

This is the important bit. Because SamCart owns checkout, the Kajabi Offer is **not** the thing
customers buy. It exists purely as the access token that SamCart grants after payment. Do not
publish a Kajabi checkout for it, or you create a second buyable path at the wrong price.

### 2.3 Landing page: BUILT (draft)

| Field | Value |
|---|---|
| Site | Go Happy Belly (`2148204891`) |
| Landing page ID | `2152286720` |
| Theme ID | `2167624377` (Encore) |
| Slug | `broth-reset` |
| Public URL (once published) | https://go-happy-belly.mykajabi.com/broth-reset |
| Builder | https://app.kajabi.com/admin/themes/2167624377/settings/edit |
| Page settings | https://app.kajabi.com/admin/landing_pages/2152286720/edit |
| Status | **PUBLISHED** (Steve published it 2026-09-22). Theme edits go live immediately, there is no draft layer. |

Ten sections: Hero, The Problem, The Shift, What's Included, How It Runs, Pattern Fit,
About Alina, Testimonials, FAQ, Screening and Final CTA.

**Conversion pass, 2026-09-22.** Four changes applied to both the Kajabi page and the local
reference:

1. **Five buy CTAs, up from one.** Previously only the hero and the final section had buy
   buttons, and the single mid-page button sent readers off to the ScoreApp quiz. Buy CTAs now
   sit after What's Included, after How It Runs, and in Pattern Fit. The quiz link is demoted
   to an inline text link inside Pattern Fit.
2. **H1 says what the offer is.** "The 3-Day Gut Reset" became "The 3-Day Bone Broth Reset".
3. **Guarantee surfaced.** "Not right for you? Reply and we'll refund you in full." now sits
   directly under every CTA. It previously appeared only once, buried in the screening block
   at the bottom of the page.
4. **Pattern Fit no longer routes buyers away.** The Wired-and-Tired entry used to end with
   "start with the Gut Reset Course instead", selling a different product mid-page. It now
   points at the kickoff call, which is where Alina would screen them anyway. The caution
   itself is unchanged and should stay.

Deliberately NOT changed: the screening block still sits directly above the final CTA, per the
source launch kit. It costs some momentum at the last decision point, but screening before
purchase is the right call for a fasting protocol, and the earlier CTAs mean it no longer gates
every path to checkout.

Still on the table from the conversion review, not yet applied: an offer recap beside the final
CTA, reordering the FAQ so "what if I have to stop partway through" leads, and moving one
testimonial up near the hero.

Style Guide tokens were set from the `landing-page.html` reference rather than Encore's
defaults: Playfair Display headings, DM Sans body, heading `#162E28`, body `#2E4438`,
secondary `#6A8278`, primary `#7AAE86`, buttons `#C07A5A` at 2px radius, page background
`#F8FAF8`.

### Cohort 01 schedule and checkout

**Checkout URL (live):** `https://mystore2429.mysamcart.com/checkout/the-3-day-gut-reset`
All five CTAs point at it. Note the SamCart slug still carries the old offer name; harmless,
but worth renaming the SamCart product for consistency at some point.

**Kickoff call:** Tuesday, September 29 at 10:00 AM PT. **Seats:** 50.
**Doors close:** Monday, September 28.

Note on the timezone: September 29 falls inside daylight saving, so Pacific is PDT, not PST.
All copy says "PT" rather than "PST" so nobody converting timezones lands an hour early.

Confirmed calendar:

| Step | Date |
|---|---|
| Doors close | Mon, September 28 |
| Kickoff Zoom call | Tue, September 29 |
| Day 1 | Wed, September 30 |
| Day 2 | Thu, October 1 |
| Day 3 | Fri, October 2 |
| Closing Zoom call | Sat, October 3, 10:00 AM PT (assumed, matches kickoff time) |
| Day 5 follow-up email | Mon, October 5 |

### Broadcast send schedule to set in the Kajabi admin

| Broadcast | ID | Send |
|---|---|---|
| BBF 02 Day 1 check-in | 2158576121 | Wed, Sept 30, 7:00 AM PT |
| BBF 03 Day 2 check-in | 2158576122 | Thu, Oct 1, 7:00 AM PT |
| BBF 04 Day 3 check-in | 2158576123 | Fri, Oct 2, 7:00 AM PT |
| BBF 05 Day 5 follow-up | 2158576124 | Mon, Oct 5, 9:00 AM PT |

Morning sends so the check-in lands before the day starts rather than after it.

### CRITICAL: the welcome email can arrive after the kickoff call

The sequence email `BBF 01` is set to day 0 at `send_time_in_minutes: 660`, which is 11:00 AM
Pacific. The sequence itself has `send_hour: 11`.

That means a contact who buys at, say, 2:00 PM on Monday September 28 (the day doors close)
would receive their prep email at 11:00 AM on Tuesday September 29, which is **one hour after
the kickoff call has already started**. They get the grocery list, the group link and the call
time too late to use any of it.

Two fixes, do both:

1. **In the Kajabi admin**, open the sequence and set `BBF 01` to send immediately on
   subscription rather than at 11:00 AM. This cannot be changed through MCP; there is no
   update tool for sequence send timing.
2. **Put the same information on the SamCart thank-you page**: kickoff call date, time and
   Zoom link, the group link, and "your prep guide is in your inbox". A thank-you page renders
   instantly and does not depend on email timing at all. This is the reliable path and the
   email becomes the backup.

Also note `BBF 01` has `publication_status: draft`. Publish it in the admin or it will not
send at all.

**Copy note:** the scarcity line originally read "seats are capped so the group stays personal."
At 50 seats that claim strains, so it now reads "50 seats, and doors close Monday, September 28."
Harder deadline, no credibility risk.

**Still outstanding:**

1. The About Alina image block is empty. Upload her photo in the builder (the local file is
   `Documents/Funnel Assets/Alina_Fence.jpg`). MCP cannot upload images.
2. Link placeholders still in the emails: `[GROUP LINK]` (emails 01, 02, 03), `[GUIDE LINK]`
   (email 01), `[CLOSING CALL ZOOM LINK]` (email 04).

**Testimonials:** now carry the three real quotes from the live site (Tiffani, Hanna, Linda).
These are 1:1 coaching clients, not reset participants, and the section subhead says so
outright. Do not delete that line unless you are replacing these with quotes from an actual
cohort. Swap in real reset testimonials after the first round finishes, which is also reel 7
in the launch sequence.

---

## 3. Checkout (Kajabi native): BUILT

**Decision, 2026-09-22:** this offer sells through Kajabi's own checkout. SamCart is not in the
path. Steve is testing Kajabi checkout on this offer before deciding whether to drop SamCart
across the whole business.

The deciding argument was not feature parity. It was that the entire automation design existed
to work around one unverified assumption: whether a SamCart-granted offer fires Kajabi's
`offer_purchased` trigger. Neither vendor documents it. Native checkout deletes the question.
With six days to kickoff, removing an untested integration beat any checkout feature delta.

Secondary reasons: the payment step now sits on Alina's own domain instead of
`mystore2429.mysamcart.com`; this offer uses none of SamCart's differentiators (no bump, no
upsell, no payment plan, and A/B testing 50 transactions is meaningless); and Kajabi offers
have a post-purchase page, which retires the welcome-email timing risk in section 4.3.

What Kajabi genuinely still lacks versus SamCart: native checkout A/B testing. That matters if
checkout optimization becomes a growth lever in the Phase 3 paid-ads plan. It does not matter
at current organic scale. Most "SamCart wins" comparisons online are SamCart's own marketing
pages and should be discounted.

**Keep the SamCart subscription running one more billing cycle** as fallback. The product and
URL still exist there.

### The offer

| Field | Value |
|---|---|
| Offer ID | `2151405804` |
| Title | The 3-Day Bone Broth Reset |
| Price | $47.00 USD, one-time |
| Status | **DRAFT.** Publish in the Kajabi admin. |
| Checkout URL | https://go-happy-belly.mykajabi.com/offers/F9gERGKo/checkout |
| Admin | https://app.kajabi.com/admin/offers/2151405804/edit |
| Products attached | **NONE.** See the blocker below. |

All five landing page CTAs point at `/offers/F9gERGKo/checkout`.

### BLOCKER: the account is at its product limit

`create_course` failed with "Your account has reached the product limit." The site already
carries seven products, all created in 2024 and none updated since November 2024:

| Product | Type |
|---|---|
| Go Happy Belly Course | Course |
| 3 Month Private 1 on 1 Coaching Package | CoachingProgram |
| 6 Month Private 1 on 1 Coaching Package | CoachingProgram |
| 12 Month Private 1 on 1 Coaching Package | CoachingProgram |
| Members | AccessGroup |
| E-Book: Making Your Way To A Happier Belly | DigitalDownload |
| Happier Belly Gut Reset Program | AccessGroup |

So the offer currently grants **no product access**. A buyer is charged $47 and Kajabi hands
them nothing automatically. Three ways forward:

1. **Ship without a product (works for cohort 01).** Everything this offer actually delivers is
   external to a Kajabi product anyway: two Zoom calls, a group, daily emails, and a guide
   file. The post-purchase message and the emails carry all the links. Zero cost, works today.
   Cost: no member library page, and call replays live in the community rather than a product.
2. **Free a slot.** Several 2024 products look dormant, particularly the two unused coaching
   packages and the two AccessGroups. Steve's call entirely; nothing was deleted.
3. **Upgrade the Kajabi plan.** Cleanest long term, costs money, and is a decision that should
   not be forced by a six-day launch.

**DECIDED 2026-09-22 (Steve): option 1.** Cohort 01 ships with no product attached. Every
deliverable is external to Kajabi anyway. Revisit the product limit after the launch.

### What "no product" means for the private group

Kajabi gates its Community with an **access group**, and access groups consume product slots.
So with no product attached, a buyer does not automatically get Kajabi Community access.

The site already has a community (`Go Happy Belly Community`, id 561052) with two access
groups, both dormant since 2024 and both holding zero posts:

| Access group | Kajabi ID | Channel | State |
|---|---|---|---|
| Members | 808267 | Q&A (feed) | 0 posts, stale since Aug 2024 |
| Happier Belly Gut Reset Program | 907663 | Q&A (feed) | 0 posts, stale since Nov 2024 |

**These two are not spare product slots. Do not delete them.** They are what gates the
community; removing either would break it. If a slot ever needs freeing, look at the unused
6-month and 12-month coaching packages instead.

Two ways to run the private group for cohort 01:

**A. Reuse the dormant `Happier Belly Gut Reset Program` access group.** Attach it to the offer,
rename it and its channel for this cohort. Costs no product slot, grants access automatically
on purchase, revokes automatically on refund, and keeps buyers inside Kajabi where replays can
live. Confirm nothing else depends on that access group first.

**B. Run the group off-platform** (WhatsApp, Facebook, Circle) and link it from the
post-purchase message and emails. Manual add and remove, no auto-revoke.

Worth weighing honestly: this is a three-day intensive where people need reassurance at hour
six, and push notifications on a phone beat a web feed nobody has notifications turned on for.
A Kajabi `chat`-type channel narrows that gap; a dormant `feed` channel does not. B is likely
better for engagement, A is better for automation and for keeping everything in one place.

### Checkout page: BUILT

Theme `2167629368`. It shipped as Kajabi's untouched boilerplate: an empty image block and a
text block still reading `[Offer title]`, `[ Insert value 1 ]`, `[ Insert value 2 ]`. Three
things were wrong and all three are fixed:

1. **Placeholder copy.** Replaced with the offer name, the cohort dates, the five inclusions,
   the refund line in a sage callout, the screening disclaimer, and Alina's credential.
2. **Broken layout.** Both content blocks were `width: 8` while the payment form takes
   `checkout_block_column_width: 5`. Eight plus five exceeds the twelve-column grid, so the
   content wrapped below the form. Both are now `width: 7`.
3. **Wrong brand.** The theme carried the generic site Style Guide (Raleway / Roboto, `#2d3331`
   dark grey, outline buttons at 50px radius), so the checkout looked nothing like the page the
   buyer just came from. Now matches the landing page: Playfair Display headings, DM Sans body,
   forest `#162E28`, sage `#7AAE86`, terracotta `#C07A5A` buttons at 2px radius, page
   background `#F8FAF8`. The checkout block itself also picked up the terracotta button and a
   light sage border.

The site logo now sits above the copy at 120px. Header and footer stay hidden on this page,
which is correct for checkout: no nav, no escape routes.

`sync_checkout_block_to_offer` is true, so the form pulls the title and $47 price from the offer
record rather than duplicating them in the copy.

**Not visually verified.** The sandbox cannot reach the Kajabi domain and the offer is still a
draft. Preview it from the admin before publishing.

### Post-purchase message: BUILT

The offer uses `thank_you_preference: custom_message`. It renders immediately on purchase and
carries the kickoff call date and time, the group link, the guide link, the full three-day
schedule, the screening disclaimer, and the refund line. This is the reliable delivery path;
the welcome email is the backup.

Three placeholders in it need real URLs before publishing: `[ADD ZOOM LINK]`,
`[ADD GROUP LINK]`, `[ADD GUIDE LINK]`.

---

## 4. Email (Kajabi): BUILT

Decision, 2026-09-22: purchaser email runs in **Kajabi**, not Mailchimp. Mailchimp still owns
the five archetype quiz sequences. See the conflict note at the end of this section.

### 4.1 Tags and segment (built)

| Object | Name | ID |
|---|---|---|
| Tag | `bbf-purchased` | 2150360706 |
| Tag | `bbf-cohort-01` | 2150360707 |
| Segment | BBF Cohort 01 (active participants) | 2148726573 |

The segment is `has_tag_id: bbf-cohort-01` AND `subscribed: true`. Each new cohort gets its own
tag (`bbf-cohort-02`, etc.) and its own segment, so broadcasts never reach a past cohort.

### 4.2 The timing split (important)

Kajabi sequences drip on **day offsets from subscription**. This offer's check-ins are tied to
**fixed cohort dates**. Someone who buys ten days before kickoff would get "the hardest day is
today" ten days before the fast starts. So only the welcome email is a sequence. Everything
else is a date-scheduled broadcast.

| # | Email | Timing | Mechanism | ID | Theme ID |
|---|---|---|---|---|---|
| 01 | Pre-call welcome | On purchase | Sequence, day 0 | 2151436189 | 2167627810 |
| 02 | Day 1 check-in | Fixed date | Broadcast | 2158576121 | 2167627811 |
| 03 | Day 2 check-in | Fixed date | Broadcast | 2158576122 | 2167627812 |
| 04 | Day 3 check-in | Fixed date | Broadcast | 2158576123 | 2167627813 |
| 05 | Day 5 follow-up | Fixed date | Broadcast | 2158576124 | 2167627814 |

**Sequence:** Bone Broth Fast, Purchaser Onboarding (`2148892278`).
All five are DRAFTS. Sending and publishing are done in the Kajabi admin.

Per cohort, duplicate the four broadcasts, repoint them at the new cohort segment, and set four
send dates. The sequence email is evergreen and never needs touching.

### 4.3 The automation (NOT built, build by hand)

Kajabi's automations MCP tools are not enabled on this account yet, so this one step cannot be
created programmatically. Build it in the Kajabi admin:

```
Trigger:  Offer purchased  ->  The 3-Day Bone Broth Reset (2151405804)
Action:   Add tag  ->  bbf-purchased
Action:   Add tag  ->  bbf-cohort-01
Action:   Subscribe to email sequence  ->  Bone Broth Fast, Purchaser Onboarding
```

Simpler than the original tag-triggered design. With native Kajabi checkout, `offer_purchased`
is a first-class event that definitely fires, so the tags become actions rather than the
trigger. They still do the cohort segmentation the broadcasts target.

Leave it as a draft until the offer is published, then publish. Publishing is what arms it.

### 4.4 Email styling

All five use Kajabi's Encore Email theme with tokens set to the locked brand design: beige
`#FAF6F0` outer background, white `#FFFFFF` content card, Georgia at 17px, line height 1.7,
navy `#1B2D4F` headings, body `#374151`, sage `#7BA987` accent rule and quote borders,
terracotta `#C67B5C` buttons at 2px radius, grey `#6B7280` P.S. and footer.

Personalization uses flat Liquid handles: `{{ first_name | default: 'there' }}`. Dotted paths
like `{{ contact.first_name }}` resolve to empty in Kajabi and must not be used. Single quotes
inside the filter, not double, or the Liquid validator rejects the save.

The logo currently hotlinks the Mailchimp CDN URL. Worth re-uploading to Kajabi's media library
at some point so the emails do not depend on the Mailchimp account staying open.

### 4.5 Placeholders to fill before sending

Every one of these appears in square brackets in the email bodies:

- `[KICKOFF DATE]`, `[KICKOFF TIME]` (email 01)
- `[GROUP LINK]` (emails 01, 02, 03)
- `[GUIDE LINK]` (email 01)
- `[CLOSING CALL DATE]`, `[CLOSING CALL TIME]` (emails 03, 04)
- `[CLOSING CALL ZOOM LINK]` (email 04)

### 4.6 Conflict with the Mailchimp archetype sequences

The five archetype sequences in Mailchimp exit on the `booked-call` tag. They do **not** exit on
purchasing this reset. A contact mid-way through, say, the Reactive Gut sequence who buys the
reset will receive archetype nurture emails and daily fast check-ins on the same days, from two
different systems.

Fix before launch, one of:

1. Add a purchase-based exit condition to each Mailchimp journey (needs the purchase to reach
   Mailchimp, so a SamCart to Mailchimp Zap applying a `bbf-purchased` tag there too), or
2. Pause archetype sends for anyone in the cohort segment for those four days manually.

Option 1 is the durable fix. This is tracked in the build checklist.

## 5. Funnel integration

The reset is a natural second offer for quiz takers whose pattern involves inflammation,
overgrowth, or bacterial location. Suggested archetype targeting for launch emails and ads:

| Archetype | Fit | Angle |
|---|---|---|
| The Reactive Gut | Strong | Giving the barrier a rest from the foods that keep provoking it |
| The Sugar-Driven Gut | Strong | Three days without feeding what's driving the cravings |
| The Bloated and Backed-Up Gut | Strong | A reset for a system that keeps refilling |
| The Underactive Gut | Moderate | Broth is easy to break down when the stove isn't hot enough |
| The Wired-and-Tired Gut | Screen carefully | Fasting can add stress to an already dysregulated system. Consider steering these to the course instead |

Primary avatars: Avatar 2 (Burned-Out Professional), Avatar 4 (Frustrated Dieter),
Avatar 5 (Health-Conscious Optimizer). Avatar 1 and Avatar 6 may be better served going
straight to a Breakthrough Call.

---

## 6. Compliance notes

Reviewed against the guardrails in CLAUDE.md. Changes applied to the page copy:

- Source said "normal detox symptoms." Page says "normal adjustment symptoms." "Detox" implies a
  physiological claim that is hard to support and easy to challenge.
- Source said "reduced inflammation" as a benefit. Page frames this as giving the gut lining a
  rest, not as an anti-inflammatory claim.
- No diagnosis language anywhere. Pattern framing only.
- No "cure" or "treat."
- Screening disclaimer appears twice on the page: once in its own section and once directly
  above the final CTA, per the source kit.
- No em dashes in any copy.

**Open item for Steve:** a fasting protocol carries more liability than content or coaching. Worth
a one-time look from whoever handles your business insurance or terms, particularly the refund
policy for someone who is screened out after purchase. Suggest an explicit line: full refund if
you buy and then realize you fall into a screening category.

---

## 7. Build checklist

- [ ] Decide final offer name (naming conflict above)
- [x] Set kickoff date (Sept 29) and seat cap (50)
- [x] Set kickoff call time (10:00 AM PT) and closing call (Sat Oct 3, 10:00 AM PT)
- [ ] Fix the day-0 send time so the welcome email cannot land after the kickoff call
- [ ] Publish the BBF 01 sequence email (currently draft)
- [ ] Add the Zoom, group and guide links to the post-purchase message
- [ ] Record or write the written guide (broth ratios, hydration plan, symptom guide)
- [x] Decided: ship cohort 01 with no product attached (Steve, 2026-09-22)
- [ ] Decide how the private group runs: reuse the dormant access group, or go off-platform
- [ ] Revisit the Kajabi product limit after cohort 01
- [x] Create Kajabi Offer at $47 one-time (draft, checkout URL live on all 5 CTAs)
- [x] Build the post-purchase thank-you message
- [x] Build the checkout page (was Kajabi placeholder boilerplate)
- [ ] Preview the checkout page before publishing the offer
- [ ] Publish the offer in the Kajabi admin
- [x] Build Kajabi landing page from `landing-page.html` (draft, /broth-reset)
- [x] ~~SamCart product~~ superseded by native Kajabi checkout, 2026-09-22
- [x] Build the 5 purchaser emails in Kajabi (1 sequence email + 4 broadcasts)
- [x] Create Kajabi tags and cohort segment
- [ ] Build the tag-triggered automation by hand in Kajabi admin (MCP automations not enabled)
- [ ] Fill the remaining group, guide and Zoom link placeholders in the emails
- [ ] Schedule the 4 broadcasts to real cohort dates
- [ ] Fix the Mailchimp archetype overlap (see section 4.6)
- [ ] Re-upload the logo to Kajabi media so emails stop hotlinking the Mailchimp CDN
- [ ] Create the group and get its link into the post-purchase message and emails
- [x] Swap real testimonials into the page (Tiffani, Hanna, Linda, sourced from the live site)
- [ ] Collect reset-specific testimonials after cohort 1 and replace the 1:1 quotes
- [ ] Record launch reels 1 through 6
- [ ] Test end to end with a $1 test product before opening doors
