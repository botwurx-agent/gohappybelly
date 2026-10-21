# $47 Mini Course — offer spec

**Status:** source material not yet received. Everything below marked PENDING
waits on the FDN deck.

## Decisions already made

| | |
|---|---|
| Price | $47, one time |
| Source | FDN done-for-you gut wellness material, Canva deck, supplied as PDF |
| Role | Front-end offer. First paid rung of the ladder |
| Ladder | $47 mini course → $147 Gut Reset Course → $1,497 3-Month Gut Reset |
| Guthub | Not in this funnel. May be mentioned, never sold. See CLAUDE.md |
| Bone Broth Reset | Second $47 offer, parked. Not this one |

PENDING: name, promise, module structure, lesson count, whether $47 survives
contact with what the deck actually teaches.

## The upsell mechanic

**Kajabi has a full post-purchase upsell funnel, with downsells.** Per Kajabi's
own docs:

- Upsell pages are built once in the Builder and attached to offers. One upsell
  page can serve several offers.
- A purchase flow holds multiple steps, one upsell per step, no documented cap.
- A **downsell** attaches beneath any step and fires when that step is declined.
  Kajabi: no functional difference between the two, a downsell is just an upsell
  shown after a decline.
- The upsell bills as a separate transaction that "will use the same payment
  method used for the Original Offer."

That last point is the one that matters: the card is already on file, so the
buyer accepts with a button, not a second checkout form. It is a one-click
upsell. Kajabi's docs never use that phrase, which is how this got recorded
wrong the first time.

```
$27 checkout  →  upsell step 1: $147 Gut Reset Course  →  accept = one click
                      ↓ decline
                 (optional downsell slot, unused for now)
                      ↓
                 post-purchase destination
```

**An earlier version of this file said the opposite.** The error came from
reading the offer object through the MCP, seeing that `post_purchase` exposes
only a thank-you body or a landing page redirect, and concluding the platform
could not do upsells. The MCP is a partial view of Kajabi, not a map of it.
Do not infer a platform limit from a tool's surface area.

### Division of labor, because the MCP cannot reach purchase flows

The commerce toolset is list/get/create/update for offers and purchases. There
are no upsell tools.

- **Agent builds** the upsell page. Upsell pages are Builder pages, so they go
  through the same theme tools and the same `Website/DESIGN-SYSTEM.md` as every
  other page.
- **Steve attaches** it in the offer's Purchase Flow tab in the Kajabi admin.

**Caveat from the docs:** editing an upsell page changes it for every offer it is
attached to. A second entry offer wanting different copy needs its own upsell
page. Name them for the offer they serve, not generically.

SamCart stays unused. The reason to move checkout there was the second card
entry, and that reason does not exist.

## What this breaks when it goes live

The quiz funnel currently ends at the Gut Breakthrough Call. Once a $47 entry
offer exists, these stop matching the funnel:

- The quiz results pages, 5 of them, whose CTAs were built for the old structure.
- The 5 archetype welcome sequences, 35 emails, which drive to the call.

Do not rewrite either until the $47 is live and converting. Launch, measure,
then rewire. Rewriting 35 emails around an offer that has not proven itself is
how you end up doing it twice.

## Compliance

FDN wrote the source material for practitioners. Practitioners may name
conditions; this audience may not be told they have one. Expect the deck to
contain diagnostic language, "heal", and probably "leaky gut", all of which are
normal in a practitioner context and banned in ours.

Every slide gets swept against the CLAUDE.md rules before any of it ships. The
sweep is not optional and it is not a formality: this is the first offer built
from copy we did not write.

## Open with Steve

1. The PDF.
2. FDN's license terms: resale allowed, attribution required, modification
   allowed. The third one decides whether the compliance rewrite is even legal.
