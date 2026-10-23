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

---

## Where the file goes: the media library will not work on its own

Confirmed 2026-10-23, and it changes step 2 above.

`Website/GUT-RESET-COURSE.md` already records the finding from the course build:

> - **Images** come back as a clean permanent CDN URL with no signing.
> - **Files** come back signed with a 7-day expiry, and the unsigned path is 403.

`place_media` states the same limit from the other direction: **"File assets
cannot be placed on themed surfaces."** A landing page button has no managed
file slot, so there is no way to hold a reference that Kajabi re-signs at render
time. A URL pasted onto the button is a snapshot that dies in a week.

This is why the download button cannot simply point at a media library asset.

### The two real options

**A. Host the PDF somewhere with a permanent public URL** (Google Drive set to
anyone-with-the-link, Dropbox, S3). The URL goes on the thank-you page button
and nothing else in the build changes. Zero friction for the reader: form, then
download.

**B. A Kajabi Download product granted by a free offer.** On platform, and the
contact ends up with real product access that can be built on later. The cost is
that she has to create a Kajabi account and set a password to read a free PDF,
which on Instagram traffic will lose a meaningful share of the people who just
gave their email.

**Recommended: A.** The purpose of this magnet is the email address, and the
form already captured that before the download is ever shown. Adding an account
signup after the capture protects nothing and costs conversions.

If A is chosen the file does not go in the media library at all. The uploader
link, should it be wanted for option B or for anything else, is
`https://app.kajabi.com/admin/sites/2148204891/media_library`.

### Worth a 30 second check either way

The signing behaviour above was observed during the course build, not re-tested
since. If Steve uploads the PDF to the media library, reading the asset back
will settle it: an unsigned permanent URL means option A can live on Kajabi and
nothing external is needed. A signed URL with an expiry confirms the note.

---

# How Kajabi actually delivers a lead magnet, 2026-10-23

Steve was right and the earlier recommendation here was wrong. The Kajabi form
block's **Thank You Page** setting is not only a page redirect. It has a
**"Download a file"** mode, and that mode simply stores a
`/resource_redirect/downloads/...` path in the same `thank_you` field.

Copied from the working `101-foods-before-one` page (landing page `2150689978`,
theme `2159076509`, form block `1621647488940`):

```
"thank_you": "/resource_redirect/downloads/file-uploads/sites/2148204891/themes/2159076509/downloads/ea4e80d-dcc2-4f6d-4880-8e2ab0458_GoHappyBelly_101_Foods_Before_One_Checklist.pdf"
```

`/resource_redirect/downloads/` is a Kajabi route that re-signs the S3 object
server side on every request. **That solves the 7-day expiry entirely.** No
external host, no Download product, no offer, no Kajabi account.

Note the path is **theme scoped**: the file sits under
`themes/2159076509/downloads/`, not in the global media library. That is why
`place_media` rejected both the collection and the product id, and why the
Pick File button in the form block is the upload route for this kind of asset.

## What that retires

The Download product route was started and is **not needed**:

| Thing | ID | Action |
|---|---|---|
| Download collection | `431713` | Delete in admin |
| Product | `2149610329` | Delete in admin |
| Free offer "Free 7-Day Lifestyle Workbook" | `2151466467` | Delete in admin, still draft |

None was ever published and nothing references them.

## Current wiring

- Opt-in form block `1792050000001_f`: `thank_you` → `/7-day-lifestyle-workbook-thank-you`
- Thank-you page download button `1792050000011_t`: `btn_action` →
  `/resource_redirect/downloads/file-uploads/sites/2148204891/files/01c016-318d-12aa-7d0a-7a5e1bc480e_Copy_of_7-Day_Healthy_Lifestyle_Challenge_Workbook.pdf`

That second path is **constructed, not copied**. The working example points at a
theme's downloads folder; the uploaded workbook is a media library asset under
`sites/2148204891/files/`. The route may or may not serve that prefix, and it
cannot be tested from this container because Cloudflare 403s the site. **Steve
tests it by clicking the button.**

If it 404s, the fix is to open the opt-in page's form block in the theme
builder, set Thank You Page to "Download a file", and use **Pick File**. That
uploads the PDF into the theme's own downloads folder and writes the proven path
shape. It also makes the separate thank-you page redundant, which is a choice
rather than a problem (see below).

## Two routes, one decision left

**A. Form downloads the file directly.** `thank_you` holds the file path. She
submits and the PDF arrives. Lowest friction, and what 101 Foods did. The
thank-you page and its quiz push disappear.

**B. Form redirects to the thank-you page**, which carries the download button
and the quiz push. One extra click, but she lands somewhere that moves her
further into the funnel rather than ending at a file.

Currently wired as **B**, because the workbook does not enter anybody into the
funnel by itself and the quiz does. 101 Foods used A because it had no next step
to offer. Flipping to A is one setting.

## Copy corrected to the real contents

Steve chose to ship the workbook as it is, so the card and the opt-in page now
describe what is actually in the file rather than the sleep and stress promise
that was never in it. Both now list the seven days: portion control, vegetables,
meal planning, smart snacking, hydration, mindful eating, active living.

The opt-in page's closing line does the one piece of repair available without
touching the PDF:

> It is a starting point, not a protocol. If you want to know what is actually
> driving your symptoms rather than build better habits around them, take the
> gut pattern quiz instead.

That names the limit of the document honestly and points at the thing that does
enter the funnel.

---

## Download moved onto the form, 2026-10-23

Steve's call. Form block `1792050000001_f` on theme `2167998577` now has
`thank_you` set to the file path instead of the thank-you page, so submitting
the form downloads the PDF directly. Verified by read.

Route A from the section above. Two things fall out of it:

1. **Thank-you page `2152353358` is now orphaned.** Nothing routes to it. It has
   never been published. Delete or keep, not decided.
2. **Automation `1191254`'s email still links to that page** as the place to
   download. If the page goes, the email link goes with it and should point at
   the file path instead. Not changed.

### The three Download-path objects cannot be deleted from here

This MCP has no delete for offers, products or download collections. The only
delete tool is `delete_navbar_link`. They have to go in the admin:

| Thing | ID | Admin |
|---|---|---|
| Download collection | `431713` | `app.kajabi.com/admin/downloads/collections/431713` |
| Product | `2149610329` | `app.kajabi.com/admin/products/2149610329` |
| Offer (draft) | `2151466467` | `app.kajabi.com/admin/offers/2151466467/edit` |
