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

**FIXED 2026-10-29.**

The fix was not a theme edit. The Encore header's menu block and the footer's
link list both reference Kajabi **navigation menus** by handle (`main-menu`
and `footer`), not inline links, so the link belongs in the menus:

| Menu | Navbar id | New link |
|---|---|---|
| Main Menu | `2148458013` | "Log In", PathLink to `/login`, link id `2151222857` |
| Footer | `2148458014` | "Log In", PathLink to `/login`, link id `2151222858` |

Both set `authenticated_only: false`, which is the point: the link has to be
visible to someone who is logged **out**. Note Kajabi offers no
"unauthenticated only" toggle, so a logged-in member sees it too; clicking it
while signed in is harmless.

Appended rather than positioned, which puts "Log In" after Shop and **before**
the terracotta quiz button, so the primary CTA keeps the rightmost slot.

**Verified** on the live site: `/gut-foundations` shows three (desktop header,
mobile menu, footer). The homepage showed zero on the plain URL and two on a
cache-busted one, which is the known Kajabi page cache, not a failure. It
rolls on its own, measured under ~66 minutes yesterday.

A navbar change does not bust the page cache, which is new: the Nova landing
pages picked it up at once because their caches were cold, while the Encore
homepage kept serving its cached copy.

### The header wrapped, and the real cause was already there

Steve sent a screenshot: adding a fifth item made the nav wrap. "Log In"
broke across two lines as "Log / In", and so did "Gut Reset Course" and
"Private Coaching".

**Two fixes, because there were two problems.**

1. Renamed the link to **"Login"**, one word, so it cannot break.
2. The real cause: the header menu block `1555988491313` had
   **`stretch: true`**, which gives every item an equal share of the menu
   width instead of sizing each to its own text. Long labels then wrap no
   matter how much room the header has. Set to **`false`**.

The `stretch` setting was pre-existing, not something this session introduced.
It had been wrapping "Gut Reset Course" and "Private Coaching" already; a
fifth item only made it obvious. So the screenshot exposed a bug that had been
live for a while.

**Verified after the fix**, cache-busted at four widths:

| Width | Result |
|---|---|
| 1440 | all six items single-line |
| 1280 | all six items single-line |
| 1024 | all six items single-line |
| 430 | collapses to the hamburger, links single-line in the drawer |

**The lesson, which is the same one as the `.gh-zig` selector.** A measurement
heuristic can lie: the first check used element height to detect wrapping and
reported every item as wrapped, including ones that were fine. Counting
`Range.getClientRects()` per link gives the true line count. And the
simulation that "removed" the Login link actually removed the whole menu
container, so that test proved nothing. **Look at the picture.**

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
2. ~~B1, the login link.~~ **Done 2026-10-29.**
3. U2, read the purchase email. It gates whether B2 is a gap or a crisis.
4. B4, look at the two video blocks.
5. B2, build the onboarding sequences.
6. U1 and U3 and U4, one test purchase covers all three.
7. H1 to H4.
