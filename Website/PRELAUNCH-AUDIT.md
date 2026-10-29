# Pre-launch audit: the customer flow for the paid offers

Run 2026-10-29, before promoting Gut Foundations ($27) and the Gut Reset
Course ($147). Scope is what a buyer experiences: checkout, access, login,
the member dashboard, and the emails.

Everything below was checked against live pages and live Kajabi records. Where
something could not be checked from here, it says so rather than assuming.

---

## Blockers. Fix before traffic.

### B1. Nothing on the site links to the login page

`/login` **exists and works.** It returns 200 with a proper Kajabi form, and
`/library` correctly bounces an anonymous visitor to it.

The problem is that **no page links to it.** Searched the homepage and
`/gut-foundations` for any login, sign-in, account or library link: zero
matches in nav, body or footer. A buyer who closes the tab has no route back
into what she paid for except guessing a URL or digging out a receipt.

Fix: a "Log In" link in the site header and footer. Site theme `2156348838`.

### B2. No automation or email sequence fires on a purchase

The whole site has **three** automations and **two** sequences:

| Automation | Trigger |
|---|---|
| Gut Secrets Webinar registration | Webinar form |
| Pre Webinar Email Sequence | Webinar form |
| 7-Day Workbook: deliver and tag | Workbook opt-in form |

| Sequence | Emails | Subscribers |
|---|---|---|
| Pre Webinar Email Sequence | 1 | 0 |
| Bone Broth Fast, Purchaser Onboarding | 1 | 0 |

**Nothing is triggered by buying Gut Foundations or the Gut Reset Course.** A
buyer receives only Kajabi's built-in transactional email, which no one has
reviewed, and then nothing ever again.

This matters more than it looks, because **both thank-you pages end with
"Check your inbox too. Your login details are on their way."** That promise
rests entirely on a default email nobody has read.

Two separate jobs: confirm the built-in purchase email actually carries login
details and looks like the brand (admin only, see U2), and build a real
onboarding sequence for each course.

### B3. The Gut Reset Course dashboard heading is close to invisible

The member dashboard welcome heading is `#b1becd`, a pale blue-grey left over
from a template. Measured against white:

| | Contrast | AA needs |
|---|---|---|
| Gut Reset dashboard H1, `#b1becd` | **1.89** | 3.0 for large text |
| Gut Foundations dashboard H1, `#162E28` | 14.43 | passes |

**Four paying members are looking at this now.** Theme `2156349489`, section
`product_body`, block `1604456922359`.

**FIXED 2026-10-29.** Changed to `#162E28`, matching the Gut Foundations
dashboard, taking it from 1.89 to 14.43. Read back from the theme to confirm
it landed. Not visually confirmed, because the member dashboard is behind a
login the agent does not have, so Steve should glance at it.

### B4. Two template video blocks on the Gut Reset dashboard

Both carry thumbnails from a different theme's template assets:
`themes/3789345/settings_images/..._TEMPLATE_1856x1044_Video_Thumbnails.png`.
Videos `2156997127` (body) and `2156997118` (sidebar).

Whether these are real Alina videos with template thumbnails, or template
placeholders entirely, cannot be determined from the theme data. **Steve has
to open the dashboard and look.** If they are placeholders they have been
visible to paying members.

---

## High priority, not strictly blocking

- **H1. Homepage title and meta description.** Copy written and waiting to be
  pasted: `Website/HOMEPAGE-METADATA.md`. The current ones break Steve's own
  banned-word list and carry a results claim.
- **H2. The $147 links to its checkout, not its sales page.** From the homepage
  and the nav, `Gut Reset Course` goes to `/offers/jmFpFL5m/checkout`. An
  undecided visitor gets a payment form instead of the sales page that exists
  at `/gut-reset-course`.
- **H3. Five lab-test checkouts sit in the homepage decision path**, $250 to
  $639, with no explanation step in front of them.
- **H4. The Gut Foundations thank-you page has no "Member login" link.** The
  Gut Reset one does. Both have "Go to my course" pointing at `/library`, so
  this is a consistency gap rather than a dead end.

---

## Cannot be checked from here. Steve has to.

- **U1. Does the $10 bump actually deliver?** The bump **is** live and visible
  on the $27 checkout at $10, confirmed on the live page. Whether buying it
  grants download `2149603425` is untested. Buy once with a 100% coupon.
- **U2. The built-in Kajabi purchase email.** Not exposed by MCP at all. Needs
  a read in Settings for content, branding, and whether it really contains
  login details, since two thank-you pages promise exactly that.
- **U3. The Purchase Flow on the $27.** Still unverified, still invisible to
  MCP. Check it is not fighting the offer's post-purchase redirect to
  thank-you page `2152353598`.
- **U4. One real end-to-end purchase**, on a phone, through to opening a
  lesson. Nothing below substitutes for this.

---

## Verified working

Worth recording so it does not get re-checked:

| Check | Result |
|---|---|
| `/login` | 200, working Kajabi form |
| `/library` when logged out | correctly redirects to login |
| Gut Foundations offer `2151464245` | $27, one time, fixed, no subscription, grants course `2149609329` |
| Gut Reset offer `2149370663` | $147, one time, fixed, no subscription, grants course `2148514926` |
| $10 bump on the $27 checkout | present and showing $10 |
| Gut Foundations thank-you | "You're in", links `/library`, support email, community |
| Gut Reset thank-you | same, plus a `/login` link |
| Gut Foundations member dashboard | fully built, on brand, correct sign-off, support address |
| Gut Reset member dashboard | built, apart from B3 and B4 |
| Both courses | published, all lessons published |

Note the two checkouts named above are now the third and fourth inspected and
found clean, against the file's earlier warning that two of two inspected
carried a price misconfiguration. The remaining lab-test checkouts are still
unaudited.

---

## Suggested order

1. ~~B3, the invisible heading.~~ **Done 2026-10-29.**
2. B1, the login link. Small, and it is the thing that makes a purchase
   feel finished.
3. U2, read the purchase email. It gates whether B2 is a gap or a crisis.
4. B4, look at the two video blocks.
5. B2, build the onboarding sequences.
6. U1 and U3 and U4, one test purchase covers all three.
7. H1 to H4.
