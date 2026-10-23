# Gut Foundations sales page ($27)

Built 2026-10-23. Landing page `2152353662` at `/gut-foundations`, theme
`2168000232`, Nova on `Website/DESIGN-SYSTEM.md`. **Draft**, because the offer
it sells is still a draft.

The gap Steve spotted: the $27 had a checkout, a course and a thank-you page,
and no page to send traffic to. It was the one rung of the ladder with no front
door.

## What the course actually contains, checked before writing

Read off course `2149609329` rather than taken from the spec, which was stale:

| | |
|---|---|
| Published lessons | **14**: 3 orientation, 8 foundations, 3 bonus |
| Video | **None.** Every lesson is `media: none` |
| Length | About ten minutes each, self-paced |
| Reflection prompts | 12 |
| Word count | 8,467 of rewritten copy |

**The no-video finding is the one that mattered.** The $147 course has video on
six of its nine module openers, so "self-paced video lessons" is true there and
would have been false here. It is exactly the line that gets copied across from
a neighbouring page without checking.

The page says "eleven short lessons", matching the offer description: the 8
foundations plus the 3 bonus modules, not counting the three orientation
lessons.

## Structure

| Section | Background | Job |
|---|---|---|
| `...001` Hero | `#F8FAF8` | Eyebrow, `<h1>`, the promise in one line, price button |
| `...002` Who it is for | `#EFF7F1` | Avatar 1's opening: the normal labs, the shrinking food list |
| `...003` What is inside | `#F8FAF8` | The eight, then the three, as a numbered rule-separated list |
| `...004` What this is not | `#EFF7F1` | No video, not a protocol, and where to go instead |
| `...005` Final CTA | `#162E28` forest | Price, button |

Forest is used once, on the final CTA, which is what §4 of the design system
reserves it for. The commerce CTA variant `gh-cta-strong` is used on the hero
and final buttons.

## The honesty section is the argument, not a disclaimer

"What this is not" says plainly that there is no video, no four week plan, no
supplement list, and that if she already knows her pattern she wants the $147
instead. That costs some conversion.

It buys two things worth more. It stops the refund that comes from a buyer who
expected video. And it is the correct setup for the upsell: a page that admits
it is groundwork makes the one-click $147 the obvious next step rather than a
second pitch. The $27 page pointing at the $147 is not a leak, it is the ladder
working.

It also answers the deck audit's objection honestly. That audit judged the
source deck "not worth $47" partly on having no video. The page does not pretend
otherwise; it sells ten-minute reading for $27, which is a claim the content
supports.

## Still to do

1. **Publish the offer** `2151464245`, still a draft. Until then the checkout
   link `/offers/yYfiaNgo/checkout` on this page 404s.
2. **Publish this page.** Left as a draft on purpose: a live sales page whose
   buy button goes nowhere is worse than no page.
3. **Confirm the upsell is attached** as step 1 of the Purchase Flow, not merely
   created.
4. **Add it to the navigation**, or to `/links`, or wherever the traffic is meant
   to come from. Right now nothing points at it.
5. SEO title and description are unset.
