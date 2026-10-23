# Replacing the Guthub CTA on the five quiz results pages

Written 2026-10-23. For Steve to paste into ScoreApp by hand.

**The agent cannot do this one.** The five results pages live on ScoreApp
(`https://gut-pattern-quiz.scoreapp.com`), which has no MCP connection here.

The agent also did not build those pages. Its own founding documents, dated
2026-05-20, list "5 results pages (one per archetype)" under **Live** as of the
day the agent was set up. Nothing in git history creates or edits them.

---

## What is being replaced

Confirmed by screenshot 2026-10-23. Each results page carries a second CTA
below the Gut Breakthrough Call, reading:

> ### Not ready to talk yet?
>
> Start tracking your patterns with **GuthubAi**, the AI gut-health platform my
> husband and I built together. It logs your meals, symptoms, and reactions so
> you can start seeing what's actually triggering you. Try it free for 7 days.
>
> **[ Start My Guthub Free Trial ]**

Steve pulled Guthub from the funnel on 2026-10-21, so this block contradicts a
standing decision. It is being replaced with the $27 mini course.

**Keep the heading "Not ready to talk yet?".** It is doing real work: it marks
this as the fallback for someone who will not book a call, which keeps the call
primary and the $1,497 path intact. A $27 self-serve course is a better fit for
that slot than a subscription trial was, because it is a complete thing someone
can buy and finish alone.

Removing Guthub here does not contradict CLAUDE.md, which allows mentioning it
"anywhere it is a true statement", such as the footer and the 3-Month Gut Reset
inclusions. The ban is on **funnel placement**, which this was.

---

## Voice

These pages are written in Alina's first person: "the platform my husband and I
built together". The replacements below keep that. This differs from most of the
website, which refers to her in the third person, and matches the Link in Bio
page, which is the other surface reached from her own profile.

---

## The replacement, per archetype

Heading, button and link are the same on all five. **Only the body changes.**

- **Heading:** Not ready to talk yet?
- **Button:** Get Gut Foundations, $27
- **Link:** `https://www.gohappybelly.com/gut-foundations`

### 1. The Wired-and-Tired Gut

> Your result points at a system that never quite stands down, not at your food.
> Gut Foundations is where I explain what that means: eleven short lessons on
> how digestion actually works, what all five patterns look like, and why yours
> behaves the way it does. About ten minutes each, read on your phone, yours to
> keep.

### 2. The Reactive Gut

> Your result points at the barrier rather than the foods, which is why your safe
> list keeps getting shorter. Gut Foundations is where I explain what that
> barrier actually is, what the other four patterns look like, and how to tell
> them apart. Eleven short lessons, about ten minutes each, yours to keep.

### 3. The Sugar-Driven Gut

> Your result points at something that has worked out how to get itself fed,
> which is why the cravings do not feel like a choice. Gut Foundations is where
> I explain that mechanism, what the other four patterns look like, and why the
> afternoon crash is so predictable. Eleven short lessons, about ten minutes
> each, yours to keep.

### 4. The Underactive Gut

> Your result points at the stage before absorption, the one almost nobody talks
> about. Gut Foundations is where I explain how that stage works, what the other
> four patterns look like, and why protein feels heaviest when this is the
> pattern. Eleven short lessons, about ten minutes each, yours to keep.

### 5. The Bloated and Backed-Up Gut

> Your result points at location rather than the bacteria themselves, which is
> also why this pattern clears up and then comes back. Gut Foundations is where
> I explain what that means and what makes it recur, alongside the other four
> patterns. Eleven short lessons, about ten minutes each, yours to keep.

---

## If you would rather paste the same thing five times

One body for all five pages. Weaker, because it drops the callback to the result
they just read, but it is one paste instead of five:

> Start with Gut Foundations. It is eleven short lessons where I explain how
> digestion actually works and what each of the five patterns means, including
> yours. About ten minutes each, read on your phone, yours to keep.

---

## Optional: tag the links so the archetypes can be compared

To see which pattern converts best, give each page its own query string instead
of the bare URL:

```
https://www.gohappybelly.com/gut-foundations?utm_source=scoreapp&utm_medium=quiz-results&utm_content=wired-tired
                                                                                              ...reactive
                                                                                              ...sugar-driven
                                                                                              ...underactive
                                                                                              ...backed-up
```

Harmless if unused, and it cannot be added retroactively, so it is worth doing at
paste time.

---

## One caution from an earlier spec

`Documents/Funnel Assets/mini-course/OFFER-SPEC.md` says not to rewire the
results pages or the 35 archetype emails until the $27 has proven itself:
"Launch, measure, then rewire."

That still holds **for the emails**, which are 35 pieces of work built around
driving to the call. It no longer holds here, because this block had to change
regardless: it was pointing at an offer that is no longer in the funnel. Swapping
one dead CTA for a live one is not the speculative rewrite that spec warned
about.

---

## Compliance

None of the five diagnoses the reader. They say "your result points at", which is
pattern language, and they make no claim to heal, seal, cure or treat. Checked
for em dashes and the banned word list: clean. Price stated as $27 throughout.
