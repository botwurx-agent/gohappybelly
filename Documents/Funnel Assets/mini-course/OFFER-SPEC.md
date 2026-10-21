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

## The upsell mechanic, and its one real constraint

Kajabi offers expose exactly one post-purchase behavior: `post_purchase`, set to
either a custom thank-you `body` or a redirect to a Kajabi landing page. Read off
offer `2149370663`, which already redirects to landing page `2150005720`
("Course Thank You Page").

**There is no native one-click post-purchase upsell.** So $47 → $147 is:

```
$47 checkout  →  post_purchase redirect  →  upsell landing page
                                               ↓
                                         $147 checkout (card entered again)
```

Two clicks and a second card entry, not one click. That costs conversion, and it
is the platform's limit, not a design choice. Worth knowing before anyone promises
a one-click bump.

SamCart is on the stack and unused. It does one-click upsells properly. If the
$47 proves out and the second card entry is visibly costing sales, that is the
argument for moving this one checkout to SamCart. Not before there is data.

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
