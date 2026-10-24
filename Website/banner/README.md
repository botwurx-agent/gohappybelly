# Facebook group cover

Redesign of the group banner, 2026-10-23.

## What was wrong with the original

Alina's version had four problems, and the first two matter more than how it
looked.

**1. It was YouTube channel art, not a Facebook group cover.** It carried
"SUBSCRIBE AND TURN ON NOTIFICATIONS" with a bell icon. Facebook groups have a
Join button; there is no subscribe and no notification bell. The asset was built
for the wrong platform, and the supplied file was 2000x735, a YouTube-ish aspect
rather than the 1640x856 a group cover wants.

**2. "Gut Healing Strategies For Longevity" breaks the compliance guardrails.**
`CLAUDE.md` bans any claim to heal, seal, cure or treat. "Gut Healing" as the
headline on a public banner is exactly that claim, in the largest type on the
page.

**3. Wrong palette.** Bright kelly green throughout. The website system is
forest `#162E28`, sage `#7AAE86`, cream `#F8FAF8`, terracotta `#C07A5A`. The
email system is navy and Georgia. The banner matched neither.

**4. Wrong type, and two photographs of the same person.** A script face and a
heavy sans, neither Playfair Display nor DM Sans. Alina appears twice, once
washed into the background and once cut out.

## The three replacements

All 1640x856, the Facebook group cover upload size.

| File | What it is |
|---|---|
| `fb-cover-3-hybrid.png` | **Recommended.** Cut-paper signpost at full bleed, cream panel, Playfair wordmark, Alina in a circle |
| `fb-cover-2-split.png` | The same split without the portrait. Cleaner, less personal |
| `fb-cover-1-forest.png` | Forest field, white wordmark, larger portrait. Darker and more formal |

### How they were made

Built as HTML and rendered with headless Chromium at exactly 1640x856, rather
than generated. That matters: the type is really Playfair Display and DM Sans
pulled from Google Fonts, the hex values are the design system's own, and
nothing is an approximation of a letterform. Source is `b1.html`, `b2.html`,
`b4.html` and `common.css` in this folder; re-render with the script in the
session scratchpad or any headless browser.

Alina's portrait is cropped from `Website/Alina_Fence.jpg` and pushed through
`saturate(.72) sepia(.12)` so the bright yellow-green bokeh behind her sits with
the brand greens instead of fighting them.

### Copy

The headline problem is solved by not making a claim at all:

- Hybrid and split: **"Five gut patterns. This is where we work out yours."**
  Describes what the group does, ties to the quiz, promises nothing.
- Forest: **"Root-cause gut health for women who are tired of being told they're
  fine."** This is already the locked footer line in `DESIGN-SYSTEM.md`.

Both avoid heal, cure, treat and longevity claims. Checked for em dashes and the
banned word list.

## One thing to watch

Facebook crops group covers differently on desktop and mobile, and the crop
behaviour changes without notice. All three keep the wordmark and tagline inside
the middle band with generous margins, so a vertical crop takes background
rather than words. Worth a look on a phone before settling.
