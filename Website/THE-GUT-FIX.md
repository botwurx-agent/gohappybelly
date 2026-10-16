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

### The sales page CTA still points at SamCart, deliberately

A draft offer's checkout is **not purchasable**: `GET` on it returns `302`,
where a published offer's checkout returns `200`. Repointing the live sales
page at it would have replaced a working buy button with a dead one, so the
CTA was left on SamCart.

Flipping it is a one-line change once the offer is published. Both CTAs on
`/the-gut-fix` (`1791990000001_c` and `1791990000006_c`) take
`btn_action: "/offers/JnHcWPaw/checkout"`.

### Before publishing

1. Upload the ebook PDF to download collection `428349`, or the buyer pays and
   receives nothing.
2. Publish offer `2151452007` in the Kajabi admin. MCP-created offers are
   always drafts and cannot be published through the API.
3. Confirm a payment processor is connected for a $10 charge.
4. Then the two CTAs can be repointed.

### Not verified visually

The checkout page could not be rendered. A draft checkout 302s to anonymous
requests, and the only way to see it would be to publish the offer, which would
make it purchasable and contradicts the instruction to keep it a draft. The
settings were read back and confirmed saved, but **the rendered page has not
been looked at.** Worth one glance once it is published, particularly the h1
size, which is set to 44px here rather than the site's 58px because the
checkout's left column is narrower than a page.

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

### Waiting on the cover file

Kajabi's API cannot upload files: `add_media` returns an uploader link for a
person to open, nothing more. The cover is not in the media library yet (a
search for it returns nothing, and the library holds only two PNGs, neither of
them the cover). So the image block is **hidden** and the hero renders as a
single left-aligned column, which is a clean state rather than a broken one.

Uploader: `https://app.kajabi.com/admin/sites/2148204891/media_library?open_uploader=image`

Once the file is in the library, three things turn it on in one pass:

1. `place_media` the asset into `1791990000001_himg` / `image`
2. Clear `hide_on_desktop` and `hide_on_mobile` on that block
3. Add `gh-has-cover` to `1791990000001_hrow`'s `custom_classes`

### Two traps found building this

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

That rule is deliberately gated behind `.gh-has-cover`. Ungated, it would halve
the headline column while the cover is still hidden, leaving the copy stranded
beside empty space.
