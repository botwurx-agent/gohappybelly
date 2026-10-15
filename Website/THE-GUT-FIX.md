# The Gut Fix sales page

| | |
|---|---|
| Page | `2152336275` |
| Theme | `2167909908` (Nova v0.2.7) |
| URL | `https://www.gohappybelly.com/the-gut-fix` |
| Status | Published, not in the main menu |
| Product | The Gut Fix ebook, $10 |
| Checkout | **SamCart** `https://mystore2429.mysamcart.com/the-gut-fix/` |

A rebuild of the SamCart sales page on the website design system. Built per the
standing rule in CLAUDE.md, which now says the design system applies to every
new page without being asked.

## Structure

| Section | Background | Job |
|---|---|---|
| `1791990000001` Hero | `#F8FAF8` | Headline, promise, price, first CTA |
| `1791990000002` The Problem | Forest `#162E28` | Six symptom lines, then the aha line |
| `1791990000003` What Is Inside | `#EFF7F1` | Three numbered cards |
| `1791990000004` Is And Is Not | `#F8FAF8` | Two panels, honest scope |
| `1791990000005` Who Wrote It | `#EFF7F1` | Portrait with FDN-P badge, Alina's story |
| `1791990000006` Final CTA | Forest | Guarantee, second CTA |

Banding runs light, forest, alt, light, alt, forest, which is the design
system's pattern with forest reserved for the validation band and the final CTA.

## What changed from the SamCart copy, and why

The source page conflicted with CLAUDE.md in several places. The rebuild fixes
all of them.

| SamCart | Here | Reason |
|---|---|---|
| "Certified Gut Health Specialist & Holistic Wellness Educator" | "Alina Nazari, FDN-P" | The credential is locked. Every other surface says FDN-P |
| "empowering for every woman" | cut | Banned word |
| "a game-changing tool" | cut | Marketing filler, and "game-changing" reads as hype next to the rest of the site |
| Em dashes throughout | none | Hard style rule |
| "Thousands of women silently struggle" / "has helped thousands of women" | cut | Specific social-proof claims that are not substantiated anywhere. Replaced with no number at all |
| "Which Foods Are Sabotaging Your Gut" | "Find what works against you" | Softer, and avoids implying a diagnosis |
| No scope limits | "What this is, and what it is not" section | States plainly that it is not a diagnosis, not a substitute for testing, and not a replacement for 1:1 work |

The "is not" panel is an addition, not a port. A $10 ebook sold by a
practitioner needs to say what it does not replace, and it also protects the
higher-ticket offers from being undercut by a ten dollar product.

## Checkout

The CTA still goes to SamCart. Moving the sale onto Kajabi needs two things
this build could not supply:

1. A Kajabi offer at $10. The existing ebook offer, `2149818047`
   "E-Book: Making Your Way To A Happier Belly" at $9.97, is a **different
   book** (leaky gut, H. pylori, smoothie recipes, meal plans). It is not The
   Gut Fix and must not be reused for it.
2. The ebook file itself, attached to a DigitalDownload product. The theme API
   cannot upload files, only reference existing URLs.

Say the word and the offer can be created as a draft, ready for the file.

Worth knowing: offer `2149818047`'s description has its own compliance
problems, naming "Leaky Gut" as a condition and using "heal your gut",
"transform" and "journey". It is live on that offer's checkout page. Not
touched here.

## Nova traps hit on this page

**A horizontal `group` does not stack on mobile.** It is `flex flex-nowrap`,
and Nova exposes no mobile direction setting for groups, so the About row's two
children split a 350px phone viewport and the portrait rendered at **139px**
wide, which is 350 minus the 72px gap, halved. The fix is to stack the group at
the mobile breakpoint, via a `gh-about-row` hook class.

Worth being precise about why the obvious fix fails: releasing the image with
`width: 100%` does nothing, because the image sizes against
`[data-nova-role='image-wrapper']`, which the portrait rules pin to
`fit-content`. Both the wrapper and the group have to be freed in the same
breakpoint. That cost two round trips to find.

## Verified

Measured on the rendered page, not eyeballed:

| | 1440 | 390 |
|---|---|---|
| Portrait | 486 x 608, matching the About spec | 320 x 400 |
| Symptom grid | two columns, 411px each | one column |
| Inside cards | 334px, all three exactly 183px tall | 350px, stacked |
| Is / is not panels | 508px, both exactly 187px tall | 350px, stacked |
| Horizontal overflow | none | none |

Content audit against CLAUDE.md, run over the rendered text: **0 em dashes, 0
banned words, no "Certified Gut Health Specialist", no diagnostic phrasing.**

One note on that audit: an early pass flagged "cure", which turned out to be
the word "Se**cure** checkout". A word-boundary check returns zero. The audit
regex was too loose, not the copy.

## Open

- The ebook cover image. There is no cover on the page because SamCart's CDN
  refuses its own asset URLs from outside (every `_assets` request returns a
  1.4KB error), and the theme API cannot upload files. Send the cover and it
  goes in the hero.
- Whether to move checkout off SamCart, per above.
- The page is not in the main menu. `/links` card 2 now points at it.
