# Automation: Gut Foundations delivery and onboarding

Drafted 2026-10-30. Closes blocker **B2** in `PRELAUNCH-AUDIT.md` for the $27
offer.

**Status: NOT YET CREATED IN KAJABI.** The `create_automation` call was
refused by the session's permission layer (category: account and standing-rule
changes). The tag below *was* created. Everything else here is ready to apply
the moment the call is approved, or to build by hand in the admin.

---

## Why this exists

Three automations exist on the site, all triggered by a form submission
(webinar x2, workbook). **None is triggered by a purchase.** A Gut Foundations
buyer currently receives Kajabi's built-in transactional email, which nobody
has read (U2), and then nothing ever again.

Meanwhile `/gut-foundations`' thank-you page ends with "Check your inbox too.
Your login details are on their way." That promise rests entirely on an
unreviewed default.

---

## Wiring

| | |
|---|---|
| Name | Gut Foundations: deliver and onboard |
| Trigger | `offer_purchased` on offer `2151464245` (Gut Foundations, $27) |
| Step 1 | `contact_tag_add` → `gut-foundations-customer` (tag `2150427047`, created 2026-10-30) |
| Step 2 | `email_send` → welcome (below) |
| Step 3 | `wait` → 2 days |
| Step 4 | `email_send` → nudge (below) |

Both emails are plain, not themed (`using_theme` unset). That is deliberate:
a delivery email that looks like a personal note from Alina lands better and
reads better than a designed template. The locked Georgia/navy system in
CLAUDE.md is the **Mailchimp** system and does not apply here.

### Step 1 is doing more work than it looks

There is currently no way to ask "who bought the $27?" without going through
the purchase list by hand. The tag is what makes every later automation,
segment and broadcast possible, including the ascension sequence.

---

## Email 1, sent immediately

**Subject:** You're in. Here's where to start.

> Hi {{ contact.first_name | default: 'there' }},
>
> Your Gut Foundations access is ready. All eleven lessons are unlocked right
> now, so you can go at whatever pace suits you.
>
> **Getting in**
>
> Log in at [gohappybelly.com/login](https://www.gohappybelly.com/login) with
> the email address you used at checkout. If you have not set a password yet,
> use the Forgot Password link on that page and one will be sent to you.
>
> **Where to start**
>
> Open **01. Understanding Your Gut**. It is about ten minutes, and everything
> after it builds on it.
>
> Before that there are three short pieces in Start Here. They take about four
> minutes together, and *What I Can And Cannot Do Here* is worth reading
> properly. It is the honest version of what this course is and is not.
>
> **What you have**
>
> - Eight core lessons, roughly ten minutes each
> - Three bonus modules: midlife and hormones, digestion under pressure, and a
>   system that stays on alert
> - One question at the end of every lesson
>
> One suggestion on pace. One lesson a day works better than four in an
> evening. The question at the end of each one is where most of the value is,
> and it needs a little time to sit.
>
> If something will not open or does not look right, reply here or write to
> support@gohappybelly.com.
>
> And the promise on the sales page stands: read it, and if it does not help,
> email inside 30 days and I will refund you.
>
> In Gut Health,
> Alina Nazari
> FDN-P

**Why the login instruction is worded loosely.** "If you have not set a
password yet, use the Forgot Password link" is true whether or not Kajabi's
built-in email already handed them one. Until U2 is read, stating the exact
mechanic would be guessing.

**Why the guarantee is repeated.** It is now a public promise on the sales
page with no Kajabi setting behind it. Restating it in writing at the point of
purchase is what makes it credible rather than decorative.

## Email 2, sent 2 days later

**Subject:** Did lesson 01 open alright?

> Hi {{ contact.first_name | default: 'there' }},
>
> Two days on. If you have already started, ignore this one.
>
> If you have not opened it yet, that is the ordinary thing to happen, and in
> my experience it is almost never about motivation. "Start the course" is a
> vague instruction, and vague instructions get moved to tomorrow.
>
> So here is a specific one instead. Open **01. Understanding Your Gut**. Ten
> minutes, on your phone, wherever you are.
> [Log in here](https://www.gohappybelly.com/login).
>
> That is the whole ask. Lesson 02 is much easier to start once 01 is behind
> you.
>
> In Gut Health,
> Alina Nazari
> FDN-P

---

## Known limitation, and the cheap fix

Email 2 goes to everyone, including people who started on day one. It opens
with "if you have already started, ignore this one", which is honest but not
as good as not sending it.

The proper fix is a second, tiny automation:

```
TRIGGER  Lesson is completed  →  "01. Understanding Your Gut" (2201324060)
STEP 1   Add tag              →  foundations-started
```

Then add `has_tag_id: foundations-started` as an **exit condition** on this
automation, and the nudge suppresses itself for anyone who has begun. Exit
conditions are free (not premium) and allow tag filters.

Not built, because it was not asked for. Recommended as the immediate
follow-up.

## Checks run against brand rules

- No em dashes
- No banned words (transform, journey, empower, authentic, passionate,
  innovative, creative, unique, elevate, synergy)
- Sign-off exactly as locked
- No diagnostic language, no claim to cure, treat, heal or seal anything
- "Eleven lessons" matches the sales page count (8 core + 3 bonus); the three
  Start Here pieces are front matter and are not counted, consistent with the
  twelve-to-eleven correction made on 2026-10-29

## Related, deliberately not handled here

**The order bump double-fires.** The Gut Fix at $10 is its own offer
(`2151452007`), so a bump purchase fires `offer_purchased` twice, once per
offer. This automation says nothing about The Gut Fix. If a Gut Fix welcome is
added later, a bump buyer receives two emails in the same minute. Whether the
bump delivers at all is still U1, untested.
