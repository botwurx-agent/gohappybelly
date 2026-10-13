# Private Coaching page (the 3-Month Gut Reset sales page)

Built 2026-10-13. This is the page CLAUDE.md listed under "Not Yet Built"
as the *3-Month Gut Reset sales page*. The free call is still the sales
mechanism, so every CTA goes to Calendly, not to a checkout.

## Where it lives

| | |
|---|---|
| Landing page | `2152330511` |
| Theme | `2167878184` (**Nova v0.2.7**) |
| Slug | `/private-coaching` |
| Preview | https://go-happy-belly.mykajabi.com/private-coaching |
| Builder | https://app.kajabi.com/admin/themes/2167878184/settings/edit |
| Status | **DRAFT.** Publishing has to be done in the Kajabi admin UI. |

## The offer question that had to be settled first

CLAUDE.md and the live gohappybelly.com disagreed about whether the
$1,497 includes the $497 GI-MAP stool test. CLAUDE.md said no and made
"optional clinical recommendation" a hard rule; the live site said
"Includes $497 GI-MAP Stool Test" next to the price.

Steve confirmed **it is included**. CLAUDE.md's offer table, its GI-MAP
note and its Hard Style Rules line were all updated to match. The other
four tests (H. Pylori, SIBO, OAT, Food Sensitivity) stay optional
post-consult recommendations, and the page says so explicitly in an FAQ
so the two ideas cannot be confused again.

**Still stale:** the live Netlify site's last FAQ says functional testing
is "always optional and never a prerequisite", which now contradicts the
GI-MAP being bundled. Fix that when the site migrates.

## Sections

| ID | Section | Note |
|---|---|---|
| ...0001 | Hero | "Your labs are normal. You are not imagining this." |
| ...0002 | Validation | navy, the five dismissals, Alina quote |
| ...0003 | Early Testimonial | Linda, the four-doctors quote |
| ...0004 | What Is Included | the 7 deliverables, GI-MAP second |
| ...0005 | How It Works | 3 steps, nested horizontal group |
| ...0006 | Who It Is For | fit / not a fit, two cards |
| ...0007 | About Alina | **no portrait yet, see Outstanding** |
| ...0008 | Testimonials | Linda, Hanna, Tiffani |
| ...0009 | Investment | $1,497, GI-MAP badge, CTA, risk reversal |
| ...0010 | FAQ | 7 native accordions |
| ...0011 | Final CTA | navy, CTA plus quiz fallback link |

Full ids are `1791920000001`–`1791920000011`.

Testimonials are the three real ones from the live site (Linda, Hanna,
Tiffani), all **1:1 coaching clients**, which is exactly the right proof
for this page. None were invented.

The "not a fit" card is deliberate. It qualifies out people who want a
diagnosis or a two-week fix, which protects Alina's time and reinforces
that she is an FDN-P rather than a physician.

## Chrome

The fresh Nova theme shipped with placeholder chrome that would have gone
live as-is: header logo reading **"Nova"** with a **"Get started"** button
pointing at `#`, and a footer reading **"© Your Brand"**. All replaced.
The footer copyright now carries the medical disclaimer.

**The nav menu block was removed from `block_order`, not deleted.** It
pointed at a `main-menu` navbar, and with Course, Shop and Contact not
built yet a nav would have led nowhere. Put `header-menu` back into
`block_order` once those pages exist.

## Nova, and what it means for the website rebuild

**New landing pages on this site are Nova v0.2.7, not Encore.** That is a
third theme engine alongside Encore LandingPage (`2167624377`, the Bone
Broth Reset) and Encore Site (`2156348838`, the homepage build). Nova has
a completely different block vocabulary.

This changes the plan in `KAJABI-REBUILD.md`, which said porting the
twelve homepage sections to a landing page would be "a transcription job
rather than a redesign". It will not be: Encore and Nova share almost no
setting names.

The upside is real though. Nova is Tailwind v4 with the browser JIT, so
arbitrary utilities, arbitrary values and arbitrary-variant selectors
(`[&_h2]:text-4xl`, `backdrop-blur-xl`, `bg-white/10`) all work from a
block's `custom_classes`. The six decorative pseudo-element effects that
had to be hacked into Encore's Style Guide CSS field, and the fragile
section-ID-targeted rules that silently break when a section is
recreated, are not needed in Nova. **Fidelity to the Netlify original
should beat the ~90% Encore managed.**

## Nova authoring notes worth keeping

- Guide is 151KB; `get_theme_skill_file_contents` blows the token cap, so
  it has to be sliced from the saved tool-result file.
- `sections`, `content_for_index` and Style Guide tokens are **flat
  siblings** under `settings`. Wrapping them in any parent key deep-merges
  to a non-rendering path and still returns `{"updated": true}`.
- Nesting is capped at section → group → leaf. The 3-up rows use exactly
  that: a vertical section holding a heading plus one horizontal `group`.
- **Every block needs a `name`**, not just every section. Different from
  Encore. Without it the editor sidebar shows `text`, `text`, `text`.
- Horizontal columns: `group` with `direction: horizontal`, `wrap: true`,
  `width: "custom"`, `width_custom: 100`, and children at `width: "fill"`.
- Brand-governed button settings are left blank on every `cta` so they
  inherit the Style Guide terracotta. Do not set them per block.
- The guide's own §6 example uses `class=` inside rich text, but §14 says
  the sanitizer strips `class=` on editor round-trips. Tailwind goes in
  `custom_classes`; inside rich text use inline `style=` only.
- Do not pin font sizes on headings or body copy. `font_size_h1_*` and
  `font_size_body_*` come from the Style Guide and handle desktop/mobile.
  Explicit sizes are only for display elements it does not govern (the
  price, the step numerals, the eyebrow, attributions).
- `{"updated": true}` means accepted, not rendered. Always read back.

## Brand tokens set on this theme

Sage `#7BA987` primary, navy `#1B2D4F` headings, `#374151` body,
`#6B7280` secondary, cream `#FAF6F0` background, terracotta `#C67B5C`
buttons with white text, Playfair Display headings, DM Sans body.

These are per-theme, so they do not touch the Bone Broth page or the Site
theme. Each new Nova landing page starts from indigo `#6366f1` defaults
and needs them set again.

## Outstanding

- **Publish it.** Draft only; publishing is admin-UI work.
- **Not visually verified.** The sandbox cannot reach the Kajabi domain,
  so this is verified as JSON, not as a rendered page. Open the preview
  URL and check it, mobile included.
- **About Alina has no portrait.** Same blocker as the homepage: the API
  cannot upload files. Source is `Website/Alina_Fence.jpg`. Upload via the
  media library, then add an `image` block to `1791920000007`.
- **Nav menu** once Course, Shop and Contact exist.
- Fix the live Netlify FAQ's "testing is always optional" line.
