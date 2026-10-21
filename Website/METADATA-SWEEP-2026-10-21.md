# Metadata and title sweep, 2026-10-21

Swept every live page's head metadata, every course module and lesson title,
every published offer title and every navbar label against the CLAUDE.md
guardrails and the banned word list, plus British spellings.

Scope: 17 live pages, 9 course modules, 55 published lesson titles, 14 draft
lesson titles, 19 published offers, 8 navbar labels.

Nothing was changed. This is a findings list.

---

## 1. The home page metadata. Fix this one first

Six fields, all carrying the same two strings.

**`<title>`, `og:title`, `twitter:title`:**

> Expert Gut Nutritionist | **Heal** Your Gut with Proven Courses & Coaching

**`description`, `og:description`, `twitter:description`:**

> **Transform** your health with expert gut nutrition coaching and courses. At
> GoHappyBelly, we offer personalized one-on-one coaching and comprehensive
> programs to **heal leaky gut**, support digestive wellness, and enhance
> overall well-being. Start your **journey** to a healthier gut today!

Four distinct violations in one sentence:

| Term | Rule |
|---|---|
| "heal leaky gut" | **"You have SIBO / Candida / Leaky Gut"** is the first entry under Never Use. This is the banned phrase and a banned verb together |
| "Transform" | Banned word list |
| "journey" | Banned word list |
| "heal" (title) | Avoided across the whole course per the same reasoning |

**Why this is the worst instance on the property.** It is not body copy that a
visitor reads after arriving. `<title>` is the Google result. `og:title` and
`og:description` are what render on the share card every time anyone posts the
link to Instagram or Facebook. These two strings are seen by more people than
any page on the site, including people who never visit it.

It survived every previous pass because head metadata is invisible unless you go
looking. It was found while scraping the page for Alina's bio.

**Not fixed, deliberately.** "Heal Your Gut" is almost certainly there because it
is a high-volume search term, so there is a real trade-off between ranking and
the compliance rules, and that is Steve's call rather than the agent's. The
description has no such defence and should go regardless.

## 2. "Fortnight", twice, in the course

| Where | Visible to |
|---|---|
| Module `2160964491` title, **The Reintroduction Fortnight** | every member, in the sidebar |
| The course description, "Then a reintroduction fortnight" | the sales page and the member library |

British. The agent's own error, shipped. It is also legible in
`course-hero-laptop.png`, the hero mockup published on the sales page today, so
it currently appears on the page selling the course.

One rename call plus one description edit.

## 3. Everything else is clean

No violations in:

- 55 published lesson titles
- 9 module titles (other than item 2)
- 14 draft lesson titles
- 19 published offer titles
- 8 navbar labels across the main menu and footer
- 16 of the 17 pages' metadata

**Considered and not flagged:** `SIBO BREATH TEST` and `H. PYLORI ONLY` as offer
titles. Those are the names of the tests being sold, which is factual product
naming, not a claim that the buyer has the condition. The guardrail is about
telling someone what they have.

---

## Two things found in passing, outside the sweep's scope

### Most pages have no metadata at all

| | |
|---|---|
| Pages with a `<title>` | 14 of 17 |
| Pages with a `description` | **4 of 17** |

**`/private-coaching`, `/shop` and `/gut-reset-course` have neither.** Those are
the three pages that sell things. Google writes its own snippet when there is no
description, and the share card falls back to the URL.

That is an SEO and conversion gap rather than a compliance one, which is why it
is listed down here. It is also the cheapest fix on this page: three titles and
three descriptions, written to the rules from the start.

### CLAUDE.md documents 8 offers. Kajabi has 19 published

Live, purchasable, and not in the documented offer suite:

| Offer | Price |
|---|---|
| DUTCH Complete Hormone Panel | $497 |
| Blood Chemistry Panel (DHA Laboratories) | $450 |
| Heavy Metal Panel, urine | $250 |
| Happy Belly Essentials Club | $9.97/mo |
| Bi-Weekly Private Group Coaching Calls | $29.97 |
| 6 Month Private 1 on 1 Coaching | $2,497 |
| 12 Month Private 1 on 1 Coaching | $4,497 |
| 3 Month Private 1 on 1 Coaching Webinar Package | $1,297 |
| E-Book: Making Your Way To A Happier Belly | $9.97 |
| The 3-Day Bone Broth Reset | $47 |
| The Gut Fix | $10 |

CLAUDE.md is the source of truth the agent prices and positions from, and it is
missing more than half the catalogue. Some of these are presumably retired and
still published, which is its own problem: a retired offer with a live checkout
can still be bought.

Worth a pass with Steve to mark each as current or retired, then bring the
survivors into CLAUDE.md.

---

# Follow-up, same day

## Done

- Module `2160964491` renamed **The Reintroduction Fortnight → The Two-Week
  Reintroduction**.
- Course description: "Then a reintroduction fortnight" → "Then a two-week
  reintroduction".

## The sweep's own scope was wrong

It scanned **titles and metadata only**, not lesson bodies. "Fortnight" is in
**14 published lesson bodies** as well, found by `search_course_content` after
the rename was requested:

| Lesson | Module |
|---|---|
| Welcome: Start Here | Start Here |
| How This Course Works | Start Here |
| Working With The Reactive Gut | Your Pattern, In Detail |
| Working With The Bloated And Backed-Up Gut | Your Pattern, In Detail |
| Working With The Wired-And-Tired Gut | Your Pattern, In Detail |
| Week 3: This Week For Your Pattern | Week 3 |
| Week 4: Widen Your Range | Week 4 |
| Week 4: This Week For Your Pattern | Week 4 |
| How Reintroduction Works | The Two-Week Reintroduction |
| Your Reintroduction Tracker | The Two-Week Reintroduction |
| Reintroducing For Your Pattern | The Two-Week Reintroduction |
| When You Have Finished | The Two-Week Reintroduction |
| Shopping List: The Bloated And Backed-Up Gut | Your Reference Shelf |
| Three Days Of Meals: The Underactive Gut | Your Reference Shelf |

So the true count was 16, not 2. **A title-and-metadata sweep is not a content
sweep.** Any future sweep has to run `search_course_content` over bodies as
well, or it will report a fraction of what is there and someone will make a
decision on the wrong number.

Not fixed, pending Steve's call. Each needs a contextual replacement rather than
a find-and-replace ("settle for a fortnight" and "the reintroduction fortnight"
want different wording), and it is 14 writes to a live course with members on it.

## The home page metadata cannot be fixed through the MCP

Established by elimination:

- `get_website_page` on the Home page (`2154501976`) returns
  `page_title: "Home"` and `page_description: null`, so the live strings are not
  set there.
- There is **no `update_website_page` tool**. The pages toolset covers landing
  pages for writes and website pages for reads only.
- There is no site-settings write tool. `get_site_summary` is read-only and does
  not return these fields.
- The site theme (`2156348838`) has no SEO section.

The strings are Kajabi's site-level SEO defaults, set in the admin under
Settings, and they are inherited by every page that does not override them.
That is also why they show up on a page whose own record is empty.

**Steve has to paste this one in.** Replacement text is in the main findings
above; the rewrite is below.
