# Favicon audit, all landing pages, 2026-10-24

All 24 landing pages now carry a favicon. Ten already had one; fourteen did not.

## What was already set

The ten pages built before the rebuild all had it, every one pointing at the
same source image, `4f72d16e-1497-43a0-b7ed-2959181589c5.jpg`, copied into each
theme's own `settings_images` folder by the Kajabi UI:

Home (old), Alina About Me, Go Happy Belly Programs, Contact, One On One
Coaching, 3 Step Guide Opt In, Functional Lab Testing, Lab Orders, 101 Foods
Before One, Shop (old).

One detail from that set is load-bearing. **Shop (old) carries Lab Orders'
theme path**, `themes/2158149725/...`, because the page was cloned from it. That
is a live published page rendering a favicon from another theme's folder, which
proves a cross-theme path resolves. The fix below leans on that.

## What was missing, and now is not

| Page | Theme | Status |
|---|---|---|
| Gut Foundations | 2168000232 | published |
| Gut Foundations Thank You | 2167999815 | published |
| 7-Day Lifestyle Workbook | 2167998577 | published |
| Gut Reset Course | 2167971291 | published |
| The Gut Fix | 2167909908 | published |
| Link in Bio | 2167908665 | published |
| Shop (new) | 2167898691 | published |
| Private Coaching | 2167882803 | published |
| Course Thank You Page | 2156348991 | published |
| Private 1 on 1 Thank You | 2156349886 | published |
| The 3-Day Bone Broth Reset | 2167624377 | draft |
| Happier Belly Gut Reset | 2157155259 | draft |
| health-sales-page-242 | 2156349874 | draft |
| Coming Soon | 2156348893 | draft |

**Every page built during the rebuild was missing one.** New themes start with
`favicon: ""` and nothing in the build process set it, so each new page shipped
with a blank browser tab. That is now part of what a new page needs.

## Two different values, deliberately

The Nova themes take the site-level brand favicon as a full CDN URL:

```
https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/sites/2148204891/images/1dbb85-040-ab24-7850-cdcd6300e253_favicon.jpg
```

That form is safe there because those themes already render full CDN URLs for
their header and footer logos.

The five older Encore themes (Course Thank You, Private 1 on 1 Thank You,
Coming Soon, health-sales-page-242, Happier Belly) were given the **relative**
path instead:

```
file-uploads/themes/2156348953/settings_images/10ece2-d17-8c3-65dc-05754f01415b_4f72d16e-1497-43a0-b7ed-2959181589c5.jpg
```

Encore themes have only ever stored relative paths, and there is no evidence
they resolve a full URL. The relative value above is the Contact page's, which
is live and resolving, and the Shop precedent shows another theme's folder works
fine. Both URLs were confirmed to return 200 before use.

## Unverified

**Nobody has seen a rendered tab.** Cloudflare blocks this environment from
gohappybelly.com, so the storage is confirmed and the rendering is not. Worth
opening two tabs to check: one Nova page such as `/gut-foundations` and one
Encore page such as `/course-thank-you-page`, since they carry different value
forms. If the Nova ones come back blank, the fix is to swap them to the same
relative path the Encore ones now use.

## Not covered

Offer checkout pages are not landing pages and were not in scope, but at least
one of them, the $27 Gut Foundations checkout, has `favicon: ""`. There are 16
published offers. Worth the same sweep.
