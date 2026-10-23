# The 7-Day workbook file: audit

Asset `4737430`, "Copy of 7-Day Healthy Lifestyle Challenge Workbook". 22 pages,
17.5 MB, 60 image objects. Produced in **Canva**, authored 2024-10-08, author
metadata "Alina Nazari". Read 2026-10-23 from its signed URL.

## The signing question is settled

The URL `get_media` returns carries `X-Amz-Expires=604800`, exactly 7 days from
2026-10-23, so it dies on **2026-10-30**. Tested three unsigned paths, all 403:

| Path | Result |
|---|---|
| `kajabi-storefronts-production.s3.amazonaws.com/<key>` | 403 |
| `kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/<key>` (the pattern that works for images) | 403 |
| `kajabi-storefronts-production.kajabi-cdn.com/<key>` | 403 |

The media library cannot serve this file from a button. The file has to live
somewhere with a permanent public URL, or behind a Kajabi Download product.

## What is actually in it

| Day | Topic |
|---|---|
| 1 | Portion Control |
| 2 | Increasing Vegetable Intake |
| 3 | Meal Planning |
| 4 | Smart Snacking |
| 5 | Hydration |
| 6 | Mindful Eating |
| 7 | Active Living |

Each day runs: teaching pages, a "Today's Task", and a "Reflection Space".

## It is not what the card promises

The `/links` card says:

> One small change a day for a week, built around **sleep, stress and meal
> timing** rather than cutting foods out.

There is **no sleep day and no stress day**. Mindful eating touches the edge of
stress and meal planning touches the edge of timing, but the promise is
substantially wrong. The opt-in page copy written on 2026-10-23 repeats the same
claim, because it was written from the card. Both need rewriting.

## It argues against the course

This is the bigger problem. Four of the five locked archetype aha lines say the
food is not the problem:

> "The food is fine. The system processing it isn't."
> "The foods aren't the problem. The barrier is."
> "The problem isn't what you're eating. It's that your stomach isn't breaking it down."
> "The bacteria aren't the problem. The location is."

The workbook's Day 1 is portion control, and Day 4 warns that "even healthy
foods can lead to weight gain if you eat too much of them". The free document
that introduces a stranger to the practice argues the opposite of what the
practice argues.

It is also **weight-management framed throughout**: "manage your weight more
effectively", "key to maintaining a healthy weight", "whether you are looking to
manage your weight". For Avatar 4, the Frustrated Dieter, who "can't lose weight
despite eating right" and "suspects something deeper is broken", eat-less-and
count-portions is precisely the advice that has already failed her.

## Hard style rule breaches

CLAUDE.md bans these outright. All are in the introduction or body text:

| Word | Count | Where |
|---|---|---|
| transform | 2 | "transformative journey", "start transforming your lifestyle" |
| journey | 2 | "transformative journey", "this 7-day journey together" |
| empower | 1 | "this challenge is designed to empower you" |
| creative | 1 | "You can get creative with adding more vegetables" |

No em dashes, which is the one rule it does keep.

## Other defects

**British spellings in a US practice:** fibre (x2), colour, flavour, yoghurt.

**A copy-paste bug on Day 1.** The Day 1 Reflection Space reads "Did you manage
to reach your hydration goal?" Day 1 is portion control. Hydration is Day 5.

**The filename.** It downloads as
`Copy_of_7-Day_Healthy_Lifestyle_Challenge_Workbook.pdf`. "Copy of" in a
customer-facing filename reads as a draft someone forgot to rename.

**17.5 MB across 22 pages.** Heavy on mobile data, which is nearly all of this
traffic, since the page is reached from Instagram. Sixty image objects, several
of them large JPEGs. It should compress to a few MB with no visible loss.

**The voice is not Alina's.** It is competent generic wellness copy, the kind a
Canva template ships with. It does not use pattern language, it does not sound
like the course, and it does not sound like her on camera.

## Recommendation

Do not publish the opt-in flow against this file as it stands.

The mechanical faults (four banned words, four British spellings, the Day 1
hydration line, the filename, the file size) are an hour in Canva.

The editorial problem is not. A portion-control and calorie-awareness workbook
is a reasonable thing in general and the wrong thing for this practice,
because it teaches the frame the course spends eight modules undoing. The first
free thing a stranger gets should rehearse the argument she will later be asked
to buy, not contradict it.

Options put to Steve 2026-10-23.
