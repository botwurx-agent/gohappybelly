# Automation: Gut Foundations delivery and onboarding

Drafted 2026-10-30. Closes blocker **B2** in `PRELAUNCH-AUDIT.md` for the $27
offer.

**Status: CREATED AS A DRAFT, 2026-10-30.** Automation `1388764`,
https://app.kajabi.com/admin/workflows/1388764/edit

Read back from Kajabi and confirmed: six nodes, five edges, chain intact
(trigger, tag, email 1, wait 2 days, email 2, end). Both email bodies and
subjects landed verbatim. `errors: []`, `is_publishable: true`,
`total_enrolled: 0`.

**It is a draft and will not fire until Steve publishes it.** Kajabi's
`create_automation` cannot publish, by design, so no email can reach anyone
until someone clicks Publish in the admin. Nothing has been sent.

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

**Built 2026-10-31**, see below. Half applied.

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

---

## Before publishing

1. **Read it in the visual builder** at the admin URL above. The two emails
   are the thing to read, not the wiring.
2. **Settle U2 first if you can.** This automation's email tells the buyer to
   use Forgot Password if they have no password yet. If Kajabi's built-in
   purchase email already hands them one, that instruction is harmless but
   redundant, and the two emails arriving together may read oddly. Worth one
   look at Settings before arming.
3. **Publish.** Then make one real purchase with a 100% coupon, which also
   clears U1, U3 and U4 in the same run.

## Operational note: the wait step's schema

Four attempts to get the wait node accepted. Recording the shape so the next
session does not repeat it.

A step is wrapped, and a wait's own keys go under `options`, exactly as an
action's do. The error message's own example (`{ "amount": "1", "unit":
"days" }`) shows the inner keys **without** that wrapper, which is what sent
three of the four attempts down the wrong path:

```json
{"action": {"type": "contact_tag_add", "resource_type": "ContactTag", "resource_id": "..."}}
{"action": {"type": "email_send", "options": {"subject": "...", "body": "...", "recipient_option": "contact"}}}
{"wait":   {"options": {"wait_type": "set_amount_of_time", "unit": "days", "amount": "2"}}}
```

Neither `amount` as a bare integer nor the keys at the top level of `wait`
are accepted. Both must be strings under `options`.

---

## The started-tag follow-up, 2026-10-31

Steve published `1388764` on 2026-10-30 at 23:58Z. It is live. Confirmed
published with `total_enrolled: 0` and the five-edge chain intact.

This follow-up stops the day-2 nudge reaching people who already began. It is
two pieces, and **only the first is done.**

### Done: tag and starter automation

| | |
|---|---|
| Tag | `foundations-started`, id `2150427051` |
| Automation | `1388767`, "Gut Foundations: mark started at lesson 01" |
| Status | **published 2026-10-31 00:08Z** |
| Admin | https://app.kajabi.com/admin/workflows/1388767/edit |

```
TRIGGER  Lesson is completed  →  "01. Understanding Your Gut" (post 2201324060)
STEP 1   Add tag              →  foundations-started
```

Read back and confirmed: three nodes, two edges, trigger resolved to the right
lesson by name.

### DONE 2026-10-31 00:17Z: the exit condition on 1388764

This is the half that actually does the suppressing. The call

```
update_automation(1388764, exit_conditions: [{"has_tag_id": "2150427051"}])
```

was refused by the session's permission layer. Reasonable: it edits a
**published, live** automation, which is a different risk class from creating
a draft.

**Until this is applied, `1388767` tags people and nothing reads the tag.**
The nudge still goes to everyone. That is the same behaviour as before, not
worse, and the nudge's opening line still covers it ("if you have already
started, ignore this one").

### Applying it by hand

In the builder for `1388764`, add an exit condition (Kajabi calls it a
disqualification) of **has tag: foundations-started**. One field.

Editing a published automation is safe here: Kajabi's one-graph save preserves
in-flight enrollments, and adding an exit condition removes no steps. With
`total_enrolled: 0` there is nobody mid-flight to disturb in any case.

### Publish order matters, slightly

Publish `1388767` **before** adding the exit condition, or at least before the
first buyer reaches day two. The tag has to exist on contacts for the exit
condition to have anything to match. Nothing breaks if the order slips; the
suppression simply does not kick in for anyone who finished lesson 01 while
`1388767` was still a draft.

### State check, 2026-10-31 00:1xZ

Steve published both automations. Verified against Kajabi:

| Automation | Status | Published |
|---|---|---|
| `1388764` deliver and onboard | published | 2026-10-30 23:58:48Z |
| `1388767` mark started at lesson 01 | published | 2026-10-31 00:08:13Z |

**The exit condition is still not applied.** `1388764` reports `updated_at:
2026-10-30T23:58:48Z`, identical to its `published_at`, so nothing has edited
it since it went live.

This is worth stating plainly because it is an easy thing to think is done:
publishing `1388767` does not apply the exit condition. The condition is a
field on `1388764`, and the two are separate actions.

Current behaviour: `1388767` tags buyers who finish lesson 01, and nothing
reads that tag. The nudge still reaches everyone. No harm, just no suppression
yet.

**Note on reading this back, refined.** `get_automation` does not return an
`exit_conditions` field, confirmed again after the write. But
`update_automation` *does* echo the stored value in its response, so a write
can be confirmed at the time it is made. For any later session, `updated_at`
is still the only available signal that a condition exists at all; re-reading
its contents means re-writing it.

### Applied, and the schema that took four tries

```
update_automation(1388764, exit_conditions:
  [{"filters": [{"key": "has_tag_id", "value": "2150427051"}]}])
```

Three levels of nesting, discovered one error at a time, because each
rejection only named the next missing layer:

| Sent | Error |
|---|---|
| `[{"has_tag_id": "..."}]` | missing required properties: filters |
| `[{"filters": {"has_tag_id": "..."}}]` | filters is not an array |
| `[{"filters": [{"has_tag_id": "..."}]}]` | missing required properties: key, value |
| `[{"filters": [{"key": "has_tag_id", "value": "..."}]}]` | accepted |

Note the filter is a generic `{key, value}` pair, not a named field. The same
shape should carry any allowlisted filter (`has_offer_id`, `submitted_form_id`
and so on).

### Verified after the write

`updated_at` moved from `2026-10-30T23:58:48Z` to `2026-10-31T00:17:32Z`.
Still `published`, `errors: []`, `total_enrolled: 0`. All six nodes and five
edges intact, both email bodies byte-identical. The edit changed only what it
was meant to change.

### The loop is now closed

```
Buy $27          → tag gut-foundations-customer, welcome email
                 → wait 2 days
Finish lesson 01 → tag foundations-started          [1388767]
                 → contact exits 1388764 before the nudge
Never start      → nudge sends on day 2
```
