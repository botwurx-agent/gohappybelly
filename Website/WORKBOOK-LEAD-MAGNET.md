# Free 7-Day Lifestyle Workbook: lead magnet

Built 2026-10-23. Everything below exists and is wired together. **Nothing is
live**, and it must not go live until the workbook file exists.

## What was found first

The card on `/links` was never working. `btn_action` on block
`1791980000002_l4` was `"#"`, so "Get the Workbook" did nothing at all. This was
not a change from ungated to gated; the lead magnet had never functioned.

There is also **no workbook file**. `list_media` returns nothing for "workbook"
or "lifestyle". Steve is supplying it.

## Decisions

**Dedicated opt-in page, not an inline form on `/links`.** A lead magnet page
can sell the thing, which an inline form in a list of five cards cannot, and it
is reusable in Stories, email and ads. `/links` stays a clean list.

**Kajabi form, synced to Mailchimp by Zapier.** Steve's call. The page is
Kajabi and on the design system, so a Kajabi form matches and can be built end
to end here. But the nurture apparatus lives in Mailchimp, so a lead captured
only in Kajabi would never reach the archetype sequences. The Zapier reuses the
pattern already running for Calendly to Mailchimp.

**The delivery email links to the thank-you page, not to the file.** That keeps
the file URL in exactly one place. Swapping it later is a single edit rather
than two that can drift apart. The "gate" is the form either way, since a direct
file URL is just as shareable as a page URL.

## What exists

| Piece | ID | State |
|---|---|---|
| Form "7-Day Lifestyle Workbook Opt In" | `2149762545` | Live, 2 fields (name, email) |
| Opt-in page | `2152353357`, theme `2167998577` | **Draft**, `/7-day-lifestyle-workbook` |
| Thank-you page | `2152353358`, theme `2167998578` | **Draft**, `/7-day-lifestyle-workbook-thank-you` |
| Tag `workbook-optin` | `2150412373` | Live, 0 contacts |
| Automation "7-Day Workbook: deliver and tag" | `1191254` | **Draft**, publishable, no validation errors |

Note: `create_landing_page` ignored the `path` argument passed to it and derived
both slugs from the title instead.

### The opt-in page

Two sections on the design system, ported from the Link in Bio theme
(`2167908665`), which is the reference Nova build. The CSS is a trimmed copy:
the link-card and portrait rules are dropped since this page uses neither.

1. `1792050000001` `#F8FAF8`: sage eyebrow, `<h1>`, two lead paragraphs, then the
   form immediately. The form sits high deliberately, so it is visible without
   scrolling on a phone.
2. `1792050000002` `#EFF7F1`: "Why this and not another food list", the argument
   for why habits beat another elimination list.

The form block's `thank_you` is set to `/7-day-lifestyle-workbook-thank-you` and
**verified as persisted**. Nova's `section/form` schema does not list
`thank_you` among its defaults, so this was worth confirming rather than
assuming.

### The thank-you page

1. `1792050000011` `#F8FAF8`: "Here is your workbook", a terracotta download
   button, and the support address.
2. `1792050000012` `#EFF7F1`: pushes the quiz. This matters more than it looks.
   The workbook is a habits document and does not enter anybody into the funnel
   by itself. The quiz does, because it writes GUTPATTERN and starts an
   archetype sequence. So the thank-you page's job is to move a fresh lead one
   step further in.

### The copy makes no claim about the seven days

The page describes the workbook thematically (sleep, stress, meal timing, the
habits around eating) and never lists a day-by-day curriculum, because the file
has not been seen. Once it exists the page can be made specific, which will
convert better. Do that before publishing.

## Still to do, in order

1. **Steve uploads the workbook** to the Kajabi media library.
2. Place it on the thank-you page's download button, block `1792050000011_t`,
   `btn_action` (currently `"#"`).
3. Rewrite the opt-in page's second section against the real contents.
4. Publish both pages (`update_landing_page` with `publish_at` set to now).
5. Point the `/links` card at the opt-in page: block `1791980000002_l4`,
   `btn_action` from `"#"` to `/7-day-lifestyle-workbook`, and set
   `new_tab: false` since it is now an internal page.
6. Steve builds the Zapier.
7. Steve arms automation `1191254` in the Kajabi admin. Agents never publish
   automations; that stays a human action, and CLAUDE.md requires explicit
   confirmation before anything sends.

**Do not do 4 or 5 before 2.** Publishing the capture without the delivery means
taking an email address and giving nothing back.

## The Zapier

| | |
|---|---|
| Trigger | Kajabi, New Form Submission, form `2149762545` |
| Action | Mailchimp, Add/Update Subscriber, audience "Go Happy Belly" |
| Tag | `workbook-optin`, to match the Kajabi tag |

Two things to watch when building it:

**The Kajabi form has one `name` field, not first and last.** Mailchimp's
`FNAME` wants a first name. Either split it with a Zapier Formatter step or
accept full names in `FNAME`, which will read oddly in any email using
`*|FNAME|*`.

**`GUTPATTERN` will be empty for these contacts.** They have not taken the quiz.
Any Mailchimp automation keyed on the merge tag has to tolerate a blank, which
is the other reason the thank-you page points at the quiz.

## Unrelated bug found on the same page

Card 5, "Watch Me on The Block, Season 17" (`1791980000002_l5`), is also dead.
Its `btn_action` is `"#"`, but there is a URL sitting in `img_action`:

```
https://www.facebook.com/BetaBlox/videos/2152813141819963/
```

`img_action` is the image click target, and the block has `hide_image: true`, so
nothing on the card can reach that URL. It looks like the link was supplied and
saved into the wrong field. One-line fix once Steve confirms that is the right
video; not changed on a guess.
