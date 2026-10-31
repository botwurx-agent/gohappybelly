# What Steve needs to do

Written 2026-10-31. Ordered: the things that block promoting the $27 come
first. Times are honest estimates.

---

## 1. Finish the exit condition — DONE 2026-10-31 00:17Z

Applied by the agent, not by hand. Nothing for Steve to do here.
Left in place as a record; the steps below are still live.

**Where:** https://app.kajabi.com/admin/workflows/1388764/edit

**Do:** add an exit condition (Kajabi may label it a disqualification) of
**has tag: `foundations-started`**.

**Why:** automation `1388767` is live and tagging people who finish lesson 01.
Nothing reads that tag yet, so the day-2 "did lesson 01 open alright?" nudge
still goes to everyone, including people who already started.

**Safe on a live automation.** Kajabi preserves in-flight enrollments, and
adding an exit condition removes no steps. `total_enrolled` is 0 right now, so
there is nobody to disturb anyway.

**Done looks like:** nothing visible. Tell the agent and it will confirm by
checking whether `updated_at` has moved off `2026-10-30T23:58:48Z`. That
timestamp is the only signal available, because `get_automation` does not
return exit conditions at all.

---

## 2. Read Kajabi's built-in purchase email (10 minutes)

**Where:** Kajabi Settings. Not visible to MCP at all, which is why this has
sat open as U2 since the pre-launch audit.

**Do:** find the transactional email Kajabi sends on purchase. Read it as a
buyer would. Three questions:

1. Does it actually contain login details or a set-password link?
2. Does it look like Go Happy Belly, or like default Kajabi?
3. Now that automation `1388764` also fires on purchase, do the two emails
   arriving together read sensibly, or do they contradict each other?

**Why it matters:** both course thank-you pages end with "Check your inbox
too. Your login details are on their way." Until tonight that promise rested
entirely on this email. It now has a second email behind it, but the agent
still cannot see either one land.

**If the built-in email already hands over a password**, tell the agent and it
will soften the Forgot Password line in the welcome email, which is currently
worded loosely on purpose.

---

## 3. One test purchase (20 minutes, highest value on this list)

**This single step clears four open unknowns at once.** Nothing else on the
list substitutes for it.

**Do:**

1. Create a 100% off coupon for the Gut Foundations offer (`2151464245`).
   *The agent has not checked whether one already exists; Kajabi coupons are
   not in its current toolset.*
2. Buy the $27 **on a phone**, through the real checkout, with the $10 Gut Fix
   bump **ticked**.
3. Follow it all the way through to opening lesson 01.

**Watch for, in order:**

| | What to check | Clears |
|---|---|---|
| a | Does the bump actually grant The Gut Fix download? | U1 |
| b | Where does it land after payment? Should be thank-you page `2152353598`, not somewhere a Purchase Flow redirected it | U3 |
| c | Which emails arrive, how many, in what order | U2 |
| d | Does the welcome email's login instruction actually work | new |
| e | Does lesson 01 open, and does `foundations-started` get tagged | new |
| f | The whole thing on a phone screen | U4 |

**Note on (e):** completing lesson 01 is what fires automation `1388767`. This
test is also the only way to confirm that automation works before a real buyer
depends on it.

**Afterwards:** refund yourself and revoke access, or the test contact sits in
the customer tag and skews everything later.

---

## 4. Look at the Gut Reset Course member dashboard (10 minutes)

Two things the agent cannot see, because the member area is behind a login it
does not have.

**Where:** log in and open the Gut Reset Course dashboard as a member.

**a. Confirm the heading fix (B3).** It was `#b1becd`, a pale blue-grey
template leftover at 1.89 contrast, effectively invisible. Changed to
`#162E28` on 2026-10-29 and read back from the theme, but never seen. Four
paying members were looking at the broken version.

**b. Decide on two video blocks (B4).** Videos `2156997127` (body) and
`2156997118` (sidebar). Both carry thumbnails from a different theme's
template assets. The agent cannot tell whether these are real Alina videos
with wrong thumbnails, or placeholders entirely. If they are placeholders,
paying members have been looking at them.

---

## 5. Paste the homepage title and description (5 minutes)

**Where: Kajabi Settings, NOT Website → Pages.**

This is the one you pasted in the wrong place last time, so: re-verified
2026-10-31. `/`, `/login` and `/store` all serve the identical title and
description, while `/blog` and the landing pages carry their own. That makes
the homepage value a **site-wide default**, which is why the field on the Home
page editor is greyed out.

Look in Settings → Site Details. The right field is the one currently
containing **"Expert Gut Nutritionist"**. The agent cannot see Kajabi settings
pages, so it cannot name the exact field label with certainty; the existing
text is the reliable way to identify it.

**Title** (59 characters):

```
Gut Nutrition Coaching & Courses for Women | Go Happy Belly
```

**Description** (156 characters):

```
Your labs came back normal but you still feel unwell. Alina Nazari, FDN-P, helps women find the pattern behind their gut symptoms. Courses and 1:1 coaching.
```

**What it replaces, and why:** the current description opens with "Transform"
and closes with "journey", both on Steve's own banned-word list, and contains
"heal leaky gut", which is the exact phrase the compliance rule names.
"Proven Courses" in the title is a results claim. Full reasoning in
`HOMEPAGE-METADATA.md`.

`og:title` and `og:description` currently mirror these, so this should fix
link previews too. Worth sharing a link afterwards to confirm.

---

## 6. The blog meta description (new, found 2026-10-31)

Not on any earlier list. `/blog` has its own description, separate from the
site-wide one, and it reads:

> Find out why gut health is so important and what your symptoms mean. You've
> tried diets before, now heal your gut and get rid of those symptoms for good.

**The problem is "get rid of those symptoms for good."** That is a results
claim close to a cure promise, and "cure" is on Steve's own banned-word list,
not the agent-written heal/seal clarification. "What your symptoms mean" is
also closer to diagnostic framing than the pattern language used everywhere
else.

Deliberately **not** making a fuss about "heal" on its own, per the provenance
work recorded in CLAUDE.md on 2026-10-29.

No replacement drafted yet. Ask the agent if you want one.

---

## Not on this list, and why

- **The $147 has no purchase automation either.** Same gap as the $27 had,
  same shape, and now a working pattern to copy. Worth doing, but it is not
  blocking the $27 launch.
- **Lab test thank-you pages.** Still blocked on Alina's lab-ordering URL.
- **The 30-day guarantee has no Kajabi setting behind it.** Honouring it is
  manual: buyer emails `support@gohappybelly.com`, Steve refunds and revokes.
  Whoever answers that inbox needs to know the policy exists and the answer is
  yes.
