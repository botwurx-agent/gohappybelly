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

---

## Logo added to both emails, 2026-10-31 01:51Z

Steve, asked whether the emails were resolved including design: "at a minimum
it should have the logo."

```html
<p style="text-align: center;"><img src="...Go_happy_belly_4-ai_1_.png" alt="Go Happy Belly" width="180"></p>
```

Prepended to both email bodies. Nothing else changed.

**180px wide matches the locked Mailchimp email spec** ("Logo at top, 180px
wide, centered"). Deliberate: the reader does not know there are two email
platforms, and the 35 archetype emails they may already have received use that
treatment.

**The logo is the Kajabi-hosted site header asset**, not the Mailchimp CDN
file recorded in CLAUDE.md under Key URLs. Same brand mark, but a Kajabi email
depending on Mailchimp's CDN is a needless cross-platform dependency. Source
is 1000x625 and renders at 180, so it stays crisp on retina. Verified
reachable: HTTP 200, `image/png`, 31,116 bytes.

**Stopped at the logo on purpose.** The locked Mailchimp treatment also has a
sage accent line below the logo, a cream outer wrapper and a white inner card.
Steve said "at a minimum the logo", and the agent had already made one
unilateral design call on these emails, so it did not add the rest. The sage
line is the obvious next element if he wants it.

### Verified after the edit

| Check | Result |
|---|---|
| `<img>` through the sanitizer | survived, both emails |
| `style="text-align: center;"` | survived, so it is centred |
| `width="180"` | survived |
| Node ids | `6618395`-`6618400` unchanged, step identity preserved |
| Wait | still 2 days |
| Exit condition | preserved, echoed back on the write |
| Status | published, `errors: []`, `total_enrolled: 0` |

Edge ids changed (`52107xx` to `52138xx`), so edges are recreated on a steps
replace while nodes are not. Graph shape identical.

### Reusable finding: the sanitizer keeps style attributes

The `email_send` body documents its allowed **tags** (`a p strong em u text img
br h1 h2 h3 span li ul ol`) and says nothing about attributes. Confirmed by
read-back that `style`, `width`, `alt` and `href` all survive. So inline
styling is available in automation emails, which means the full locked email
treatment could be built here without `using_theme: true` if that is ever
wanted.

### Still unresolved, and not ours

The other emails a buyer receives in the same minute are still unread: the
Kajabi purchase/receipt email (U2), any offer grant email, and whatever the
$10 Gut Fix bump sends (U1). `get_offer` exposes no email settings at all, so
none of this is visible from here. The test purchase is what answers it.

Confirmed from `get_offer` while checking: post-purchase preference is
`landing_page` pointing at `2152353598`, the correct thank-you page. Whether a
Purchase Flow overrides that is still U3.

---

## U2 located: the email templates page, 2026-10-31

Steve: "all email templates can be customized here:
https://app.kajabi.com/admin/sites/2148204891/email_templates"

That is where the built-in transactional emails live. **The agent cannot
reach it.** Searched the full Kajabi MCP tool surface for an email-template
tool and found none; the `emails` toolset covers broadcasts and sequences
only. The URL is behind admin auth, so WebFetch cannot read it either. Same
class as Purchase Flows: visible to Steve, invisible from here.

### The risk this creates right now

**Two logos.** The logo was added inline to both automation email bodies on
the assumption that no template layer existed. If that page sets a global
header carrying the logo, a buyer sees it twice.

If there is a global wrapper, the correct fix is to brand the template once
and **remove the inline `<img>` from both emails in `1388764`**, not to keep
both. One line to strip, whenever it is confirmed.

### What is needed from that page before changing anything

1. Is there a purchase or receipt template, and does it carry login details?
2. Is there a global header/footer wrapping every send, or is each template
   standalone?
3. Do automation emails appear in that list, or only transactional ones?

Question 3 is the one that decides the inline logo. Note the broadcast and
sequence tools both refer to "the site's default email preset", which implies
site-level email presets exist, but those attach to *themed* emails
(`using_theme: true`). The two automation emails here are not themed, so
whether any preset or template wraps them is genuinely unknown.

The test purchase answers all three by showing what actually lands.

### The template list, supplied by Steve 2026-10-31

61 transactional templates. **Exactly one is "Customized"; every other is
"Default".** Answers to the three questions above:

**1. Three Default templates fire on a $27 purchase.**

| Template | Kajabi's description | Status |
|---|---|---|
| Offer Purchase Confirmation | Sent to members after completing a purchase | Default |
| Offer Grant Confirmation | Sent to members when they are granted a new product | Default |
| Member Welcome Email | Sent when a member doesn't create an account after purchase, or when an offer is granted manually, through automations, or via webhooks | Default |

**Member Welcome Email is almost certainly the login email**, on its
description alone. That makes it the thing both thank-you pages' promise
("your login details are on their way") actually rests on, and it has never
been read.

**The real problem is the pile-up, not any single email.** A buyer may receive
three system emails plus the automation's welcome email within the same
minute, and a fourth if the $10 bump grants The Gut Fix separately.

**2. There is a Branding tab** alongside Templates. That is the global layer,
so the double-logo risk recorded above is live, not hypothetical. Check it
before deciding whether the inline `<img>` in `1388764` stays.

**3. Automation emails are NOT in this list.** It is transactional templates
only. The automation's two emails live in the workflow, which is why MCP can
read and write them while this page cannot. Whether the Branding tab wraps
them anyway is still unknown.

### Unrelated find: an unreviewed abandoned-cart email is live

**"Abandoned Checkout" is the only Customized template on the site.** Someone
wrote it at some point and it is sending now, to everyone who starts a
checkout and does not finish, the $27 included. It appears nowhere in this
project's notes. Worth reading on its own merits, independently of the
launch work.

### Likely consequence for the welcome email, once the above is read

If Member Welcome Email already carries login details, the automation's
welcome email duplicates it. The fix would be to drop its "Getting in"
paragraph and lead with "Where to start" instead, since that is the part no
system template covers. Not changed yet: it needs the actual template text
first, and guessing is what put the inline logo at risk of doubling.

### Template contents read, 2026-10-31

Steve supplied screenshots of the Branding tab and three templates.

#### URGENT: the global email button fails contrast at 1.78

Sampled from the screenshots, the button is **`#9ACEAA`** with white text in
all three template previews **and** in the Branding tab's Button Color
swatch, confirming one global setting.

| | Contrast vs white | AA |
|---|---|---|
| `#9ACEAA` button, white text | **1.78** | fails 4.5 and even 3.0 |

Same class of defect as the login page button fixed 2026-10-29 (1.47 to
4.80), in a worse place: it renders as **"Set up password"** on Member
Welcome Email, the single most important button in the funnel. A buyer who
cannot see it cannot get in, and will not report it.

**Cheapest fix is the Font Color swatch, not Button Color**, keeping the
existing green:

| Font colour on `#9ACEAA` | Ratio |
|---|---|
| White (current) | 1.78 |
| Forest `#162E28` | **8.10** |
| Body `#2E4438` | 5.89 |

Alternative, white text on a darker button: `#A85F3E` 4.80, `#162E28` 14.43.
Brand terracotta `#C07A5A` only reaches 3.40 and brand sage `#7AAE86` 2.55,
so neither passes. Note this is the same two-terracotta question already open
in the design system.

#### Offer Purchase Confirmation is wrong for first-time buyers

> You can login with your **email and password** at the link below. [Login]

A new buyer has no password. That is exactly what Member Welcome Email
exists to supply (`{{invite_url}}`, "set up a password"). So the receipt
sends them to a login they cannot pass, while the email that works arrives
separately, and order of arrival is not controlled.

#### The three templates, as they stand

| Template | Subject | Sign-off |
|---|---|---|
| Member Welcome Email | `Your New {{site.title}} Account` | `-- {{site.title}}` |
| Offer Purchase Confirmation | `Purchase confirmation for '{{offer.title}}'` | `-- {{site.title}}` |
| Abandoned Checkout | `Looks  Like You Left Something In Your Cart!` | `Alina Nazari / {{site.title}} / support@` |

None uses the locked sign-off. Abandoned Checkout's subject contains a
**double space** between "Looks" and "Like", and it opens "Hey There!",
which is not Alina's voice. It is live and sending now.

**Constraint on any rewrite:** these templates allow `<a>` tags only, stated
in the UI as "Only html &lt;a&gt; tags are allowed. Please no images, divs,
etc." So no sage accent line, no inline styling. The Branding tab (logo,
button colour, button font colour) is the only design lever.

Liquid available per template, from the UI:
- Member Welcome Email: `{{member}}`, `{{site}}`, `{{site_login_url}}`, `{{invite_url}}`
- Offer Purchase Confirmation: `{{member}}`, `{{offer}}`, `{{site}}`, `{{site_login_url}}`
- Abandoned Checkout: `{{email}}`, `{{offer}}`, `{{site}}`, `{{offer_checkout_url}}`

#### Consequence for the automation's welcome email

Confirmed: Member Welcome Email carries the invite link, so a buyer receives
**three** different login instructions. The automation's welcome email should
drop its "Getting in" paragraph and lead with "Where to start", the only part
no system template covers. Not changed yet, to avoid rewriting it twice
before the two issues above are settled.

#### Logo, still unresolved

The Branding logo is active and appears atop all three previews, and it is
the same file used inline in the automation emails
(`Go_happy_belly_4-ai_1_.png`). Whether Branding also wraps automation emails
is still unknown; the test purchase settles it.

---

## Welcome email rewritten after the templates landed, 2026-10-31 04:36Z

Steve pasted all three transactional rewrites. With Member Welcome Email now
carrying the invite link properly and Offer Purchase Confirmation no longer
telling new buyers to use a password they do not have, the automation's
welcome email no longer needs to explain access at all.

**Removed:** the whole "Getting in" paragraph, which was the third and now
redundant set of login instructions.

**The email now leads with "Where to start"**, the only thing no system
template covers.

**Kept, but moved and shortened**, down with the troubleshooting lines rather
than up front as a section:

> Not set your password yet? There is a separate email, "Set up your Go Happy
> Belly password". Start there and all of this will be waiting.

That is a pointer, not a competing instruction. It routes a stuck reader to
the email that actually works instead of giving them a fourth method, and it
names that email by the exact subject now live on the template.

### Both emails now link to /library, not /login

Re-verified before shipping it: `https://www.gohappybelly.com/library` returns
200, redirects a logged-out visitor to `/login`, and that page has a working
password form. So one link serves both cases. A member lands in their library;
anyone else gets the login page. `/login` only ever served the second.

### Verified after the edit

| Check | Result |
|---|---|
| "Getting in" paragraph | gone |
| Opens on "Where to start" | yes |
| `/library` links | both emails |
| Password pointer | present, in the troubleshooting block |
| Logo | intact, both emails |
| Node ids | `6618395`-`6618400` unchanged |
| Wait | 2 days |
| Exit condition | preserved |
| Status | published, `errors: []`, `total_enrolled: 0` |

### Coupling to watch

The welcome email quotes the Member Welcome Email's subject line verbatim
("Set up your Go Happy Belly password"). If that template's subject changes,
this quote has to change with it, or it points a stuck buyer at an email they
cannot find. Same coupling already noted between the two transactional
templates in `EMAIL-TEMPLATE-REWRITES.md`.

### Observed in passing

The `/library` check returned the page title
`Expert Gut Nutritionist | Heal Your Gut with Proven Courses & Coaching`,
so the site-wide SEO string is still unchanged. Step 5 in
`STEVE-CHECKLIST.md` is still outstanding.
