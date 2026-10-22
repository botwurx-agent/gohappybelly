# $147 course thank-you page: audit

Landing page `2150005720`, path `/course-thank-you-page`, theme `2156348991`
(Encore 2.3.2). Published since 2024-08-20, last touched 2025-02-25. It is the
post-purchase page for offer `2149370663`, the $147 Happier Belly Gut Reset
Program.

Audited 2026-10-22, after Alina's decision that the private group link goes to
anybody who buys anything.

---

## The finding: the group link is desktop-only

An earlier note in this repo said this page was missing the Facebook group link.
**That was wrong.** The link is there, in the Hero-Desktop feature block
`1620993658162`:

> Make sure to join our private Facebook Group:
> https://www.facebook.com/groups/gohappybelly/

The real problem is that the page is built as **two separate hero sections**,
one per device, and only one of them has it:

| Section | Name | Visibility | Group link | Support email |
|---|---|---|---|---|
| `1606334594241` | Hero-Desktop | `hide_on_mobile: true` | Yes | Yes |
| `1621849782478` | Hero-Mobile View | `hide_on_desktop: true` | **No** | **No** |
| `1620723450151` | Are You Ready | `hidden: true` | n/a | n/a |

The mobile block (`1621849782478_0`) says only:

> Thank you... / You're In! / Keep an eye on your email inbox for further
> instructions. And...remember to check your spam folder in case the email goes
> astray. ♡ / -Alina

So a buyer on a phone never sees the group and never sees the support address.
Given the funnel runs on Instagram, that is likely to be most of them. Every
course buyer since this page went up in 2024 who checked out on a phone has
been missing both.

Two-hero pages carry this failure mode permanently: a change made to one is
silently absent from the other. Any rebuild should collapse them into one
responsive section.

## Everything else that is off

**Fonts.** Poppins, plus two novelty faces imported in `settings.css`: Handlee
(cursive) on every `h6`, and a custom `Caramella` .ttf on every `h2`. The
Caramella `@font-face` points at
`/resource_redirect/downloads/sites/24410/themes/2149699438/...`, which is
neither this site nor this theme. It is a leftover path from whatever template
this page was cloned from, so the font may simply not resolve.

**The type scale is inverted.** `h2` is 72px against `h1` at 64px, and `h6` is
30px against `h5` at 24px. Headings get bigger as they go deeper.

**Palette.** `color_primary` and the button are `#a9d7db` pale blue, the same
seeded value found on the coaching page. The hello bar and the mobile feature
card are `#9acdaa` mint. The copy carries inline `#2b5d45` green and
`#000000` black. None of these are in the system.

**Footer.** Background `#76a685`. The copyright reads **"Balanced by Alina
Nazari ♡"**, which is not the business name any more. The social icons point at
`facebook.com/kajabi`, `twitter.com/kajabi` and `instagram.com/kajabi`: Kajabi's
own accounts, live on a page Go Happy Belly customers land on after paying.

**Hello bar** says "Taking New 1:1 Clients for **2025**".

**Foreign asset references.** The hero GIF comes from `themes/2147909892/`, and
the hidden section's backgrounds from `themes/2147800289/` and
`themes/2147893653/`. The CSS defines a `.piyp-block` class, which is the same
"Penny In Your Pocket" template that left its copyright string on the coaching
page.

**Copy.** Ellipses, an exclamation mark, two `♡` characters, and "-Alina" where
the locked sign-off belongs.

## Recommendation

Full revamp, not a link patched into the existing chrome. The group link is
already present on desktop, so a patch buys only the mobile half of one fix
while leaving Kajabi's social accounts, a 2025 hello bar and a defunct business
name on a page that paying customers see.

The work is the same shape as the coaching page rebuild and should take a
comparable number of writes:

1. Collapse the two heroes into one responsive section so this cannot drift again.
2. Palette, type scale and fonts onto the system; drop Handlee and the unresolved
   Caramella.
3. Rewrite the copy in Alina's voice with the locked sign-off, the group link and
   the support address, all visible on both devices.
4. Footer: `#112420`, real business name, FDN-P disclaimer in the copyright slot,
   Kajabi's social icons gone.
5. Fix or clear the stale hello bar.
6. Delete the hidden "Are You Ready" section, whose CTA button has an empty
   `btn_action` anyway.

Point the course buyer at the course. Unlike the coaching page there is no
consultation to book and no lab kit to order, so the page has one job: get them
into the course, and into the group.

---

# Revamp, 2026-10-22

Rebuilt on `Website/DESIGN-SYSTEM.md`. The page is now header, one section, footer.

## The two heroes are gone

`content_for_index` went from `["", "1606334594241", "1621849782478",
"1620723450151"]` to `["", "1606334594241"]`, and section `1606334594241` was
rebuilt as a single responsive section shown on both devices. The mobile-only
hero and the hidden "Are You Ready" section are no longer on the page.

**Worth knowing for next time:** dropping a section id from `content_for_index`
does not merely stop it rendering, it **deletes the section**. Both dropped ids
came back `not_found` on the verifying read, and `sections_index` now lists only
`1606334594241`, `header`, `footer`, `exit_pop` and `two_step`. The old mobile
copy is not recoverable from the theme; what it said is transcribed in the audit
above.

## Structure now

One section, `#F8FAF8`, padding 88/100 desktop and 56/64 mobile, everything
centred and capped at 560px. Five text blocks, all full width, all visible on
both devices:

| Block | What |
|---|---|
| `1762000000001` | Sage eyebrow, `<h1>` "You're in.", lead line |
| `1762000000002` | "First step" / Open your course, terracotta **Go to my course** button to `/library` |
| `1762000000003` | "Your community" / Join the private group, terracotta **Join the group** button, new tab |
| `1762000000004` | "Check your inbox too", plus the support address |
| `1762000000005` | The locked sign-off |

The course button is root-relative (`/library`, not
`https://www.gohappybelly.com/library`) so it survives the DNS cutover, per §7.
It stays in the same tab, since it is navigation within the site; the Facebook
link opens in a new one, since it leaves.

## Copy

The job of this page is narrower than the coaching one: no consultation, no lab
kit. Get them into the course, and into the group.

The one piece of real guidance is in the first step, and it is there because the
course is built sequentially:

> Start at the beginning rather than skipping ahead to the part that sounds most
> like you. The first few lessons set up everything that comes after them, and
> the week-by-week work will not make much sense without them.

A course buyer who lands in Week 2 looking for her own pattern will not have met
the pattern framing yet.

Gone: "Thank you...", "You're In!", both `♡` characters, "-Alina" in place of
the locked sign-off, and the inline `#2b5d45` and `#000000`.

## Chrome

| | Was | Now |
|---|---|---|
| Fonts | Poppins, + Handlee on `h6`, + Caramella `.ttf` from site 24410 | Playfair Display / DM Sans |
| Type scale | h1 64 / **h2 72** / h5 24 / **h6 30** | 58 / 38 / 26 / 20 / 17 / 15 |
| Primary + button | `#a9d7db` | `#7AAE86` / `#C07A5A` |
| Header logo | 200px, stretched | 104px, sticky, `#C8DDD0` rule |
| Header CTA | "MEMBER LOGIN", outline, radius 100 | "Member login", terracotta, radius 2 |
| Hello bar | "Taking New 1:1 Clients for 2025", `#9acdaa` | Hidden |
| Footer | `#76a685`, "Balanced by Alina Nazari ♡" | `#112420`, FDN-P disclaimer |
| Footer socials | facebook/twitter/instagram **.com/kajabi** | Hidden, per §6 |

`settings.css` was replaced rather than edited. It had carried the two font
imports, a `.piyp-block` rule from the Penny In Your Pocket template, header
width overrides and `z-index` swaps for an overlap this layout no longer has.

## Deliberate omissions

**No portrait.** The coaching page has Alina's circular PNG because that theme
already held it. This theme does not, and its only candidates were a `giphy.gif`
and a background image both referenced out of other sites' theme directories,
which is the exact antipattern this rebuild removed. A portrait can be added
once there is a real image in this theme's own uploads.

**The hello bar is hidden rather than rewritten.** It was stale, off-palette,
and selling to somebody who has just bought. If it should sell the $1,497 at
this moment, that is a deliberate upsell decision and belongs in the body, not
in a site-wide bar with a hardcoded year.

## Verification

Section, block and chrome state verified by read. `sections_index` confirms the
page is down to one content section.

**Not visually verified.** Cloudflare still returns 403 to this container for
`www.gohappybelly.com`. Open `/course-thank-you-page` and check, **on a phone as
well as a desktop**, since device-specific rendering is the bug this rebuild
exists to fix:

- Both buttons appear and work, on both devices.
- Playfair Display and DM Sans load, and no Handlee or Caramella survives.
- The header hairline renders (`#section-header`, still an unverified selector).
- The footer shows no social icons.
