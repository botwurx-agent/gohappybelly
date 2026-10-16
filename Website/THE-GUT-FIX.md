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
| `1791990000003` What Is Inside | `#EFF7F1` | Three numbered cards, sage-light left trim |
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

A draft Kajabi offer now exists alongside the SamCart one.

| | |
|---|---|
| Offer | `2151452007` "The Gut Fix", **draft**, $10.00 USD one time |
| Product | `2149603425` "The Gut Fix", DigitalDownload, collection `428349` |
| Checkout URL | `https://www.gohappybelly.com/offers/JnHcWPaw/checkout` |
| Checkout theme | `2167910104` (Encore 2.14.8) |

The checkout page is styled to the design system: Playfair and DM Sans, forest
headings, terracotta submit button at a 2px radius, a 3px card radius, sage
bullets, and header and footer hidden so the page is a checkout and nothing
else. The preset's placeholder copy (`[Offer title]`, `[ Insert value 1 ]`) is
replaced with real copy carrying the FDN-P credential and the same compliance
note as the sales page. The empty image block is hidden rather than deleted, so
the ebook cover drops straight into it later.

### CTAs now point at the Kajabi checkout

The offer was published on 2026-10-16 and its checkout returns `200`, so both
CTAs were repointed from SamCart to `/offers/JnHcWPaw/checkout`. Verified on
the rendered page: both read that href, and the page contains zero SamCart
references.

The ebook PDF is attached and confirmed byte-identical to the corrected file
(sha256 `1b35306a…`), 18 pages, title "The Gut Fix", both Calendly links live.

Payments work. An earlier note here claimed they were paused site-wide. That
was wrong, and the cause is worth recording.

### Before publishing

1. Upload the ebook PDF to download collection `428349`, or the buyer pays and
   receives nothing.
2. Publish offer `2151452007` in the Kajabi admin. MCP-created offers are
   always drafts and cannot be published through the API.
3. Confirm a payment processor is connected for a $10 charge.
4. Then the two CTAs can be repointed.

### Checkout, now verified

Rendered once the offer was published. The design built blind is correct:

| | |
|---|---|
| h1 | Playfair Display 44px, `rgb(22,46,40)` |
| Body | DM Sans |
| Page background | `rgb(248,250,248)` |
| Preset placeholder copy | gone |
| Price | $10 shown |
| Horizontal overflow | none |

### The "Payments are paused" false alarm

The first render of the checkout showed "Payments are paused on this site.
Contact site owner for assistance." with the pay button disabled, and that was
reported as a live blocker. It was not. Kajabi Payments is connected and the
checkout takes cards.

The message is injected client side, not served in the HTML: `curl` on the
checkout returns 52KB with no such phrase anywhere. It appeared because this
container relays every browser request through a proxy, and Stripe's endpoints
refuse it: `403` on `r.stripe.com`, `422` on `verify_apple_pay_domain`. With
its payment scripts failing, the checkout falls back to that message. On a
clean run it does not appear at all.

**The lesson for this harness:** the Playwright relay is reliable for layout,
geometry and computed styles, and unreliable for anything that depends on a
third-party script completing a call. Before reporting a payment, analytics or
embed problem seen through it, check whether the phrase exists in the raw HTML
and whether the relay logged failures for that vendor's domain.

### A real defect the same render did find

The pay button rendered `rgb(52, 51, 50)`, Kajabi's default `#343332`, not the
terracotta. The section's `checkout_block_btn_color` setting saves and reads
back as `#C07A5A` but does not reach the button. The colour is now set in the
theme's `css` alongside the casing and tracking, which were already landing
there. Verified: `rgb(192, 122, 90)`, uppercase, 1.56px tracking, 12px, enabled,
with Stripe card fields present.

Disabled-state styling was added at the same time, so a button that cannot be
pressed no longer looks pressable.

### Product thumbnail

The checkout's product image slot is **16:9**, rendering at 256x144 at the top
of the card and 98x54 in the order summary. The ebook cover is 1147x2000
portrait, so placing it directly (media `4541809` on `Product` `2149603425`,
attribute `thumbnail`) made Kajabi auto-crop a horizontal slab out of the
middle: the top of the book and the "by Alina Nazari" line were cut off.

`crop_media` cannot fix this. Its `clip` fit returned 370x645, the whole image
scaled down but still portrait, because the tool fits inside the box without
padding. There is no letterbox option, so the slot crops it again.

The fix is a pre-composed 16:9 image: the book centred at 88% height on white,
white because the checkout card behind it is white. That cannot be generated
into Kajabi, since the API has no upload path, so it is built locally and
uploaded by hand like the cover was.

Leftovers from the attempts, both harmless and unused once the real thumbnail
lands: media `4553622` ("the-gut-fix-cover (1147x645)", actually 370x645).

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

- The ebook cover image. See "Hero cover" below.
- Publishing the Kajabi offer, per above, and then repointing the two CTAs.
- The page is not in the main menu. `/links` card 2 now points at it.


## Hero cover

The hero was rebuilt as a two-column row ready for the ebook cover, which goes
to the right of the copy.

```
1791990000001 (section)
└── 1791990000001_hrow   group, horizontal, gap 60, class gh-hero-row
    ├── 1791990000001_hleft   group, vertical
    │   ├── 1791990000001_ht   text   eyebrow, h1, lead
    │   ├── 1791990000001_hc   cta    Get The Gut Fix for $10
    │   └── 1791990000001_hn   text   reassurance line
    └── 1791990000001_himg   image  class gh-cover  (hidden until the cover exists)
```

The old top-level `_t` / `_c` / `_n` blocks are still defined on the section but
are no longer in `block_order`, so they do not render. A deep merge cannot
delete them.

### The cover file

Media asset **`4541809`**, `the-gut-fix-cover.png`, 1147 x 2000, 1.06MB,
transparent background. Steve uploaded it through the media library; Kajabi's
API cannot upload files, so `add_media` only returns an uploader link.

It is referenced by its **unsigned CDN URL**:

```
https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/sites/2148204891/images/80374fa-d0e2-fda7-27c6-8448ef0fe504_the-gut-fix-cover.png
```

Not the `image_url` that `list_media` returns. That one is an S3 link signed
with `X-Amz-Expires=604800`, so it would have stopped resolving after seven
days. Both the s3.amazonaws.com and kajabi-cdn.com hosts serve the file
unsigned; the CDN host is used because the rest of the themes use it.

`place_media` could not do the placement: it only addresses blocks directly on
a section, and this one is nested inside the hero group. It fails with "Block
not found in section". The image was set through `update_theme_content`
instead.

### Traps found building this

**An empty Nova image block is not invisible.** It renders a dashed
placeholder box with an icon, about 400 x 225, which looked broken on the live
page. Hiding the block is the only way to stage an image slot ahead of its
file.

**A horizontal group's children do not size themselves on desktop.** Nova
emitted only `max-md:flex-1` and `max-md:w-full` for the two children, so above
the mobile breakpoint both sized to their content, reached the full 1044px and
wrapped onto separate rows, because `.nova-group` carries `flex-wrap`. Setting
`width: "fill"` on the children did not change this. The fix is the same one
the card grids already use: force the widths in CSS on `.nova-group > *`, here
`calc(50% - 30px)` so the 60px gap yields the design system's two 492px hero
columns.

That rule is gated behind `.gh-has-cover`, which was useful while the cover was
absent: ungated it would have halved the headline column with nothing beside it.

**A descendant selector is wrong for a nested group.** The first version of the
rule was `.gh-hero-row .nova-group > *`. The hero nests a vertical group inside
the horizontal one and *both* carry `.nova-group`, so it matched the inner
column's children too and halved 492 to **216**, squeezing the headline into a
narrow ribbon. The row's own children need the child combinator:
`.gh-hero-row.gh-has-cover > div > .nova-group > *`. The inner column then gets
its own rule putting its children at 100%.

**A cta block centres its button with `text-align`, not `justify-content`.**
The button is an `inline-flex` anchor inside a `display: block` wrapper, so a
`justify-content: flex-start` on the wrapper computed fine and did nothing at
all. The button stayed 109px off the headline's left edge until the rule became
`text-align: left`.

### Verified

| | 1440 | 390 |
|---|---|---|
| h1 | x 198, w 492 | x 20, w 350 |
| CTA | x 198, flush with the headline | x 58, centred |
| Cover | x 796, 400 x 697 | x 55, 280 x 488, stacked below |
| Horizontal overflow | none | none |


## Card accent trim

The What Is Inside cards carry the design system's offer-card left bar,
`3px solid #A8CAB2` with the card's existing 3px radius. Checked against the
live home page first rather than guessed: it uses exactly two left-bar
accents, `#7AAE86` on the testimonial cards and `#A8CAB2` on the offer row,
both at 3px, which is what the design system documents.

`#A8CAB2` was the right one of the two here. These are a three-up row of
equal informational cards, structurally the offer row rather than a quote, and
it matches the link in bio cards already built on the same pattern. The
stronger `#7AAE86` is reserved for testimonials, where the bar marks a voice.

The rule is scoped `.gh-grid-3 .gh-card` so the is / is not panels below,
which also use `.gh-card`, stay plain. Verified: all three trimmed cards read
`3px rgb(168, 202, 178)` and both panels read `0px`. Card widths (334) and
equal heights (183) are unchanged, because Nova is border-box so the trim eats
into padding rather than growing the card.

## The ebook PDF

The deliverable for download collection `428349`. Source of truth is a Google
Doc, [The Gut Fix](https://docs.google.com/document/d/177HZhvea1-YhxCW1FWkR2J0cWnuq4PR_jCJYLVntwi0/edit),
owned by `support@guthub.ai`. The PDF is an export of it, 18 pages, US Letter,
Arial.

### Fixed in the PDF

**The back page sold an offer that does not exist.** Page 18 read "Book your
Gut Reset Call now for just $97 (normally $197)". There is no $97 consultation
in the offer suite or in Kajabi, and the documented funnel runs on the free 20
minute Gut Breakthrough Call. Worse, the PDF contained **zero link
annotations**, so even that dead offer had no way to be acted on.

Page 18 was replaced with a new one: the free call, a terracotta button and a
plain-text URL both carrying a real link annotation, the locked sign-off with
the FDN-P credential, and a medical disclaimer the ebook previously had
nowhere. Pages 1 to 17 are copied through byte for byte.

The link is `https://calendly.com/gohappybelly/gut-breakthrough-call`, without
the `?month=2026-10` parameter Steve supplied. That parameter pins Calendly to
October 2026, which is wrong in an evergreen product someone may open a year
from now.

**Metadata.** `/Title` was `The Bloat Fix`, an earlier working name left by the
Google Docs export, and it showed in the reader title bar. Now `The Gut Fix`,
with `/Author` `Alina Nazari, FDN-P`.

### NOT fixed, and why

The body text still breaks house style: 27 em dashes, "transform" once,
"journey" twice, the unsubstantiated "thousands of women", and no FDN-P
credential anywhere in chapters 1 to 17.

These cannot be fixed in the PDF. It is a Google Docs render, so the text is
positioned glyph runs; swapping words in place reflows nothing and would leave
visibly broken spacing. They have to be fixed in the Doc and re-exported.

**There is no Google Docs connector on this account** (Drive, Gmail and
Calendar only). Drive can read and export a Doc but cannot edit one, so the
body edits need either that connector enabled or Steve editing the Doc by hand.

If the Doc is edited and re-exported, **the page 18 replacement and the
metadata fix are lost**, because they live in the PDF and not in the Doc. Fix
the back page in the Doc at the same time, or re-apply both afterwards.

### Also worth knowing

The master Doc's sharing is `role: writer, type: anyone`: anyone with the link
can edit the product being sold. Worth restricting.
