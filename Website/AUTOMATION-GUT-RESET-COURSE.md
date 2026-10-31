# Automation: Gut Reset Course delivery and onboarding

Built 2026-10-31. Closes the remaining half of blocker **B2**: the $147 had
no purchase automation either.

**Both are DRAFTS.** Kajabi's `create_automation` cannot publish, so nothing
sends until Steve arms them in the admin.

| | id | status |
|---|---|---|
| Gut Reset Course: deliver and onboard | `1390134` | draft |
| Gut Reset Course: mark pattern found at the quiz | `1390135` | draft |

https://app.kajabi.com/admin/workflows/1390134/edit
https://app.kajabi.com/admin/workflows/1390135/edit

## Wiring

```
TRIGGER   Offer is purchased  →  Gut Reset Course ($147, offer 2149370663)
STEP 1    Add tag             →  gut-reset-customer (2150427430)
STEP 2    Email               →  "You're in. Start with the quiz."
STEP 3    Wait 2 days
STEP 4    Email               →  "Have you found your pattern yet?"
EXIT IF   has tag gut-reset-pattern-found (2150427431)

TRIGGER   Lesson is completed →  "The Gut Pattern Quiz" (post 2180146833)
STEP 1    Add tag             →  gut-reset-pattern-found
```

The exit condition was set **at creation** this time, in one call, now that
the three-level schema is known. The $27 needed a separate update for it.

## This is not a copy of the $27 automation, deliberately

Read the course structure first (62 published lessons, 9 modules) and it
changes the design.

**The Gut Reset Course branches.** Every one of the four weeks contains a
lesson called *This Week For Your Pattern*, there are five "Working With The
..." lessons, five shopping lists and five meal plans. All of it keys off
**The Gut Pattern Quiz** in the Find Your Pattern module.

So a buyer who starts at Week 1 without taking the quiz is reading the
general version of a course they paid for the personalised version of. That
is the single biggest failure mode for this product, and it is invisible:
they will not know they are doing it wrong.

Three consequences, all different from the $27:

1. **The welcome email leads with the quiz**, not with "open lesson 01". It
   says explicitly to do it before Week 1 and explains why.
2. **The nudge asks about the quiz**, not about opening the first lesson.
3. **The "started" marker is the quiz**, not the first lesson. Completing
   *Welcome: Start Here* means someone pressed play. Completing the quiz
   means the course can actually work for them. That is the right bar for
   suppressing the nudge.

Tag named `gut-reset-pattern-found` rather than `gut-reset-started` for the
same reason: it records something meaningful, not just activity.

## Two deliberate copy choices

**It points at "When To Stop And See Your Doctor"** (lesson `2201292321`, in
Start Here) and calls it the page that matters more than any other in the
course. That lesson already exists; the email just makes sure it is seen
before someone changes their diet. Good practice on a health product, and it
costs one sentence.

**No access term is stated.** CLAUDE.md records that the $147 grants a year,
but the email does not say so. If that is wrong or changes, it becomes a
mis-promise in writing. The sales page carries the terms.

The guarantee line matches what `/gut-reset-course` already says: "full
refund inside 30 days."

## Verified after creation

| Check | `1390134` | `1390135` |
|---|---|---|
| Trigger resolved | "Offer is purchased: Gut Reset Course" | "Post is completed: The Gut Pattern Quiz" |
| Nodes / edges | 6 / 5 | 3 / 2 |
| Email bodies | both present, verbatim | n/a |
| Wait | 2 days | n/a |
| Exit condition | set at creation, echoed back | n/a |
| `errors` | `[]` | `[]` |
| `total_enrolled` | 0 | 0 |

## Before publishing

1. Read both emails in the builder.
2. **Publish `1390135` first**, or at least before the first buyer reaches
   day two, so the tag is landing before the exit condition needs it.
3. Then publish `1390134`.

**Note the course already has 4 members.** They are unaffected: the trigger
fires on new purchases only, so nobody existing gets a welcome email.

## Coupling to watch

Both emails quote the Member Welcome Email's subject ("Set up your Go Happy
Belly password"). If that transactional template's subject changes, these two
and the two Gut Foundations emails all need the quote updated. Four places.
