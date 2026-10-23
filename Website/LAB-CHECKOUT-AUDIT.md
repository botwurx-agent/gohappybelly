# Lab test checkout audit, 2026-10-23

All eight published lab test checkouts, read in full. **The expectation going in
was wrong.** The $1,497, $147 and $27 checkouts were each broken in obvious ways,
so these were assumed broken too. They are not. They are substantially the best
written checkouts on the site.

Each carries a real test description, the marker categories, links to sample
reports, kit ordering instructions, the state restrictions, and a disclaimer.
Nothing here needed rewriting. What it needed was a proofread.

---

## The eight

| Test | Price | Offer | Checkout theme |
|---|---|---|---|
| Food Sensitivity | $639 | 2149722672 | 2167629157 |
| GI-MAP Stool | $497 | 2149722769 | 2167629155 |
| Organic Acids (OAT) | $497 | 2149722771 | 2167629166 |
| SIBO Breath | $425 | 2149722775 | 2167629165 |
| DUTCH Hormone | $497 | 2149722777 | 2167629162 |
| H. Pylori | $250 | 2149722778 | 2167629161 |
| Blood Chemistry | $450 | 2149722784 | 2167629163 |
| Heavy Metal | $250 | 2149746783 | 2167629164 |

**Every price in the copy matches its offer.** That was the thing most likely to
be quietly costing money, and it is clean across all eight.

---

## Fixed

**Heavy Metal said "Clinician Pricing: $250.00".** Every other one says "Client
Pricing". Practitioner wholesale language on a consumer checkout, where a buyer
could reasonably read it as a price that is not theirs. Corrected to Client.

**Heavy Metal was missing its FDA disclaimer.** The offer description carries
"This test was developed and its performance characteristics were determined by
LabCorp. It has not been cleared or approved by the Food and Drug
Administration." The checkout, the page where money actually changes hands, did
not. Added above the existing not-doctors disclaimer.

**SIBO and H. Pylori pointed at `gohappybelly@gmail.com`** for support. The other
six, and the Gut Foundations course itself, all use `support@gohappybelly.com`.
Changed to match. **If the gmail address is the monitored one, revert these two**,
but seven surfaces against two says it is stale.

**All eight checkout buttons** were on `#76a685`, an old sage, except H. Pylori
which had no colour set at all and fell back to Kajabi's dark grey. All now
terracotta `#C07A5A` at radius 2, per the standing design system rule.

---

## Left alone, and why

**Blood Chemistry has an empty checkout body.** Title, price, title again, two
empty paragraphs, then boilerplate. No description, no markers, and no "FREE 30
minute test reading consultation" line that the other seven carry.

The content exists, in the offer description, but wrapped in raw Elementor div
soup pasted from another site. Cleaning that up is straightforward. What is not
straightforward is the consultation line: that is a **fulfilment promise**, and
whether this $450 test includes the free reading is Steve's to confirm, not the
agent's to infer from the other seven. Left untouched pending that answer.

**Vendor compliance language.** Two descriptions carry claims that sit awkwardly
against the compliance guardrails:

- Food Sensitivity: food additives "can cause chronic inflammation and increased
  intestinal permeability (leaky gut)", and "If you are diagnosed with or suspect
  intestinal permeability, autoimmune disorders, or chronic inflammation you may
  benefit from this panel."
- OAT: the panel "can accurately identify conditions associated with genetic
  disorders, nutrient deficiencies, intestinal dysbiosis, and toxicity."

Both are the laboratory's own copy, written for practitioners. Both are followed
by the not-doctors disclaimer. Neither tells the reader they have anything, so
neither breaks the diagnosing-the-reader rule outright, but "can cause" and
"accurately identify conditions" are stronger than the pattern framing used
everywhere else on the site.

This is Alina's call, not the agent's. Rewriting a laboratory's description of
its own test risks misstating what the test does, which is worse than the
original problem.

---

## True of all eight, and worth a decision

**`sync_checkout_block_to_offer` is false on every one.** The price in the body
copy is typed by hand and does not follow the offer. They all match today. The
day one changes in Kajabi, the page keeps the old number and nothing warns
anyone. This is exactly what went wrong on the $147 checkout, which sat at $197.

Turning sync on changes how the price renders, so it is a deliberate change
rather than a silent fix. Recommended, but Steve's call.

**No product is attached to any of them** (`products: []`), so a purchase grants
nothing in Kajabi. For physical kits fulfilled by the lab that is probably
correct, and the copy says info arrives by email. Worth confirming the email
actually goes out.

**No thank-you page on any of them** (`post_purchase.preference: "disabled"`).
A buyer who has just spent $250 to $639 lands on Kajabi's default confirmation.
Still blocked on Alina's lab-ordering URL.

**Every image block is empty.**

---

## Not in the offer suite

`CLAUDE.md` lists five lab tests. Eight are published. The three undocumented
ones are **DUTCH Complete Hormone Panel ($497)**, **Blood Chemistry Panel
($450)** and **Heavy Metal Panel ($250)**.

Several other published offers are also absent from the brief: Happy Belly
Essentials Club ($9.97/month, a live subscription), Bi-Weekly Private Group
Coaching Calls ($29.97), E-Book Making Your Way To A Happier Belly ($9.97),
The Gut Fix ($10), and a free Members offer.
