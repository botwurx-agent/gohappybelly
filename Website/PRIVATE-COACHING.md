# Private Coaching — the 3-Month Gut Reset sales page

Built 2026-10-14 to the locked design system in `DESIGN-SYSTEM.md`. This
replaces the October 13 Nova page (`2152330511`), which Steve deleted because
it predated the system and did not match the home page.

| | |
|---|---|
| Landing page | `2152331486` |
| Theme | `2167882803` (Nova v0.2.7) |
| Slug | `/private-coaching` |
| Live | https://go-happy-belly.mykajabi.com/private-coaching |
| Builder | https://app.kajabi.com/admin/themes/2167882803/settings/edit |
| Status | **Published.** Published so the build could be rendered and measured; a draft landing page 404s for anonymous requests, so there is no other way to verify one. |

The header's "Private Coaching" link now points here instead of the 2024
`/one-on-one-coaching` page.

## Why Nova, not Encore

The home page is an Encore **Site** theme. Kajabi creates every new landing
page from the **`nova_blank`** preset, and there is no API to assign an
existing theme to a new page, so Nova is the engine for every inner page from
here on. The design system is therefore **replicated per theme, not
inherited** — `DESIGN-SYSTEM.md` is the source of truth and each theme is a
copy of it.

## Sections

| # | Section | Background | Job on the page |
|---|---|---|---|
| 001 | Hero | `#F8FAF8` | The promise, the price-free ask, the call |
| 002 | Why Normal Labs Miss It | `#EFF7F1` | Teaches the reference-range gap |
| 003 | The Five Patterns | `#162E28` | Connects to the core IP and the quiz |
| 012 | What The GI-MAP Shows | `#F8FAF8` | Justifies the $497 that is bundled |
| 005 | Your Three Months | `#EFF7F1` | Month-by-month, removes the unknown |
| 004 | What Is Included | `#F8FAF8` | The deliverables |
| 013 | Honest Comparison | `#EFF7F1` | Handles "why not do it myself" |
| 006 | Who It Is For | `#F8FAF8` | Qualifies in and out |
| 007 | Who You Are Working With | `#EFF7F1` | Credibility and scope of practice |
| 008 | Testimonials | `#F8FAF8` | Proof |
| 009 | Investment | `#EFF7F1` | The number and the CTA |
| 010 | FAQ | `#F8FAF8` | Residual objections |
| 011 | Final CTA | `#162E28` | Close |

### What changed after the first build, and why

The first version of this page reused the home page's section list with the
copy swapped. Steve's read was right: it was nearly a copy. The design system
is meant to be shared; the **content architecture is not**. A home page
introduces a practice. A sales page has to answer, in order, the questions
somebody asks before spending $1,497.

| Dropped | Reason |
|---|---|
| Validation band | Re-sold a problem the visitor had already read on the home page. Replaced by **Why Normal Labs Miss It**, which explains *why* their results came back fine instead of listing their symptoms back at them. |
| Early Testimonial | Two testimonial moments on one page is the home page's pattern, not a sales page's. Linda's stronger four-doctors quote was promoted into the main testimonial block instead. |
| Home page About copy | Was verbatim. Rewritten as positioning: why Alina works this way, what functional diagnostics actually is, and an explicit statement that she is not a physician. |
| One FAQ | "How is this different from a doctor" is now a whole section, so the question was redundant. |

| Added | Reason |
|---|---|
| **What The GI-MAP Shows** | The single biggest omission. A $497 test is bundled and the page never said what it looks at. Six marker groups in plain language, plus the point that the reading is a consultation and not an emailed PDF. |
| **Honest Comparison** | Answers "why not just do it myself" head-on, with the real alternatives priced: free, $497 for the test alone, $1,497 with the test inside. Frames the actual delta as $1,000 for three months of interpretation. |
| **The Five Patterns** | The offer is built on the archetype framework and the first build never mentioned it. Deliberately a compact forest band rather than the home page's five-card grid, so it reads as a different treatment of the same IP. |
| **Your Three Months** | Replaced a generic three-step "how it works" with a month-by-month arc: find it, work it, keep it. Removes the fear of an open-ended commitment. |

Compliance note: the GI-MAP section describes **markers**, never diagnoses.
"Yeast overgrowth patterns", not "you have candida". The comparison section
names a price delta but makes no outcome promise.

## Measured against the home page

| | Home | This page |
|---|---|---|
| Content band | 1044px | 1044px |
| Hero text column | 492px | 492px |
| Hero portrait | 380 x 507, 3/4 | 380 x 507, 3/4 |
| About portrait | 486 x 608, 4/5 | 486 x 608, 4/5 |
| Card row (3-up) | 335px | 335px |
| Header logo | 104 x 65 at x=198 | 104 x 65 at x=198 |
| Footer | `#112420` centred stack | `#112420` centred stack |

## Five Nova traps this build hit

Each cost a render-and-measure cycle. They are the reason inner pages should
start from this file rather than from scratch.

1. **The footer takes no `text` block.** Schema is logo, link_list, copyright,
   social_icons only — same as Encore. The tagline is drawn as a `::before`.
   The write is rejected wholesale if you try, so nothing is lost, but it
   costs a round trip.
2. **Nova puts section gutters INSIDE the width cap.** `max-w-7xl` (1280px)
   with `px-28` inside it. To land 1044px of content the cap must be set to
   **1100**, not 1044.
3. **Every block carries a default 10px desktop / 20px mobile padding.** It
   pushed every column 10px inward, so columns came out 20px narrower than
   spec. Zeroed with a rule matching only blocks still carrying the default
   values, so explicit card and panel paddings survive.
4. **`data-nova-role='image-wrapper'` does not hug its image.** It inherits
   full column width, so a portrait cannot centre and a badge anchored to it
   lands on the column corner, not the photo's. Needs
   `width: fit-content !important`.
5. **Deep-merging a nested block needs the full path.** Addressing
   `sections.X.blocks.CARD` when the card actually lives inside a group
   silently creates a new orphan block at section level and leaves the real
   one untouched. The API returns success either way. Four edits landed in the
   wrong place before this was caught by diffing the rendered page.

Trap 5 left four orphan blocks (`1791960000004_c2`, `_c5`,
`1791960000010_q2`, `_q6`) at section level. They are absent from every
`block_order`, so they do not render and do not appear in the builder sidebar.
There is no delete primitive on this API; they are harmless but worth knowing
about if the JSON is ever read directly.

## Open

- The hero headline uses "disagrees" as the terracotta italic accent, mirroring
  the home page's "findable". Worth Steve's eye as copy, not layout.
- The page is published but carries no SEO title or description yet.
- CLAUDE.md still lists the 3-Month Gut Reset sales page under "Not Yet Built".
