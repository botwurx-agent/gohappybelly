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
