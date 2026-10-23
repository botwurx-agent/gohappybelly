# Replacing the Guthub CTA on the quiz results pages

Written 2026-10-23. For Steve to paste into ScoreApp by hand.

**The agent cannot do this one.** The results pages live on ScoreApp
(`https://gut-pattern-quiz.scoreapp.com`), which has no MCP connection here. The
agent did not build them either: its founding documents, dated 2026-05-20, list
"5 results pages (one per archetype)" under **Live** as of the day it was set up.

---

## The block is shared, not per archetype

**Corrected 2026-10-23 by Steve.** This section renders identically on all five
results pages. It is one block, not five, so the body cannot reference the
reader's specific pattern and there is no way to tag the link per archetype.

An earlier version of this file was wrong about that and gave five separate
bodies. Deleted. One body, below.

The constraint is less limiting than it looks: every reader arrives having just
been given a pattern, whichever one it was. The copy leans on that.

---

## What is being replaced

Confirmed by screenshot. Below the Gut Breakthrough Call CTA:

> *(Guthub logo)*
>
> ### Not ready to talk yet?
>
> Start tracking your patterns with **GuthubAi**, the AI gut-health platform my
> husband and I built together. It logs your meals, symptoms, and reactions so
> you can start seeing what's actually triggering you. Try it free for 7 days.
>
> **[ Start My Guthub Free Trial ]**

Steve pulled Guthub from the funnel on 2026-10-21, so this contradicts a
standing decision. Replaced with the $27 mini course.

**Delete the Guthub logo as well as the text.** Changing only the copy leaves a
Guthub logo sitting above a Gut Foundations CTA.

**Keep the heading "Not ready to talk yet?".** It marks this as the fallback for
someone who will not book a call, which keeps the call primary and the $1,497
path intact. A $27 self-serve course suits that slot better than a subscription
trial did, being a complete thing someone can buy and finish alone.

Removing Guthub here does not contradict CLAUDE.md, which permits mentioning it
"anywhere it is a true statement", such as the footer and the 3-Month Gut Reset
inclusions. The ban is on **funnel placement**, which this was.

---

## What to paste

Logo: delete the image block.

Heading, unchanged:

```
Not ready to talk yet?
```

Body, recommended:

```
Your result names your pattern. Gut Foundations is where I explain it: eleven short lessons on how digestion actually works, what all five patterns look like, and why yours behaves the way it does. About ten minutes each, and yours to keep for $27.
```

Button label:

```
Get Gut Foundations, $27
```

Button link:

```
https://www.gohappybelly.com/gut-foundations
```

### Shorter, if the box is tight

The original Guthub body ran about 37 words. The recommended body is 45. If it
pushes the layout, this one is 29:

```
Your result names your pattern. Gut Foundations is where I explain it: eleven short lessons on how digestion works and why yours behaves the way it does. About ten minutes each, yours to keep for $27.
```

It gives up "what all five patterns look like", which is the line that separates
the course from the free quiz. Prefer the longer one if it fits.

---

## Voice

First person. The live block reads "the platform my husband and I built
together", so these pages speak as Alina rather than about her, the same as Link
in Bio and unlike most of the site.

Optional: the old copy bolded **GuthubAi**. Bolding **Gut Foundations** on its
first appearance keeps that rhythm.

---

## What this does not cover

The 35 archetype welcome emails still drive to the call and are untouched.
`Documents/Funnel Assets/mini-course/OFFER-SPEC.md` says to leave them until the
$27 has proven itself: "Launch, measure, then rewire." That still holds. It did
not hold for this block, which had to change anyway because it pointed at an
offer no longer in the funnel.

---

## Compliance

Does not diagnose the reader. "Your result names your pattern" is pattern
language. No claim to heal, seal, cure or treat. Checked for em dashes and the
banned word list: clean. Price stated as $27.
