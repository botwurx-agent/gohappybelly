# Course revamp status

Review doc (plan + all drafts): https://claude.ai/code/artifact/ec1a7423-c6b3-4c23-80ad-a83c96b41464

## Done on the live course
- 2026-10-17: five safety fixes applied with Steve's approval. See SAFETY-FIXES-2026-10-17.md.
  Nothing else in the live course has been touched.

## Drafted, awaiting review (all in the doc, nothing in Kajabi)
| Piece | Count | Blocked on |
|---|---|---|
| The five pattern pages | 5 | Alina: every supplement dose, duration, and the red-flag sign-off |
| Weekly teaching pages | 4 | |
| "This week for your pattern" inserts | 4 pages x 5 patterns | Alina, same as above |
| Baseline score sheet / food journal | 1 | |
| Reintroduction tracker | 1 | |
| Five shopping lists, one per pattern | 5 | |
| Supplement reference | 1 | Alina: every dose and duration; cautions are drafted and need her confirmation |
| Start Here: Welcome, How this course works, When to see your doctor, What we are doing | 4 | |

## Still to draft
- FAQ rewrite. BLOCKED on Steve: the current FAQ promises "lifetime access to the membership area",
  which contradicts both the 3-Month Gut Reset (3-month access) and the $147 standalone course.
  Need the real terms before writing it.
- Closing lesson bridging to the Gut Breakthrough Call / 3-Month Gut Reset / testing.
- Per-pattern meal plans.
- Bristol chart page (the bowel lesson was made safe in the safety pass but still has no chart).
- Smoothie recipes re-tagged by pattern.

## Open decisions for Steve
1. **The seven videos.** The Week 4 transcript confirms the video advises eating dirt and frames it
   as helping heal leaky gut, which is a treatment claim and a diagnosis term both. Week 4's page
   now contradicts the video deliberately, so that one should come down whatever is decided about
   the rest. The other six name sections and topics that have moved. All Wistia IDs are recorded in
   REBUILD-2026-10-20.md, so pulling them is reversible.
2. **The five Amazon affiliate lists:** keep or drop. If kept they need an affiliate disclosure,
   which the course does not have anywhere.

## Resolved
- **Four weeks or six** (2026-10-21): four weeks plus a separate Reintroduction Fortnight module.
- **Access terms** (2026-10-20): one year with auto-renew, not lifetime. FAQ corrected.
- **Supplement doses** (2026-10-20): published live. Still awaiting Alina's confirmation.
- **The quiz** (2026-10-21): a course-only ScoreApp clone, "What's Your Gut Pattern? - Course Only",
  with **no Mailchimp connection at all**. Steve's call, and it closes the real risk: the public
  quiz applies the tags that start the seven-email archetype welcome sequences, which would have
  sold the course, or the Reset, to people who had already bought it.

## The quiz: what is left to do
The lesson (2180146833) embedded a dead Typeform from Aug 2024, not ScoreApp. Removed on
2026-10-21; members are routed to The 5 Gut Patterns meanwhile.

On the ScoreApp clone:
- No Mailchimp integration. No tags, no GUTPATTERN write, nothing connected.
- No email capture step. They are already logged into the course.
- Results CTA becomes "go back and read your pattern page" rather than the public version's
  Book a Call / Start Guthub Trial pair. One soft line about the Breakthrough Call is fine.
- The 12 questions and the scoring stay exactly as they are, so results still map to the five
  patterns the course is built on.

Then: **the clone's URL or embed code is needed** to put it back in the lesson. Guessing the
subdomain does not work. ScoreApp serves a generic marketing page with a 200 for any unknown
subdomain, so a probe cannot distinguish a wrong guess from a real quiz. The live public quiz
returns the title "What's Your Gut Pattern?"; six guessed slugs all returned the generic page.

## Style note for anyone picking this up
US spellings and US vegetable names throughout (zucchini, eggplant, arugula, beets, celiac,
anemia, fiber, color, program). A consistency pass on 2026-10-17 fixed drift into British forms
in both the drafts and two live lessons.
