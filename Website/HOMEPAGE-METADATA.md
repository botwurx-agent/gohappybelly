# Homepage title and meta description

Written 2026-10-29. For Steve to paste. **The agent cannot do this one:** the
Kajabi MCP exposes `list_website_pages` and `get_website_page` but no
`update_website_page`, and no site-settings writer. Website page SEO is
read-only from here.

**Where it lives:** the Home website page, id `2154501976`, path `""`.
https://app.kajabi.com/admin/website_pages/2154501976/edit

Note `og:title` and `og:description` currently mirror the same values, so
fixing these two fields should fix link previews at the same time. Worth
re-checking a shared link afterwards to confirm.

---

## What is there now

**Title** (70 characters, will truncate in search results around 60):

```
Expert Gut Nutritionist | Heal Your Gut with Proven Courses & Coaching
```

**Description** (279 characters, Google displays roughly 160):

```
Transform your health with expert gut nutrition coaching and courses. At GoHappyBelly, we offer personalized one-on-one coaching and comprehensive programs to heal leaky gut, support digestive wellness, and enhance overall well-being. Start your journey to a healthier gut today!
```

## What is wrong with it

Four problems, and the first three break rules **Steve wrote himself** in the
original CLAUDE.md, not the agent-written "heal/seal" clarification:

1. **"Transform"** opens the description. On Steve's own banned-word list.
2. **"journey"** closes it. Same list.
3. **"heal leaky gut"** is the exact phrase the compliance rule names. The rule
   bans "any claim to heal, seal, cure or treat **it**", where "it" is leaky
   gut. Even read at its narrowest, this is squarely inside it.
4. **"Proven Courses"** is a results claim.

Two further issues neither the audit nor the agent flagged at first:

5. **"Expert Gut Nutritionist" may misstate the credential.** Alina is a
   Functional Diagnostic Nutrition Practitioner. "Nutritionist" is a protected
   title in some jurisdictions and is not what she holds. This is worth a
   decision independently of the rest.
6. **Both fields are the wrong length.** The title is at 70 characters and the
   description is 279, so search results truncate both mid-sentence.

**A correction on the record.** The agent first called the *title's* "Heal Your
Gut" a direct breach of a locked rule. That was overstated: the title's claim is
general, and the rule is scoped to leaky gut. The *description* is the real
breach, because it says "heal leaky gut" verbatim. See the provenance section in
CLAUDE.md.

---

## Replacement, CHOSEN BY STEVE 2026-10-29

**Title** (59 characters):

```
Gut Nutrition Coaching & Courses for Women | Go Happy Belly
```

Steve picked the "Gut Nutrition" wording over "Gut Health". It keeps the
search term people actually type while naming the subject rather than claiming
the protected title "Nutritionist", which Alina does not hold.

**Description** (156 characters):

```
Your labs came back normal but you still feel unwell. Alina Nazari, FDN-P, helps women find the pattern behind their gut symptoms. Courses and 1:1 coaching.
```

## Alternatives, not used

**Title, "Gut Health" wording** (56 characters):

```
Gut Health Coaching & Courses for Women | Go Happy Belly
```

**Title, shorter and closer to the brand line** (48 characters):

```
Root-Cause Gut Health for Women | Go Happy Belly
```

"Root-cause investigation" is how CLAUDE.md describes Alina's specialty, and the
footer already carries "Root-cause gut health for women who are tired of being
told they're fine." It is accurate as a description of the practice. Note the
homepage audit wanted "root cause" language qualified, though its concern was
about telling the *reader* her cause, which a practice description does not do.

**Description, plainer** (145 characters):

```
Alina Nazari, FDN-P, helps women understand what is actually driving their gut symptoms. Self-paced courses, functional testing and 1:1 coaching.
```

## Why these

**The recommended description leads with the objection, not the service.** "Your
labs came back normal but you still feel unwell" is the sentence Avatar 1 has
said to herself, and it mirrors the `/private-coaching` headline that is already
proven brand copy. A search result competes on whether someone recognises
herself in it, and a list of services does not do that.

**"Find the pattern behind their gut symptoms"** keeps pattern language and
describes what the practice does, without telling the reader what she has.

**The credential is stated correctly**, FDN-P rather than "nutritionist".

Checked clean: no banned words, no em dashes, no heal/seal/cure/treat, no
results claim, nothing diagnostic, and both fields inside the lengths search
engines display.

---

## The credential question, resolved

The old title carried "Expert Gut Nutritionist". Dropping "Nutritionist" is the
compliant choice, since Alina holds FDN-P and the title is protected in some
jurisdictions, but it risked losing a term people search for.

**Resolved 2026-10-29: "Gut Nutrition".** It names the subject rather than
claiming the title, so it keeps the search term and states nothing untrue. Used
in the chosen title above.
