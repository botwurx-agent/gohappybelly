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
| Public name | The 3-Day Gut Reset: Bone Broth Fast |
| Internal name | BBF-[COHORT-MONTH] (e.g. BBF-2026-10) |
| Price | $47 |
| Early-bird | None. Flat $47, urgency comes from the capped seat count |
| Format | Live cohort, 3 days, capped seats |
| Delivery | 2 Zoom calls, private group, 3 daily check-ins, written guide |
| Position in suite | Entry / ascension offer. Sits above Guthub ($13/mo), below Gut Reset Course ($147) |
| Ascension path | Closing call soft-pitches 1:1 coaching and GI-MAP as optional next steps |

### Naming conflict to resolve before build

The suite now contains three products using "Gut Reset":

- **3-Month Gut Reset** ($1,497) flagship
- **Gut Reset Course** ($147)
- **3-Day Gut Reset** ($47) this offer

"3-Day" and "3-Month" are one character apart in most contexts and will get confused in subject
lines, ad copy, DMs, and support questions. Refund disputes are the real risk: someone who
believes they bought the $1,497 program.

Alternatives that keep the reset framing without the collision:
- **The Broth Reset** (clearest, no numeral clash)
- **3 Days of Broth**
- **The Bone Broth Reset**

Recommendation: **The Broth Reset**. Steve's call. Page and spec currently use the original
"3-Day Gut Reset: Bone Broth Fast" name until he decides.

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
| Status | Draft. Publish from the Kajabi admin. |

Eleven sections: Hero, The Problem, The Shift, What's Included, How It Runs, Pattern Fit,
About Alina, Testimonials, FAQ, Screening and Final CTA.

Style Guide tokens were set from the `landing-page.html` reference rather than Encore's
defaults: Playfair Display headings, DM Sans body, heading `#162E28`, body `#2E4438`,
secondary `#6A8278`, primary `#7AAE86`, buttons `#C07A5A` at 2px radius, page background
`#F8FAF8`.

**Two placeholders must be replaced before publishing:**

1. Both CTA buttons point at `https://REPLACE-WITH-SAMCART-CHECKOUT-URL`. Swap for the real
   SamCart URL once the product exists.
2. The About Alina image block is empty. Upload her photo in the builder (the local file is
   `Documents/Funnel Assets/Alina_Fence.jpg`). MCP cannot upload images.

Also fill in `[DATE]`, `[TIME]`, and `[X]` seats throughout, and replace the three testimonial
placeholders or delete that section.

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
| Product Purchased | Grant Kajabi Offer `BBF-[COHORT-MONTH] Access` |
| Product Refunded | Revoke Kajabi Offer `BBF-[COHORT-MONTH] Access` |

If the native integration misbehaves, Zapier has a prebuilt SamCart "New Order" to Kajabi
"Grant Access to Offer" zap as a fallback.

### Thank-you page

Redirect to a Kajabi thank-you page that includes:
- Kickoff call date, time, and Zoom link
- Private group join link
- "Check your email for the prep guide"
- The screening disclaimer, repeated

---

## 4. Mailchimp

Email stays in Mailchimp. Add:

| Tag | Applied when |
|---|---|
| `bbf-purchased` | SamCart order (via Zapier, mirroring the existing Calendly to Mailchimp zap) |
| `bbf-[cohort]` | Cohort identifier, e.g. `bbf-2026-10` |

**Sequence (5 emails):**

1. **Pre-call** (immediately on purchase): welcome, what to expect, grocery/broth sourcing list, kickoff call time + group link, screening disclaimer repeated
2. **Day 1**: "The hardest day is today, it gets easier." Hydration reminder, one tip, group prompt
3. **Day 2**: "This is where it starts to shift." Normalize the cravings dip and energy change, encourage a group check-in, tomorrow's call time
4. **Day 3**: "You made it, here's how to finish strong." Breaking-the-fast prep, closing call reminder
5. **Day 5 follow-up**: how it went, soft next step (Gut Pattern quiz if they haven't taken it, or Breakthrough Call)

Use the locked email template: beige `#FAF6F0` wrapper, white `#FFFFFF` inner card, Georgia 17px,
logo at 180px, sage accent line, one bold navy aha line, terracotta CTA button.

**Journey exit:** exits on `booked-call` tag, matching the archetype sequences.

---

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
- [ ] Build Kajabi landing page from `landing-page.html`
- [ ] Create SamCart product at $47
- [ ] Wire SamCart to Kajabi integration rules (grant + revoke)
- [ ] Build SamCart to Mailchimp zap for `bbf-purchased` tag
- [ ] Load 5-email sequence in Mailchimp
- [ ] Set up private group (Kajabi Community or existing channel)
- [ ] Swap real testimonials into the page (placeholders are marked in the HTML)
- [ ] Record launch reels 1 through 6
- [ ] Test end to end with a $1 test product before opening doors
