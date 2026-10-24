# Sweep for gohappybelly@gmail.com, 2026-10-23

Steve: "there should be no gohappybelly@gmail.com anywhere at all on any of the
landing pages, nowhere. It should only be the support email."

## Result

**Two instances found, both fixed.** Both were lab test checkouts:

| Surface | Was | Now |
|---|---|---|
| SIBO Breath Test checkout, theme 2167629165 | `gohappybelly@gmail.com` | `support@gohappybelly.com` |
| H. Pylori checkout, theme 2167629161 | `gohappybelly@gmail.com` | `support@gohappybelly.com` |

Nothing else on the site carries it.

## What was checked

**All ten published landing pages not rebuilt on the design system**, read in
full and grepped: Contact, Alina About Me, Go Happy Belly Programs, One On One
Coaching, Functional Lab Testing, Lab Orders, the old `/Home`, 3 Step Guide Opt
In, 101 Foods Before One, the old `/Shop`. Zero hits. Contact and Lab Orders
both already use `support@gohappybelly.com`; the rest carry no email at all.

**Thirteen of sixteen published offer checkouts**: all eight lab tests, plus
Happy Belly Essentials Club, Bi-Weekly Group Coaching, the E-Book, and the
$1,497, $147 and $27, whose copy was written in this session. Zero hits beyond
the two fixed.

**Not checked:** the Gut Fix and Members checkouts, four draft landing pages
(Coming Soon, health-sales-page-242, Happier Belly Gut Reset, Bone Broth Reset),
the site theme's own website pages, and course lesson bodies. The Gut
Foundations course welcome page uses `support@gohappybelly.com`, which is how
that address was confirmed as current.

## Method, worth keeping

Kajabi has no search. Each theme has to be read whole. A full `get_theme_content`
on these older Encore themes runs 60KB to 95KB, which overflows the tool result
and gets written to a file under the session's `tool-results/` directory. That
file can then be grepped for pennies instead of read.

So the pattern for any future site-wide text sweep: fire the full reads, let the
big ones spill to disk, then `grep` the directory. It turned what looked like a
thirty-read grind into something affordable.
