# Gut Foundations CTA for the five quiz results pages

Written 2026-10-23, for Steve to paste into ScoreApp.

**The agent cannot do this one.** The five results pages live on ScoreApp
(`https://gut-pattern-quiz.scoreapp.com`), which has no MCP connection here.
Everything below is ready to paste by hand.

The agent also did not build those pages. Checked 2026-10-23: the agent's own
founding documents, `docs/superpowers/plans/2026-05-20-gohappybelly-agent-setup.md`
and the matching design spec, both list "5 results pages (one per archetype)"
under **Live** as of 2026-05-20, which is the day this agent was set up. They
predate it. Nothing in git history creates or edits them, and there has never
been a ScoreApp tool connected.

---

## Check the Guthub CTA while you are in there

This matters more than the $27 placement below.

That same founding spec records the results pages as carrying a **dual CTA**:

```
Results page: 1 of 5 archetypes - dual CTA:
  [Book a Gut Breakthrough Call]  OR  [Start Guthub Trial]
```

Steve pulled Guthub from the funnel on 2026-10-21. CLAUDE.md now says, in as
many words, "do not put its trial in a quiz results CTA", and "treat any funnel
placement of Guthub as a mistake".

So unless those buttons were changed in the five months since, **all five
results pages are still sending quiz takers to a Guthub trial**, against a
decision made two days ago. The agent cannot see the pages to confirm it. Worth
looking at first, because it is a live contradiction and the fix is deleting a
button rather than writing anything.

---

## Where it goes, and a decision to make first

The documented funnel is: quiz, results page, seven-email sequence, Gut
Breakthrough Call, 3-Month Gut Reset. **The call is the sales mechanism**, so
the safe placement is to leave whatever CTA is there now as the primary action
and add this one **beneath it** as the secondary.

That keeps high-intent people going to the call and catches the ones who were
never going to book, which is most of them. It is additive and disturbs nothing.

The alternative is to make Gut Foundations the primary CTA and demote the call.
That would almost certainly sell more $27 courses and fewer calls. Since a call
leads to a $1,497 offer and this leads to $27, that trade is Steve's to make,
not the agent's. **Recommendation: secondary, for now.** Revisit once there are
numbers.

---

## The copy

Each heading is that archetype's own locked aha line, which the reader has just
seen on the results page. The echo is deliberate: it carries the sentence they
just read straight into the offer. If the line already appears immediately above
where this block will sit, swap the heading for the first sentence of the body
so it does not read twice.

Button text is the same on all five: **Get Gut Foundations, $27**
Button link is the same on all five: **https://www.gohappybelly.com/gut-foundations**

### 1. The Wired-and-Tired Gut

> **The food is fine. The system processing it is not.**
>
> That sentence is the whole of your result, and it raises the obvious question:
> what is actually going on in there? Gut Foundations answers it. Eleven short
> lessons on how digestion works, what all five patterns look like, and why
> yours behaves the way it does. About ten minutes each, yours to keep.

### 2. The Reactive Gut

> **The foods are not the problem. The barrier is.**
>
> Which is why the list keeps getting longer while the foods stay the same. Gut
> Foundations explains what that barrier actually is, what the other four
> patterns look like, and how to tell them apart. Eleven short lessons, about
> ten minutes each, yours to keep.

### 3. The Sugar-Driven Gut

> **The cravings are not yours.**
>
> Your result points at something that has worked out how to get itself fed. Gut
> Foundations explains the mechanism behind that, what the other four patterns
> look like, and why the afternoon crash is so predictable. Eleven short
> lessons, about ten minutes each, yours to keep.

### 4. The Underactive Gut

> **It is not what you are eating. It is what is breaking it down.**
>
> Your result points at the stage before absorption, the one almost nobody talks
> about. Gut Foundations explains how that stage works, what the other four
> patterns look like, and why protein feels heaviest when this is the pattern.
> Eleven short lessons, about ten minutes each, yours to keep.

### 5. The Bloated and Backed-Up Gut

> **The bacteria are not the problem. The location is.**
>
> Which is also why this pattern clears up and then comes back. Gut Foundations
> explains what that means, what the other four patterns look like, and what
> makes this one recur. Eleven short lessons, about ten minutes each, yours to
> keep.

---

## Optional: tag the links so the archetypes can be compared

If Steve wants to know which pattern converts best, append a different query
string per page instead of using the bare URL:

```
https://www.gohappybelly.com/gut-foundations?utm_source=scoreapp&utm_medium=quiz-results&utm_campaign=gut-foundations&utm_content=wired-tired
                                                                                                                                  ...reactive
                                                                                                                                  ...sugar-driven
                                                                                                                                  ...underactive
                                                                                                                                  ...backed-up
```

Harmless if unused, and it cannot be added retroactively, so it is worth doing
at paste time.

---

## Compliance

None of the five diagnoses the reader. They say "your result points at", which
is pattern language, and they make no claim to heal, seal, cure or treat.
Checked for em dashes and the banned word list: clean.
