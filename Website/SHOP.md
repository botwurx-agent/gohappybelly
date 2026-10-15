# Shop page

Built 2026-10-15 to the locked design system in `DESIGN-SYSTEM.md`. Products
carried over from the 2025 Shop page (`2151041244`, theme `2160497533`), which
is still live at `/Shop` and untouched.

| | |
|---|---|
| Landing page | `2152334359` |
| Theme | `2167898691` (Nova v0.2.7) |
| Slug | `/shop` |
| Live | https://go-happy-belly.mykajabi.com/shop |
| Status | **Published**, so the build could be rendered and measured. Not yet linked from the nav. |

## Sections

| # | Section | Background | Job |
|---|---|---|---|
| 001 | Shop Header | `#F8FAF8` | What this list is, and the affiliate disclosure |
| 002 | Products | `#EFF7F1` | Ten product cards, three across |
| 003 | Guidance CTA | `#162E28` | Sends an undecided visitor to the quiz first |

## Products

Ten of the eleven brands from the old page, each with its original image and
affiliate link. Card titles were rewritten to the **brand name**, with the old
marketing line moved into the description, because the old page mixed the two
(some cards were titled "The cleanest, tastiest, grass-fed and finished beef
protein that..." while others were just a brand).

| Brand | Price shown | Affiliate param |
|---|---|---|
| Grüns | $47.99 | `snowball=ALINA76447` |
| Equip Foods | $54 | `ref=superfiliate-GOHAPPYBELLY` |
| True Sea Moss | $47.50 | `ref=GoHappyBelly` |
| Brodo | — | Impact `campaign=GoHappyBelly` |
| Fodzyme | — | `partners.fodzyme.com/GOHAPPYBELLY` |
| Dose Daily | — | `referralCode=alina566` |
| Llama Naturals | — | `affiliate-687747` |
| BUOY | — | `snowball=ALINA56946` |
| Elavi | — | `dt_id=1950405` |
| Lorissa's Kitchen | — | `sref_id=yw40fzd` |

Prices only appear where the old page carried one. Both the card image and the
button go to the affiliate link, and every one opens in a new tab.

## Three things worth knowing

**1. The Lumen card was left off, because its link is broken.** On the old page
the Lumen Metabolism Tracker's "Buy Now" points at
`https://ugc.production.linktr.ee/5be8ed96-...image.png` — a linktr.ee **image
file**, not Lumen. Anyone clicking it lands on a picture. Rather than ship a
dead button or invent an affiliate URL and lose the commission, the card is
omitted. Send the correct Lumen link and it takes two minutes to add.

**2. There was no affiliate disclosure.** Every link on the old page carries a
referral parameter and nothing said so, which the FTC requires. A disclosure
now sits directly under the page heading, above the products, in the visitor's
reading path rather than buried in a footer.

**3. The product images still live in the old theme's uploads**
(`themes/2160497533/settings_images/...`), referenced by absolute CDN URL. They
render fine cross-theme, but if the old Shop page and its theme are ever
deleted, these images break. Re-upload them into `2167898691` before retiring
the old page.

## Two Nova traps this build hit

Both are new, and both are now in `DESIGN-SYSTEM.md`:

1. **`custom_classes` land on the block wrapper, not the flex row.** A group
   block renders `wrapper > div > .nova-group > children`. A `.hook > *`
   selector sizes that intermediate `div`, so all ten cards ended up stacked in
   a one-third-width column. The selector has to reach through:
   `.hook .nova-group > *`.
2. **The feature block hides an `<article>` in its flex chain.** Bottom-aligning
   the buttons needs an unbroken grow chain from card to actions row, and the
   `<article>` between Nova's inner div and the details block ships with
   `flex: 0 1 auto`. Miss it and `margin-top: auto` silently resolves to zero,
   with no error and no visual clue beyond buttons sitting at different heights.

## Open

- `/shop` and the old `/Shop` are both live. Decide which to retire; if the new
  one wins, add it to the main menu and redirect the old path.
- No SEO title or description set yet.
- The six Amazon storefront lists in `AFFILIATE-PRODUCTS.md` (one per gut
  pattern, from inside the course) are a separate catalogue and were **not**
  added here. They would make a natural second section if Steve wants them
  public.
