# Post-purchase pages across the offer suite

Audited 2026-10-23. Kajabi gives each offer a `post_purchase.preference` with
three settings: **disabled** (Kajabi's generic confirmation screen),
**custom_message** (rich text on Kajabi's chrome), or **landing_page**
(redirect to a real page on this site).

| Offer | Price | Status | Post-purchase | Product attached |
|---|---|---|---|---|
| 3 Month Private 1 on 1 Coaching | $1,497 | published | landing page, rebuilt on the design system | yes |
| Happier Belly Gut Reset Program | $147 | published | landing page, rebuilt on the design system | yes |
| **The 3-Day Bone Broth Reset** | **$47** | **published** | custom message, **broken** | **none** |
| Gut Foundations | $27 | draft | **disabled** | yes, the course |
| GI MAP Stool Test | $497 | **published** | **disabled** | none |
| The other seven lab tests | $250 to $639 | published | not individually checked, GI-MAP's state is the likely pattern | none |
| Happy Belly Essentials Club | $9.97/mo | published | not checked | none |

## The urgent one: Bone Broth, $47, live and sellable

`2151405804` is published, takes $47, and its thank-you message contains:

- **Three unreplaced placeholders**: `[ADD ZOOM LINK]`, `[ADD GROUP LINK]`,
  `[ADD GUIDE LINK]`
- **Dates from a cohort that has already run**: kickoff "Tuesday, September 29",
  the three days "Wednesday, September 30 through Friday, October 2", closing
  "Saturday, October 3". Today is 23 October
- **No product attached**, so the purchase grants nothing

Anyone who buys it today pays $47, is told to join a call that happened three
weeks ago via a link that says `[ADD ZOOM LINK]`, and receives no product.
CLAUDE.md records this offer as "parked for now", but parked and published are
not the same thing. **Either unpublish it or fix it.** Unpublishing is one call
and reversible.

## The $27 mini course

`2151464245`, draft, `preference: disabled`. No thank-you page at all, so a
buyer would land on Kajabi's generic confirmation. It does have its course
attached (`2149609329`), so access works; only the welcome is missing. Being a
draft, nothing is at risk yet, but it needs a page before it is published.

## The lab tests are the bigger miss

The GI-MAP is $497, published, and `disabled`. Someone pays nearly five hundred
dollars and gets Kajabi's default screen.

Worse, these buyers have **exactly the same next step as the $1,497 client**:
they have to set up a profile on the lab-ordering site before Alina can order
the kit. Without that, the test they paid for never ships. Right now nothing on
the confirmation screen tells them so.

That is also why this is blocked on the same input: the lab-ordering URL Alina
still has not supplied.

**One page serves all eight tests.** The next step is identical whichever kit
was bought, so a single "your test is on its way" page can be the post-purchase
destination for every one of them, with the kit name the only variable, and that
can be left generic.

## The approach, proposed

Use **landing_page** for every paid offer, not custom_message. It is what the
$147 and $1,497 already do, it keeps every page on the website design system
rather than Kajabi's chrome, and it is editable in one place.

Each page answers the same three questions in the same order:

1. **What you just got**, in one line
2. **What to do first**, as the only instruction on the page
3. **The private Facebook group**, per Alina's decision that it goes to anybody
   who buys anything

Plus the support address, and the locked sign-off.

| Page | First step |
|---|---|
| $27 Gut Foundations | Open the course, start at the beginning |
| $47 Bone Broth | Save the kickoff call, join the group, download the guide |
| Lab tests, shared | Set up your lab profile, because the kit cannot ship until you do |
| Essentials Club | Not yet looked at |

## Suggested order

1. **Bone Broth.** It is live and broken. Unpublish or fix, today.
2. **Lab tests.** Live, high value, and the buyer is currently given no idea
   that the ball is in her court. Blocked on the lab URL, but the page can be
   built around it the same way the coaching page was.
3. **$27 Gut Foundations.** Draft, so no exposure. Needs a page before launch.
4. **Essentials Club.** Check what it does now before deciding.
