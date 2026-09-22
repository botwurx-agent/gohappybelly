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
| Format | Live cohort, 3 days, capped seats |
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

**Two placeholders must be replaced before publishing:**

1. Both CTA buttons point at `https://REPLACE-WITH-SAMCART-CHECKOUT-URL`. Swap for the real
   SamCart URL once the product exists.
2. The About Alina image block is empty. Upload her photo in the builder (the local file is
   `Documents/Funnel Assets/Alina_Fence.jpg`). MCP cannot upload images.

Also fill in `[DATE]`, `[TIME]`, and `[X]` seats throughout.

**Testimonials:** now carry the three real quotes from the live site (Tiffani, Hanna, Linda).
These are 1:1 coaching clients, not reset participants, and the section subhead says so
outright. Do not delete that line unless you are replacing these with quotes from an actual
cohort. Swap in real reset testimonials after the first round finishes, which is also reel 7
in the launch sequence.

---

## 3. SamCart build

**Product name:** 3-Day Gut Reset: Bone Broth Fast
**Price:** $47 one-time
**Early-bird:** none currently. If you later want a launch discount, add a SamCart coupon code
rather than a second product, so there is only ever one buyable URL.

### Integration rules (SamCart to Kajabi)

SamCart's App Marketplace supports Kajabi rules directly, no Zapier needed:

| Trigger | Action |
|---|---|
| Product Purchased | Grant Kajabi Offer `BBF Cohort 01 Access` |
| Product Purchased | Add Kajabi tag `bbf-purchased` |
| Product Purchased | Add Kajabi tag `bbf-cohort-01` |
| Product Refunded | Revoke Kajabi Offer `BBF Cohort 01 Access` |
| Product Refunded | Remove Kajabi tags `bbf-purchased`, `bbf-cohort-01` |

**Why the tags and not just the offer grant.** The purchase happens in SamCart. Kajabi only
ever sees an offer *grant* arriving through an integration, never a native checkout. Neither
Kajabi's nor SamCart's documentation confirms whether a granted offer fires Kajabi's
`offer_purchased` automation trigger. If it does not, the automation silently never runs and
buyers receive nothing. Triggering the automation on a tag that SamCart applies removes that
dependency entirely and is testable in a minute with a $1 test product.

If SamCart's native Kajabi app cannot apply tags, use Zapier: SamCart "New Order" to Kajabi
"Add Tag", alongside the existing "Grant Access to Offer" action.

### Thank-you page

Redirect to a Kajabi thank-you page that includes:
- Kickoff call date, time, and Zoom link
- Private group join link
- "Check your email for the prep guide"
- The screening disclaimer, repeated

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
Trigger:  Contact tag added  ->  bbf-purchased
Action:   Subscribe to email sequence  ->  Bone Broth Fast, Purchaser Onboarding
```

Leave it as a draft until the SamCart product is live, then publish. Publishing is what arms it.

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
- [ ] Set cohort dates, kickoff call time, closing call time, seat cap
- [ ] Record or write the written guide (broth ratios, hydration plan, symptom guide)
- [ ] Create Kajabi Product and populate modules
- [ ] Create Kajabi Offer as access grant, no public checkout
- [x] Build Kajabi landing page from `landing-page.html` (draft, /broth-reset)
- [ ] Create SamCart product at $47
- [ ] Wire SamCart to Kajabi integration rules (grant + revoke)
- [ ] Confirm SamCart can apply Kajabi tags natively; fall back to Zapier if not
- [x] Build the 5 purchaser emails in Kajabi (1 sequence email + 4 broadcasts)
- [x] Create Kajabi tags and cohort segment
- [ ] Build the tag-triggered automation by hand in Kajabi admin (MCP automations not enabled)
- [ ] Fill the date, time, group, guide and Zoom placeholders in all 5 emails
- [ ] Schedule the 4 broadcasts to real cohort dates
- [ ] Fix the Mailchimp archetype overlap (see section 4.6)
- [ ] Re-upload the logo to Kajabi media so emails stop hotlinking the Mailchimp CDN
- [ ] Set up private group (Kajabi Community or existing channel)
- [x] Swap real testimonials into the page (Tiffani, Hanna, Linda, sourced from the live site)
- [ ] Collect reset-specific testimonials after cohort 1 and replace the 1:1 quotes
- [ ] Record launch reels 1 through 6
- [ ] Test end to end with a $1 test product before opening doors
